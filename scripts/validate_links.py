"""Validate global IDs, typed links, Evidence rules, and supersession graphs."""

from __future__ import annotations

import sys
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    ENTITY_PREFIX,
    KnowledgeError,
    ValidationIssue,
    discover_markdown_entities,
    discover_yaml_packages,
    entity_type_from_id,
    parse_front_matter,
    parse_iso_date,
    safe_load_yaml,
    validate_id,
)

ROOT = Path(__file__).resolve().parents[1]

REFERENCE_FIELDS: dict[str, dict[str, set[str]]] = {
    "fact": {
        "evidence_ids": {"evidence"},
        "refuting_evidence_ids": {"evidence"},
        "qualifying_evidence_ids": {"evidence"},
        "concept_ids": {"concept"},
        "service_ids": {"service"},
        "related_fact_ids": {"fact"},
        "supersedes": {"fact"},
        "superseded_by": {"fact"},
    },
    "concept": {
        "broader_concept_ids": {"concept"},
        "narrower_concept_ids": {"concept"},
        "related_concept_ids": {"concept"},
        "fact_ids": {"fact"},
        "implemented_by_service_ids": {"service"},
    },
    "service": {
        "parent_service_id": {"service"},
        "related_service_ids": {"service"},
        "fact_ids": {"fact"},
        "integration_service_ids": {"service"},
        "implemented_concept_ids": {"concept"},
    },
    "view": {
        "entity_ids": {"fact", "evidence", "concept", "service"},
        "reading_order": {"fact", "evidence", "concept", "service"},
    },
    "report": {
        "fact_ids": {"fact"},
        "evidence_ids": {"evidence"},
        "concept_ids": {"concept"},
        "service_ids": {"service"},
    },
}


@dataclass(frozen=True)
class EntityRecord:
    """An entity plus its physical location and logical type."""

    entity_type: str
    data: dict[str, Any]
    path: Path
    locator: str


def load_entities(root: Path = ROOT) -> list[EntityRecord]:
    """Load canonical and Markdown entity records for link validation."""
    entities: list[EntityRecord] = []
    for path in discover_yaml_packages(root):
        package = safe_load_yaml(path)
        if not isinstance(package, dict):
            raise KnowledgeError(f"{path}: package must be a mapping")
        entity_type = package.get("entity_type")
        records = package.get("records")
        if not isinstance(entity_type, str) or not isinstance(records, list):
            raise KnowledgeError(f"{path}: invalid entity_type or records")
        for index, record in enumerate(records):
            if not isinstance(record, dict):
                raise KnowledgeError(f"{path}: records[{index}] must be a mapping")
            entities.append(EntityRecord(entity_type, record, path, f"records[{index}]"))
    for path in discover_markdown_entities(root):
        metadata, _ = parse_front_matter(path)
        entity_type = "view" if path.parent.name == "views" else "report"
        entities.append(EntityRecord(entity_type, metadata, path, "front_matter"))
    return entities


def _as_references(value: Any) -> list[str]:
    """Normalize a single-ID or list-of-IDs link field."""
    if isinstance(value, str):
        return [value]
    if isinstance(value, list):
        return [item for item in value if isinstance(item, str)]
    return []


def _build_registry(
    entities: list[EntityRecord],
) -> tuple[dict[str, EntityRecord], list[ValidationIssue]]:
    """Build the global ID registry and report duplicates and invalid prefixes."""
    registry: dict[str, EntityRecord] = {}
    issues: list[ValidationIssue] = []
    for entity in entities:
        entity_id = entity.data.get("id")
        if not isinstance(entity_id, str):
            issues.append(
                ValidationIssue("error", entity.path, entity.locator, "entity has no string ID")
            )
            continue
        expected_prefix = ENTITY_PREFIX.get(entity.entity_type)
        if expected_prefix is None or not validate_id(entity_id, expected_prefix):
            issues.append(
                ValidationIssue(
                    "error",
                    entity.path,
                    f"{entity.locator}.id",
                    f"ID {entity_id!r} does not match entity type {entity.entity_type!r}",
                )
            )
        if entity_id in registry:
            first = registry[entity_id]
            issues.append(
                ValidationIssue(
                    "error",
                    entity.path,
                    f"{entity.locator}.id",
                    f"duplicate ID {entity_id}; first declared at {first.path}:{first.locator}",
                )
            )
        else:
            registry[entity_id] = entity
    return registry, issues


def _validate_reference_fields(
    entities: list[EntityRecord], registry: dict[str, EntityRecord]
) -> list[ValidationIssue]:
    """Validate existence, target type, and self-reference for registered link fields."""
    issues: list[ValidationIssue] = []
    for entity in entities:
        entity_id = entity.data.get("id")
        for field, target_types in REFERENCE_FIELDS.get(entity.entity_type, {}).items():
            if field not in entity.data:
                continue
            references = _as_references(entity.data[field])
            raw = entity.data[field]
            if not isinstance(raw, (str, list)):
                issues.append(
                    ValidationIssue(
                        "error",
                        entity.path,
                        f"{entity.locator}.{field}",
                        "link field must contain an ID or list of IDs",
                    )
                )
            for reference in references:
                target = registry.get(reference)
                if target is None:
                    issues.append(
                        ValidationIssue(
                            "error",
                            entity.path,
                            f"{entity.locator}.{field}",
                            f"broken reference {reference}",
                        )
                    )
                    continue
                if target.entity_type not in target_types:
                    expected = ", ".join(sorted(target_types))
                    issues.append(
                        ValidationIssue(
                            "error",
                            entity.path,
                            f"{entity.locator}.{field}",
                            f"{reference} targets {target.entity_type}, expected {expected}",
                        )
                    )
                if reference == entity_id:
                    issues.append(
                        ValidationIssue(
                            "error",
                            entity.path,
                            f"{entity.locator}.{field}",
                            "self-reference is prohibited",
                        )
                    )
        if entity.entity_type == "fact":
            for field in ("subject", "object"):
                value = entity.data.get(field)
                if (
                    isinstance(value, str)
                    and entity_type_from_id(value) is not None
                    and value not in registry
                ):
                    issues.append(
                        ValidationIssue(
                            "error",
                            entity.path,
                            f"{entity.locator}.{field}",
                            f"broken reference {value}",
                        )
                    )
    return issues


def _validate_fact_rules(entities: list[EntityRecord]) -> list[ValidationIssue]:
    """Validate cross-field Fact rules and emit review warnings."""
    issues: list[ValidationIssue] = []
    today = date.today()
    for entity in entities:
        if entity.entity_type != "fact":
            continue
        status = entity.data.get("status")
        evidence = _as_references(entity.data.get("evidence_ids", []))
        refuting = _as_references(entity.data.get("refuting_evidence_ids", []))
        if status in {"candidate", "under_review"} and not evidence:
            issues.append(
                ValidationIssue(
                    "warning", entity.path, entity.locator, "candidate Fact has no Evidence"
                )
            )
        if status == "confirmed" and not evidence:
            issues.append(
                ValidationIssue(
                    "error", entity.path, entity.locator, "confirmed Fact requires Evidence"
                )
            )
        if status == "disputed" and not evidence and not refuting:
            issues.append(
                ValidationIssue(
                    "error",
                    entity.path,
                    entity.locator,
                    "disputed Fact requires supporting or refuting Evidence",
                )
            )
        if status == "refuted" and not refuting:
            issues.append(
                ValidationIssue(
                    "error",
                    entity.path,
                    entity.locator,
                    "refuted Fact requires refuting_evidence_ids",
                )
            )
        if status == "superseded" and not _as_references(entity.data.get("superseded_by", [])):
            issues.append(
                ValidationIssue(
                    "error", entity.path, entity.locator, "superseded Fact requires superseded_by"
                )
            )
        review_date = entity.data.get("next_review_at")
        if isinstance(review_date, str):
            try:
                if parse_iso_date(review_date) < today and status not in {
                    "superseded",
                    "refuted",
                    "archived",
                }:
                    issues.append(
                        ValidationIssue(
                            "warning",
                            entity.path,
                            f"{entity.locator}.next_review_at",
                            "Fact review is overdue",
                        )
                    )
            except ValueError as exc:
                issues.append(
                    ValidationIssue(
                        "error", entity.path, f"{entity.locator}.next_review_at", str(exc)
                    )
                )
    return issues


def _validate_supersession(
    registry: dict[str, EntityRecord],
) -> list[ValidationIssue]:
    """Validate symmetry and acyclicity of Fact supersession links."""
    issues: list[ValidationIssue] = []
    graph: dict[str, set[str]] = {}
    fact_records = {
        entity_id: entity for entity_id, entity in registry.items() if entity.entity_type == "fact"
    }
    for entity_id, entity in fact_records.items():
        older_ids = set(_as_references(entity.data.get("supersedes", [])))
        graph[entity_id] = {older_id for older_id in older_ids if older_id in fact_records}
        for older_id in older_ids:
            older = fact_records.get(older_id)
            if older is None:
                continue
            if entity_id not in _as_references(older.data.get("superseded_by", [])):
                issues.append(
                    ValidationIssue(
                        "error",
                        entity.path,
                        f"{entity.locator}.supersedes",
                        f"asymmetric supersession: {older_id} does not declare "
                        f"superseded_by {entity_id}",
                    )
                )
        for newer_id in _as_references(entity.data.get("superseded_by", [])):
            newer = fact_records.get(newer_id)
            if newer is None:
                continue
            if entity_id not in _as_references(newer.data.get("supersedes", [])):
                issues.append(
                    ValidationIssue(
                        "error",
                        entity.path,
                        f"{entity.locator}.superseded_by",
                        f"asymmetric supersession: {newer_id} does not declare "
                        f"supersedes {entity_id}",
                    )
                )

    state: dict[str, int] = {}
    stack: list[str] = []

    def visit(node: str) -> None:
        state[node] = 1
        stack.append(node)
        for target in graph.get(node, set()):
            if state.get(target, 0) == 0:
                visit(target)
            elif state.get(target) == 1:
                start = stack.index(target)
                cycle = stack[start:] + [target]
                entity = fact_records[node]
                issues.append(
                    ValidationIssue(
                        "error",
                        entity.path,
                        f"{entity.locator}.supersedes",
                        f"supersedes cycle detected: {' -> '.join(cycle)}",
                    )
                )
        stack.pop()
        state[node] = 2

    for node in sorted(graph):
        if state.get(node, 0) == 0:
            visit(node)
    return issues


def validate_links(root: Path = ROOT) -> list[ValidationIssue]:
    """Run all global ID and link validations."""
    entities = load_entities(root)
    registry, issues = _build_registry(entities)
    issues.extend(_validate_reference_fields(entities, registry))
    issues.extend(_validate_fact_rules(entities))
    issues.extend(_validate_supersession(registry))
    return issues


def main() -> int:
    """Run link validation and return a shell-friendly exit code."""
    try:
        issues = validate_links(ROOT)
    except (OSError, ValueError, yaml.YAMLError, KnowledgeError) as exc:
        print(f"ERROR link validation setup failed: {exc}")
        return 1
    for issue in issues:
        print(issue.render(ROOT))
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    if errors:
        print(f"FAILED link validation: {errors} error(s), {warnings} warning(s)")
        return 1
    print(f"OK link validation: {warnings} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
