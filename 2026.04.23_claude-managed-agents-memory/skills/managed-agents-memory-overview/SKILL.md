---
name: managed-agents-memory-overview
description: Conceptual guidance for using built-in, filesystem-based memory with Claude Managed Agents (portable memories, enterprise controls, and operational considerations).
---

## Instructions
Use this skill when you need to interpret or plan around Claude Managed Agents memory, especially for production deployments.

Focus on:
1) **Cross-session learning goals**: Define what the agent should remember across sessions (user preferences, recurring domain facts, verification outcomes) and what it should not.
2) **Filesystem-based organization**: Treat memories as files the agent can read/write using its normal tooling (bash and code execution).
3) **Portability and governance**: Plan for exporting, redacting, rolling back, and auditing memory changes.
4) **Shared vs per-user stores**: Consider separate stores with different access scopes (e.g., org-wide read-only vs per-user read/write).

## Examples
### Example: Turn a post summary into implementation questions
- What categories of information should be persisted across sessions?
- Which memory stores exist (org-wide, team, per-user), and what are their access scopes?
- How will we review and audit what was learned (session events, audit logs)?
- What is our policy for redaction/rollback when incorrect or sensitive content is retained?

### Example: Draft a small rollout checklist
- Start with a limited-scope store (e.g., per-team) and a narrow memory policy.
- Validate that changes are traceable (session events/audit logs).
- Test export and rollback procedures.

## Source
- https://claude.com/blog/claude-managed-agents-memory
