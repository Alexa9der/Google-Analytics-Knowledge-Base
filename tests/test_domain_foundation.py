"""Production foundation acceptance tests."""

from __future__ import annotations

import json
from pathlib import Path

from scripts import (
    generate_index,
    validate_knowledge,
    validate_links,
    validate_markdown_frontmatter,
)

ROOT = Path(__file__).resolve().parents[1]
DEMO_IDS = {
    "CONCEPT-01J00000000000000000000001",
    "CONCEPT-01J00000000000000000000002",
    "SERVICE-01J00000000000000000000003",
    "FACT-01J00000000000000000000004",
    "FACT-01J00000000000000000000005",
    "FACT-01J00000000000000000000006",
    "EVID-01J00000000000000000000007",
    "EVID-01J00000000000000000000008",
    "VIEW-01J00000000000000000000009",
    "REPORT-01J0000000000000000000000A",
}


def _rows() -> list[dict[str, object]]:
    """Build and parse the current canonical index rows for acceptance checks."""
    return [json.loads(line) for line in generate_index.build_index(ROOT).splitlines()]


def test_production_entity_counts_and_no_demo_ids() -> None:
    """Assert the expected post-Phase-5 production inventory and absence of demo IDs."""
    rows = _rows()
    counts = {
        entity_type: sum(row["entity_type"] == entity_type for row in rows)
        for entity_type in ("fact", "evidence", "concept", "service", "view", "report")
    }
    assert counts == {
        "fact": 486,
        "evidence": 184,
        "concept": 41,
        "service": 7,
        "view": 12,
        "report": 11,
    }
    assert DEMO_IDS.isdisjoint({str(row["id"]) for row in rows})


def test_research_roadmap_references_all_services_in_order() -> None:
    """Assert that the roadmap contains every registered service in canonical order."""
    metadata, _ = validate_markdown_frontmatter.parse_front_matter(
        ROOT / "views" / "research-roadmap.md"
    )
    service_ids = [str(row["id"]) for row in _rows() if row["entity_type"] == "service"]
    assert len(metadata["reading_order"]) == 7
    assert set(metadata["reading_order"]) == set(service_ids)
    assert metadata["reading_order"] == metadata["entity_ids"]


def test_all_production_validators_pass() -> None:
    """Assert that all canonical knowledge, link, and front-matter validators pass."""
    knowledge_errors = [
        issue for issue in validate_knowledge.validate_all(ROOT) if issue.severity == "error"
    ]
    assert not knowledge_errors
    assert not [issue for issue in validate_links.validate_links(ROOT) if issue.severity == "error"]
    assert validate_markdown_frontmatter.validate_markdown(ROOT) == []
