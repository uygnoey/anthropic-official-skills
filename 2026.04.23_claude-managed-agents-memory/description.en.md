**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post announces public beta support for built-in, filesystem-based memory in Claude Managed Agents.

## When is it useful?
It’s useful when you want production agents that improve across sessions without building and operating your own memory infrastructure.

## Key points
- Memory is designed for long-running agents that learn across sessions and can share learnings across agents.
- Memory mounts directly onto a filesystem so agents can work with memories using familiar tooling (bash and code execution).
- Memories are portable files with enterprise controls (scoped permissions, audit logs, export/rollback/redaction, and programmatic management via API).
- Updates appear as session events in the Claude Console for traceability.

## Bundled resources
- Skill: managed-agents-memory-overview (conceptual overview and implementation considerations)
- Guide: managed-agents-memory (deployment/operations checklist)

## Source
https://claude.com/blog/claude-managed-agents-memory
