---
name: long-horizon-agent-runs
description: Hand an agent work that runs for hours unattended and get something you would actually keep — by stating the invariants up front, giving the agent the real debugging tools, and requiring it to name what it does not know instead of asserting the first plausible answer. Use when delegating a migration or a backlog of bugs overnight, when an agent drifts off-task on long runs, when triage answers stop being trusted, or when deciding whether a task is safe to leave running.
---

# Running an agent through the night

Cognition built Devin, its autonomous AI software engineer, in early 2024, when the basic mechanics of
an agent barely held together. Devin takes on the work engineers never quite get to: codebase
migrations, the backlog of bugs, the features that keep slipping. Customers range from high-growth
startups to Fortune 500 companies, so code written by Devin has to be reliable and production-ready —
a small bug introduced quietly can cause real problems downstream.

Silas Alberti, SVP of Research at Cognition, has run nearly every Claude generation behind Devin. The
constraint he kept hitting was not intelligence but **horizon**: how long an agent could run before it
lost the thread.

> "Before Fable, you could delegate agents that could stay on-task for a couple of minutes, maybe an
> hour."

## Instructions

### 1. Decide whether the task is horizon-shaped

Long unattended runs are for work with a clear objective and a long middle: a codebase migration, a
backlog of bugs, a feature that keeps slipping. What makes them hard is not any single step — it is
staying coherent across hundreds of them.

Before delegating overnight, check the failure modes the post names, listed in full in
[references/failure-modes.md](references/failure-modes.md):

- **Drift.** Sessions lose the thread after their horizon.
- **Overload.** Give an earlier model five ideas to weigh at once and it loses track and gets confused.
- **Quiet damage.** On one database migration, a prior model technically finished the job but
  introduced a series of subtle bugs along the way. Finishing is not the same as succeeding.

### 2. Make the agent state its invariants before it executes

The behavior that made a previously failing migration work was that the model **stated the invariants
it would hold itself to, then executed against them**. This is the single most transferable practice
in the post: on a long run, the invariants are what stands in for your supervision.

Use [templates/invariants-brief.md](templates/invariants-brief.md) to require this up front. Get the
invariants back and read them *before* the run starts — that review is far cheaper than reading eight
hours of diff.

### 3. Give the agent your real debugging tools

Claude Fable 5 was the first model to properly use Cognition's internal debugging tools — paging
through logs in the browser and drawing conclusions despite the noise. The horizon held because the
model stayed clear-headed in messy context.

The implication for your own setup: an agent that can only read what you paste in is limited to your
attention span. An agent with access to the log viewer, the traces, and the internal tooling can keep
investigating while you sleep. Wire up the tools you actually use.

### 4. Require the agent to say what it does not know

Earlier models tended to stay at the surface of the logs instead of digging for the relevant line, and
they were trained to give an answer no matter what — so they would "confidently claim the first
plausible thing they discover and then stop." Engineers learned to tune them out.

What rebuilt trust, in Alberti's account, was the opposite behavior: on triage, the model pinned down
the root cause **and said what it didn't know**.

Make that an explicit requirement in the task brief. An answer with a stated confidence boundary is
usable; a confident answer with no boundary gets ignored after the second time it is wrong.

### 5. Judge the output the way an engineer would

Cognition's bar for a model is whether its highest-taste developers would keep the code after a real
day of work. Apply the same bar to a long run: the question is not whether the agent finished, but
whether you would keep what it produced. See
[examples/overnight-run.md](examples/overnight-run.md) for what a good run looked like.

### 6. Extend from delegated runs to proactive ones

Once horizon is reliable, the run does not have to start with you. Devin can watch a Slack channel and
jump into an issue without being tagged, or monitor production and triage a spike on its own. Alberti:
when it gets one of those right, it feels "like a real engineer on the team."

He expects this to become the default — in a year or two, 90% of agent sessions being proactive ones
that find a problem, scan the codebase, and message you with the fix. Treat delegated overnight runs
as the step that earns the trust for that, not as the destination.

## Examples

### A task brief for an overnight migration

```
Objective: migrate the orders schema from v3 to v4 across the service and its consumers.

Before you touch anything, state the invariants you will hold yourself to and stop.
I will review them before you proceed.

While running:
- Use the log viewer and traces directly; do not wait for me to paste anything.
- If you reach a decision you cannot make safely, record it and continue with the
  parts you can do — do not guess.
- When you finish, report what you changed, what you verified, and what you are
  unsure about.
```

### Triage output that earns trust

> Root cause: the connection pool is exhausted because `close()` is skipped on the retry path in
> `orders/client.py`. Confirmed from the pool metrics and the retry log lines.
>
> What I don't know: whether the retry path is reachable outside the timeout case. I did not find a
> caller that hits it another way, but I could not rule it out from the logs alone.

### Triage output that gets tuned out

> The 500s are caused by high load. Scaling up should resolve it.

First plausible thing, stated confidently, investigation stopped. This is the pattern engineers
learned to ignore.

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
