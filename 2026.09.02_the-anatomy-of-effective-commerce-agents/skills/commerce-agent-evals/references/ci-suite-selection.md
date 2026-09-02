# Shipping with large organizations

Many teams own interconnected systems, and every change ripples across a shared context window.
Three practices keep that workable.

## 1. Ownership follows systems

- Each **skill** and each **tool** has a single owner team.
- The **shared prompt** has a platform-level owner, plus domain owners for its sections.
- Adding a skill means contributing test cases with it: **positive, negative, and boundary**.

## 2. Changes ship with cases; CI runs a selective suite

The full suite per pull request is too slow and too expensive. Build the CI set from:

- core high-traffic cases,
- **all** safety cases,
- the cases that touch the change.

### Selection by change type

| Change | CI set |
|---|---|
| A skill | That skill's own cases, plus neighboring skills' boundary cases. |
| A tool | Every case that calls it. |
| The shared prompt | The full suite. |

## 3. Put the agent in the release calendar

The agent is a single deployment unit: a bad change reaches all users at once. So treat it like
one.

- **Canary rollout** for prompt and skill changes.
- **Disable-without-deploy switches** so a bad capability can be turned off in seconds.
- **Freeze before peak periods.**

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
