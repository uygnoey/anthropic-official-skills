# Choosing model and configuration

Model selection is a measurement problem across two axes — intelligence and latency — bounded by
a cost budget.

## 1. Define the metrics first

- **Quality thresholds** — task completion, relevance, grounding.
- **Latency** — p50 and p99, not the average.
- **Cost budget** — expressed per task.

## 2. Sweep

Run the **full** eval suite across every candidate model and every candidate effort level. A
partial suite hides the failure modes that drive retries.

## 3. Iterate

Prompts tune to specific models. A prompt that works on a larger model will usually need more
explicit instruction to work on a smaller one — smaller models need spelled out what larger ones
infer. Re-tune before concluding a model is worse.

## 4. Measure per-task cost

Per-call cost is misleading. Account for:

- turn count per task,
- failure and retry rates,
- the extra turns a less capable model spends recovering.

## The tie-breaker

> When the result is close, and the cost fits your per-task economics and latency, choose
> intelligence.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
