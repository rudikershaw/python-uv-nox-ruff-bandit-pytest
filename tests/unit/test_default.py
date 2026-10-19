"""Default test."""

import runpy
from pathlib import Path

import pytest

from main import main as main_module


def test_main(caplog: pytest.LogCaptureFixture) -> None:
    with caplog.at_level("INFO"):
        runpy.run_path(str(Path(main_module.__file__)), run_name="__main__")
    assert "This is the main module." in caplog.text
