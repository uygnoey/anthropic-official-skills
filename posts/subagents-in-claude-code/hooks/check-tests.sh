#!/bin/bash
# Stop hook: if `npm test` is failing, block the main agent from ending its turn
# and feed the failure back so it fixes the tests before finishing.
#
# Source: https://claude.com/blog/subagents-in-claude-code (published 2026-04-07)
# Install path expected by the companion hook JSON: .claude/hooks/check-tests.sh
# Requires: jq on PATH, `npm test` as the authoritative test command in the project.

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
