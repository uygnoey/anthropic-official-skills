---
name: auto-mode-permissions
description: Distills guidance from "Auto mode for Claude Code" for use in Claude Code.
---

# Auto mode permissions workflow

## Instructions
1. Choose auto mode when you want fewer permission interruptions than the default mode but more safeguards than --dangerously-skip-permissions.
2. Enable auto mode with `claude --enable-auto-mode`, then switch permission modes within a session (e.g., Shift+Tab) as needed.
3. Expect auto mode to automatically approve actions that look safe while blocking actions that look risky; if actions are repeatedly blocked, be ready to approve a prompt or adjust the plan.
4. Use isolated environments when running long tasks, and treat auto mode as risk-reducing rather than risk-eliminating.
5. If you are an admin and need to prevent use of auto mode, set the managed setting `disableAutoMode` to disable it.

## Examples
```
User: "Refactor the project to use the new config format across all packages; keep tests passing."
Assistant: "I will enable auto mode to reduce approval interruptions during the multi-file changes, and I will avoid any mass-deletion commands."
```
```
User: "Run a long migration script and update docs. Stop and ask if anything looks destructive."
Assistant: "I will proceed in auto mode for routine edits, and I will pause for confirmation if the classifier blocks an action repeatedly."
```

## Human-readable descriptions
Summarized in [../../description.en.md](../../description.en.md), [../../description.ko.md](../../description.ko.md), [../../description.es.md](../../description.es.md), [../../description.ja.md](../../description.ja.md).

## Source
Distilled from [Auto mode for Claude Code](https://claude.com/blog/auto-mode) (published 2026-03-24).
