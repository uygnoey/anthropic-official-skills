---
name: senior-scope-delegation
description: Hand a model the work that was previously reserved for your most senior or most specialized engineers — core changes touching interdependent parts — by briefing the goal and the why rather than every step, front-loading a question round, letting it run unattended, and gating on human review before shipping. Use when a core system change is blocked waiting for a specific engineer to free up, when deciding whether a non-engineer can own a piece of technical work, or when calibrating how much specification a model actually needs.
---

# Delegating the work that used to need your most senior engineers

Base44's product and engineering teams have always moved quickly on small and medium-scope features.
But changes to the platform's core that touch multiple interdependent parts could only be entrusted to
the most senior engineers — and one class of work, the native mobile infrastructure, only to engineers
with mobile expertise.

Yoav Orlev, Base44's first employee and now head of product, describes what changed when Claude Fable 5
could be trusted with that tier of work.

This skill describes the delegation pattern as the post presents it.

## Instructions

### 1. Identify the work that is queued behind specific people

At Base44 the bottlenecks were concrete:

- **The system prompt and its hundreds of permutations,** varying by whether someone is on their first
  app or their fifth, a free user or a subscriber, and by the category and features of the app being
  built.
- **The native mobile infrastructure,** which only engineers with mobile expertise could change.

The common property is not difficulty in the abstract. It is that the change touches multiple
interdependent parts, so the blast radius of a naive edit is large — which is why it waited for the top
three engineers or a specialist to free up.

### 2. Check that the model reasons about *where* to work, not just *what* to write

The behavior that kept earlier models off this tier: when a model got stuck on an error, it would keep
working the spot in front of it instead of recognizing the fix probably already existed elsewhere in the
code and searching for it.

> "The decision on what to do next is a crucial one and most of the time [earlier] models would take, I
> would say, a naive approach." — Yoav Orlev

The contrast case is the one to look for. When Claude Fable 5 got stuck on a change to the harness
behind Base44's in-app agent, it reasoned that the same problem had probably been solved elsewhere in
the codebase, went to investigate that part, and came back with the fix.

> "This reasoning of 'this probably has been solved somewhere else, so I should go there to investigate'
> is something we haven't seen so often in other models." — Yoav Orlev

### 3. Brief like a senior engineer: the goal and the why

Orlev compares working with Claude Fable 5 to working with a senior engineer. A junior engineer needs
every step specified and constant checking; a senior one you brief on the goal and the why.

Use [templates/goal-and-why-brief.md](templates/goal-and-why-brief.md).

### 4. Front-load a question round, then let it run

The shape of the system prompt rebuild:

1. **About an hour** of back-and-forth questions.
2. **Four hours** of the model running on its own.
3. **90% to 95%** of what the team needed, returned.

The question round is where the interdependencies get surfaced. It is not overhead on top of the run —
it is what makes the unattended run worth starting.

### 5. Keep review as the gate, not supervision as the method

The model executes tasks while the team reviews, tests, and approves the code before shipping it. The
change is not that review disappeared; it is that steering during the work did.

Base44 used its A/B testing infrastructure to measure and ship the rebuilt system prompt the same
afternoon. See [references/review-gate.md](references/review-gate.md).

### 6. Widen who is allowed to touch the core

Once the model can be trusted with this tier, the constraint on who owns a piece of technical work
loosens. A **product manager** who wanted to bring native mobile app building inside Base44 pointed
Claude Fable 5 at the job and after roughly two and a half hours had a working environment that was
about 90% of what the team needed to move to production.

Orlev now encourages product managers and designers to build in parts of the platform they were
previously not willing to touch for fear of breaking anything.

> "Fable has given us the confidence to make bolder moves with the business. It's bringing the product to
> a whole new area and possibilities that before that we were, I would say, scared to do." — Yoav Orlev

## Examples

The Base44 handoffs as the post reports them — the system prompt rebuild, the harness fix, and the
native mobile environment — are in [examples/base44-handoffs.md](examples/base44-handoffs.md).

| Job | Who it used to need | How it ran | Result |
| --- | --- | --- | --- |
| Rebuild the system prompt (hundreds of permutations) | Most senior engineers only | ~1 hour of questions, then 4 hours unattended | 90–95% of what was needed; measured and shipped that afternoon |
| Fix a stuck change to the in-app agent harness | Senior engineer | Model investigated elsewhere in the codebase | Returned with the fix |
| Bring native mobile app building in-house | Engineers with mobile expertise | Product manager pointed the model at it, ~2.5 hours | ~90% of a working environment for production |

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
