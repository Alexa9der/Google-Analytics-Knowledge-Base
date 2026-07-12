"""Tests for global IDs and typed links."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts import validate_links


def _facts(root: Path) -> Path:
    return root / "knowledge" / "facts" / "core.yaml"


def test_fixture_links_are_valid(project_copy: Path) -> None:
    issues = validate_links.validate_links(project_copy)
    assert not [issue for issue in issues if issue.severity == "error"]


def test_invalid_prefix_is_error(project_copy: Path) -> None:
    path = _facts(project_copy)
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "FACT-01J00000000000000000000004",
            "EVID-01J00000000000000000000004",
        ),
        encoding="utf-8",
    )
    issues = validate_links.validate_links(project_copy)
    assert any("does not match entity type" in issue.message for issue in issues)


def test_broken_reference_is_error(project_copy: Path) -> None:
    path = _facts(project_copy)
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "EVID-01J00000000000000000000007",
            "EVID-01J0000000000000000000000B",
        ),
        encoding="utf-8",
    )
    issues = validate_links.validate_links(project_copy)
    assert any("broken reference" in issue.message for issue in issues)


def test_evidence_link_to_concept_is_type_error(project_copy: Path) -> None:
    path = _facts(project_copy)
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "EVID-01J00000000000000000000007",
            "CONCEPT-01J00000000000000000000001",
        ),
        encoding="utf-8",
    )
    issues = validate_links.validate_links(project_copy)
    assert any("targets concept, expected evidence" in issue.message for issue in issues)


def test_confirmed_without_evidence_is_link_error(project_copy: Path) -> None:
    path = _facts(project_copy)
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            'evidence_ids: ["EVID-01J00000000000000000000007"]',
            "evidence_ids: []",
            1,
        ),
        encoding="utf-8",
    )
    issues = validate_links.validate_links(project_copy)
    assert any("confirmed Fact requires Evidence" in issue.message for issue in issues)


def test_candidate_without_evidence_is_warning_only(project_copy: Path) -> None:
    issues = validate_links.validate_links(project_copy)
    candidate_issues = [issue for issue in issues if "candidate Fact" in issue.message]
    assert candidate_issues and all(issue.severity == "warning" for issue in candidate_issues)


def test_global_duplicate_id_is_error(project_copy: Path) -> None:
    path = project_copy / "knowledge" / "concepts" / "core.yaml"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "CONCEPT-01J00000000000000000000002",
            "CONCEPT-01J00000000000000000000001",
        ),
        encoding="utf-8",
    )
    issues = validate_links.validate_links(project_copy)
    assert any("duplicate ID" in issue.message for issue in issues)


def test_link_main_returns_success(monkeypatch: pytest.MonkeyPatch, project_copy: Path) -> None:
    monkeypatch.setattr(validate_links, "ROOT", project_copy)
    assert validate_links.main() == 0
