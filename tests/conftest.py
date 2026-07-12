"""Shared pytest fixtures."""

from __future__ import annotations

import shutil
from pathlib import Path

import pytest


@pytest.fixture
def project_copy(tmp_path: Path) -> Path:
    """Build an isolated project from test-only knowledge fixtures."""
    source = Path(__file__).resolve().parents[1]
    target = tmp_path / "project"
    shutil.copytree(source / "tests" / "fixtures" / "valid", target)
    shutil.copytree(source / "schemas", target / "schemas")
    return target
