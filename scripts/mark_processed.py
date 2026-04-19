#!/usr/bin/env python3
"""Mark a blog URL as processed in state/processed.json.

Usage:
    python scripts/mark_processed.py <url> <slug> [--source-date YYYY-MM-DD]
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
    parser.add_argument("slug")
    parser.add_argument("--source-date", default=None)
    args = parser.parse_args()

    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    else:
        data = {"description": "Map of processed blog URLs", "meta": {}, "entries": {}}

    data.setdefault("meta", {})
    data.setdefault("entries", {})[args.url] = {
        "slug": args.slug,
        "processed_at": dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "source_date": args.source_date,
    }

    STATE_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"Marked processed: {args.url} -> skills/{args.slug}/")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
