---
name: realistic-agent-evals
description: Build an internal evaluation that reflects how engineers actually prompt a coding agent — underspecified requests, missing context, wrong premises — instead of well-defined benchmark problems, and score whether the model understood the request rather than only whether the answer was right. Use when public benchmark scores stop matching what your developers report, when designing an internal benchmark, when writing eval tasks from real user prompts, or when a suspiciously high score needs to be checked by reading traces.
---

# Evals that look like real developer work

Cursor's evals team noticed that public benchmark scores and real developer reception had stopped
lining up. Models would ace a benchmark and then get quietly abandoned mid-task by the engineers using
them. So they built their own eval, CursorBench, around a different premise: capture the messy,
underspecified ways engineers actually prompt their models.

> "Many evals look like this: here's a well-defined problem, here are the constraints, go fix it. But
> the prompts we get from real users don't really look like that. The model has to infer that the user
> has a problem and what they're trying to convey, identify the root cause, fix it, validate the fix,
> and report back."
> — Nate Schmidt, Cursor

## Instructions

### 1. Source tasks from real prompts, not from problem statements

The unit of an eval task is the prompt a user would actually send, in the state they would actually
send it. Do not clean it up, do not add the constraints, do not name the file. If your real users
paste a stack trace and type one word, that is the task.

Design details in [references/benchmark-design.md](references/benchmark-design.md).

### 2. Include tasks that require inferring intent

Cursor's canonical example: one eval task is just a stack trace pasted in with the single word
**"fix."** The model has to infer the intent, find the root cause, and validate the change on its own.
Nothing else is provided.

Scoring such a task means scoring the full chain, not the diff:

1. Infer that the user has a problem and what they are trying to convey.
2. Identify the root cause.
3. Fix it.
4. Validate the fix.
5. Report back.

### 3. Include tasks whose premise is wrong

Another CursorBench task tells the model the **wrong module is broken**, to see whether it challenges
the user's assumption or follows it into a dead end. This is the load-bearing category: a model
optimized to be agreeable will fail it while looking cooperative.

Every internal eval should have some fraction of tasks where the stated premise is false.

Templates for writing all three task shapes:
[templates/eval-task-template.md](templates/eval-task-template.md).
Filled-in examples: [examples/eval-tasks.md](examples/eval-tasks.md).

### 4. Score comprehension, not just correctness

> "When Schmidt's team runs a new model through CursorBench, the right answer is table stakes. What
> they're scoring is whether the model understood what it was being asked."

Treat the correct output as a precondition for scoring rather than as the score. What distinguishes
models on ambiguous tasks is whether they understood the request — and two models can produce the same
patch for entirely different reasons.

Track operation count alongside outcome. Cursor observed the frontier model getting there with fewer
operations: token-efficient relative to the work it completed. Efficiency is a signal about
understanding, not just about cost.

### 5. When a score jumps, read the traces before believing it

Cursor's response to an unexpectedly high score was suspicion, not celebration:

> "One of two things is happening: either the model's very smart, or the model is cheating."

So the team read the traces — the model's actual reasoning on the hardest tasks, the ones where the
prompt looks simple but cracking it requires understanding the whole system. What they found:

> "We just kept seeing the model dig out wins that no other model was doing previously."

Make trace review a required step for any result that surprises you. A number you have not
investigated is not yet a result. Note that the Cursor team ran this check on a real headline result —
72.9% at Max effort on CursorBench, a new high — rather than only on results they distrusted.

### 6. Report the effort setting with the score

CursorBench results are reported at a named effort setting. A score without the setting it was
produced at is not comparable to anything, so record it in the result itself.

### 7. Keep raising the ceiling

Cursor's next step after a model saturates the current eval is to build "more sophisticated,
closer-to-reality eval environments that will measure whatever comes next" — plus longer runs, since
Schmidt's next experiment is how long a model can manage a back-end system unattended over
days-to-weeks. Treat an eval as something that expires when models catch up to it.

## Examples

### A task that requires inferring intent

```
[pasted stack trace, 40 lines]
fix
```

Scored on: did it infer the problem, find the root cause, fix it, validate the fix, and report back?

### A task with a wrong premise

```
The auth middleware is broken — users are getting 500s on /orders. Fix the middleware.
```

The middleware is fine; the failure is elsewhere. Scored on: does the model challenge the assumption,
or does it follow the user into a dead end?

### A task that requires whole-system understanding

A prompt that looks simple but cannot be cracked without understanding how the pieces fit together.
These are the tasks whose traces you read when a score moves.

### What a scored result looks like

| Field | Example |
| --- | --- |
| Benchmark | CursorBench |
| Effort setting | Max effort |
| Score | 72.9% |
| Traces reviewed | Yes — hardest subset |
| Operations relative to work completed | Fewer than prior models |

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
