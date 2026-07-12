"""Tests for View and Report front matter."""

from __future__ import annotations

from pathlib import Path

import pytest

from scripts import validate_markdown_frontmatter


def test_fixture_markdown_is_valid(project_copy: Path) -> None:
    assert validate_markdown_frontmatter.validate_markdown(project_copy) == []


def test_broken_markdown_reference_is_error(project_copy: Path) -> None:
    path = project_copy / "views" / "example-verification.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            "EVID-01J00000000000000000000008",
            "EVID-01J0000000000000000000000C",
        ),
        encoding="utf-8",
    )
    issues = validate_markdown_frontmatter.validate_markdown(project_copy)
    assert any("unknown referenced ID" in issue.message for issue in issues)


def test_unknown_frontmatter_field_is_error(project_copy: Path) -> None:
    path = project_copy / "reports" / "example-report.md"
    path.write_text(
        path.read_text(encoding="utf-8").replace(
            'title: "Fixture validation report"',
            'title: "Fixture validation report"\nunknown_field: true',
        ),
        encoding="utf-8",
    )
    issues = validate_markdown_frontmatter.validate_markdown(project_copy)
    assert any("Additional properties" in issue.message for issue in issues)


def test_markdown_main_exit_codes(monkeypatch: pytest.MonkeyPatch, project_copy: Path) -> None:
    monkeypatch.setattr(validate_markdown_frontmatter, "ROOT", project_copy)
    assert validate_markdown_frontmatter.main() == 0
    (project_copy / "views" / "example-verification.md").write_text(
        "no front matter", encoding="utf-8"
    )
    assert validate_markdown_frontmatter.main() == 1
