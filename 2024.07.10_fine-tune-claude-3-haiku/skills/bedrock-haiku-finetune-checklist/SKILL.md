---
name: bedrock-haiku-finetune-checklist
description: Checklist-style workflow for preparing prompt–completion training data and evaluating a fine-tuned Claude 3 Haiku model in Amazon Bedrock.
---

## Instructions

Use this skill as a lightweight project checklist when you are about to fine-tune Claude 3 Haiku in Amazon Bedrock.

1. Define the target task and success criteria
   - State the task in one sentence.
   - Decide how you will measure improvement (accuracy, consistency, formatting compliance, latency/cost).

2. Build prompt–completion pairs
   - Collect representative inputs.
   - Write the ideal completions you want the model to produce.
   - Keep formatting consistent with the desired production output.

3. Validate data quality
   - Remove ambiguous or contradictory examples.
   - Ensure labels and rubric match the completions.
   - Check for sensitive data and compliance requirements.

4. Run an initial fine-tune and evaluate
   - Test on a held-out evaluation set.
   - Compare against a baseline model.
   - Inspect failure cases and add targeted examples.

5. Iterate and prepare for deployment
   - Repeat fine-tuning with updated data until metrics and qualitative checks meet your bar.
   - Plan the deployment path in Bedrock (console or API) and monitor ongoing performance.

## Examples

- Classification moderation example: create labeled prompt–completion pairs for categories like insults, threats, or explicit content, then evaluate accuracy improvements against your baseline.
- Structured output example: build prompt–completion pairs where completions adhere to your report/schema format and verify formatting consistency during evaluation.
