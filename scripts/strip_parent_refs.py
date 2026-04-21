#!/usr/bin/env python3
"""Remove ../ references from artifact files (SKILL.md, agents/*.md, etc.).

Rules applied, in order, per artifact file:

1. Drop any *entire line* that contains a `../` markdown link or bare `../` path.
   This removes summary lines like "Summarized in [../../description.en.md](...), ..."
   and companion bullets like "- Guide: [../../guides/foo.md](...)" that cross
   the artifact boundary.
2. Collapse runs of blank lines left behind by deletions.
3. Trim trailing whitespace and ensure file ends with a single newline.
4. Remove obsolete section headers that become empty after the line drops:
   - "## Companion resources", "## Related resources", "## Related files",
     "## Human-readable descriptions" with no remaining bullets.

Usage:
    python3 scripts/strip_parent_refs.py            # apply changes
    python3 scripts/strip_parent_refs.py --dry-run  # print what would change
"""
from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent

ARTIFACT_GLOBS = (
    "*/skills/*/SKILL.md",
    "*/agents/*.md",
    "*/hooks/*.md",
    "*/output-styles/*.md",
)

PARENT_RE = re.compile(r"\.\./[\w./-]+")

EMPTY_SECTIONS = (
    "## Companion resources",
    "## Related resources",
    "## Related files",
    "## Human-readable descriptions",
    "## Related artifacts",
    "## See also",
)


def line_has_parent_ref(line: str) -> bool:
    return bool(PARENT_RE.search(line))


def collapse_blank_runs(lines: list[str]) -> list[str]:
    out: list[str] = []
    prev_blank = False
    for ln in lines:
        blank = not ln.strip()
        if blank and prev_blank:
            continue
        out.append(ln)
        prev_blank = blank
    # Trim trailing blank lines.
    while out and not out[-1].strip():
        out.pop()
    return out


def drop_empty_sections(lines: list[str]) -> list[str]:
    """Remove `## Header\\n(blank | bullets)*` blocks where no non-blank non-bullet
    content remains after the header and only if header is in EMPTY_SECTIONS."""
    result: list[str] = []
    i = 0
    while i < len(lines):
        stripped = lines[i].strip()
        if stripped in EMPTY_SECTIONS:
            # Look ahead to next `##` header or EOF.
            j = i + 1
            body = []
            while j < len(lines) and not lines[j].lstrip().startswith("## "):
                body.append(lines[j])
                j += 1
            # If body contains no real content (only blanks), drop the whole section.
            has_content = any(b.strip() for b in body)
            if not has_content:
                i = j
                continue
        result.append(lines[i])
        i += 1
    return result


def process_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text(encoding="utf-8")
    lines = original.splitlines()
    kept = [ln for ln in lines if not line_has_parent_ref(ln)]
    if kept == lines:
        return False
    kept = collapse_blank_runs(kept)
    kept = drop_empty_sections(kept)
    kept = collapse_blank_runs(kept)
    new_text = "\n".join(kept) + "\n"
    if new_text == original:
        return False
    if dry_run:
        print(f"WOULD UPDATE: {path.relative_to(REPO)}")
    else:
        path.write_text(new_text, encoding="utf-8")
        print(f"updated: {path.relative_to(REPO)}")
    return True


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    changed = 0
    for pattern in ARTIFACT_GLOBS:
        for path in sorted(REPO.glob(pattern)):
            if process_file(path, dry_run):
                changed += 1
    print(f"\n{'would update' if dry_run else 'updated'} {changed} file(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
