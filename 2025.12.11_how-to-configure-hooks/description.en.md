**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?

This post explains how to configure Claude Code hooks to automate repetitive steps, enforce project rules, and inject context into coding sessions.

## When is it useful?

Use it when you want Claude Code to run commands or prompts automatically at key lifecycle events (before/after tool use, session start/end, compaction, stop events, etc.).

## Key points

- Hooks are configured with JSON that maps lifecycle events (for example: PreToolUse, PostToolUse, SessionStart, Stop) to one or more hook actions.
- Hook actions can run commands or prompt-based checks.
- Matchers are case-sensitive, and multiple matching hooks may run in parallel.
- Hooks run with your user permissions; validate/sanitize stdin and be careful around sensitive files.
- There is a default timeout (60 seconds) that can be configured.

## Bundled resources

- A reusable hook wrapper script for logging hook input/output: `hooks/log-wrapper.sh`
- Example hook configs for common patterns:
  - Validate file paths before writing (`hooks/pretooluse-validate-write-path.json`)
  - Restrict test commands via PermissionRequest (`hooks/permissionrequest-validate-tests.json`)
  - Auto-format files after Write/Edit (`hooks/posttooluse-format-written-files.json`)
  - Backup transcripts before compaction (`hooks/precompact-backup-transcript.json`)
  - Show project context on SessionStart (`hooks/sessionstart-show-context.json`)
  - Log sessions on SessionStart (`hooks/sessionstart-log-session.json`)
  - Require completion check on Stop (`hooks/stop-completion-check.json`)
  - Review subagent outputs on SubagentStop (`hooks/subagentstop-review.json`)
  - Load sprint context on UserPromptSubmit (`hooks/userpromptsubmit-inject-context.json`)

## Source

- https://claude.com/blog/how-to-configure-hooks
