# Base44's handoffs, as the post reports them

## The company

Base44 is a vibe-coding platform that allows anyone, regardless of technical ability, to build full
stack applications and websites. Its customers range from small businesses with no developers to
companies using it to build full SaaS products.

Yoav Orlev joined as its first employee and now runs product. One of the most satisfying parts of his
work is seeing what small businesses can do with the platform when they otherwise lacked the time,
budget, or knowhow — a digital storefront, or a shift-management application for restaurant staff. His
team's mission is to keep widening the product's capabilities while keeping it usable for everyone.

## The bottleneck

The product and engineering teams have always moved quickly on small or medium-scope features. But any
changes to the platform's core that touch multiple interdependent parts could only be entrusted to the
most senior engineers.

Two named bottlenecks:

- **The system prompt and its hundreds of permutations** — varying by whether someone is on their first
  app or their fifth, a free user or a subscriber, and by the category and features of the app being
  built.
- **The native mobile infrastructure** — which only engineers with mobile expertise could change.

## Handoff 1: rebuilding the system prompt

Previously reserved for the most senior engineers.

| Stage | Detail |
| --- | --- |
| Question round | About an hour of back-and-forth |
| Unattended run | Four hours |
| Returned | 90% to 95% of what the team needed |
| Shipped | Measured and shipped via A/B testing infrastructure that afternoon |
| Bonus | Flagged that the team was not testing for cache hits — a prompt change can break the cache, and at the scale of millions of users that drives up cost |

## Handoff 2: the in-app agent harness

Claude Fable 5 got stuck on a change to the harness behind Base44's in-app agent. Rather than keep
working the spot in front of it, it reasoned that the same problem had probably been solved elsewhere in
the codebase, went to investigate that part, and came back with the fix.

> "This reasoning of 'this probably has been solved somewhere else, so I should go there to investigate'
> is something we haven't seen so often in other models." — Yoav Orlev

The contrast with earlier models, in Orlev's words: when a model got stuck on an error, it would keep
working the spot in front of it instead of recognizing the fix probably already existed elsewhere in the
code and searching for it. "The decision on what to do next is a crucial one and most of the time
[earlier] models would take, I would say, a naive approach."

## Handoff 3: native mobile, owned by a product manager

Previously required an engineer with mobile expertise.

A product manager wanted to bring native mobile app building inside Base44. He pointed Claude Fable 5 at
the job and after roughly **two and a half hours** had a working environment that was about **90%** of
what the team needed to move to production.

## The comparison Orlev draws

Working with Claude Fable 5 is like working with a senior engineer. A junior engineer needs every step
specified and constant checking; a senior one you brief on the goal and the why.

Claude Fable 5 was the first model the team tested that could reason as if it had an understanding of
how software is built.

## What's next

As Claude model capabilities advance, so do the team's goals for the platform. Base44 aims to turn the
product from a tool that builds apps into one that also helps people manage and grow what they have
built. **Base44 Superagents**, now public, run workflows around those apps.

Knowing they can trust Fable 5 with complex tasks, Orlev now encourages product managers and designers
to build in parts of the platform they were previously not willing to touch for fear of breaking
anything.

> "Fable has given us the confidence to make bolder moves with the business. It's bringing the product to
> a whole new area and possibilities that before that we were, I would say, scared to do." — Yoav Orlev

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
