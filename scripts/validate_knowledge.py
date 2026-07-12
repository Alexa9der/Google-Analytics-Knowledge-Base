"""Validate canonical packages and Markdown metadata against project schemas."""

from __future__ import annotations

import re
import sys
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator, FormatChecker

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    KnowledgeError,
    ValidationIssue,
    discover_markdown_entities,
    discover_yaml_packages,
    load_schema,
    parse_front_matter,
    safe_load_yaml,
)

ROOT = Path(__file__).resolve().parents[1]
EXPECTED_DIRECTORY = {
    "fact": "facts",
    "evidence": "evidence",
    "concept": "concepts",
    "service": "services",
}


def _schema_issues(
    value: Any,
    schema: dict[str, Any],
    path: Path,
    locator: str,
) -> list[ValidationIssue]:
    """Return sorted JSON Schema errors for one value."""
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    issues: list[ValidationIssue] = []
    for error in sorted(validator.iter_errors(value), key=lambda item: list(item.absolute_path)):
        suffix = ".".join(str(part) for part in error.absolute_path)
        resolved = f"{locator}.{suffix}" if suffix else locator
        issues.append(ValidationIssue("error", path, resolved, error.message))
    return issues


def _atomicity_warnings(record: dict[str, Any], path: Path, locator: str) -> list[ValidationIssue]:
    """Return non-blocking heuristics for potentially non-atomic Fact statements."""
    statement = record.get("statement")
    if not isinstance(statement, str):
        return []
    messages: list[str] = []
    if re.search(r"(?m)^\s*[-*+]\s+", statement):
        messages.append("statement contains a bulleted list")
    if len(re.findall(r"[.!?](?:\s|$)", statement.strip())) > 1:
        messages.append("statement appears to contain multiple sentences")
    if len(statement) > 400:
        messages.append("statement exceeds the recommended 400-character atomicity threshold")
    if re.search(r"\b(and|also|as well as)\b", statement, flags=re.IGNORECASE):
        messages.append("statement contains a conjunction that may join independent claims")
    return [ValidationIssue("warning", path, locator, message) for message in messages]


def validate_yaml_packages(root: Path = ROOT) -> list[ValidationIssue]:
    """Validate package envelopes and records for all canonical YAML files."""
    issues: list[ValidationIssue] = []
    package_schema = load_schema(root, "package.schema.json")
    record_schemas = {
        entity_type: load_schema(root, f"{entity_type}.schema.json")
        for entity_type in EXPECTED_DIRECTORY
    }
    for path in discover_yaml_packages(root):
        try:
            package = safe_load_yaml(path)
        except (OSError, yaml.YAMLError, KnowledgeError) as exc:
            issues.append(ValidationIssue("error", path, "document", str(exc)))
            continue
        issues.extend(_schema_issues(package, package_schema, path, "package"))
        if not isinstance(package, dict):
            continue
        entity_type = package.get("entity_type")
        if not isinstance(entity_type, str) or entity_type not in record_schemas:
            continue
        if path.parent.name != EXPECTED_DIRECTORY[entity_type]:
            issues.append(
                ValidationIssue(
                    "error",
                    path,
                    "package.entity_type",
                    f"{entity_type!r} package must be stored under "
                    f"{EXPECTED_DIRECTORY[entity_type]!r}",
                )
            )
        records = package.get("records")
        if not isinstance(records, list):
            continue
        for index, record in enumerate(records):
            locator = f"records[{index}]"
            issues.extend(_schema_issues(record, record_schemas[entity_type], path, locator))
            if entity_type == "fact" and isinstance(record, dict):
                issues.extend(_atomicity_warnings(record, path, f"{locator}.statement"))
    return issues


def validate_markdown_schemas(root: Path = ROOT) -> list[ValidationIssue]:
    """Validate View and Report front matter schemas."""
    issues: list[ValidationIssue] = []
    schemas = {
        "views": load_schema(root, "view-frontmatter.schema.json"),
        "reports": load_schema(root, "report-frontmatter.schema.json"),
    }
    for path in discover_markdown_entities(root):
        try:
            metadata, _ = parse_front_matter(path)
        except (OSError, yaml.YAMLError, KnowledgeError) as exc:
            issues.append(ValidationIssue("error", path, "front_matter", str(exc)))
            continue
        issues.extend(_schema_issues(metadata, schemas[path.parent.name], path, "front_matter"))
    return issues


def validate_all(root: Path = ROOT) -> list[ValidationIssue]:
    """Run all structural knowledge validations."""
    return validate_yaml_packages(root) + validate_markdown_schemas(root)


def main() -> int:
    """Run structural validation and return a shell-friendly exit code."""
    try:
        issues = validate_all(ROOT)
    except (OSError, ValueError, KnowledgeError) as exc:
        print(f"ERROR validation setup failed: {exc}")
        return 1
    for issue in issues:
        print(issue.render(ROOT))
    errors = sum(issue.severity == "error" for issue in issues)
    warnings = sum(issue.severity == "warning" for issue in issues)
    if errors:
        print(f"FAILED knowledge validation: {errors} error(s), {warnings} warning(s)")
        return 1
    print(f"OK knowledge validation: {warnings} warning(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
