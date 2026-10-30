from pathlib import Path


def test_monorepo_structure():
    """Verify presence of core architectural monorepo directories and configuration files."""
    repo_root = Path(__file__).resolve().parent.parent

    required_dirs = [
        "frontend",
        "backend",
        "worker",
        "shared",
        "shared/schemas",
        "infrastructure",
        "docs",
        "docs/adr",
        "tests",
    ]

    for d in required_dirs:
        target = repo_root / d
        assert target.is_dir(), f"Expected directory {d} to exist in repository"

    required_files = [
        "Makefile",
        "README.md",
        "LICENSE",
        ".gitignore",
        ".env.example",
        "AGENTS.md",
        "docs/architecture.md",
        "docs/adr/0001-licensing-and-ultralytics.md",
        "docs/adr/0002-technology-stack-and-architecture.md",
        ".github/workflows/ci.yml",
        "backend/requirements.txt",
        "backend/alembic.ini",
        "frontend/package.json",
        "frontend/vite.config.js",
    ]

    for f in required_files:
        target = repo_root / f
        assert target.is_file(), f"Expected file {f} to exist in repository"
