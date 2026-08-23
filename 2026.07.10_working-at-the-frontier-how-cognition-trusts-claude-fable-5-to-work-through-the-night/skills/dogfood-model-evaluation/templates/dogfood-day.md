# Dogfood day

A template for the practice Cognition uses in place of trusting a score: its highest-taste developers
put each new model through a real day of work, and the bar is whether the code is something they'd
actually keep.

---

## Setup

```yaml
model_under_test: <model id and any effort/config settings>
baseline: <the model currently in production, same settings shape>
evaluators:
  - <name>   # chosen for taste, not availability
  - <name>
date: <YYYY-MM-DD>
```

**Selection rule.** Evaluators must be people who can tell production-ready code from code that merely
works. That distinction is the entire point of the exercise, and it is the one a benchmark cannot
draw.

**Work rule.** A real day of the work they would have done anyway. Not curated prompts, not a demo
script, not the tasks you know the model is good at.

---

## During the day

Record as you go, not from memory afterward.

```yaml
tasks:
  - description: <what you actually needed done>
    kind: <migration | bug | feature | triage | review | other>
    outcome: <finished | partial | abandoned>
    kept: <yes | no>          # would you actually keep this code?
    why: <one line — the reason for the kept verdict>
    intervention: <none | corrected once | had to take over>
    surprises: <anything that changed your read of the model>
```

Log negative results with the same care as positive ones. The failure this exercise exists to catch is
a model that looks good in aggregate and falls apart on a specific real task.

---

## The verdict

One question, answered per evaluator:

> After a real day of work with this model: is the code something you'd actually keep?

```yaml
verdicts:
  - evaluator: <name>
    keep: <yes | no>
    summary: <two or three sentences>
```

Do not average this into a rating. Cognition's bar is binary, and a "mostly" from a high-taste
evaluator usually means no.

---

## Corroboration

Fill this in against your internal benchmark. The strong signal is agreement between the two.

```yaml
benchmark:
  name: <e.g. Frontier Code>
  hardest_subset_baseline: <%>
  hardest_subset_candidate: <%>
first_reaction: <record it honestly — "is there a bug?" is a healthy default>
agreement: <dogfooding agrees with the numbers | they disagree | inconclusive>
```

If they disagree, the post's history says what usually follows: engineers arguing for weeks over
whether the model is actually better in practice. That argument is the normal case, and it is a signal
in itself — a release that needs weeks of arguing is not a step change.

---

## Classification

```yaml
classification: <step change | incremental | no change | regression>
evidence:
  - <benchmark movement>
  - <dogfood verdicts>
  - <change in internal usage, if measurable>
notes: <what this release makes possible that was not possible before>
```

Cognition's reference class: Claude 3.6 Sonnet in late 2024 was the first model that could reliably
chain tools and hold a multi-step task, and internal usage tripled when they plugged it into Devin.
True step changes come roughly once a year. Keep your own version of that list — without it you cannot
tell a step change from noise.

## Source

[Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) — Claude blog, July 10, 2026.
