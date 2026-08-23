---
name: dogfood-model-evaluation
description: Decide whether a new model is actually better by putting it through a real day of work with your highest-taste engineers and asking whether the code is something they would keep, rather than trusting a benchmark score. Use when a model aces a benchmark but you are unsure it will hold up in practice, when building an anti-slop internal benchmark, when a score jump needs corroboration, or when a team keeps arguing for weeks about whether a release is an improvement.
---

# "We trust no eval"

Cognition has been burned by benchmarks. The company has watched models ace a score and then fall
apart the moment its engineers tried to use them.

> "We've been burned like this a bunch of times." — Silas Alberti, SVP of Research, Cognition

So the team trusts its own engineers over any score. Its highest-taste developers put each new model
through a real day of work, and the bar is whether the code is something they'd actually keep.

> As Alberti puts it, "we trust no eval."

That stance is not anti-measurement — Cognition also maintains its own benchmark. It is a rule about
what counts as *evidence*.

## Instructions

### 1. Make the dogfood day the primary signal

Not a smoke test, not a set of curated prompts: a real day of the work your engineers actually do,
run by the developers whose judgment you trust most. Structure in
[templates/dogfood-day.md](templates/dogfood-day.md).

The single question at the end is the bar Cognition uses: **is the code something you'd actually
keep?** Not "did it compile," not "did it pass," not "was it impressive."

### 2. Pick evaluators by taste, not availability

The post is specific that it is the company's *highest-taste* developers who run the new model. The
signal depends on the evaluator being able to tell production-ready code from code that merely works —
which is the distinction a benchmark cannot draw.

### 3. Build an anti-slop benchmark to sit alongside it

Cognition grades models on **Frontier Code**, a benchmark it built because existing ones kept
rewarding code that passed tests but wouldn't survive a real codebase. Alberti calls it an
"anti-slop" standard.

The design principle to carry over: score survival in a real codebase, not test-passing. Criteria in
[references/anti-slop-criteria.md](references/anti-slop-criteria.md).

On the hardest subset of Frontier Code, the prior Opus model scored around 10%; Claude Fable 5 scored
about 30%.

### 4. Treat a large jump as suspicious until dogfooding corroborates it

The team's first reaction to the Frontier Code result was not celebration:

> "Is there a bug? This can't be true."

That is the correct default. Usually a benchmark jump comes with engineers arguing for weeks over
whether the model is actually better in practice.

### 5. The signal is when the two agree

What made this release different was convergence:

> This time the dogfooding agreed with the numbers. "It was kind of a shocker, honestly."

A score and a dogfood day that agree is a much stronger result than either alone. A score without
corroboration is a hypothesis. A dogfood day without a score is an anecdote.

### 6. Calibrate against your own history

Alberti's team has run nearly every Claude generation since the start, and he traces the first real
jump to Claude 3.6 Sonnet in late 2024 — the first model that could reliably chain tools and hold a
multi-step task. When they plugged it into Devin, internal usage tripled.

That history is what makes him hard to impress, and it gives him a reference class: he puts the Fable
5 jump in a small class of true step changes, the kind that come roughly once a year.

Keep your own record of which releases actually changed your product's behavior. Without it, every
release looks either like a step change or like noise, and you have no way to tell which.

Note the second-order metric in that history: **internal usage tripled**. Adoption by your own
engineers is a measurement, and often a more honest one than a score.

## Examples

### The bar, stated as a question

> After a real day of work with this model: is the code something you'd actually keep?

Yes / No. Not a rating.

### Evidence strength, ranked

| Evidence | Strength |
| --- | --- |
| Public benchmark score alone | Weak — Cognition has been burned by this repeatedly |
| Internal anti-slop benchmark alone | Better, but still a hypothesis |
| Dogfood day alone | An anecdote, but from a trusted evaluator |
| Internal benchmark **and** dogfooding agreeing | Strong — the case in this post |
| A step change in internal adoption | Strong, and lagging |

### A result worth acting on

- Frontier Code, hardest subset: prior model ~10% → new model ~30%.
- First reaction: "Is there a bug? This can't be true."
- Dogfooding by highest-taste developers: agreed with the numbers.
- Classification: a true step change, the kind that comes roughly once a year.

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
