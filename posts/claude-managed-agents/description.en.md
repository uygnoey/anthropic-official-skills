[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Managed Agents: get to production 10x faster

## What is this post?

A product announcement for **Claude Managed Agents**, a suite of composable APIs on the Claude Platform that provides a hosted agent harness plus production infrastructure (sandboxed code execution, checkpointing, credential management, scoped permissions, tracing). The post frames what teams previously had to build themselves, lists what Managed Agents handles, and shares launch case studies from Notion, Rakuten, Asana, Vibecode, Sentry, Atlassian, Casetext, and others.

## When is it useful?

- You are deciding whether to build your own agent runtime or adopt a managed one
- You want to understand what an "agent harness" needs to cover before going to production
- You are scoping a new agentic product and need concrete deployment patterns and third-party case studies
- You are briefing stakeholders on the state of production agent infrastructure as of April 2026

## Key points

- Managed Agents pairs an orchestration harness with production infrastructure so teams can go from prototype to launch in days rather than months
- Core features: production-grade sandboxed agents, long-running sessions that survive disconnections, multi-agent coordination (research preview), and scoped-permission governance with execution tracing
- You define outcomes and success criteria; Claude self-evaluates and iterates (research preview). Traditional prompt-and-response is also supported
- In internal structured-file-generation tests, outcome task success improved up to 10 points over a standard prompting loop, with the largest gains on hardest problems
- Pricing: standard Claude Platform token rates plus $0.08 per session-hour of active runtime
- Access via the Claude Console, the new CLI, or Claude Code's built-in claude-api Skill ("start onboarding for managed agents in Claude API")

## Bundled resources

- `guides/managed-agents-adoption.{en,ko,es,ja}.md` — a deployment playbook that mirrors the post's decision points, capability list, and case-study patterns

The post does not define reusable developer-facing patterns or named agent roles with operational rules, so no Skill or Subagent artifact is produced.

## Source

Distilled from [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) (published 2026-04-08).
