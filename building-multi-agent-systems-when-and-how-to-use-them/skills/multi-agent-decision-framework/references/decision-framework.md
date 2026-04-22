# Decision framework for multi-agent systems

This reference summarizes the post’s criteria for when multi-agent systems tend to outperform a single agent.

## Start with a single agent
Multi-agent systems add overhead (more prompts to maintain, more failure modes) and typically increase token usage substantially.

## When multi-agent is worth it
### 1) Context protection
Use subagents to isolate large, irrelevant tool outputs or intermediate reasoning that would pollute the orchestrator’s context.

Good fits:
- Subtasks that generate 1000+ tokens of intermediate output that the main agent does not need.
- Well-defined lookups/retrieval tasks where the orchestrator only needs a compact summary.

### 2) Parallelization
Use subagents to explore multiple facets in parallel (especially research/search).

Tradeoff:
- Often costs more tokens and can take longer wall-clock time if thoroughness is prioritized.

### 3) Specialization
Use specialized agents to improve reliability via:
- Focused tool sets
- Tailored system prompts/personas
- Deep domain expertise

Signals you may need tool-set specialization:
1. Tool quantity grows beyond ~20.
2. Tools span unrelated domains, causing confusion.
3. Adding tools degrades performance on tasks that used to work.

## Signals you are outgrowing single-agent architectures
- You are approaching context limits.
- You are managing ~15–20+ tools.
- You have clear parallelizable subtasks.

## Context-centric decomposition
Prefer boundaries like:
- Independent research paths
- Separate components with clean interfaces
- Black-box verification (verifier sees only what it needs)

Avoid boundaries like:
- Pure sequential phases
- Tightly coupled steps
- Work that requires heavy shared state
