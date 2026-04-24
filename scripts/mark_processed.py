#!/usr/bin/env python3
"""Mark a blog URL as processed in state/processed.json.

The on-disk layout is one folder per blog post at the repo root as
`<YYYY.MM.DD>_<blog-slug>/`, where <blog-slug> is the last path segment of
the blog URL and the date prefix is `--source-date` (required if the folder
does not yet exist with a prefix).

Usage:
    python scripts/mark_processed.py <url> [--source-date YYYY-MM-DD]

Notes:
    A legacy positional <slug> argument (the skill name) is accepted for
    backward compatibility but ignored. The blog slug is always derived
    from the URL. If a folder without a date prefix exists at <blog-slug>/
    and --source-date is provided, it is renamed (via `git mv` when
    available) to `<YYYY.MM.DD>_<blog-slug>/`.
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("url")
    parser.add_argument(
        "legacy_slug",
        nargs="?",
        default=None,
        help="(deprecated) legacy skill name; ignored if provided",
    )
    parser.add_argument("--source-date", default=None)
    args = parser.parse_args()

    import re
    import subprocess

    bare_slug = args.url.rstrip("/").rsplit("/", 1)[-1]

    # Prefer a folder that already has a date prefix, otherwise look for the
    # bare slug. If --source-date is provided and the folder is bare, rename
    # it in-place so the repo stays consistent.
    prefixed_dir = None
    date_iso_re = re.compile(r"^(\d{4})-(\d{2})-(\d{2})$")
    for entry in ROOT.iterdir():
        if not entry.is_dir():
            continue
        if entry.name.endswith(f"_{bare_slug}") and re.match(r"^\d{4}\.\d{2}\.\d{2}_", entry.name):
            prefixed_dir = entry
            break

    if prefixed_dir is not None:
        final_slug = prefixed_dir.name
    elif args.source_date and date_iso_re.match(args.source_date):
        final_slug = f"{args.source_date.replace('-', '.')}_{bare_slug}"
        bare_dir = ROOT / bare_slug
        target = ROOT / final_slug
        if bare_dir.exists() and not target.exists():
            try:
                subprocess.run(
                    ["git", "mv", bare_slug, final_slug],
                    cwd=ROOT,
                    check=True,
                    capture_output=True,
                    text=True,
                )
            except subprocess.CalledProcessError:
                bare_dir.rename(target)
            # Normalize source.json inside the renamed folder if present.
            sj = target / "source.json"
            if sj.exists():
                try:
                    sdata = json.loads(sj.read_text(encoding="utf-8"))
                    sdata["blog_slug"] = final_slug
                    sj.write_text(
                        json.dumps(sdata, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8",
                    )
                except Exception:
                    pass
    else:
        final_slug = bare_slug

    post_dir = ROOT / final_slug

    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    else:
        data = {"description": "Map of processed blog URLs", "meta": {}, "entries": {}}

    data.setdefault("meta", {})
    data.setdefault("entries", {})[args.url] = {
        "blog_slug": final_slug,
        "processed_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_date": args.source_date,
    }

    STATE_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Marked processed: {args.url} -> {post_dir.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
