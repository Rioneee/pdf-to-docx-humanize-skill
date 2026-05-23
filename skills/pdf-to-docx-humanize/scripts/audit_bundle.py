#!/usr/bin/env python3
"""
Lightweight bundle auditor for PDF-to-DOCX Humanize.

Prints a JSON summary of likely input roles and notable assets so the caller
can draft the task and choose a workflow path.
"""

from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass, asdict
from pathlib import Path


PDF_RE = re.compile(r"\.pdf$", re.IGNORECASE)
DOCX_RE = re.compile(r"\.docx$", re.IGNORECASE)
TEX_RE = re.compile(r"\.tex$", re.IGNORECASE)


@dataclass
class BundleAudit:
    root: str
    pdf_files: list[str]
    docx_files: list[str]
    tex_files: list[str]
    screenshot_files: list[str]
    image_files: list[str]
    top_level_dirs: list[str]


def classify_files(root: Path) -> BundleAudit:
    pdf_files: list[str] = []
    docx_files: list[str] = []
    tex_files: list[str] = []
    screenshot_files: list[str] = []
    image_files: list[str] = []

    for path in root.rglob("*"):
        if not path.is_file():
            continue
        rel = str(path.relative_to(root))
        name = path.name.lower()
        if PDF_RE.search(name):
            pdf_files.append(rel)
        elif DOCX_RE.search(name):
            docx_files.append(rel)
        elif TEX_RE.search(name):
            tex_files.append(rel)
        elif name.endswith((".png", ".jpg", ".jpeg", ".webp", ".bmp", ".tif", ".tiff")):
            image_files.append(rel)
            if any(token in name for token in ("page", "figure", "table", "shot", "screenshot")):
                screenshot_files.append(rel)

    top_level_dirs = sorted([item.name for item in root.iterdir() if item.is_dir()])
    return BundleAudit(
        root=str(root),
        pdf_files=sorted(pdf_files),
        docx_files=sorted(docx_files),
        tex_files=sorted(tex_files),
        screenshot_files=sorted(screenshot_files),
        image_files=sorted(image_files),
        top_level_dirs=top_level_dirs,
    )


def main() -> int:
    parser = argparse.ArgumentParser(description="Audit a PDF bundle for the humanize workflow.")
    parser.add_argument("bundle_root", help="Path to the input bundle folder")
    args = parser.parse_args()

    root = Path(args.bundle_root).resolve()
    if not root.exists():
        raise SystemExit(f"Missing bundle root: {root}")
    if not root.is_dir():
        raise SystemExit(f"Bundle root is not a directory: {root}")

    audit = classify_files(root)
    print(json.dumps(asdict(audit), ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
