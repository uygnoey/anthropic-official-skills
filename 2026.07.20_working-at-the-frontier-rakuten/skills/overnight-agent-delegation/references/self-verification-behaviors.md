# The three behaviors that make an unattended run viable

Everything here is what the post states. Where it does not specify something, that is marked.

## 1. It re-checks its own assumptions

**What the post says.** When the state of the task changes midway, Fable 5 notices and corrects a wrong
assumption before acting on it, rather than committing to a bad path and discovering it hours later.

**Why it matters for run length.** The pre-Fable failure was not that the model took a wrong first
step — any model can do that. It was that nothing caught the wrong step, so it compounded across the
whole run. Kaji: "If they choose the right path in the first step, everything is fine. But if they
choose the wrong direction in the first pass, the agent spends significant time to fix the path, or
even fails to reach the destination."

**Not specified.** How often the re-check happens, what triggers it, or how it is surfaced to the
operator.

## 2. It returns to first principles at each step

**What the post says.** It re-validates against the original intent without being told — the
course-correction Kaji used to have to make himself when a run started down the wrong path.

**Why it matters.** A long run drifts. Re-validating against the original intent at each step is what
lets the model "re-navigate to the right outcome without anyone steering it."

**Not specified.** Whether the original intent is re-read from the brief, from memory, or reconstructed.

## 3. It matches the team's taste

**What the post says.** Even with minimal guidance, its judgment on ambiguous calls lines up with the
team's. Kaji coined a term for this: *taste alignment*.

> "Taste alignment is smoother with Fable than any previous model from your company, or any other model
> we've used." — Yusuke Kaji

**Why it matters.** Ambiguous calls are the ones a chunked brief used to resolve in advance. If the
model's judgment on them matches yours, you do not have to pre-resolve them, which is what makes
handing over a whole task possible.

**Not specified.** How taste alignment is measured, or whether it is established through prompting,
memory, examples, or none of these.

## Memory between runs

Separate from the three behaviors, and stated once in the post:

> "Our agents with memory remember what went wrong in past sessions and avoid repeating those mistakes."

The post does not describe the memory mechanism.

## What changes when all of this holds

- The unit of delegation rises from a well-defined chunk to a whole task.
- Several tasks can run at once, because none needs supervision.
- Sign-off becomes feasible: the human reviews an outcome instead of steering a run.
- The unit of work the human handles shifts from the task to the decision.

## Source

[Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
