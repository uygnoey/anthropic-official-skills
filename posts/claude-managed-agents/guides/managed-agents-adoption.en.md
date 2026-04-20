[English](./managed-agents-adoption.en.md) · [한국어](./managed-agents-adoption.ko.md) · [Español](./managed-agents-adoption.es.md) · [日本語](./managed-agents-adoption.ja.md)

# Claude Managed Agents adoption playbook

Distilled from the April 8, 2026 launch announcement of [Claude Managed Agents](https://claude.com/blog/claude-managed-agents). The blog post is a product announcement, so this guide reorganizes its content as a decision-making and adoption playbook — not as reusable developer patterns the post does not supply.

## Why a managed harness

Before Managed Agents, shipping a production agent required the engineering team to build or integrate, at minimum:

- Sandboxed code execution
- Checkpointing for resumable long-running work
- Credential management
- Scoped permissioning across real systems
- End-to-end tracing
- Agent loops reworked on every model upgrade

Managed Agents pairs an **orchestration harness** (decides when to call tools, how to manage context, how to recover from errors) with that operational infrastructure so teams ship the product and not the platform.

## What's in the suite

| Capability | What it does | Availability |
|---|---|---|
| Production-grade agents | Secure sandboxing, authentication, tool execution handled for you | Public beta |
| Long-running sessions | Operate autonomously for hours; progress and outputs persist through disconnections | Public beta |
| Multi-agent coordination | Agents spin up and direct other agents to parallelize complex work | Research preview (request access) |
| Trusted governance | Scoped permissions, identity management, execution tracing into real systems | Public beta |
| Outcome-based mode | You define outcomes + success criteria; Claude self-evaluates and iterates | Research preview (request access) |
| Classic prompt-and-response | Tighter control flow when you want it | Public beta |

## Decision checklist: build vs. adopt

Work through these before writing any agent runtime of your own. Each maps to something Managed Agents already handles.

- [ ] Do we have a team that will own sandbox isolation, kernel hardening, and breakout monitoring?
- [ ] Are we committed to rebuilding our agent loop on every Claude model upgrade?
- [ ] Can we keep long-running sessions durable across disconnects, deploys, and failovers?
- [ ] Do we have a way to trace every tool call, decision, and failure in an auditable form?
- [ ] Do we have scoped-permission infrastructure that treats agents as first-class identities against real systems?
- [ ] Can we deliver the product value in weeks rather than months if we first build all of the above?

Any "no" is an argument for the managed runtime.

## What teams shipped on Managed Agents

The post enumerates live integrations at launch. Use them as adoption references, not prescriptive patterns:

| Team | Use case | Source |
|---|---|---|
| Notion | Delegate work to Claude inside a Notion workspace; dozens of tasks in parallel, team collaborates on output | Eric Liu, PM — [article](https://claude.com/blog/claude-managed-agents) |
| Rakuten | Enterprise agents for product/sales/marketing/finance plugged into Slack and Teams; each specialist deployed in a week | Yusuke Kaji, GM of AI for Business — [article](https://claude.com/blog/claude-managed-agents) |
| Asana | AI Teammates — collaborative agents inside Asana projects that take on tasks and draft deliverables | Amritansh Raghav, CTO — [article](https://claude.com/blog/claude-managed-agents) |
| Vibecode | Prompt-to-deployed-app platform; customers spin up infra at least 10x faster | Ansh Nanda, Co-founder — [article](https://claude.com/blog/claude-managed-agents) |
| Sentry | Seer (debugging agent) paired with a Claude-powered agent that writes the patch and opens the PR | Indragie Karunaratne, Sr Director Eng AI/ML — [article](https://claude.com/blog/claude-managed-agents) |
| Atlassian | Developer agents embedded in Jira workflows; tasks assigned directly from Jira | Sanchan Saxena, SVP Teamwork Collection — [article](https://claude.com/blog/claude-managed-agents) |
| Casetext | System that codes up custom tools on the fly to answer any query from users' documents and correspondence | Javed Qadrud-Din, CTO — [article](https://claude.com/blog/claude-managed-agents) |
| Rewatch | Meeting prep agent with calendar/contacts tools over MCP; shipped in days | John Han, Co-founder — [article](https://claude.com/blog/claude-managed-agents) |

## Adoption path

Step-by-step adoption mapped to capabilities named in the post.

1. **Pick a single-task runner first.** The post's common pattern is "specialist agent deployed within a week" — start there, not with multi-agent coordination.
2. **Define tasks, tools, and guardrails.** Those are your inputs; the harness handles orchestration, context management, and error recovery.
3. **Run on the Claude Platform.** Use the Claude Console, the new CLI, or Claude Code with the built-in `claude-api` Skill (`"start onboarding for managed agents in Claude API"`).
4. **Instrument and inspect.** Use session tracing, integration analytics, and troubleshooting in the Claude Console to review every tool call and failure mode.
5. **Decide on outcome-based mode.** If your task has checkable success criteria, request research-preview access to outcome mode; otherwise stay with prompt-and-response.
6. **Add multi-agent coordination only when warranted.** Request research-preview access when parallel specialist agents add measurable value.

## Pricing model to plan against

- Standard Claude Platform token rates
- Plus **$0.08 per session-hour** for active runtime

Two cost levers to plan for: token consumption per decision and wall-clock time an agent sits active. Long-running autonomous sessions cost more in session-hours than short bursts; keep that trade-off in capacity planning.

## What this post is **not**

- It is not a reference for how to build your own agent harness
- It does not define named agent roles with operational rules
- It does not prescribe hooks, output styles, or plugin bundling

Treat the post as an adoption and scoping reference. For reusable Claude Code patterns, use the Skills and Subagents elsewhere in this repository.

## Source

[Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) (published 2026-04-08).
