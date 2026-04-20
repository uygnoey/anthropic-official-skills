[English](./description.en.md) · **한국어** · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Code에서 Subagent 사용하기

## 이 스킬이 뭔가요
Subagent는 **자체 컨텍스트 창을 가진 독립된 Claude 인스턴스**입니다. 메인 세션 컨텍스트가 터지기 전에 탐색·병렬 작업·신선한 검토를 subagent에 위임하고 결과만 돌려받는 패턴을 정리했습니다.

## 언제 써야 하나요 (강한 신호)
- **탐색이 많은 작업**: 10개 이상 파일을 읽어야 할 때
- **독립 과제 3개 이상**: 서로 의존 없는 수정 여러 건
- **신선한 관점이 필요할 때**: 구현과 분리된 리뷰
- **커밋 전 검증**: 2차 의견
- **파이프라인**: 설계 → 구현 → 테스트를 단계별로

## 쓰지 말아야 할 때
- 순차·의존 작업
- 같은 파일을 동시에 편집해야 하는 작업
- 오버헤드가 결과보다 큰 소규모 작업
- 에이전트 간 협력이 필요한 경우 (subagent끼리는 통신 불가 → Agent Teams 사용)

## 4가지 호출 방법

### A. 대화형 (가장 쉬움)
자연어로 요청하면 Claude가 적절히 위임합니다.
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

### B. 커스텀 Subagent 파일
`.claude/agents/`(프로젝트) 또는 `~/.claude/agents/`(전역)에 MD 파일로 정의.

```markdown
---
name: security-reviewer
description: Reviews code changes for security vulnerabilities, injection risks, auth issues, and sensitive data exposure. Use proactively before commits touching auth, payments, or user data.
tools: Read, Grep, Glob
model: sonnet
---

You are a security-focused code reviewer. Analyze the provided changes for:
- SQL injection, XSS, and command injection risks
- Authentication and authorization gaps
- Sensitive data in logs, errors, or responses
- Insecure dependencies or configurations

Return a prioritized list of findings with file:line references and a recommended fix for each.
Be critical. If you find nothing, say so explicitly rather than inventing issues.
```

호출: `Have the security-reviewer look at the staged changes.`

### C. CLAUDE.md 정책으로 자동 위임
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md

Return findings as a prioritized list with file:line references.
```

### D. Skill 기반 슬래시 명령
`.claude/skills/deep-review/SKILL.md` 식으로 스킬을 만들고 `/deep-review`로 호출.

## 실전 패턴 4가지
1. **Research-before-implement** — 영역 탐색 후 구현
2. **Parallel edits** — 독립 파일 여러 개 동시 수정
3. **Fresh-eyes review** — 구현 끝나면 read-only subagent로 검증
4. **Pipeline** — 설계 / 구현 / 테스트를 분담

## 운영 팁
- `Ctrl+B` 로 subagent를 백그라운드로 보내고 메인 작업을 계속한다.
- `/tasks` 로 진행 중인 subagent 상태를 확인한다.
- 전문 에이전트를 과하게 만들면 자동 위임 판단이 흔들린다 — 꼭 필요한 역할만.
- Subagent 사이엔 직접 통신이 없으니, 협력이 필요하면 Agent Teams를 쓴다.

## 번들 리소스
- Skills (2개): `skills/using-subagents/SKILL.md`, `skills/deep-review/SKILL.md`
- Agent (1개): `agents/security-reviewer.md`
- Hook (1개): `hooks/check-tests.json` / `hooks/check-tests.md`

## 출처
[How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) (2026-04-07) 요약. 권위 있는 사용법은 원문을 참조하세요.
