# Model eval run record

One record per candidate model. Keep the app types and stress builds fixed across models so runs are
comparable.

---

## Candidate

**Model:**
**Currently in production:**
**Run date:**
**Owner:**

## Evals across app types

| App type | Latency | Cost | Build errors | Turns to completion | Complete from first prompt? |
| --- | --- | --- | --- | --- | --- |
| | | | | | |
| | | | | | |
| | | | | | |

Include app types that span your user spread — e.g. a no-developer small-business site at one end and a
full SaaS product at the other. If your system prompt varies by user state (first app vs. fifth, free
vs. subscriber, app category, app features), cover more than one permutation.

## Stress builds

Builds chosen to exercise reasoning the ordinary app types do not reach.

| Stress build | What it exercises | Result | Notes |
| --- | --- | --- | --- |
| e.g. Minecraft clone | Game physics and mechanics | | |
| | | | |

## Edge cases skipped

List the edge cases the incumbent model skipped from the first prompt, and whether the candidate
covered them.

| Edge case | Incumbent | Candidate |
| --- | --- | --- |
| | | |

## Caching

- [ ] Cache-hit rate measured for the candidate
- [ ] Cache-hit rate measured after any prompt change made for the candidate

**Cache-hit rate, incumbent:**
**Cache-hit rate, candidate:**
**Projected cost impact at full scale:**

A prompt change can break the cache. At scale, that drives up cost without changing any output-quality
score.

## Reasoning behavior worth noting

- **When stuck, did it search elsewhere in the codebase for an existing solution?** yes / no — where:
- **Did it flag a gap in the eval suite or the surrounding process?** yes / no — what:

## Decision

- [ ] Route generation to the candidate
- [ ] Keep the incumbent
- [ ] Route a subset — which:

**Shipping path:** A/B test / staged rollout / other:
**Measured on:**

## Source

Pattern from [Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
