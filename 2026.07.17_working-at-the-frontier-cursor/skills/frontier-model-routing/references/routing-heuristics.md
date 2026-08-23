# Routing heuristics

Signals drawn from how Cursor decides which model to spend on a task. Everything here comes from the
source post; where the post does not say, this file says so rather than filling the gap.

## The primary rule

> "If you have a good sense of what the path from A to B looks like, you might not need Fable. If
> you're at A and you have no idea where B is, Fable is an excellent choice."
> — Nate Schmidt, Cursor

Two conditions, one decision. Note that the rule is about *your* knowledge of the path, not about the
size of the change. A large but fully specified change is path-known. A three-line change whose
correct form depends on understanding the whole system is path-unknown.

## Local reasoning vs. global reasoning

The capability difference Schmidt observed, in his words:

- **Local reasoning** — "thinking about what just happened and what's immediately about to happen."
- **Global reasoning** — "thinking about the entire mission."

Practical read: if solving the task well requires holding the whole system and the objective in mind
at once — and if a greedy next-step choice can lead somewhere unrecoverable — that is a global
reasoning task.

The moon-landing run is the illustration. Local reasoning produced the loop *out of fuel → add fuel →
too heavy to launch → out of fuel*, repeated across twelve to sixteen hours. Global reasoning produced
a two-phase plan: fly an orbital mission to collect telemetry first, then use the telemetry to inform
the landing attempt.

## Signals that push toward the frontier model

- You cannot state the acceptance criteria yet.
- The prompt you would write is underspecified because *you* do not know the specifics.
- The first plausible answer is likely to be wrong, and a wrong answer is expensive to detect.
- The user's stated premise might itself be wrong and needs to be challenged.
- The task is one of "the p99 of problems," where time to solution is the thing to optimize.
- The work has been shelved on effort grounds — a rewrite everyone agrees would be better but nobody
  could justify weeks on.

## Signals that push toward a lighter model

- The change is defined and the validation is obvious.
- The task is routine and repeated.
- Latency matters more than depth.
- It is a supporting task around the real work — for example, having an agent read a teammate's recent
  commits and flag conflicts before you touch shared code.

## The mixed configuration

Cursor pairs the frontier model with faster, lighter models for routine work and brings the frontier
model in for the problems where capability is the constraint. Schmidt describes that combination as
the most effective setup his team has run. The post does not give a percentage split or a routing
implementation — the rule is applied by judgment per task.

## What the post does not specify

- Any automated router, classifier, or threshold for making the choice programmatically.
- Cost figures or a budget model.
- Which specific lighter models Cursor pairs with.

If you need those, treat them as your own engineering decision rather than as guidance from the post.

## Source

[Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) — Claude blog, July 17, 2026.
