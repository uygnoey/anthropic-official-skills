# check-tests Stop hook

Blocks the main Claude Code agent from ending its turn while `npm test` is failing. Feeds a `decision: "block"` response back so the model sees the failure and fixes it before finishing. Uses `stop_hook_active` to avoid infinite loops.

## Install

1. Copy [`check-tests.sh`](./check-tests.sh) into your project as `.claude/hooks/check-tests.sh` and `chmod +x` it.
2. Merge [`check-tests.json`](./check-tests.json) into your `.claude/settings.json` (or user-level `~/.claude/settings.json`).

One-liner from the repo root (adjust the source path to wherever you cloned this repo):

```bash
mkdir -p .claude/hooks
cp path/to/skills-from-claude-blog/posts/subagents-in-claude-code/hooks/check-tests.sh .claude/hooks/check-tests.sh
chmod +x .claude/hooks/check-tests.sh
```

## Script reference

The executable script lives in [`check-tests.sh`](./check-tests.sh) next to this file. The full listing:

```bash
#!/bin/bash
INPUT=$(cat)
STOP_HOOK_ACTIVE=$(echo "$INPUT" | jq -r '.stop_hook_active // false')

# Don't loop forever — if we already blocked once this turn, let it through
if [ "$STOP_HOOK_ACTIVE" = "true" ]; then
  exit 0
fi

if ! npm test --silent > /dev/null 2>&1; then
  jq -n '{
    decision: "block",
    reason: "Tests are failing. Run `npm test` to see the failures and fix them before finishing."
  }'
  exit 0
fi

exit 0
```

## Notes

- Requires `jq` on PATH.
- Only meaningful in projects where `npm test` is the authoritative test command. Adapt per project.
- Consider scoping to a matcher if you don't want it running on every Stop event.

## Source

Distilled from [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (published 2026-04-07).
