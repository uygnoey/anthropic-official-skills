[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Building agents with the Claude Agent SDK

## 이 글이 뭔가요
A practical overview of the Claude 에이전트 SDK (formerly the Claude Code SDK) and the core patterns used to build reliable 에이전트s: an iterative 에이전트 loop, context gathering, action execution, and verification.

## 언제 유용한가요
Use it when you are designing or improving an 에이전트 that must work on real tasks (code or non-code) with access to tools such as the terminal, files, and external integrations.

## 핵심 포인트
- Use an explicit agent loop: gather context → take action → verify → repeat.
- Prefer tool access (search, file ops, bash) over asking the model to “guess”.
- Use subagents for parallel research and isolated reasoning contexts.
- Add verification steps (rules, visual checks, LLM-as-judge) to reduce regressions.
- Improve reliability with test sets/evals based on real user workflows.

## 번들 리소스
- Skill bundle: a reusable agent-loop checklist and verification checklist.

## 출처
- https://claude.com/blog/building-agents-with-the-claude-agent-sdk
