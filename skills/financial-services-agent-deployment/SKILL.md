---
name: financial-services-agent-deployment
description: Guides building and deploying AI agents in financial services with emphasis on integration, regulation, and real-time risk controls. Trigger when the user asks how to safely operationalize agents for banking, insurance, wealth management, fraud, compliance, or financial operations.
---

# Financial Services Agent Deployment

Use this skill to turn a financial-services agent idea into a deployable plan that accounts for legacy systems, regulatory expectations, auditability, and safe escalation for high-risk actions.

## Instructions
1. Clarify the use case and risk profile (e.g., customer service triage vs. fraud monitoring vs. compliance recommendations) and identify what the agent can do autonomously vs. what requires human approval.
2. Map the data the agent must read (transactions, market data, policy/regulatory documents, internal procedures) and the actions it must take in existing workflows.
3. Plan integration with legacy systems and data silos using connectors (APIs, MCP, or middleware), with a focus on data integrity and reliable synchronization.
4. Build in traceability from day one: logs, rationale, and an audit trail sufficient for troubleshooting and regulatory review.
5. Design real-time risk controls:
   - Transparent reasoning for decisions
   - Escalation pathways to specialists
   - Override capability
   - Fail-safe defaults that prioritize customer protection
6. Start with high-impact, low-risk deployments (e.g., internal knowledge retrieval, routine data validation, deadline monitoring), then expand to more complex workflows.
7. For customer-facing experiences, ensure transparency (disclose AI vs. human) and provide a clear path to a human.

## Examples
- Transaction monitoring agent that recognizes unusual patterns, drafts a risk recommendation grounded in relevant regulations, and routes it to an analyst for review.
- Anomaly detection agent that reviews 100% of transactions, groups expenses, flags policy concerns, and provides explanations plus recommended actions.
- Compliance agent that monitors deadlines and automates document classification, escalating exceptions.

## Anti-patterns
- Deploying agents without observability, audit trails, and explicit escalation/override paths.
- Letting agents take high-risk actions without a defined human-in-the-loop approval step.
- Building one-off integrations instead of reusable foundations (e.g., shared document processing).

## Bundled resources
This skill folder ships with additional materials that follow their own Claude specs:

- [`guides/deployment-playbook.md`](guides/deployment-playbook.md) — free-form staged rollout playbook, integration patterns, risk controls, named industry examples, and a decision checklist. Read this when you need depth beyond the step list above.
- [`agents/transaction-monitor.md`](agents/transaction-monitor.md) — Claude Code [subagent](https://code.claude.com/docs/en/sub-agents) definition for transaction pattern review.
- [`agents/expense-anomaly-reviewer.md`](agents/expense-anomaly-reviewer.md) — subagent for full-coverage expense review with grouped findings.
- [`agents/compliance-deadline-monitor.md`](agents/compliance-deadline-monitor.md) — subagent for deadline tracking and regulatory document triage.

The three agent files are ready to drop into `.claude/agents/` (project) or `~/.claude/agents/` (user) as-is.

## Human-readable descriptions
This skill is summarized for humans in [description.en.md](description.en.md) and [description.ko.md](description.ko.md).

## Source
Distilled from [Building AI agents for financial services | Claude](https://claude.com/blog/building-ai-agents-in-financial-services) (published 2025-10-30).
