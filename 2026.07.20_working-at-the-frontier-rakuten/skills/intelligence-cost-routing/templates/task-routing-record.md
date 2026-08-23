# Task routing record

One record per task class. The decision rule: send the frontier model the work where the extra
capability changes the outcome; let smaller models keep the rest.

---

## Task class

**Name:**
**Typical run length:**
**Volume per week:**
**Owner:**

## Measurements

Measure both. Neither decides alone.

| Model | Task completion ratio | Cost per task | Tokens per task | Wrong turns per run | Human check-ins per run |
| --- | --- | --- | --- | --- | --- |
| Smaller model | | | | | |
| Frontier model | | | | | |

## The routing question

**Does the extra capability change the outcome on this task class?** yes / no

**Evidence:**

If **no**, route to the smaller model regardless of the completion-ratio gap — the gap is not buying a
different result.

If **yes**, describe what specifically changes:
- [ ] Unattended run finishes where the smaller model stalls
- [ ] Fewer wrong turns, so the run is shorter and cheaper despite the per-token price
- [ ] Less hand-holding, removing human check-in cost
- [ ] Taste on ambiguous calls matches without extra guidance
- [ ] Other:

## Decision

**Route to:**
**Decided on:**
**Re-evaluate at:** next model launch

## Re-evaluation log

| Date | Model launch | Completion ratio change | Cost change | New route |
| --- | --- | --- | --- | --- |
| | | | | |

## Source

Pattern from [Working at the frontier: How Rakuten builds agents overnight with Claude Fable 5](https://claude.com/blog/working-at-the-frontier-rakuten) — Claude blog, July 20, 2026.
