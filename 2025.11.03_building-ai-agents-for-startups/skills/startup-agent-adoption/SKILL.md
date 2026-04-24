---
name: startup-agent-adoption
description: Select, launch, and scale AI agent use cases in a startup with a pragmatic approach to risk, modularity, and human oversight.
---

This skill is derived from: https://claude.com/blog/building-ai-agents-for-startups (published 2025-11-03).

## Instructions
- Identify candidate workflows where time is spent repeatedly and outcomes can be reviewed by a human.
- Choose an initial project with high impact and low-to-moderate risk; define a clear acceptance test for outputs.
- Design the agent as modular capabilities (shared components, shared prompts, shared tools) so it can expand to other teams.
- Make decisions observable: log inputs/outputs and provide a rationale or evidence trail when possible.
- Add human-in-the-loop checkpoints for high-stakes actions or ambiguous decisions.
- Scale from the first win by expanding coverage (more cases) and raising automation (more steps) only after quality is stable.

## Examples
### Example: picking a first agent project

- Workflow: inbound support triage

- Human oversight: agent drafts classification and response; human approves before sending

- Acceptance: 95% correct routing + fewer than N unsafe responses per week


### Example: scaling after an initial win

- Reuse the same classification module across support, sales lead qualification, and ops requests

- Add observability (reason + citations) before increasing automation

## Templates
See:
- templates/first-project-scorecard.md
- templates/scaling-plan.md

## References
See:
- references/adoption-principles.md
