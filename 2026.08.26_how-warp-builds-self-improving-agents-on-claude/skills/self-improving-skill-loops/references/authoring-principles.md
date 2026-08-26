# Authoring principles for self-improving skills

Guidance collected from Warp's account of running self-improvement loops in production.

## Write principles, not rules

> Construct the skill as though you're instructing a smart person, not like you're programming a
> computer. Including direction like "Look for repeated code" provides better direction than
> exhaustive variable naming rules.

A rule list is brittle: it covers the cases you thought of and nothing else. A principle plus its
rationale lets the agent reason about the case in front of it.

## Explain the why

Rationale behind a rule enables the agent to reason about problems rather than follow rigid
instructions, which improves generalization. Every non-obvious instruction in a base skill should
carry the reason it exists.

## Make feedback effortless to give

Capture feedback where people already work — direct PR or issue comments — and collect it
automatically, without an extra submission step.

> Low friction is what keeps signal flowing. If you make it too hard you're not going to get the
> feedback and you're not going to be able to improve the skill.

Explicit feedback works best: not only *what* was wrong but *why*.

> A human could affirm, "this was a good, useful comment," but detailed reasons like "our code
> base convention is this type of global variable uses this particular naming context" tell the
> agent how to improve.

## Keep skills small; use progressive disclosure

Good skill files reference resource files and scripts rather than dumping everything into context
at once. The base skill should read like an index of what matters, with detail one hop away.

## Feedback quality exceeds volume — but volume helps

Detailed, domain-specific feedback from senior engineers outweighs cursory feedback.

> You can get really good signal even from a relatively small sample size if it's very detailed
> feedback from a person around domain specific knowledge that the agent otherwise would have no
> way of getting.

## Put extra effort into the improver skill

The investment pays dividends, because improver skills are highly reusable across different use
cases. The base skill is domain-specific; the loop around it usually is not.

## Skills are not memory

Skills are procedural and stable — "how to do X" — run-agnostic and deliberately changed. Memory
is auto-written by agents at inference time and constantly changes. Conflating the two is the
most common mistake when starting out.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26)
