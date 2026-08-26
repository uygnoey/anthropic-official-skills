# Rollout questions before scaling self-improvement loops

The questions the Warp team recommends answering before putting self-improving agents into wider
use, with their answers.

## Are you conflating skills with memory?

Skills are procedural and stable — "how to do X," run-agnostic, deliberately changed. Memory is
auto-written by agents at inference time and constantly changes. Keep the distinction: what the
improver loop edits is a skill, reviewed and merged like code.

## Do you need one improver loop, or one per agent?

Meet in the middle. A templated base loop captures the overlap across agents, with
domain-specific weights layered on top. A handful of agents can each own an improver; a hundred
should share.

## What happens when the feedback is wrong?

Assume it will be. Don't let agents accept feedback blindly:

- Give the agent context to sanity-check what it reads.
- Filter whose input counts.
- Keep humans in the loop at the filtering stage, the final-review stage, or both.

## Is your domain verifiable?

Build the verification harness first, then let the agent tune against it:

1. Generate a reference corpus.
2. Compare output to the reference.
3. Fix.
4. Repeat.

## And if it isn't domain verifiable?

Lean on deterministic evals against golden outputs wherever they exist. Where human feedback is
necessary, restrict it to domain experts — don't open the floodgates.

## How do you know the whole system is improving?

Track the global metrics humans already monitor — time to merge, contributor count, cost — and
feed them back into the improver agents. Progress gradually from crawl to walk to run on
deployment.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26)
