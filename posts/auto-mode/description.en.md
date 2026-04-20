**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
Introduces Auto mode in Claude Code: a permissions mode where Claude can approve many tool actions automatically while using safeguards to block risky behavior.

## When is it useful?
Useful when you want to run longer Claude Code tasks with fewer approval interruptions, but you do not want to fully bypass permissions with --dangerously-skip-permissions.

## Key points
- Default Claude Code permissions prompt on every file write and bash command; auto mode is designed to reduce those interruptions.
- Before each tool call, a classifier checks for potentially destructive actions (e.g., mass deletion, sensitive data exfiltration, malicious code execution).
- Safe actions proceed automatically; risky actions are blocked and Claude is redirected to try a different approach, with a user prompt as a fallback if blocked repeatedly.
- Auto mode reduces risk versus skipping permissions, but does not eliminate risk; it is still recommended to use it in isolated environments.
- Enable with `claude --enable-auto-mode` (then cycle modes with Shift+Tab); admins can disable via managed setting `disableAutoMode`.

## Bundled resources
- 1 skill (auto-mode-permissions)

## Source
- Auto mode for Claude Code (2026-03-24): https://claude.com/blog/auto-mode
