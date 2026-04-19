#!/usr/bin/env python3
"""Mark a blog URL as processed in state/processed.json.

The on-disk layout is one folder per blog post under posts/<blog-slug>/,
where <blog-slug> is the last path segment of the blog URL.

Usage:
    python scripts/mark_processed.py <url> [--source-date YYYY-MM-DD]

Notes:
    A legacy positional <slug> argument (the skill name) is accepted for
    backward compatibility but ignored. The blog slug is always derived
    from the URL.
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

    blog_slug = args.url.rstrip("/").rsplit("/", 1)[-1]
    post_dir = ROOT / "posts" / blog_slug

    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    else:
        data = {"description": "Map of processed blog URLs", "meta": {}, "entries": {}}

    data.setdefault("meta", {})
    data.setdefault("entries", {})[args.url] = {
        "blog_slug": blog_slug,
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
