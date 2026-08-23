# Long-run failure modes

Everything Cognition observed about where agents lose the thread on long tasks, as stated in the
source post. Each entry pairs the failure with the behavior that fixed it.

## 1. Horizon drift

> "Before Fable, you could delegate agents that could stay on-task for a couple of minutes, maybe an
> hour." After that, sessions drifted.

**What it looks like:** the agent is still working, still producing plausible steps, but no longer
working on the thing you asked for.

**What changed it:** horizon. Alberti's summary — "The biggest thing we noticed was the horizon, how
long it can be self-sufficient." His concrete case:

> "There have been tasks where I was about to go to bed and I was like, 'Okay, just please keep
> working on this and don't stop until I wake up.' And then I wake up, and it's been working for eight
> hours straight and actually making real progress. I hadn't seen that before."

## 2. Overload on parallel considerations

> Give an earlier model five ideas to weigh at once, and it would lose track and get confused.

**What it looks like:** the agent handles each consideration correctly in isolation and cannot hold
them together.

**Mitigation while it persists:** reduce the number of simultaneous constraints, or make them explicit
and written down rather than implicit in the prompt — which is what the invariants practice does.

## 3. Finishing without succeeding

> On one database migration, a prior Opus model technically finished the job but introduced a series
> of subtle bugs along the way.

**What it looks like:** the task reports complete. The migration ran. The bugs surface downstream,
quietly, later. For Cognition this is the expensive failure — Devin's customers include Fortune 500
companies, and "a small bug introduced quietly can cause real problems downstream."

**What fixed it:** on a migration that had tripped up earlier models, Claude Fable 5 stated the
invariants it would hold itself to, then executed against them.

## 4. Surface-level triage

Two behaviors compounding:

> Earlier models tended to stay at the surface of the logs instead of digging for the relevant line…

> …and they were trained to give an answer no matter what — so they'd "confidently claim the first
> plausible thing they discover and then stop."

**Consequence:** "Engineers learned to tune them out." This is a trust failure, not only a capability
failure. A model whose output is ignored provides no value even when it is occasionally right.

**What fixed it:** on triage, the model pinned down the root cause **and said what it didn't know** —
which Alberti says is what actually rebuilds trust.

## 5. Not being able to use the real tools

Claude Fable 5 was the first model to properly use Cognition's internal debugging tools, paging
through logs in the browser and drawing conclusions despite the noise.

**Read this as a prerequisite, not a bonus.** The horizon held because the model stayed clear-headed
in messy context. An agent that cannot navigate your actual observability stack cannot investigate
without you, which caps its horizon at your availability regardless of how good it is.

## What the post does not specify

- Any harness-level mechanism for detecting drift mid-run.
- Checkpointing, resumption, or supervision protocols for long runs.
- How Cognition decides which tasks are safe to leave unattended.

Those are your own engineering decisions. The post describes what changed in model behavior, not a
control system around it.

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
