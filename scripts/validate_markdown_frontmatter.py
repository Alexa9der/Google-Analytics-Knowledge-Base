"""Validate View and Report front matter, prefixes, and referenced IDs."""

from __future__ import annotations

import sys
from pathlib import Path

import yaml
from jsonschema import Draft202012Validator, FormatChecker

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    ENTITY_PREFIX,
    KnowledgeError,
    ValidationIssue,
    collect_id_strings,
    discover_markdown_entities,
    discover_yaml_packages,
    load_schema,
    parse_front_matter,
    safe_load_yaml,
    validate_id,
)

ROOT = Path(__file__).resolve().parents[1]


def _canonical_ids(root: Path) -> set[str]:
    """Collect IDs from canonical YAML records."""
    ids: set[str] = set()
    for path in discover_yaml_packages(root):
        package = safe_load_yaml(path)
        if not isinstance(package, dict) or not isinstance(package.get("records"), list):
            continue
        for record in package["records"]:
            if isinstance(record, dict) and isinstance(record.get("id"), str):
                ids.add(record["id"])
    return ids


def validate_markdown(root: Path = ROOT) -> list[ValidationIssue]:
    """Validate all Markdown entities and references to canonical IDs."""
    issues: list[ValidationIssue] = []
    canonical_ids = _canonical_ids(root)
    schemas = {
        "view": load_schema(root, "view-frontmatter.schema.json"),
        "report": load_schema(root, "report-frontmatter.schema.json"),
    }
    for path in discover_markdown_entities(root):
        entity_type = "view" if path.parent.name == "views" else "report"
        try:
            metadata, _ = parse_front_matter(path)
        except (OSError, yaml.YAMLError, KnowledgeError) as exc:
            issues.append(ValidationIssue("error", path, "front_matter", str(exc)))
            continue
        validator = Draft202012Validator(schemas[entity_type], format_checker=FormatChecker())
        for error in sorted(
            validator.iter_errors(metadata), key=lambda item: list(item.absolute_path)
        ):
            locator = ".".join(str(part) for part in error.absolute_path)
            issues.append(ValidationIssue("error", path, locator or "front_matter", error.message))
        entity_id = metadata.get("id")
        if not isinstance(entity_id, str) or not validate_id(entity_id, ENTITY_PREFIX[entity_type]):
            issues.append(
                ValidationIssue("error", path, "id", f"invalid {ENTITY_PREFIX[entity_type]} ID")
            )
        own_id = {entity_id} if isinstance(entity_id, str) else set()
        for reference in sorted(collect_id_strings(metadata) - own_id):
            if reference not in canonical_ids:
                issues.append(
                    ValidationIssue(
                        "error", path, "front_matter", f"unknown referenced ID {reference}"
                    )
                )
    return issues


def main() -> int:
    """Run Markdown front matter validation."""
    try:
        issues = validate_markdown(ROOT)
    except (OSError, ValueError, yaml.YAMLError, KnowledgeError) as exc:
        print(f"ERROR Markdown validation setup failed: {exc}")
        return 1
    for issue in issues:
        print(issue.render(ROOT))
    if any(issue.severity == "error" for issue in issues):
        print("FAILED Markdown front matter validation")
        return 1
    print("OK Markdown front matter validation")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
