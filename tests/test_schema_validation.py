"""Tests for package, record, and restricted YAML validation."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts import validate_knowledge
from scripts.common import (
    DuplicateKeyError,
    ForbiddenYamlFeature,
    generate_id,
    safe_load_yaml_text,
    validate_id,
)


def _fact_file(root: Path) -> Path:
    return root / "knowledge" / "facts" / "core.yaml"


def test_fixture_project_passes_structural_validation(project_copy: Path) -> None:
    issues = validate_knowledge.validate_all(project_copy)
    assert not [issue for issue in issues if issue.severity == "error"]


def test_candidate_without_evidence_is_schema_valid(project_copy: Path) -> None:
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert not [issue for issue in issues if "records[0].evidence_ids" in issue.locator]


def test_confirmed_without_evidence_is_schema_error(project_copy: Path) -> None:
    path = _fact_file(project_copy)
    text = path.read_text(encoding="utf-8").replace(
        'evidence_ids: ["EVID-01J00000000000000000000007"]',
        "evidence_ids: []",
        1,
    )
    path.write_text(text, encoding="utf-8")
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert any("non-empty" in issue.message for issue in issues)


def test_unknown_field_is_schema_error(project_copy: Path) -> None:
    path = _fact_file(project_copy)
    text = path.read_text(encoding="utf-8").replace(
        '    created_at: "2026-07-12"\n',
        '    created_at: "2026-07-12"\n    unknown_field: "not allowed"\n',
        1,
    )
    path.write_text(text, encoding="utf-8")
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert any("Additional properties" in issue.message for issue in issues)


def test_damaged_yaml_is_error(project_copy: Path) -> None:
    _fact_file(project_copy).write_text("records: [\n", encoding="utf-8")
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert any(issue.severity == "error" for issue in issues)


def test_yaml_anchor_and_alias_are_rejected() -> None:
    with pytest.raises(ForbiddenYamlFeature):
        safe_load_yaml_text("value: &shared 1\ncopy: *shared\n")


def test_duplicate_yaml_key_is_rejected() -> None:
    with pytest.raises(DuplicateKeyError):
        safe_load_yaml_text("value: 1\nvalue: 2\n")


def test_generated_id_is_a_valid_ulid() -> None:
    entity_id = generate_id("FACT")
    assert validate_id(entity_id, "FACT")


def test_id_generator_rejects_unknown_prefix() -> None:
    with pytest.raises(ValueError, match="Unsupported ID prefix"):
        generate_id("REL")


def test_refuted_without_refuting_evidence_is_schema_error(project_copy: Path) -> None:
    path = _fact_file(project_copy)
    text = path.read_text(encoding="utf-8").replace('status: "confirmed"', 'status: "refuted"', 1)
    path.write_text(text, encoding="utf-8")
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert any("refuting_evidence_ids" in issue.message for issue in issues)


def test_superseded_without_successor_is_schema_error(project_copy: Path) -> None:
    path = _fact_file(project_copy)
    text = path.read_text(encoding="utf-8").replace(
        'status: "confirmed"', 'status: "superseded"', 1
    )
    path.write_text(text, encoding="utf-8")
    issues = validate_knowledge.validate_yaml_packages(project_copy)
    assert any("superseded_by" in issue.message for issue in issues)


def test_knowledge_main_returns_success(
    monkeypatch: pytest.MonkeyPatch, project_copy: Path
) -> None:
    monkeypatch.setattr(validate_knowledge, "ROOT", project_copy)
    assert validate_knowledge.main() == 0
