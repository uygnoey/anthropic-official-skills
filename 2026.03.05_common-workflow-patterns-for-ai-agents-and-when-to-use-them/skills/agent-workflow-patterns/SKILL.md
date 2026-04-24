---
name: agent-workflow-patterns
description: Helps choose and apply common AI agent workflow patterns (sequential, parallel, evaluator–optimizer). Use when designing multi-step agent systems, deciding whether to parallelize subtasks, or improving output quality with iterative evaluation.
---

# Agent workflow patterns

## Instructions

### 1) Start with a single-agent baseline
1. Try the task as a single agent call first.
2. If it meets your quality bar, stop—avoid extra orchestration.
3. If it falls short, identify whether the gap is **dependency**, **latency**, or **quality**.

### 2) Choose a pattern
Use the decision checklist in [references/decision-checklist.md](references/decision-checklist.md).

#### Sequential workflow
Use when later steps depend on earlier outputs.
- Plan explicit handoffs between stages.
- Expect higher latency because steps wait for each other.

#### Parallel workflow
Use when subtasks are independent and doing them one-by-one is too slow.
- Define your aggregation strategy before you run agents.
- Be prepared for contradictions between parallel results.

#### Evaluator–optimizer workflow
Use when first-pass quality is consistently insufficient.
- Define clear evaluation criteria.
- Set stopping rules (max iterations and pass/fail thresholds) before starting.

### 3) Add operational guardrails
- Define fallback behavior and retry logic per step.
- Track cost (token usage) and latency.
- Prefer deterministic tools (linters, tests) when possible.

## Examples

### Example: sequential (draft → review → polish)
Use a sequential workflow when each stage needs the output of the prior stage.

### Example: parallel (multi-dimension review)
Run multiple reviewers in parallel (e.g., security, correctness, style), then aggregate.

### Example: evaluator–optimizer (iterate until criteria pass)
Run a generator that drafts the output, and an evaluator that checks it against explicit criteria.

## Source
- https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
