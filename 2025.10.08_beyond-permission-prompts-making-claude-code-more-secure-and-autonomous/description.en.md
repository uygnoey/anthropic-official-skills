**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces two new Claude Code features built on **native sandboxing** to make agentic coding more secure and more autonomous: a sandboxed bash tool (research preview) and Claude Code on the web (cloud sandbox).

## When is it useful?
Use these ideas when you want Claude Code (or another coding agent) to run more actions without repeated permission prompts, while reducing risk from prompt injection and other unintended tool use.

## Key points
- Claude Code’s baseline model is permission-based (read-only by default), but frequent approvals can cause “approval fatigue.”
- The post argues sandboxing is safer and more autonomous than per-action permissions.
- Effective sandboxing requires both **filesystem isolation** (limit what files/directories can be read/written) and **network isolation** (limit what hosts can be contacted).
- The sandboxed bash tool enforces restrictions using OS primitives (e.g., bubblewrap on Linux, seatbelt on macOS).
- Claude Code on the web runs each session in an isolated cloud sandbox while keeping sensitive credentials outside the sandbox, using a proxy for git operations.

## Bundled resources
- No ready-to-run policy files, hook configs, or scripts are provided in the post; it mainly describes concepts and product features.

## Source
- https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
