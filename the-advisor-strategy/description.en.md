**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces the “advisor strategy”: pairing a stronger model (Opus) as an advisor with a cheaper model (Sonnet or Haiku) as the executor, to get near frontier-level guidance at lower overall cost.

## When is it useful?
Use it when you want an agentic workflow that can run end-to-end with tools most of the time, but occasionally needs higher-quality reasoning for a hard decision—without paying for the strongest model for every token.

## Key points
- The executor (Sonnet/Haiku) runs the task end-to-end: calls tools, reads results, iterates.
- When needed, the executor consults the advisor (Opus), which returns a plan/correction/stop signal but does not call tools or produce user-facing output.
- The Claude Platform “advisor tool” makes this a small change to a Messages API request and keeps the handoff within a single request.
- You can cap advisor calls with `max_uses`, and advisor usage is reported separately.

## Bundled resources
- A skill that documents the advisor strategy and includes the exact API snippet from the post: `skills/advisor-strategy-playbook/SKILL.md`.
- A runnable example file containing the API snippet: `skills/advisor-strategy-playbook/examples/messages_api_example.py`.

## Source
- https://claude.com/blog/the-advisor-strategy
