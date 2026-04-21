---
name: bedrock-ga-implementation-checklist
description: Checklist for implementing model usage on Amazon Bedrock based on this Claude GA announcement, including considerations for agentic orchestration via AWS Lambda and enterprise customization.
---

## Instructions
Use this skill to turn the GA announcement into an actionable implementation plan.

1. **Confirm platform requirements**
   - Identify which AWS accounts/regions will access Claude on Amazon Bedrock.
   - Clarify security, compliance, and data-handling constraints.

2. **Decide on orchestration patterns**
   - If you plan agentic workflows, map actions to callable functions (for example, AWS Lambda functions) that can be orchestrated by an agent layer.

3. **Plan customization**
   - Determine whether you will use customization or fine-tuning with your data.
   - Define safety requirements and evaluation criteria.

4. **Pilot and evaluate**
   - Start with a narrowly scoped use case.
   - Measure quality, latency, and failure modes.

See [implementation notes](./references/implementation-notes.md) for a condensed set of decision points.

## Examples
- If you need the agent to take actions (for example, updating an order), define the action surface as callable functions that can be orchestrated.
- If you need domain-specific behavior, plan for customization with your internal data and validate safety.

## Source
- https://claude.com/blog/amazon-bedrock-general-availability
