#!/usr/bin/env python3
"""Rebuild the `## Index` table in README.md from the filesystem.

For every post folder matching `<YYYY.MM.DD>_<slug>/` that has a
`source.json`, emit one table row:

    | [<title>](<url>) | <YYYY-MM-DD> | <artifact summary> |

Rows are sorted newest published_date first, then by slug for ties.

The artifact summary is derived from the folder contents:

- `skills/<name>/SKILL.md`      -> 1 skill
- `agents/<name>.md`            -> 1 agent
- `hooks/<name>.json`           -> 1 hook
- `guides/<stem>.{en,ko,es,ja}.md` (grouped by stem) -> 1 guide
- `output-styles/<name>.md`     -> 1 style
- `plugin/.claude-plugin/plugin.json` -> 1 plugin

Pieces are joined as "N skill + N agent + N hook + N guide + N style + N plugin",
dropping any that are zero. If everything is zero, writes "(no artifacts)".

After rewriting README.md, runs `sync_readme_index.py` to keep the 3
translated READMEs in sync.

Usage:
    python3 scripts/rebuild_readme_index.py
    python3 scripts/rebuild_readme_index.py --dry-run
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
README = ROOT / "README.md"
SYNC_SCRIPT = ROOT / "scripts" / "sync_readme_index.py"

FOLDER_RE = re.compile(r"^(\d{4})\.(\d{2})\.(\d{2})_(.+)$")
INDEX_HEADER = "## Index"
# Match the table block: header row | sep row | N data rows, terminated by a
# blank line or the next `## ` header.
TABLE_RE = re.compile(
    r"(\| Blog post \| Published \| Artifacts \|\s*\n\|[-| ]+\|\s*\n)(?:\|[^\n]*\n)*",
)


def collect_posts() -> list[dict]:
    posts = []
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir():
            continue
        m = FOLDER_RE.match(entry.name)
        if not m:
            continue
        source = entry / "source.json"
        if not source.exists():
            continue
        data = json.loads(source.read_text(encoding="utf-8"))
        y, mo, d, slug = m.group(1), m.group(2), m.group(3), m.group(4)
        posts.append(
            {
                "folder": entry,
                "date_iso": f"{y}-{mo}-{d}",
                "slug": slug,
                "title": data.get("title", slug),
                "url": data.get("url", ""),
            }
        )
    posts.sort(key=lambda p: (p["date_iso"], p["slug"]), reverse=True)
    return posts


def summarize_artifacts(folder: Path) -> str:
    parts: list[str] = []
    # skills
    skills_dir = folder / "skills"
    n_skills = (
        sum(1 for d in skills_dir.iterdir() if d.is_dir() and (d / "SKILL.md").exists())
        if skills_dir.exists()
        else 0
    )
    if n_skills:
        parts.append(f"{n_skills} skill")
    # agents
    agents_dir = folder / "agents"
    n_agents = (
        sum(1 for f in agents_dir.iterdir() if f.is_file() and f.suffix == ".md")
        if agents_dir.exists()
        else 0
    )
    if n_agents:
        parts.append(f"{n_agents} agent")
    # hooks
    hooks_dir = folder / "hooks"
    n_hooks = (
        sum(1 for f in hooks_dir.iterdir() if f.is_file() and f.suffix == ".json")
        if hooks_dir.exists()
        else 0
    )
    if n_hooks:
        parts.append(f"{n_hooks} hook")
    # guides (group by stem, only count if all 4 langs present)
    guides_dir = folder / "guides"
    n_guides = 0
    if guides_dir.exists():
        stems: dict[str, set[str]] = {}
        for f in guides_dir.iterdir():
            if not f.is_file():
                continue
            m = re.match(r"(.+)\.(en|ko|es|ja)\.md$", f.name)
            if not m:
                continue
            stems.setdefault(m.group(1), set()).add(m.group(2))
        n_guides = sum(1 for langs in stems.values() if len(langs) >= 1)
    if n_guides:
        parts.append(f"{n_guides} guide")
    # output-styles
    styles_dir = folder / "output-styles"
    n_styles = (
        sum(1 for f in styles_dir.iterdir() if f.is_file() and f.suffix == ".md")
        if styles_dir.exists()
        else 0
    )
    if n_styles:
        parts.append(f"{n_styles} style")
    # plugin
    if (folder / "plugin" / ".claude-plugin" / "plugin.json").exists():
        parts.append("1 plugin")
    return " + ".join(parts) if parts else "(no artifacts)"


def build_table(posts: list[dict]) -> str:
    lines = [
        "| Blog post | Published | Artifacts |",
        "|---|---|---|",
    ]
    for p in posts:
        artifacts = summarize_artifacts(p["folder"])
        # Escape pipes in titles so they don't break the markdown table layout.
        safe_title = p["title"].replace("|", "\\|")
        lines.append(f"| [{safe_title}]({p['url']}) | {p['date_iso']} | {artifacts} |")
    return "\n".join(lines) + "\n"


def rewrite_readme(new_table: str) -> bool:
    text = README.read_text(encoding="utf-8")
    match = TABLE_RE.search(text)
    if not match:
        print("ERROR: could not locate existing index table in README.md")
        return False
    new_text = text[: match.start()] + new_table + text[match.end() :]
    if new_text == text:
        return False
    README.write_text(new_text, encoding="utf-8")
    return True


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    posts = collect_posts()
    table = build_table(posts)
    if dry_run:
        print(table)
        print(f"# {len(posts)} posts")
        return 0

    changed = rewrite_readme(table)
    print(f"README.md: {'updated' if changed else 'unchanged'} ({len(posts)} rows)")

    # Always sync translated READMEs, even if en README is unchanged —
    # a prior sync may have failed (e.g. broken header marker) and left
    # the translated files out of date.
    if SYNC_SCRIPT.exists():
        subprocess.run([sys.executable, str(SYNC_SCRIPT)], check=True)

    return 0


if __name__ == "__main__":
    sys.exit(main())
