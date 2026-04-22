[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Building agents with the Claude Agent SDK

## この記事について
A practical overview of the Claude Agent SDK (formerly the Claude Code SDK) and the core patterns used to build reliable agents: an iterative agent loop, context gathering, action execution, and verification.

## どんなときに役立つか
Use it when you are designing or improving an agent that must work on real tasks (code or non-code) with access to tools such as the terminal, files, and external integrations.

## 主なポイント
- Use an explicit agent loop: gather context → take action → verify → repeat.
- Prefer tool access (search, file ops, bash) over asking the model to “guess”.
- Use subagents for parallel research and isolated reasoning contexts.
- Add verification steps (rules, visual checks, LLM-as-judge) to reduce regressions.
- Improve reliability with test sets/evals based on real user workflows.

## 同梱リソース
- Skill bundle: a reusable agent-loop checklist and verification checklist.

## 出典
- https://claude.com/blog/building-agents-with-the-claude-agent-sdk
