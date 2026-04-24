#!/usr/bin/env python3
"""Rename blog post folders to include a YYYY.MM.DD_ date prefix.

Reads each `<slug>/source.json` for `published_date`, and renames the folder
to `<YYYY.MM.DD>_<slug>/`. Also updates `state/processed.json` entries so
`blog_slug` reflects the new folder name.

Idempotent: folders already starting with a valid date prefix are left alone
(their `source.json` and state entries are still normalized for safety).

Usage:
    python3 scripts/rename_with_date_prefix.py            # apply
    python3 scripts/rename_with_date_prefix.py --dry-run
"""
from __future__ import annotations

import json
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"

DATE_PREFIX_RE = re.compile(r"^(\d{4})\.(\d{2})\.(\d{2})_(.+)$")
ISO_DATE_RE = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")


def iter_post_dirs() -> list[Path]:
    posts: list[Path] = []
    for entry in sorted(ROOT.iterdir()):
        if not entry.is_dir():
            continue
        if entry.name.startswith("."):
            continue
        if entry.name in {"scripts", "state", "cron_tracking", "skills"}:
            continue
        if (entry / "source.json").exists():
            posts.append(entry)
    return posts


def main() -> int:
    dry_run = "--dry-run" in sys.argv
    state = json.loads(STATE_FILE.read_text(encoding="utf-8")) if STATE_FILE.exists() else {"entries": {}}
    entries: dict = state.get("entries", {})

    # Reverse lookup: current blog_slug -> list of urls.
    slug_to_urls: dict[str, list[str]] = {}
    for url, entry in entries.items():
        slug = entry.get("blog_slug", "")
        slug_to_urls.setdefault(slug, []).append(url)

    renamed = 0
    for post in iter_post_dirs():
        source = json.loads((post / "source.json").read_text(encoding="utf-8"))
        date = source.get("published_date", "")
        if not ISO_DATE_RE.match(date or ""):
            print(f"skip (no ISO date): {post.name}")
            continue

        prefix = date.replace("-", ".")
        m = DATE_PREFIX_RE.match(post.name)
        if m:
            existing_prefix = f"{m.group(1)}.{m.group(2)}.{m.group(3)}"
            bare_slug = m.group(4)
            if existing_prefix == prefix:
                # Already correctly prefixed; just make sure source.json + state agree.
                new_name = post.name
            else:
                new_name = f"{prefix}_{bare_slug}"
        else:
            bare_slug = post.name
            new_name = f"{prefix}_{bare_slug}"

        new_path = ROOT / new_name
        source_slug = source.get("blog_slug", bare_slug)

        if post.name == new_name:
            # Normalize source.json + state only.
            if source_slug != new_name:
                if dry_run:
                    print(f"WOULD NORMALIZE source.json: {post.name}  blog_slug -> {new_name}")
                else:
                    source["blog_slug"] = new_name
                    (post / "source.json").write_text(
                        json.dumps(source, indent=2, ensure_ascii=False) + "\n",
                        encoding="utf-8",
                    )
                    print(f"normalized source.json: {post.name}")
            # Make sure state entries also point to the prefixed name.
            for url in slug_to_urls.get(bare_slug, []) + slug_to_urls.get(new_name, []):
                cur = entries.get(url, {})
                if cur.get("blog_slug") != new_name:
                    if dry_run:
                        print(f"WOULD UPDATE state entry {url} -> {new_name}")
                    else:
                        cur["blog_slug"] = new_name
            continue

        if new_path.exists():
            print(f"ERROR target exists: {new_path}")
            continue

        if dry_run:
            print(f"WOULD RENAME: {post.name}  ->  {new_name}")
        else:
            # Use `git mv` so history is preserved.
            try:
                subprocess.run(
                    ["git", "mv", post.name, new_name],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                    text=True,
                )
            except subprocess.CalledProcessError as e:
                # Fall back to plain rename (e.g. not in a git repo).
                print(f"  (git mv failed, falling back to os.rename: {e.stderr.strip()})")
                post.rename(new_path)
            # Update source.json inside the renamed folder.
            sj = new_path / "source.json"
            try:
                data = json.loads(sj.read_text(encoding="utf-8"))
                data["blog_slug"] = new_name
                sj.write_text(
                    json.dumps(data, indent=2, ensure_ascii=False) + "\n",
                    encoding="utf-8",
                )
            except Exception as e:
                print(f"  (could not update source.json: {e})")
            print(f"renamed: {post.name}  ->  {new_name}")

        # Update any state entries.
        for url in slug_to_urls.get(bare_slug, []):
            cur = entries.get(url, {})
            if cur.get("blog_slug") != new_name:
                if dry_run:
                    print(f"  WOULD UPDATE state entry {url} -> {new_name}")
                else:
                    cur["blog_slug"] = new_name
        renamed += 1

    if not dry_run:
        STATE_FILE.write_text(
            json.dumps(state, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
        )

    print(f"\n{'would rename' if dry_run else 'renamed'} {renamed} folder(s).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
