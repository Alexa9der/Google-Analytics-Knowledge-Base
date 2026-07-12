"""Generate the deterministic, derived INDEX.jsonl entity locator."""

from __future__ import annotations

import argparse
import json
import os
import sys
import tempfile
from pathlib import Path
from typing import Any

import yaml

if __package__ in {None, ""}:
    sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from scripts.common import (
    KnowledgeError,
    calculate_checksum,
    collect_id_strings,
    discover_markdown_entities,
    discover_yaml_packages,
    parse_front_matter,
    safe_load_yaml,
)

ROOT = Path(__file__).resolve().parents[1]


def _title(entity_type: str, record: dict[str, Any]) -> str:
    """Select the human-readable title for an indexed entity."""
    fields = {
        "fact": "title",
        "evidence": "summary",
        "concept": "preferred_label",
        "service": "name",
        "view": "title",
        "report": "title",
    }
    return str(record.get(fields[entity_type], ""))[:240]


def _aliases(entity_type: str, record: dict[str, Any]) -> list[str]:
    """Return searchable aliases without canonical body text."""
    if entity_type in {"concept", "service"}:
        values = record.get("synonyms", record.get("aliases", []))
        return [str(value) for value in values] if isinstance(values, list) else []
    return []


def _updated_at(entity_type: str, record: dict[str, Any]) -> str | None:
    """Select the most relevant entity update date."""
    candidates = {
        "fact": ("last_verified_at", "created_at"),
        "evidence": ("last_verified_at", "retrieved_at"),
        "concept": ("last_reviewed_at", "created_at"),
        "service": ("last_reviewed_at", "created_at"),
        "view": ("updated_at",),
        "report": ("created_at",),
    }
    for key in candidates[entity_type]:
        value = record.get(key)
        if isinstance(value, str):
            return value
    return None


def _scope_summary(entity_type: str, record: dict[str, Any]) -> str:
    """Build a short locator summary without copying full canonical knowledge."""
    if entity_type == "fact":
        value: Any = record.get("scope", {})
    elif entity_type == "evidence":
        value = record.get("source_location", "")
    elif entity_type in {"concept", "service"}:
        value = record.get("boundaries", "")
    else:
        value = record.get("question", record.get("research_question", ""))
    if isinstance(value, (dict, list)):
        text = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    else:
        text = str(value)
    return text[:240]


def _index_record(
    *,
    entity_type: str,
    record: dict[str, Any],
    domain: str,
    owner: str,
    path: Path,
    locator: str,
    root: Path,
) -> dict[str, Any]:
    """Convert a canonical entity into its compact index projection."""
    entity_id = str(record["id"])
    title = _title(entity_type, record)
    aliases = _aliases(entity_type, record)
    related_ids = sorted(collect_id_strings(record) - {entity_id})
    search_terms = sorted({term.lower() for term in [title, *aliases, entity_type, domain] if term})
    return {
        "id": entity_id,
        "entity_type": entity_type,
        "title": title,
        "aliases": aliases,
        "domain": domain,
        "status": record.get("status"),
        "owner": record.get("owner", owner),
        "path": path.relative_to(root).as_posix(),
        "record_locator": locator,
        "updated_at": _updated_at(entity_type, record),
        "checksum": calculate_checksum(record),
        "scope_summary": _scope_summary(entity_type, record),
        "related_ids": related_ids,
        "search_terms": search_terms,
    }


def build_index(root: Path = ROOT) -> str:
    """Build and serialize the complete deterministic index."""
    rows: list[dict[str, Any]] = []
    for path in discover_yaml_packages(root):
        package = safe_load_yaml(path)
        if not isinstance(package, dict):
            raise KnowledgeError(f"{path}: package must be a mapping")
        entity_type = package.get("entity_type")
        records = package.get("records")
        if not isinstance(entity_type, str) or not isinstance(records, list):
            raise KnowledgeError(f"{path}: invalid package metadata or records")
        for index, record in enumerate(records):
            if not isinstance(record, dict) or "id" not in record:
                raise KnowledgeError(f"{path}: records[{index}] is not an entity mapping")
            rows.append(
                _index_record(
                    entity_type=entity_type,
                    record=record,
                    domain=str(package.get("domain", "")),
                    owner=str(package.get("owner", "")),
                    path=path,
                    locator=f"records[{index}]",
                    root=root,
                )
            )
    for path in discover_markdown_entities(root):
        record, _ = parse_front_matter(path)
        entity_type = "view" if path.parent.name == "views" else "report"
        rows.append(
            _index_record(
                entity_type=entity_type,
                record=record,
                domain="navigation" if entity_type == "view" else "reports",
                owner=str(record.get("owner", record.get("author", ""))),
                path=path,
                locator="front_matter",
                root=root,
            )
        )
    rows.sort(key=lambda row: str(row["id"]))
    ids = [row["id"] for row in rows]
    if len(ids) != len(set(ids)):
        raise KnowledgeError("Cannot generate index: duplicate entity IDs")
    return "".join(
        json.dumps(row, ensure_ascii=False, sort_keys=True, separators=(",", ":")) + "\n"
        for row in rows
    )


def write_index(content: str, root: Path = ROOT) -> None:
    """Atomically replace INDEX.jsonl with fully generated content."""
    destination = root / "INDEX.jsonl"
    temporary: Path | None = None
    try:
        with tempfile.NamedTemporaryFile(
            mode="w",
            encoding="utf-8",
            newline="\n",
            prefix=".index-",
            suffix=".jsonl",
            dir=root,
            delete=False,
        ) as handle:
            handle.write(content)
            handle.flush()
            os.fsync(handle.fileno())
            temporary = Path(handle.name)
        os.replace(temporary, destination)
    finally:
        if temporary is not None and temporary.exists():
            temporary.unlink()


def check_index(content: str, root: Path = ROOT) -> bool:
    """Return whether the tracked index exactly matches generated content."""
    destination = root / "INDEX.jsonl"
    return destination.exists() and destination.read_text(encoding="utf-8") == content


def main(argv: list[str] | None = None) -> int:
    """Run index generation or freshness checking."""
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Check freshness without writing")
    args = parser.parse_args(argv)
    try:
        content = build_index(ROOT)
        if args.check:
            if not check_index(content, ROOT):
                print("ERROR INDEX.jsonl is missing or stale")
                return 1
            print("OK INDEX.jsonl is current")
            return 0
        write_index(content, ROOT)
        print(f"OK indexed {content.count(chr(10))} entities")
        return 0
    except (OSError, ValueError, yaml.YAMLError, KnowledgeError) as exc:
        print(f"ERROR index generation failed: {exc}")
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
