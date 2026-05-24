"""Nox sessions for testing, linting, and formatting."""

from nox import Session, options
from nox_uv import session

options.default_venv_backend = "uv"
options.reuse_existing_virtualenvs = True
options.sessions = ["lint", "security", "tests"]


@session(uv_no_install_project=True, uv_quiet=True, uv_groups=["lint", "dev"])
def lint(session: Session) -> None:
    """Run linters."""
    session.run("ruff", "check", "src", "tests", "noxfile.py")
    session.run("ruff", "format", "--check", "--diff", "src", "tests", "noxfile.py")
    session.run("mypy", "src", "noxfile.py")


@session(uv_no_install_project=True, uv_quiet=True, uv_groups=["lint"])
def format_apply(session: Session) -> None:
    """Format code with ruff."""
    session.run("ruff", "check", "--fix", "src", "tests", "noxfile.py")
    session.run("ruff", "format", "src", "tests", "noxfile.py")


@session(uv_no_install_project=True, uv_quiet=True, uv_groups=["lint"])
def security(session: Session) -> None:
    """Audit dependencies for security vulnerabilities."""
    session.run("bandit", "-r", "src")
    session.run("uv", "audit", external=True)


@session(uv_quiet=True, uv_groups=["test"])
def tests(session: Session) -> None:
    """Run tests with pytest and check coverage."""
    session.run(
        "pytest",
        "tests",
        "--doctest-modules",
    )
