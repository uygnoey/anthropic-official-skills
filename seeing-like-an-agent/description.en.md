**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post explains how the Claude Code team designs and iterates on agent tools by thinking from the model’s perspective—“seeing like an agent.”

## When is it useful?
Useful when you are building agent tooling (or an agent platform) and need to decide whether to add a new tool, how to shape its interface, and how to avoid overwhelming the model with options.

## Key points
- Tool interfaces should match the model’s current capabilities; revisit assumptions as model capabilities change.
- Adding tools has a cost: more options to consider increases decision burden.
- Prefer progressive disclosure (and reusable “skills” documentation) over adding narrowly scoped tools.
- When a tool becomes a bottleneck, replace it with a more expressive primitive (e.g., replacing a todos tool with a task abstraction).
- For user clarification, a dedicated question tool can be more reliable than overloading another tool.

## Bundled resources
- Skill: design heuristics for agent tool interfaces, progressive disclosure, and “high bar” criteria for adding new tools.

## Source
- https://claude.com/blog/seeing-like-an-agent
