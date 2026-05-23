#!/usr/bin/env python3
"""Validate the public pdf-to-docx-humanize skill repository."""

from __future__ import annotations

import json
import py_compile
import subprocess
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
SKILL_DIR = REPO_ROOT / "skills" / "pdf-to-docx-humanize"


REQUIRED_FILES = [
    "README.md",
    "LICENSE",
    "CONTRIBUTING.md",
    "SECURITY.md",
    ".gitignore",
    ".github/workflows/validate.yml",
    "scripts/install.ps1",
    "scripts/install.sh",
    "scripts/validate_repo.py",
    "skills/pdf-to-docx-humanize/SKILL.md",
    "skills/pdf-to-docx-humanize/agents/openai.yaml",
    "skills/pdf-to-docx-humanize/references/workflow.md",
    "skills/pdf-to-docx-humanize/references/examples.md",
    "skills/pdf-to-docx-humanize/references/lessons.md",
    "skills/pdf-to-docx-humanize/scripts/audit_bundle.py",
]


PRIVATE_PATTERNS = [
    "C:" + "\\Users\\",
    "/c/" + "Users/",
    "\\Users\\" + "Rione\\",
    "MinerU_latex_" + "978-3-031-01759-9_2053004965459886080",
    "translated_" + "full_",
]


def fail(message: str) -> None:
    print(f"ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def require_files() -> None:
    missing = [rel for rel in REQUIRED_FILES if not (REPO_ROOT / rel).exists()]
    if missing:
        fail("Missing required files:\n" + "\n".join(f"  - {item}" for item in missing))


def validate_skill_frontmatter() -> None:
    skill_md = (SKILL_DIR / "SKILL.md").read_text(encoding="utf-8")
    if not skill_md.startswith("---\n"):
        fail("SKILL.md must start with YAML front matter")
    header = skill_md.split("---", 2)[1]
    if "name: pdf-to-docx-humanize" not in header:
        fail("SKILL.md front matter must name pdf-to-docx-humanize")
    if "description:" not in header:
        fail("SKILL.md front matter must include a description")
    for phrase in ["humanize-gen-plan", "humanize-refine-plan", "humanize-rlcr", "--max 2"]:
        if phrase not in skill_md:
            fail(f"SKILL.md is missing required workflow phrase: {phrase}")


def validate_public_text() -> None:
    text_files = [
        path
        for path in REPO_ROOT.rglob("*")
        if path.is_file()
        and ".git" not in path.parts
        and path.suffix.lower() in {".md", ".py", ".ps1", ".sh", ".yaml", ".yml", ".txt"}
    ]
    for path in text_files:
        text = path.read_text(encoding="utf-8")
        for pattern in PRIVATE_PATTERNS:
            if pattern in text:
                fail(f"Private/local pattern found in {path.relative_to(REPO_ROOT)}: {pattern}")


def compile_python() -> None:
    for path in list((REPO_ROOT / "scripts").glob("*.py")) + list((SKILL_DIR / "scripts").glob("*.py")):
        py_compile.compile(str(path), doraise=True)


def run_audit_smoke_test() -> None:
    audit_script = SKILL_DIR / "scripts" / "audit_bundle.py"
    completed = subprocess.run(
        [sys.executable, str(audit_script), str(SKILL_DIR)],
        cwd=str(REPO_ROOT),
        text=True,
        capture_output=True,
        check=True,
    )
    data = json.loads(completed.stdout)
    if data.get("root") != str(SKILL_DIR.resolve()):
        fail("audit_bundle.py returned an unexpected root")
    if "scripts" not in data.get("top_level_dirs", []):
        fail("audit_bundle.py smoke test did not see expected top-level dirs")


def main() -> int:
    require_files()
    validate_skill_frontmatter()
    validate_public_text()
    compile_python()
    run_audit_smoke_test()
    print("Repository validation passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
