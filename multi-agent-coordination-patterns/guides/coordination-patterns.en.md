**English** · [한국어](./coordination-patterns.ko.md) · [Español](./coordination-patterns.es.md) · [日本語](./coordination-patterns.ja.md)

# Multi-agent coordination patterns: selection guide

## What is this guide?
A compact guide to selecting and evolving between five multi-agent coordination patterns described in the post.

## When is it useful?
Use it when you already decided a multi-agent approach is warranted and need an architecture that matches your task structure and operational constraints.

## Quick selection table

| Situation | Pattern |
| --- | --- |
| Quality-critical output with explicit evaluation criteria | Generator-verifier |
| Clear task decomposition with bounded subtasks | Orchestrator-subagent |
| Parallel, independent, long-running subtasks | Agent teams |
| Event-driven pipeline, growing agent ecosystem | Message bus |
| Collaborative work where agents build on each other’s findings | Shared state |
| No single point of failure required | Shared state |

## How to evolve
- Start with the simplest pattern that could work.
- Observe the primary failure mode.
- Evolve only when the failure mode is persistent and structural.

## Source
- https://claude.com/blog/multi-agent-coordination-patterns
