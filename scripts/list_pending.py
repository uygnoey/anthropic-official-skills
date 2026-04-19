#!/usr/bin/env python3
"""List pending blog URLs, newest first.

Priority order:
  1. Posts appearing on https://www.claude.com/blog (newest → oldest as rendered)
  2. Posts only found in sitemap.xml (appended at the end, alphabetical)

Each line printed:
    <url>\t<YYYY-MM-DD or "unknown">

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
# Matches the blog index HTML: each card exposes href="/blog/<slug>" then
# eventually a human date like "April 14, 2026".
INDEX_LINK_PATTERN = re.compile(r'href="/blog/([a-z0-9-]+)"')
INDEX_DATE_PATTERN = re.compile(
    r"([A-Z][a-z]+) (\d{1,2}), (20\d{2})"
)


def _fetch(url: str) -> str:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8", errors="ignore")


def load_processed() -> set[str]:
    if not STATE_FILE.exists():
        return set()
    data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    return set(data.get("entries", {}).keys())


def fetch_sitemap_urls() -> list[str]:
    body = _fetch(SITEMAP_URL)
    return sorted(set(BLOG_URL_PATTERN.findall(body)))


def fetch_blog_index() -> list[tuple[str, str]]:
    """Return [(url, 'YYYY-MM-DD'), ...] in the order rendered on /blog.

    The blog index renders each card as: a hero link, then metadata including
    a date. We walk the HTML once, alternately collecting the first unseen
    slug and the next date that follows it. The on-page order is newest-first,
    so preserving index order yields a newest-first list.
    """
    html = _fetch(BLOG_INDEX_URL)

    # Collect match positions for slugs and dates.
    link_iter = list(INDEX_LINK_PATTERN.finditer(html))
    date_iter = list(INDEX_DATE_PATTERN.finditer(html))

    # Deduplicate slugs keeping first occurrence (cards often repeat links).
    seen: set[str] = set()
    slug_positions: list[tuple[int, str]] = []
    for m in link_iter:
        slug = m.group(1)
        if slug in seen:
            continue
        seen.add(slug)
        slug_positions.append((m.start(), slug))

    date_positions = [(m.start(), m.group(0)) for m in date_iter]

    # For each slug, pick the nearest date whose position is >= slug position.
    results: list[tuple[str, str]] = []
    di = 0
    for pos, slug in slug_positions:
        while di < len(date_positions) and date_positions[di][0] < pos:
            di += 1
        if di >= len(date_positions):
            date_str = "unknown"
        else:
            raw = date_positions[di][1]
            try:
                date_str = datetime.strptime(raw, "%B %d, %Y").strftime("%Y-%m-%d")
            except ValueError:
                date_str = "unknown"
        results.append((f"https://claude.com/blog/{slug}", date_str))
    return results


def build_pending(processed: set[str]) -> list[tuple[str, str]]:
    # 1) Blog index — newest first (sorted by date desc; unknown dates last).
    try:
        index_entries = fetch_blog_index()
    except Exception as e:  # noqa: BLE001
        print(f"# warn: blog index fetch failed: {e}", file=sys.stderr)
        index_entries = []
    index_urls: set[str] = set()
    dated: list[tuple[str, str]] = []
    for url, date in index_entries:
        index_urls.add(url)
        if url in processed:
            continue
        dated.append((url, date))
    # Sort: known dates descending first, then unknowns in original order.
    dated.sort(key=lambda ud: (ud[1] == "unknown", ud[1]), reverse=False)
    # The above puts unknowns last but dates ascending. Reverse the dated-only part.
    known = sorted([ud for ud in dated if ud[1] != "unknown"], key=lambda ud: ud[1], reverse=True)
    unknown = [ud for ud in dated if ud[1] == "unknown"]
    pending: list[tuple[str, str]] = known + unknown

    # 2) Sitemap-only (alphabetical), appended after the index-sourced ones.
    try:
        sitemap_urls = fetch_sitemap_urls()
    except Exception as e:  # noqa: BLE001
        print(f"# warn: sitemap fetch failed: {e}", file=sys.stderr)
        sitemap_urls = []
    for url in sitemap_urls:
        if url in processed or url in index_urls:
            continue
        pending.append((url, "unknown"))

    return pending


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--limit", type=int, default=None)
    parser.add_argument(
        "--urls-only",
        action="store_true",
        help="Print URLs only (no date column)",
    )
    args = parser.parse_args()

    processed = load_processed()
    pending = build_pending(processed)
    if args.limit:
        pending = pending[: args.limit]

    for url, date in pending:
        if args.urls_only:
            print(url)
        else:
            print(f"{url}\t{date}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
