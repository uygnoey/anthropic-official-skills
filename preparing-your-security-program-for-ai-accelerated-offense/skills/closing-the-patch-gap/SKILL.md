---
name: closing-the-patch-gap
description: Prioritizes and operationalizes software patching for an environment where AI models quickly reverse patches into exploits. Use when planning patch policy, reducing time-to-patch on internet-exposed systems, triaging large CVE backlogs with KEV and EPSS, or rolling out automated patch deployment.
---

# Closing the patch gap

Applies the post's "close your patch gap" discipline as a reusable, prioritized rollout pattern. The goal is to shrink the window between a patch being published and an exploit being usable against your systems, given that AI can reliably reverse patches into working exploits.

## Instructions

1. **Treat the CISA KEV catalog as non-negotiable.** Any vulnerability on the CISA Known Exploited Vulnerabilities catalog that is reachable from a network is an emergency. Patch these immediately, above every other security queue.
2. **Prioritize the remainder with EPSS.** Use the Exploit Prediction Scoring System to rank open CVEs by the daily-updated probability that they will be exploited in the next 30 days. Choose an EPSS threshold for "must patch soon" and apply it to everything not already on KEV.
3. **Set explicit time-to-patch targets.** Internet-facing applications: within 24 hours of an exploit becoming available. Other systems: within days of a patch being available.
4. **Automate patch deployment and reboots** where the risk of an automated update causing an outage is acceptable. Manual approval steps add delay, and delay is now the primary risk.
5. **Use vendor-shipped automation first.** Most cloud and OS vendors ship patch automation; enabling it is typically a single configuration change.
6. **Wire KEV/EPSS metadata into CI.** Run an open-source container-image or dependency-manifest scanner as a CI step and annotate CVEs with KEV and EPSS data so prioritization is automatic.
7. **Define an emergency change procedure in advance.** Decide, ahead of time, who can authorize an emergency patch rollout, a service take-down, a credential rotation, or a network block, and how fast. A two-week change-approval cycle for emergency patches is itself a security risk.
8. **Measure outcomes, not activity.** Track time-to-patch on internet-facing systems and time-to-patch on KEV entries. If either is sliding, your queue discipline is degrading regardless of how busy the patching team looks.

## Examples

Queue for a typical Monday morning (ordered):

1. Any CVE newly added to KEV affecting a network-reachable asset → page the on-call patching role immediately.
2. CVEs above the chosen EPSS threshold on internet-facing services → assign a 24-hour SLA.
3. Remaining CVEs above EPSS threshold on internal systems → several-day SLA.
4. Everything below EPSS threshold → queued for the next routine cycle.

Example CI annotation output on a container image scan:

```
CVE-2026-10492 [KEV] [EPSS 0.97] → patch now; network-reachable
CVE-2026-10110 [EPSS 0.41] → patch within week; internal only
CVE-2024-99887 [EPSS 0.02] → backlog
```

## Anti-patterns

- Manual approval chains gating emergency patches — they turn "patch published" into "patch exploited before it lands".
- Relying on CVSS severity alone; CVSS does not reflect active exploitation like KEV and EPSS do.
- Patching on a fixed monthly cadence regardless of KEV additions.

## Source

Distilled from [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (published 2026-04-10).
