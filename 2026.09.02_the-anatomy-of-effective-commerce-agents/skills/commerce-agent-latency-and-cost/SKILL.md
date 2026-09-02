---
name: commerce-agent-latency-and-cost
description: Make a commerce agent fast and affordable by attacking task-completion latency, perceived latency, and prompt-caching hit rate separately. Covers the three latency levers (fewer turns, faster tools, faster tokens), pre-loading context, parallel tool use, eager dispatch, progressive streaming and progress lines, the three-segment cache layout that reaches 90-99% hit rates, and how to sweep models and effort levels against quality, latency and per-task cost. Use when an agent feels slow, when per-task cost is too high, or when choosing a model and configuration.
---

# Commerce agent latency and cost

Latency and cost are two views of the same structure: how many model turns a task takes, how big
the prefix is on each of them, and how much of that prefix is cached.

Task-completion latency decomposes as:

```
(model turns × time to last token) + tool processing time
```

## Instructions

### 1. Pull the three latency levers

**Fewer turns.** Pre-load the context the agent is likely to need, use a more capable model, and
let the model call tools in parallel.

**Faster tools.** Optimize the backends the tools call, and dispatch tools eagerly instead of
waiting for the full turn.

**Faster tokens.** Choose model and configuration by running an eval sweep, not by intuition.

### 2. Pre-load context the agent will obviously need

If the user arrives from a product page, inject that product. If a merchant arrives from a
dashboard, inject the figures already on screen. Each avoided lookup is a whole model turn
removed from the critical path.

### 3. Let intelligence buy back turns

A smarter model produces fewer tokens per second but often needs fewer turns on complex queries,
and the turn count usually dominates. Measure end to end rather than comparing token rates.

### 4. Enable parallel tool calls

Commerce constantly needs several independent lookups at once — searching multiple products,
querying several policy documents, fetching several slices of sales data. Configure the agent so
the model can issue multiple tool calls in one turn, and make sure your executor actually runs
them concurrently.

### 5. Dispatch tools eagerly

Start executing a tool as soon as its arguments have finished streaming, while the rest of the
turn is still being generated. This turns multi-second gaps into hundreds of milliseconds.

### 6. Attack perceived latency separately

- **Stream components progressively.** A 500-700 token response should not land as one block;
  break it into progressive renders.
- **Show the work.** Emit a short progress line for each step — "finding hotels near the water".
  Build these from the tool arguments, or add a dedicated `user_facing_message` parameter to the
  tool schema so the model writes the line itself.

### 7. Get prompt caching to 90-99%

Caching is the single largest cost lever. Cached input reads cost a tenth of fresh tokens; a
cache write carries roughly a 1.25x premium that pays for itself on the second use. Cached tokens
are also about 1.5-2x faster at around 100k tokens.

Lay the context out in three segments ordered by how often they change — global, session,
volatile — and roll the breakpoints forward each turn. Full layout and the common mistakes are
in [references/prompt-cache-segments.md](references/prompt-cache-segments.md).

### 8. Choose the model by sweep, not by default

Define quality, latency and cost metrics, run the full eval suite across candidate models and
effort levels, and re-tune prompts per model. Measure **per-task** cost, not per-call cost.
The procedure is in [references/model-selection-sweep.md](references/model-selection-sweep.md).

When the result is close, and the cost fits your per-task economics and latency, choose
intelligence.

## Examples

### A slow search turn

A shopper asks for "a waterproof jacket under $150 and matching gloves". Before: two sequential
search turns, each waiting on a full generation, ~6s. After: parallel tool calls put both
searches in one turn, eager dispatch starts the first search while the second is still
streaming, and a progress line ("checking jackets and gloves") renders immediately. Same result,
one turn.

### A cache miss that costs real money

A deployment injected the current timestamp into the system prompt "for freshness". Every
session was a full cache miss on the global segment. Moving the timestamp to the end of the
volatile segment restored the byte-identical global prefix and took hit rate from near zero to
the 90s.

### A model sweep that changed the answer

Candidate A was cheaper per call but needed 40% more turns on multi-constraint searches and
failed more often, so retries pushed its per-task cost above candidate B. The sweep, not the
price sheet, produced the decision.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (published 2026-09-02)
