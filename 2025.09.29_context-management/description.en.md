**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces two capabilities for long-running agents on the Claude Developer Platform: context editing (automatically removing stale tool results when near token limits) and the memory tool (persisting information outside the context window in a file-based store you control).

## When is it useful?
Use this when building agents that run for many steps or over multiple sessions, where you want to prevent context exhaustion while preserving key decisions, findings, and state across turns.

## Key points
- Context editing clears stale tool calls/results near token limits while preserving conversation flow.
- The memory tool persists information in a dedicated directory managed by the developer (client-side via tool calls).
- Claude Sonnet 4.5 is described as improving context-awareness for these workflows.

## Bundled resources
- Skill: a practical playbook for deciding what stays in context vs what should be written to persistent memory, plus a reference checklist of common “store vs keep” decisions.

## Source
- https://claude.com/blog/context-management
