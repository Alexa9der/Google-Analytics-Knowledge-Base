"""Tests for deterministic and atomic index generation."""

from __future__ import annotations

import json
from pathlib import Path

import pytest
import yaml

from scripts import generate_index
from scripts.common import KnowledgeError


def test_generation_indexes_all_fixture_entities(project_copy: Path) -> None:
    content = generate_index.build_index(project_copy)
    rows = [json.loads(line) for line in content.splitlines()]
    assert len(rows) == 10
    assert [row["id"] for row in rows] == sorted(row["id"] for row in rows)


def test_index_is_deterministic(project_copy: Path) -> None:
    assert generate_index.build_index(project_copy) == generate_index.build_index(project_copy)


def test_check_mode_detects_current_and_stale_index(project_copy: Path) -> None:
    content = generate_index.build_index(project_copy)
    (project_copy / "INDEX.jsonl").write_text("stale\n", encoding="utf-8")
    assert not generate_index.check_index(content, project_copy)
    generate_index.write_index(content, project_copy)
    assert generate_index.check_index(content, project_copy)
    (project_copy / "INDEX.jsonl").write_text("stale\n", encoding="utf-8")
    assert not generate_index.check_index(content, project_copy)


def test_index_omits_full_fact_statement_and_evidence_excerpt(project_copy: Path) -> None:
    content = generate_index.build_index(project_copy)
    assert "accepts exactly one fixture input" not in content
    assert "fixture excerpt must not enter index" not in content


def test_failed_build_does_not_replace_existing_index(project_copy: Path) -> None:
    destination = project_copy / "INDEX.jsonl"
    destination.write_text("sentinel\n", encoding="utf-8")
    broken = project_copy / "knowledge" / "facts" / "broken.yaml"
    broken.write_text("records: [\n", encoding="utf-8")
    with pytest.raises(yaml.YAMLError):
        generate_index.build_index(project_copy)
    assert destination.read_text(encoding="utf-8") == "sentinel\n"


def test_generator_main_exit_codes(project_copy: Path, monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr(generate_index, "ROOT", project_copy)
    assert generate_index.main([]) == 0
    assert generate_index.main(["--check"]) == 0
    (project_copy / "knowledge" / "facts" / "broken.yaml").write_text("[", encoding="utf-8")
    assert generate_index.main([]) == 1


def test_build_rejects_duplicate_ids(project_copy: Path) -> None:
    source = project_copy / "knowledge" / "concepts" / "core.yaml"
    text = source.read_text(encoding="utf-8")
    duplicate = text.replace(
        "CONCEPT-01J00000000000000000000002",
        "CONCEPT-01J00000000000000000000001",
    )
    source.write_text(duplicate, encoding="utf-8")
    with pytest.raises(KnowledgeError, match="duplicate entity IDs"):
        generate_index.build_index(project_copy)
