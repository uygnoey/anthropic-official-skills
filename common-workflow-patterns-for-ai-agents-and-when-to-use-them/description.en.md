**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains three production-proven workflow patterns for AI agents—sequential, parallel, and evaluator–optimizer—and how to choose between them.

## When is it useful?
Use it when you’re designing multi-step agent systems and need to trade off latency, cost, and reliability by choosing an execution pattern that matches your task.

## Key points
- Start simple: try a single agent first, then graduate to workflows only if needed.
- Sequential workflows fit dependency chains, but add latency.
- Parallel workflows reduce wall-clock time for independent subtasks, but require an aggregation strategy and may increase cost.
- Evaluator–optimizer improves quality via iteration, but increases token usage and needs clear stopping criteria.

## Bundled resources
- A reusable "decision checklist" and pattern descriptions converted into an Agent Skill.

## Source
- https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
