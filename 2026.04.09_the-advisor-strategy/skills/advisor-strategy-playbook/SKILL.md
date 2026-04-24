---
name: advisor-strategy-playbook
description: Pair a lower-cost executor model with a higher-capability advisor model to get targeted guidance for hard decisions without paying frontier-model cost for every token.
---

## Overview
This skill captures the “advisor strategy” described in the Claude blog post and provides an implementation template for using the Claude Platform advisor tool in a Messages API request.

## When to use
Use this approach when:
- Your agent can usually make progress with a cost-effective model (executor) using tools and iteration.
- Occasionally, the agent reaches a decision point where higher-quality reasoning would materially improve outcomes.
- You want to cap and measure the higher-cost model’s usage (e.g., max advisor consultations per request).

## Instructions
1. Choose an executor model (e.g., Sonnet or Haiku) to run the task end-to-end.
2. Choose an advisor model (e.g., Opus) to provide guidance only when invoked.
3. Add the advisor tool entry to your Messages API `tools` list and set:
   - `model`: the advisor model
   - `max_uses`: maximum number of advisor consultations per request
4. Keep the advisor’s role limited to guidance:
   - It should return a plan, correction, or stop signal.
   - It should not call tools.
   - It should not produce user-facing final output.
5. Track costs and behavior:
   - Review the usage block for separate advisor token accounting.
   - Evaluate executor-only vs executor+advisor vs advisor-only to validate impact.

## Examples
- Messages API example (from the post): [examples/messages_api_example.py](./examples/messages_api_example.py)

## Source
- https://claude.com/blog/the-advisor-strategy
