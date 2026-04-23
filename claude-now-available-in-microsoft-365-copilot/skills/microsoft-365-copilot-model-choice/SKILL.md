---
name: microsoft-365-copilot-model-choice
description: Help an organization map Microsoft 365 Copilot entry points (Researcher, Copilot Studio) to appropriate Claude model choices mentioned in the announcement.
---

## Instructions
Use this skill when someone asks how Claude is positioned within Microsoft 365 Copilot per the announcement, and what that implies for selecting models.

1) Identify the Microsoft 365 Copilot surface
- Researcher (reasoning agent)
- Copilot Studio (agent building/orchestration)

2) Map to the announced Claude model options
- Researcher: Claude Opus 4.1 (as stated in the post)
- Copilot Studio: Claude Sonnet 4 and Claude Opus 4.1

3) Capture rollout/administration constraints
- Note that availability is described as opt-in via Microsoft’s Frontier Program.
- Record that Anthropic models are hosted outside Microsoft-managed environments and are subject to Anthropic Terms and Conditions.
- Confirm whether an admin must enable access in the Microsoft 365 admin center.

## Examples
### Example: Quick eligibility and routing
Input:
- We want Claude in Microsoft 365 Copilot. Where does it show up, and what models can we choose?

Output:
- Entry points: Researcher (multistep research) and Copilot Studio (build/manage agents).
- Model options: Researcher can use Claude Opus 4.1; Copilot Studio can use Claude Sonnet 4 or Claude Opus 4.1.
- Ops notes: rollout is described via Frontier Program (opt-in); admin enablement may be required; models are hosted outside Microsoft-managed environments.

## Source
- https://claude.com/blog/claude-now-available-in-microsoft-365-copilot
