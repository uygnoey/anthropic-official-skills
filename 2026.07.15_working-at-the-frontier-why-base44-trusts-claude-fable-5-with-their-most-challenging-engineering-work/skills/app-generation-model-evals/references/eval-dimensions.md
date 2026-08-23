# Eval dimensions for an app-generation engine

What the post states about how Base44 evaluates a new model, and how each dimension connects to the
product decision.

## The suite

| Component | What the post says |
| --- | --- |
| Evals across different app types | Base44 runs each new Claude model through evals across different app types, measuring latency, cost, and build errors. |
| Stress builds | The team also runs tests like building a Minecraft clone to see how a model handles game physics and mechanics. |

## Why "across different app types" matters here

Base44's customers "range from small businesses with no developers to companies using it to build full
SaaS products." The system prompt itself has hundreds of permutations that vary by:

- whether someone is on their first app or their fifth,
- whether they are a free user or a subscriber,
- the category of the app being built,
- the features of the app being built.

A model that behaves well on one app type is not evidence about that spread.

## The three measured metrics

### Latency

User-visible in a vibe-coding product: the wait between a prompt and a working app.

### Cost

Base44 operates "at the scale of millions of users," which is why the cache-hit gap mattered so much
(below).

### Build errors

Whether the generated app actually builds. Note that this is a floor, not a ceiling — see the two
signals below, which a build-error metric alone does not capture.

## Two signals beyond the standard metrics

With Claude Fable 5, two things stood out that the three metrics above do not directly measure:

- **Turns to completion.** It finished tasks in far fewer turns. In a vibe-coding platform, each extra
  turn is a user having to ask again.
- **First-prompt completeness.** It built more complete apps from the first prompt, *including the edge
  cases that earlier models skipped*. A build-error metric passes an app that builds cleanly and omits
  an edge case.

## The gap the model found: cache hits

While Claude Fable 5 was rebuilding Base44's system prompt, it flagged that the team was not testing
for cache hits — even though a prompt change can break the cache, and at the scale of millions of users
that drives up cost.

The general shape of the gap: an eval that scores output quality but not caching behavior will pass a
prompt change that quietly multiplies production cost. The post notes that the model "raised a blind
spot and corrected it."

## Shipping path

Base44 used its A/B testing infrastructure to measure and ship the rebuilt system prompt the same
afternoon the model finished its four-hour run.

## What the post does not specify

- The number of app types in the suite, or which ones.
- Latency, cost, or build-error thresholds.
- How the Minecraft-clone build is scored.
- What the cache-hit test looks like once added.
- Which A/B metrics gate a ship.

## Source

[Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
