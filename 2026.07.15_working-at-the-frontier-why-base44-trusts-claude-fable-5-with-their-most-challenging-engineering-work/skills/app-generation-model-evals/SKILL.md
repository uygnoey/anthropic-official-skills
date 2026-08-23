---
name: app-generation-model-evals
description: Evaluate a new model for an app-generation product by running it across different app types and measuring latency, cost, and build errors, plus stress builds that exercise unusual capabilities — then read the signals that matter for production, such as turns to completion, first-prompt completeness, and whether prompt changes break the cache. Use when a new model ships and someone asks whether to switch the generation engine, when designing an eval suite for a codegen or app-building product, or when an eval passes but production cost or latency regresses anyway.
---

# Evaluating a new model for an app-generation engine

Base44 is a vibe-coding platform that lets anyone, regardless of technical ability, build full stack
applications and websites. Claude models have powered its app generation engine since it launched in
early 2025. Yoav Orlev, the company's first employee and now head of product, describes how each new
model is put through evals before it is trusted with production generation.

This skill describes that evaluation pattern as the post presents it.

## Instructions

### 1. Run the eval across different app types, not one representative app

Base44 runs each new Claude model through evals **across different app types**. The platform's users
range from small businesses with no developers to companies building full SaaS products, and the app
being generated varies by category and feature set. An eval on a single app shape does not tell you
how the model behaves across that spread.

### 2. Measure latency, cost, and build errors

Those are the three metrics the post names. Together they cover the production question: does the
generated app work, how long did the user wait, and what did the generation cost.

See [references/eval-dimensions.md](references/eval-dimensions.md) for how each dimension connects to
the product decision, and what the post leaves unspecified.

### 3. Add stress builds that exercise capabilities the standard suite misses

The team also runs tests like **building a Minecraft clone**, to see how a model handles game physics
and mechanics.

The point of a stress build is not that users are building Minecraft clones. It is that a build with
demanding physics and mechanics exercises reasoning the ordinary app types never reach, and separates
models that the standard suite scores identically.

### 4. Read turns to completion and first-prompt completeness

With Claude Fable 5, two things stood out:

- **It finished tasks in far fewer turns.**
- **It built more complete apps from the first prompt,** including the edge cases that earlier models
  skipped.

Both are product-visible in a vibe-coding platform, where each extra turn is a user having to ask
again and each skipped edge case is a bug the user finds later. Score them explicitly — a suite that
only checks whether the app eventually builds will miss both.

Record a run with [templates/model-eval-run.md](templates/model-eval-run.md).

### 5. Test for cache hits, because a prompt change can break the cache

While Claude Fable 5 worked on rebuilding Base44's system prompt, it flagged a gap in Base44's own
evals: the team was not testing for cache hits, even though a prompt change can break the cache — and
at the scale of millions of users that drives up cost. The model raised a blind spot and corrected it.

The general form of this gap: any eval that scores output quality but not the caching behavior of the
prompt will pass a change that quietly multiplies production cost. If your system prompt is cached, the
cache-hit rate belongs in the eval suite.

### 6. Ship behind measurement

Base44 used its **A/B testing infrastructure** to measure and ship the rebuilt system prompt the same
afternoon the model finished. Evals decide whether a change is worth trying; the A/B infrastructure is
what makes shipping it the same day defensible.

## Examples

The Claude Fable 5 evaluation as the post reports it — what stood out, what the model flagged, and what
the team shipped — is in [examples/fable-5-evaluation.md](examples/fable-5-evaluation.md).

Summary:

| Signal | Result |
| --- | --- |
| Turns to completion | Far fewer than earlier models |
| First-prompt completeness | More complete apps, including edge cases earlier models skipped |
| Eval-suite gap found by the model | Cache hits were not being tested |
| Shipping path | A/B testing infrastructure; measured and shipped the same afternoon |

The eval suite as the post describes it:

| Component | What it covers |
| --- | --- |
| Evals across different app types | Latency, cost, build errors |
| Stress builds (e.g. a Minecraft clone) | Game physics and mechanics |

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
