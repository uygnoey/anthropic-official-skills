# CursorBench: what the post says about its design

Cursor built CursorBench after noticing that public benchmark scores and real developer reception had
stopped lining up. This file collects everything the source post states about how it is built, and
marks where it stops.

## The problem it was built to solve

Cursor supports every major frontier model alongside its own, which makes the company an unusually
neutral judge of how each one actually performs. Nate Schmidt maintains that scorecard — he works on
evals and model behavior, studying how models succeed, how they fail, and "what makes a developer
quietly switch away from one mid-task."

That last phrase is the design brief. The failure a public benchmark does not capture is the one where
a developer silently gives up on a model in the middle of a task.

## The design premise

> CursorBench was built to capture the messy, underspecified ways engineers actually prompt their
> models.

Contrast with the conventional shape, in Schmidt's words:

> "Many evals look like this: here's a well-defined problem, here are the constraints, go fix it. But
> the prompts we get from real users don't really look like that."

## The chain a task must exercise

> "The model has to infer that the user has a problem and what they're trying to convey, identify the
> root cause, fix it, validate the fix, and report back."

Five stages. A conventional benchmark hands the model stages 1 and 2 for free and scores stage 3.
CursorBench tasks start at stage 1.

## Task shapes named in the post

1. **Underspecified.** A stack trace pasted in with the single word "fix." The model has to infer the
   intent, find the root cause, and validate the change on its own.
2. **Wrong premise.** The model is told the wrong module is broken, to see whether it challenges the
   user's assumption or follows it into a dead end.
3. **Whole-system.** Tasks "where the prompt looks simple but cracking it requires understanding the
   whole system." These form the hardest subset, and are the ones whose traces the team reads.

## What is scored

> "The right answer is table stakes. What they're scoring is whether the model understood what it was
> being asked."

Secondary signal recorded in the post: operations used relative to work completed. The frontier model
was "token-efficient relative to the work it completed."

## Reporting

Results are stated with an effort setting attached — the reported high was 72.9% at Max effort. The
post does not enumerate the other available settings.

## Verification by trace review

When a score comes in unexpectedly high, the team's stated stance is suspicion:

> "One of two things is happening: either the model's very smart, or the model is cheating."

The check is to read the traces — the model's actual reasoning on the hardest tasks. In this case the
finding supported the score: "We just kept seeing the model dig out wins that no other model was doing
previously."

## Where the eval goes next

Two directions the post names:

- **Longer horizons.** Schmidt wants to see how long a model can manage a back-end system unattended;
  days-to-weeks runs are his next experiment.
- **Closer-to-reality environments.** The team is using the model to build "the more sophisticated,
  closer-to-reality eval environments that will measure whatever comes next."

Beyond the benchmark, Cursor is also using the model to hunt performance bottlenecks and user pain
points proactively rather than waiting for reports.

## What the post does not specify

- The number of tasks in CursorBench, or how the score is aggregated.
- The rubric used to judge "understood what it was being asked."
- Which models besides the two discussed were scored, or their numbers.
- Whether CursorBench is or will be published.

Do not infer these. If you are building your own version, they are decisions you own.

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
