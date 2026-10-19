"""Enforce package structure rules."""

from pathlib import Path

import pytest

SRC = Path(__file__).parents[2] / "src"
MAX_MODULES = 4
MAX_DEPTH = 4


def _packages() -> list[Path]:
    return [p.parent for p in SRC.rglob("__init__.py")]


@pytest.mark.parametrize("package", _packages(), ids=str)
def test_modules_per_package(package: Path) -> None:
    modules = [f for f in package.glob("*.py") if f.name != "__init__.py"]
    assert len(modules) <= MAX_MODULES


def test_nesting_depth() -> None:
    deepest = max(len(p.relative_to(SRC).parts) for p in _packages())
    assert deepest <= MAX_DEPTH
