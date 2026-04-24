---
name: native-sandboxing-basics
description: Establish safer, more autonomous boundaries for agentic coding by applying filesystem and network isolation (a "native sandboxing" approach) so the agent can operate with fewer per-action permission prompts.
---

## Instructions

Use this skill when you want an agent to operate autonomously inside a clearly bounded environment.

1. Define the threat model.
   - Assume a prompt-injected or otherwise compromised agent may try to read sensitive files, modify files outside the project, or exfiltrate data over the network.
2. Apply **filesystem isolation**.
   - Decide which directories are in-scope for read/write.
   - Default to allowing read/write only within the current working directory (the project root) and deny modifications outside it.
3. Apply **network isolation**.
   - Decide which hosts/domains are allowed.
   - Default to denying outbound network access, or allow-list only what the workflow requires (e.g., your VCS host).
4. Prefer sandboxing boundaries over repeated approvals.
   - Avoid designs that require constant manual approvals (approval fatigue).
   - Instead, let the agent work freely within the sandbox, and require explicit confirmation only when crossing sandbox boundaries.
5. Start the sandboxed runtime.
   - In Claude Code, run: `claude --sandbox`.

## Examples

### Example: Document a project sandbox policy
- Filesystem boundary: allow read/write under `./` only.
- Network boundary: allow-list only the domains required for your workflow.
- Escalation: if the agent requests access outside the boundaries, treat it as a high-signal event and review before approving.

### Example: Review a proposed sandbox configuration
Checklist:
- Does it include both filesystem and network isolation?
- Is the default restrictive enough to prevent accidental data exposure?
- Are exceptions (paths/domains) minimal and justified by the workflow?

## Notes
- This post describes product features and concepts; it does not include complete configuration files or hook examples.

## Source
- https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous
