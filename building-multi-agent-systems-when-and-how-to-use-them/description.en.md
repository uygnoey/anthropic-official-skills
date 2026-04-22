**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains when multi-agent systems outperform a single agent, and how to decompose and verify work safely.

## When is it useful?
Use these ideas when a single agent starts failing due to context pollution, when you need parallel exploration, or when specialization improves reliability.

## Key points
- Start with a single agent; multi-agent systems add overhead and token cost.
- Use multi-agent systems primarily for context protection, parallelization, and specialization.
- Prefer context-centric decomposition (split by context boundaries, not by “phase”).
- Use a verification subagent to independently validate outputs, with explicit criteria to avoid “early victory.”

## Bundled resources
- Skill: multi-agent-decision-framework
- Examples: context protection, parallel research, specialization routing, verification subagent loop

## Source
- https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them
