#!/usr/bin/env python3
"""Record the current UTC date as the last batch run timestamp.

Should be called exactly once at the END of each batch run (even if no posts
were processed) so the next run can distinguish NEW vs BACKLOG posts.

Usage:
    python scripts/update_last_run.py
"""
from __future__ import annotations

import datetime as dt
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE_FILE = ROOT / "state" / "processed.json"


def main() -> int:
    if STATE_FILE.exists():
        data = json.loads(STATE_FILE.read_text(encoding="utf-8"))
    else:
        data = {"description": "Map of processed blog URLs", "meta": {}, "entries": {}}

    meta = data.setdefault("meta", {})
    today = dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d")
    meta["last_run_at"] = today

    STATE_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
    )
    print(f"last_run_at = {today}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
