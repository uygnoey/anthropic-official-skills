# The Claude Fable 5 evaluation at Base44

## Context

Claude models have powered Base44's app generation engine since the platform launched in early 2025.
Base44 runs each new Claude model through evals across different app types, measuring latency, cost, and
build errors, plus tests like building a Minecraft clone to see how a model handles game physics and
mechanics.

## What stood out

Two things:

1. **It finished tasks in far fewer turns.**
2. **It built more complete apps from the first prompt,** including the edge cases that earlier models
   skipped.

## What earlier models did instead

Orlev describes the behavior that kept earlier models off the hardest work. When a model got stuck on an
error, it would keep working the spot in front of it instead of recognizing the fix probably already
existed elsewhere in the code and searching for it.

> "The decision on what to do next is a crucial one and most of the time [earlier] models would take, I
> would say, a naive approach." — Yoav Orlev

Claude Fable 5 was the first model the team tested that could reason as if it had an understanding of
how software is built.

## The system prompt rebuild

Base44's system prompt has hundreds of permutations, varying by whether someone is on their first app or
their fifth, a free user or a subscriber, and by the category and features of the app being built. It was
one of two pieces of work that could only be entrusted to the most senior engineers.

The team pointed Claude Fable 5 at rebuilding it:

- **About an hour** of back-and-forth questions first.
- Then the model **ran on its own for four hours**.
- It returned **90% to 95%** of what they needed.
- Using its A/B testing infrastructure, the team measured and shipped the changes **that afternoon**.

## The gap the model found

While Claude Fable 5 worked, it flagged a gap in Base44's own evals: the team was not testing for cache
hits, even though a prompt change can break the cache, and at the scale of millions of users that drives
up cost. The model raised a blind spot and corrected it.

## The harness fix

When Claude Fable 5 got stuck on a change to the harness behind Base44's in-app agent, it reasoned that
the same problem had probably been solved elsewhere in the codebase, went to investigate that part, and
came back with the fix.

> "This reasoning of 'this probably has been solved somewhere else, so I should go there to investigate'
> is something we haven't seen so often in other models." — Yoav Orlev

## The native mobile job

The other piece of work previously restricted to specialists was changing the native mobile
infrastructure, which only engineers with mobile expertise could do.

A **product manager** — not an engineer — wanted to bring native mobile app building inside Base44. He
pointed Claude Fable 5 at the job and after roughly **two and a half hours** had a working environment
that was about **90%** of what the team needed to move to production.

## Before and after

| | Before Fable 5 | After |
| --- | --- | --- |
| Core changes touching interdependent parts | Waited for Base44's top three engineers or a specialist to free up | The model executes; the team reviews, tests, and approves before shipping |
| Native mobile infrastructure | Only engineers with mobile expertise | A product manager got to ~90% in ~2.5 hours |
| System prompt (hundreds of permutations) | Most senior engineers only | ~1 hour of questions, 4 hours unattended, 90–95% returned, shipped that afternoon |

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
