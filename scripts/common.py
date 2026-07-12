"""Shared, dependency-light helpers for knowledge tooling."""

from __future__ import annotations

import hashlib
import json
import os
import re
import time
from dataclasses import dataclass
from datetime import date
from pathlib import Path
from typing import Any

import yaml
from yaml.constructor import ConstructorError
from yaml.nodes import MappingNode
from yaml.tokens import AliasToken, AnchorToken, TagToken

ALLOWED_PREFIXES = {"FACT", "EVID", "CONCEPT", "SERVICE", "VIEW", "REPORT"}
ENTITY_PREFIX = {
    "fact": "FACT",
    "evidence": "EVID",
    "concept": "CONCEPT",
    "service": "SERVICE",
    "view": "VIEW",
    "report": "REPORT",
}
CROCKFORD_ALPHABET = "0123456789ABCDEFGHJKMNPQRSTVWXYZ"
ID_PATTERN = re.compile(r"^(FACT|EVID|CONCEPT|SERVICE|VIEW|REPORT)-[0-7][0-9A-HJKMNP-TV-Z]{25}$")


class KnowledgeError(Exception):
    """Base class for controlled knowledge-tool failures."""


class ForbiddenYamlFeature(KnowledgeError):
    """Raised when YAML uses a deliberately unsupported feature."""


class DuplicateKeyError(KnowledgeError):
    """Raised when a YAML mapping repeats a key."""


@dataclass(frozen=True)
class ValidationIssue:
    """A structured validation result suitable for CLI and tests."""

    severity: str
    path: Path
    locator: str
    message: str

    def render(self, root: Path | None = None) -> str:
        """Return a stable human-readable representation of this issue."""
        display_path = self.path
        if root is not None:
            try:
                display_path = self.path.relative_to(root)
            except ValueError:
                pass
        return f"{self.severity.upper()} {display_path}:{self.locator}: {self.message}"


class StrictSafeLoader(yaml.SafeLoader):
    """Safe YAML loader that also rejects duplicate mapping keys."""


def _construct_mapping(
    loader: StrictSafeLoader, node: MappingNode, deep: bool = False
) -> dict[Any, Any]:
    """Construct a mapping while rejecting duplicate keys and merge keys."""
    mapping: dict[Any, Any] = {}
    for key_node, value_node in node.value:
        key = loader.construct_object(key_node, deep=deep)
        if key == "<<":
            raise ForbiddenYamlFeature("YAML merge keys are prohibited")
        try:
            duplicate = key in mapping
        except TypeError as exc:
            raise ConstructorError(
                "while constructing a mapping",
                node.start_mark,
                "found an unhashable key",
                key_node.start_mark,
            ) from exc
        if duplicate:
            raise DuplicateKeyError(f"Duplicate YAML key: {key!r}")
        mapping[key] = loader.construct_object(value_node, deep=deep)
    return mapping


StrictSafeLoader.add_constructor(
    yaml.resolver.BaseResolver.DEFAULT_MAPPING_TAG,
    _construct_mapping,
)


def reject_forbidden_yaml(text: str) -> None:
    """Reject anchors, aliases, custom tags, and merge keys before loading YAML."""
    try:
        for token in yaml.scan(text):
            if isinstance(token, AnchorToken):
                raise ForbiddenYamlFeature("YAML anchors are prohibited")
            if isinstance(token, AliasToken):
                raise ForbiddenYamlFeature("YAML aliases are prohibited")
            if isinstance(token, TagToken):
                raise ForbiddenYamlFeature("YAML custom tags are prohibited")
    except yaml.YAMLError:
        raise


def safe_load_yaml_text(text: str) -> Any:
    """Load YAML using the restricted project profile."""
    reject_forbidden_yaml(text)
    return yaml.load(text, Loader=StrictSafeLoader)


def safe_load_yaml(path: Path) -> Any:
    """Read and safely load one UTF-8 YAML file."""
    return safe_load_yaml_text(path.read_text(encoding="utf-8"))


def parse_front_matter(path: Path) -> tuple[dict[str, Any], str]:
    """Parse a Markdown file with a required YAML front matter block."""
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines(keepends=True)
    if not lines or lines[0].strip() != "---":
        raise KnowledgeError("Markdown front matter must start with '---'")
    closing = next(
        (index for index, line in enumerate(lines[1:], 1) if line.strip() == "---"), None
    )
    if closing is None:
        raise KnowledgeError("Markdown front matter has no closing '---'")
    metadata_text = "".join(lines[1:closing])
    metadata = safe_load_yaml_text(metadata_text)
    if not isinstance(metadata, dict):
        raise KnowledgeError("Markdown front matter must be a mapping")
    return metadata, "".join(lines[closing + 1 :])


def calculate_checksum(value: Any) -> str:
    """Calculate a stable SHA-256 checksum for a JSON-compatible value."""
    payload = json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))
    return hashlib.sha256(payload.encode("utf-8")).hexdigest()


def generate_id(prefix: str) -> str:
    """Generate a globally unique `<TYPE>-<ULID>` identifier.

    Args:
        prefix: One of the registered uppercase entity prefixes.

    Raises:
        ValueError: If the prefix is unsupported or not uppercase.
    """
    if prefix not in ALLOWED_PREFIXES:
        allowed = ", ".join(sorted(ALLOWED_PREFIXES))
        raise ValueError(f"Unsupported ID prefix {prefix!r}; expected one of: {allowed}")
    timestamp_ms = int(time.time() * 1000)
    if timestamp_ms >= 1 << 48:
        raise OverflowError("Current timestamp does not fit the ULID 48-bit timestamp field")
    value = (timestamp_ms << 80) | int.from_bytes(os.urandom(10), "big")
    encoded = "".join(
        CROCKFORD_ALPHABET[(value >> (5 * index)) & 31] for index in range(25, -1, -1)
    )
    entity_id = f"{prefix}-{encoded}"
    if not validate_id(entity_id, prefix):
        raise RuntimeError("Generated identifier failed internal validation")
    return entity_id


def validate_id(entity_id: str, expected_prefix: str | None = None) -> bool:
    """Return whether an ID is a valid project ULID with the expected prefix."""
    match = ID_PATTERN.fullmatch(entity_id)
    if match is None:
        return False
    return expected_prefix is None or match.group(1) == expected_prefix


def discover_yaml_packages(root: Path) -> list[Path]:
    """Return canonical YAML packages in deterministic path order."""
    knowledge = root / "knowledge"
    if not knowledge.exists():
        return []
    return sorted((*knowledge.rglob("*.yaml"), *knowledge.rglob("*.yml")))


def discover_markdown_entities(root: Path) -> list[Path]:
    """Return View and Report Markdown files in deterministic path order."""
    paths: list[Path] = []
    for directory in (root / "views", root / "reports"):
        if directory.exists():
            paths.extend(directory.rglob("*.md"))
    return sorted(paths)


def load_schema(root: Path, name: str) -> dict[str, Any]:
    """Load a JSON Schema by file name."""
    path = root / "schemas" / name
    value = json.loads(path.read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise KnowledgeError(f"Schema {name} must contain an object")
    return value


def parse_iso_date(value: str) -> date:
    """Parse an ISO 8601 calendar date."""
    try:
        return date.fromisoformat(value)
    except ValueError as exc:
        raise ValueError(f"Invalid ISO date: {value!r}") from exc


def entity_type_from_id(entity_id: str) -> str | None:
    """Return the logical entity type encoded by a valid ID prefix."""
    if not validate_id(entity_id):
        return None
    prefix = entity_id.split("-", 1)[0]
    for entity_type, candidate in ENTITY_PREFIX.items():
        if candidate == prefix:
            return entity_type
    return None


def collect_id_strings(value: Any) -> set[str]:
    """Recursively collect valid entity IDs from a structured value."""
    found: set[str] = set()
    if isinstance(value, str) and validate_id(value):
        found.add(value)
    elif isinstance(value, dict):
        for child in value.values():
            found.update(collect_id_strings(child))
    elif isinstance(value, list):
        for child in value:
            found.update(collect_id_strings(child))
    return found
