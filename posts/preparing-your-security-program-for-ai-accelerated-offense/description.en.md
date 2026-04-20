[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Preparing your security program for AI-accelerated offense

## What is this post?

Guidance from Anthropic's Security Engineering and Research teams on how to adapt a security program for an environment where AI models rapidly find, chain, and exploit vulnerabilities. The post is organized into seven "what to do now" areas (patch gap, vulnerability report volume, pre-ship bug finding, existing code audit, design-for-breach, exposure reduction, incident response), plus a section on how to submit high-quality vulnerability reports, advice for solo / small-team maintainers, and a reference table mapping topics to standards (CISA KEV, EPSS, NIST SSDF, OWASP ASVS, SLSA, OpenSSF Scorecard, CISA Zero Trust Maturity Model, MITRE ATT&CK, NIST CSF 2.0, and more).

## When is it useful?

- You are re-scoping an existing security program to match the pace of AI-driven exploitation
- You are drafting patch-gap, vulnerability management, or incident-response policy updates
- You are standing up AI-assisted review (SAST-adjacent) in CI and want a responsible rollout path
- You are about to submit (or receive) AI-assisted vulnerability reports and want a quality bar
- You lead a small organization or open-source project and need a simplified action list

## Key points

- Close the patch gap: KEV catalog immediately, EPSS for the rest, 24-hour target on internet-facing, automate where safe
- Plan for an order-of-magnitude increase in vulnerability reports; use AI for triage, dedup, and patch drafting
- Find bugs before you ship: SAST + AI review in CI, pen-test in CD, secure the build (SLSA), Secure by Design, prefer memory-safe languages
- Audit existing code: prioritize parsers, auth boundaries, internet-reachable paths, and legacy code
- Design for breach: zero trust, hardware-bound identity, short-lived tokens, replace "friction" controls with real barriers
- Reduce and inventory exposure; decommission unowned services; run autonomous external red-teaming
- Shorten incident response with a triage agent at the front of the queue, dwell-time metrics, AI as scribe, and emergency change procedures agreed in advance
- Write AI-assisted vulnerability reports a human has verified and will put their name on
- Everything maps cleanly onto existing SOC 2 / ISO 27001 controls

## Bundled resources

- `skills/closing-the-patch-gap/SKILL.md` — reusable prioritization and rollout pattern for the patch-gap discipline
- `skills/writing-quality-vuln-reports/SKILL.md` — checklist and self-check for AI-assisted vulnerability reports
- `agents/security-triage-agent.md` — triage agent over a SIEM query tool (named in the post)
- `agents/vulnerability-scanning-agent.md` — isolated agent for scanning parsers / auth / reachable paths (named in the post)
- `agents/external-red-team-agent.md` — autonomous external red-team agent against your own perimeter (named in the post)
- `guides/security-program-playbook.{en,ko,es,ja}.md` — the full 7-area rollout playbook with standards references, in all four languages

## Source

Distilled from [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (published 2026-04-10).
