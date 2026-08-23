# Goal-and-why brief

For work you would previously have queued behind a senior or specialist engineer. Orlev's rule: a junior
engineer needs every step specified and constant checking; a senior one you brief on the goal and the
why.

If you find yourself writing steps, you are briefing the old way.

---

## The job

**Name:**
**Previously required:** (which engineer / which specialty)
**Why it was restricted:** (what interdependent parts it touches)

## The goal

State the outcome. One or two sentences.

## The why

The reason this outcome matters, and the constraint it has to respect. This is what the model
re-validates against when it hits an ambiguous call.

## What it touches

List the interdependent parts, so the blast radius is explicit rather than discovered.

| Part | How this change affects it |
| --- | --- |
| | |

If the thing has permutations (user state, plan tier, category, feature set), enumerate the axes here
rather than a representative case.

## Question round

Front-load this. Roughly an hour of back-and-forth on the Base44 system-prompt job, before four hours of
unattended work.

**Questions asked:**
**Interdependencies surfaced that were not in the brief:**
**Assumptions confirmed:**

## The run

**Started:**
**Ran unattended for:**
**Human check-ins:** (target: none)

## Result

**Percentage of what was needed:**
**What was missing:**
**Did it flag anything the team had missed?** (gaps in evals, process, adjacent code)

## Review gate

Review is the gate; supervision is not the method.

- [ ] Reviewed
- [ ] Tested
- [ ] Approved

**Shipping path:** A/B test / staged rollout / other:
**Shipped:**

## Source

Pattern from [Working at the frontier: Why Base44 trusts Claude Fable 5 with their most challenging engineering work](https://claude.com/blog/working-at-the-frontier-why-base44-trusts-claude-fable-5-with-their-most-challenging-engineering-work) — Claude blog, July 15, 2026.
