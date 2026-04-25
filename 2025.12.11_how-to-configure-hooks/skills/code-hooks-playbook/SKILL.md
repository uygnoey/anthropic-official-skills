---
name: code-hooks-playbook
description: "Configure and maintain Claude Code hooks: choosing lifecycle events, writing matchers, selecting hook types (command vs prompt), and applying safety/operational best practices. Use when a user wants to automate Claude Code workflows via hooks or needs help authoring or reviewing hook JSON and companion scripts."
---

# Claude Code hooks playbook

## Instructions

Use this skill to help users design, implement, and review Claude Code hooks based on established patterns.

### 1) Choose the right lifecycle event

Common events and when to use them:

- **PreToolUse**: Validate inputs before a tool runs (e.g., path rules before `Write`).
- **PostToolUse**: Run follow-up actions (e.g., formatting after `Write`/`Edit`).
- **PermissionRequest**: Gate sensitive commands (e.g., restrict which `Bash(...)` commands can be approved).
- **SessionStart**: Print or log context at the beginning of a session.
- **UserPromptSubmit**: Inject dynamic context right when the user submits a prompt.
- **PreCompact**: Save backups before compaction.
- **Stop / SubagentStop**: Insert review prompts to enforce completeness/quality.

For concrete JSON examples, see:

- [Hook examples](./examples/hook-examples.md)

### 2) Write matchers carefully

- Matchers are **case-sensitive**.
- Prefer narrow matchers when validating/gating (e.g., `Write`, `Bash(npm test*)`) to avoid unexpected execution.

### 3) Pick hook types

- Use **command** hooks to run shell commands.
- Use **prompt** hooks to inject an evaluation checklist or completion gate.

### 4) Safety and operational best practices

- Treat hook stdin as untrusted input: validate/sanitize and quote variables.
- Prefer absolute paths for scripts.
- Avoid processing sensitive files (like `.env` or credentials).
- Hooks execute with your user permissions; do not approve hooks you do not understand.

### 5) Understand runtime behavior

- Default timeout is **60 seconds** (can be configured per hook).
- If multiple hooks match, they may run in **parallel**, and identical commands may be deduplicated.
- Hook config edits require review/approval via the `/hooks` menu before taking effect.

## Examples

- Auto-format after edits: see `hooks/posttooluse-format-written-files.json`.
- Completion gate on Stop: see `hooks/stop-completion-check.json`.
- Logging wrapper that forwards the hook payload to another command: see `hooks/log-wrapper.sh`.

## References

- [Full post notes](./references/post-notes.md)
