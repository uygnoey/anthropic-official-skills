---
name: intelligence-cost-routing
description: Decide which work gets a frontier model and which gets a smaller one by measuring task completion ratio alongside cost per task, then sending the frontier model only the work where the extra capability changes the outcome. Use when frontier pricing limits how widely a model can be deployed, when justifying a more expensive model for a subset of work, or when comparing models whose per-token price differs but whose token usage and wrong-turn rate also differ.
---

# Balancing intelligence against cost across a large deployment

Frontier capability comes at a frontier price, and Yusuke Kaji, General Manager of AI for Business at
Rakuten, is direct that cost decides how widely he can deploy: "As a large enterprise, we want to
balance intelligence and cost."

This skill describes the routing pattern as the post presents it.

## Instructions

### 1. Measure two numbers together, not one

Kaji's team measures **task completion ratio** alongside **cost per task**.

Neither number decides anything alone. A cheap model with a low completion ratio produces work that
gets redone; an expensive model with a high completion ratio may still be the wrong choice for work
that the cheap model finishes fine. The pair is the signal.

Record both per task class with
[templates/task-routing-record.md](templates/task-routing-record.md).

### 2. Route by whether extra capability changes the outcome

The rule the post states: send Fable 5 the work where the extra capability *changes the outcome*, and
let smaller models keep the rest.

This is a per-task-class decision, not a per-organization one. The question is not "is this model
better" but "on this class of task, does the better model produce a different result?" Where the answer
is no, the routing decision is already made.

### 3. Count the second-order costs, not just the per-token price

Kaji names two things that make the math work in Fable 5's favor:

- **It gets more done with fewer tokens and fewer wrong turns.** A higher per-token price does not
  settle the comparison if the cheaper model spends its run recovering from a bad early path.
- **It needs less hand-holding.** Human check-ins are a real cost that does not appear in a token bill.

The reference for how these signals relate to the model's self-verification behavior is in
[references/cost-signals.md](references/cost-signals.md).

### 4. Re-run the comparison when a model launches

Rakuten has tested Claude models since September 2024, across nearly a dozen model launches. Routing is
not a one-time decision: each launch can move a task class from the smaller model to the frontier one,
or the reverse, as capability and price both move.

## Examples

**Rakuten's stated position.** As a large enterprise, Rakuten wants to balance intelligence and cost.
The team measures task completion ratio alongside cost per task, then sends Fable 5 the work where the
extra capability changes the outcome and lets smaller models keep the rest.

**The two arguments in Fable 5's favor, as the post states them:**

| Signal | What it means for the cost math |
| --- | --- |
| More done with fewer tokens and fewer wrong turns | The run itself is shorter and less wasteful, offsetting a higher per-token price |
| Needs less hand-holding | Removes human check-in time, a cost the token bill does not show |

**A worked routing shape** (the structure, filled with your own classes):

| Task class | Completion ratio, small model | Completion ratio, frontier | Cost per task, small | Cost per task, frontier | Outcome changes? | Route |
| --- | --- | --- | --- | --- | --- | --- |
| Long unattended multi-hour run | low | high | low | high | yes | frontier |
| Routine bounded task | high | high | low | high | no | smaller |

The post does not publish Rakuten's own numbers; the shape above is the decision rule it describes.

## Source

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
