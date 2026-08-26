#!/usr/bin/env python3
"""Collect recent human feedback on an agent's output and emit it as JSON.

Reference implementation of the collection step described in Warp's self-improvement loop:
the improver skill authenticates, "ran a bundled Python script to pull recent issues with
feedback, summarized findings into JSON, and identified concrete signals."

This version reads GitHub issues (or pull requests) that the agent commented on and gathers the
human replies that followed. It shells out to the `gh` CLI, so it inherits whatever
authentication the scheduled run already established.

Usage:
    ./collect_feedback.py --repo owner/name --since 7d --out feedback.json
    ./collect_feedback.py --repo owner/name --kind pr --agent-login my-agent[bot]
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from datetime import datetime, timedelta, timezone

DURATION_RE = re.compile(r"^(\d+)([dhw])$")
UNIT_HOURS = {"h": 1, "d": 24, "w": 24 * 7}


def parse_since(value: str) -> datetime:
    m = DURATION_RE.match(value)
    if not m:
        raise argparse.ArgumentTypeError("expected a duration like 7d, 24h or 2w")
    amount, unit = int(m.group(1)), m.group(2)
    return datetime.now(timezone.utc) - timedelta(hours=amount * UNIT_HOURS[unit])


def gh_json(args: list[str]) -> object:
    proc = subprocess.run(["gh", *args], capture_output=True, text=True)
    if proc.returncode != 0:
        sys.exit(f"gh {' '.join(args)} failed: {proc.stderr.strip()}")
    return json.loads(proc.stdout or "[]")


def list_items(repo: str, kind: str, limit: int) -> list[dict]:
    cmd = [kind, "list", "--repo", repo, "--state", "all", "--limit", str(limit),
           "--json", "number,title,url,updatedAt"]
    return gh_json(cmd)  # type: ignore[return-value]


def item_comments(repo: str, kind: str, number: int) -> list[dict]:
    data = gh_json([kind, "view", str(number), "--repo", repo, "--json", "comments"])
    return data.get("comments", []) if isinstance(data, dict) else []


def collect(repo: str, kind: str, since: datetime, agent_login: str, limit: int) -> list[dict]:
    records = []
    for item in list_items(repo, kind, limit):
        updated = datetime.fromisoformat(item["updatedAt"].replace("Z", "+00:00"))
        if updated < since:
            continue
        comments = item_comments(repo, kind, item["number"])
        agent_said = [c for c in comments if c.get("author", {}).get("login") == agent_login]
        if not agent_said:
            continue
        humans = [c for c in comments if c.get("author", {}).get("login") != agent_login]
        if not humans:
            continue
        records.append({
            "number": item["number"],
            "title": item["title"],
            "url": item["url"],
            "updated_at": item["updatedAt"],
            "agent_output": [c["body"] for c in agent_said],
            "human_feedback": [
                {"author": c.get("author", {}).get("login"), "body": c["body"],
                 "created_at": c.get("createdAt")}
                for c in humans
            ],
        })
    return records


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--repo", required=True, help="owner/name")
    ap.add_argument("--kind", choices=["issue", "pr"], default="issue")
    ap.add_argument("--since", type=parse_since, default="14d",
                    help="only items updated within this window (e.g. 7d, 24h, 2w)")
    ap.add_argument("--agent-login", default="github-actions[bot]",
                    help="login the agent posts under")
    ap.add_argument("--limit", type=int, default=100, help="how many items to scan")
    ap.add_argument("--out", help="write JSON here instead of stdout")
    args = ap.parse_args()

    since = args.since if isinstance(args.since, datetime) else parse_since(args.since)
    records = collect(args.repo, args.kind, since, args.agent_login, args.limit)
    payload = json.dumps({"repo": args.repo, "kind": args.kind,
                          "since": since.isoformat(), "items": records}, indent=2)
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(payload + "\n")
        print(f"wrote {len(records)} item(s) to {args.out}", file=sys.stderr)
    else:
        print(payload)


if __name__ == "__main__":
    main()
