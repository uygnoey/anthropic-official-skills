**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post surveys five common multi-agent coordination patterns—generator-verifier, orchestrator-subagent, agent teams, message bus, and shared state—and explains their mechanics, trade-offs, and selection guidance.

## When is it useful?
Useful when you’ve decided a multi-agent system is appropriate and need to choose (or evolve) a coordination architecture based on task decomposition, context boundaries, information flow, and operational constraints.

## Key points
- Start with the simplest pattern that could work, observe failure modes, then evolve.
- Generator-verifier fits quality-critical output with explicit evaluation criteria and bounded iteration.
- Orchestrator-subagent fits clear decomposition and bounded subtasks, but can become an information bottleneck.
- Agent teams fit long-running independent subtasks with persistent worker context, but need careful partitioning.
- Message bus fits event-driven pipelines and growing ecosystems, but increases debugging/routing complexity.
- Shared state fits collaborative work with direct sharing of findings, but needs strong termination conditions to avoid reactive loops.

## Bundled resources
- Skill: choosing and applying multi-agent coordination patterns, including a quick selection table and evolution guidelines.

## Source
- https://claude.com/blog/multi-agent-coordination-patterns
