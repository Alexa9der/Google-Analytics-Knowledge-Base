"""Tests for supersession symmetry and cycle detection."""

from __future__ import annotations

from pathlib import Path

from scripts import validate_links


def test_asymmetric_supersession_is_error(project_copy: Path) -> None:
    path = project_copy / "knowledge" / "facts" / "core.yaml"
    text = path.read_text(encoding="utf-8").replace(
        '    title: "Fixture response relationship"',
        '    supersedes:\n      - "FACT-01J00000000000000000000005"\n'
        '    title: "Fixture response relationship"',
    )
    path.write_text(text, encoding="utf-8")
    issues = validate_links.validate_links(project_copy)
    assert any("asymmetric supersession" in issue.message for issue in issues)


def test_supersedes_cycle_is_detected(project_copy: Path) -> None:
    path = project_copy / "knowledge" / "facts" / "core.yaml"
    text = path.read_text(encoding="utf-8")
    text = text.replace(
        '    title: "One fixture input"',
        '    supersedes:\n      - "FACT-01J00000000000000000000006"\n'
        '    title: "One fixture input"',
    )
    text = text.replace(
        '    title: "Fixture response relationship"',
        '    supersedes:\n      - "FACT-01J00000000000000000000005"\n'
        '    title: "Fixture response relationship"',
    )
    path.write_text(text, encoding="utf-8")
    issues = validate_links.validate_links(project_copy)
    assert any("supersedes cycle detected" in issue.message for issue in issues)
