#!/usr/bin/env python3
"""List pending blog URLs, with two-tier priority.

Priority:
  TIER 1 — NEW posts (published after the last batch run): newest → oldest
  TIER 2 — BACKLOG posts (older than the last batch run): oldest → newest
  TIER 3 — Posts only in sitemap.xml (no known date): alphabetical

"Last batch run" is read from state/processed.json -> meta.last_run_at.
If missing, TIER 1 is empty and everything dated goes into TIER 2.

Each output line:
    <url>\t<YYYY-MM-DD or "unknown">\t<tier: NEW|BACKLOG|UNKNOWN>

Usage:
    python scripts/list_pending.py [--limit N] [--urls-only]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import urllib.request
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"

SITEMAP_URL = "https://www.claude.com/sitemap.xml"
BLOG_INDEX_URL = "https://www.claude.com/blog"
UA = {"User-Agent": "Mozilla/5.0"}

BLOG_URL_PATTERN = re.compile(r"https://claude\.com/blog/[a-z0-9-]+")
INDEX_LINK_PATTERN = re.compile(r'href="/blog/([a-z0-9-]+)"')
INDEX_DATE_PATTERN = re.compile(r"([A-Z][a-z]+) (\d{1,2}), (20\d{2})")


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def load_state() -> dict:
    if not STATE_FILE.exists():
        return {"description": "", "meta": {}, "entries": {}}
    return json.loads(STATE_FILE.read_text(encoding="utf-8"))


def fetch_sitemap_urls() -> list[str]:
    body = _fetch(SITEMAP_URL)
    return sorted(set(BLOG_URL_PATTERN.findall(body)))


def fetch_blog_index() -> list[tuple[str, str]]:
    """Return [(url, 'YYYY-MM-DD' | 'unknown'), ...] from the /blog page.

    The page renders each card with a link then a human date. We walk the HTML
    in order, pairing each first-seen slug with the next date after it.
    """
    html = _fetch(BLOG_INDEX_URL)

    link_positions: list[tuple[int, str]] = []
    seen: set[str] = set()
    for m in INDEX_LINK_PATTERN.finditer(html):
        slug = m.group(1)
        if slug in seen:
            continue
        seen.add(slug)
        link_positions.append((m.start(), slug))

    date_positions = [(m.start(), m.group(0)) for m in INDEX_DATE_PATTERN.finditer(html)]

    results: list[tuple[str, str]] = []
    di = 0
    for pos, slug in link_positions:
        while di < len(date_positions) and date_positions[di][0] < pos:
            di += 1
        if di >= len(date_positions):
            date_str = "unknown"
        else:
            try:
                date_str = datetime.strptime(
                    date_positions[di][1], "%B %d, %Y"
                ).strftime("%Y-%m-%d")
            except ValueError:
                date_str = "unknown"
        results.append((f"https://claude.com/blog/{slug}", date_str))
    return results


def build_pending(state: dict) -> list[tuple[str, str, str]]:
    processed: set[str] = set(state.get("entries", {}).keys())
    last_run = (state.get("meta", {}) or {}).get("last_run_at")  # "YYYY-MM-DD" or None

    try:
        index_entries = fetch_blog_index()
    except Exception as e:  # noqa: BLE001
        print(f"# warn: blog index fetch failed: {e}", file=sys.stderr)
        index_entries = []

    index_urls: set[str] = set()
    new_tier: list[tuple[str, str]] = []        # published > last_run
    backlog_dated: list[tuple[str, str]] = []   # published <= last_run (or no last_run)
    backlog_unknown: list[tuple[str, str]] = [] # date couldn't be parsed

    for url, date in index_entries:
        index_urls.add(url)
        if url in processed:
            continue
        if date == "unknown":
            backlog_unknown.append((url, date))
        elif last_run and date > last_run:
            new_tier.append((url, date))
        else:
            backlog_dated.append((url, date))

    # TIER 1: new posts — newest first
    new_tier.sort(key=lambda ud: ud[1], reverse=True)
    # TIER 2: backlog — oldest first (user preference)
    backlog_dated.sort(key=lambda ud: ud[1], reverse=False)

    pending: list[tuple[str, str, str]] = []
    for url, date in new_tier:
        pending.append((url, date, "NEW"))
    for url, date in backlog_dated:
        pending.append((url, date, "BACKLOG"))
    for url, date in backlog_unknown:
        pending.append((url, date, "UNKNOWN"))

    # TIER 3: sitemap-only leftovers (alphabetical).
    try:
        sitemap_urls = fetch_sitemap_urls()
    except Exception as e:  # noqa: BLE001
        print(f"# warn: sitemap fetch failed: {e}", file=sys.stderr)
        sitemap_urls = []
    for url in sitemap_urls:
        if url in processed or url in index_urls:
            continue
        pending.append((url, "unknown", "UNKNOWN"))

    return pending


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--urls-only",
        action="store_true",
        help="Print URLs only (no date/tier columns)",
    )
    args = parser.parse_args()

    state = load_state()
    pending = build_pending(state)
    if args.limit:
        pending = pending[: args.limit]

    for url, date, tier in pending:
        if args.urls_only:
            print(url)
        else:
            print(f"{url}\t{date}\t{tier}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
