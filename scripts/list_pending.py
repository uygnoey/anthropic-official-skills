#!/usr/bin/env python3
"""List pending blog URLs (not yet processed).

Usage:
    python scripts/list_pending.py [--limit N]

Prints pending URLs to stdout, one per line.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"
SITEMAP_URL = "https://www.claude.com/sitemap.xml"
BLOG_PATTERN = re.compile(r"https://claude\.com/blog/[a-z0-9-]+")


def load_processed() -> set[str]:
    if not STATE_FILE.exists():
        return set()
    data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return set(data.get("entries", {}).keys())


def fetch_blog_urls() -> list[str]:
    req = urllib.request.Request(SITEMAP_URL, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = resp.read().decode("utf-8", errors="ignore")
    urls = sorted(set(BLOG_PATTERN.findall(body)))
    return urls


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    args = parser.parse_args()

    processed = load_processed()
    urls = fetch_blog_urls()
    pending = [u for u in urls if u not in processed]
    if args.limit:
        pending = pending[: args.limit]
    for u in pending:
        print(u)
    return 0


if __name__ == "__main__":
    sys.exit(main())
