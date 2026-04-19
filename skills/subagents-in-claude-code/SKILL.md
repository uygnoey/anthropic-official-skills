# Claude Code에서 Subagent 사용하기 / Using Subagents in Claude Code

> **출처 / Source**: [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code)
> **게시일 / Published**: 2026-04-07

---

## 🇰🇷 한국어

### 한 줄 요약
Subagent는 **자체 컨텍스트 창을 가진 독립된 Claude 인스턴스**다. 메인 세션의 컨텍스트가 터지기 전에, 탐색·병렬 작업·신선한 검토를 subagent에 위임하고, 결과만 돌려받는다.

### 언제 써야 하는가 (강한 신호)
- **탐색이 많은 작업**: 10개 이상 파일을 읽어야 할 때 (예: 인증 흐름 추적)
- **독립 과제 3개 이상**: 서로 의존 없는 수정 여러 건
- **신선한 관점이 필요할 때**: 구현과 분리된 리뷰
- **커밋 전 검증**: 2차 의견
- **파이프라인**: 설계 → 구현 → 테스트를 단계별로

### 쓰지 말아야 할 때
- 순차·의존 작업
- 같은 파일을 동시에 편집해야 하는 작업
- 오버헤드가 결과보다 큰 소규모 작업
- 에이전트 간 협력이 필요한 경우 (subagent끼리는 통신 불가 → Agent Teams 사용)

### 4가지 호출 방법
#### A. 대화형 (가장 쉬움)
자연어로 요청하면 Claude가 적절히 위임한다.
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```
기타 예: `Use a subagent to explore how authentication works in this codebase`, `Have a separate agent review this code for security issues`, `Spin up subagents to fix these TypeScript errors across the different packages`.

#### B. 커스텀 Subagent 파일
`.claude/agents/`(프로젝트) 또는 `~/.claude/agents/`(전역)에 MD 파일로 정의. `/agents`로 생성 가능.

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

#### C. CLAUDE.md 정책으로 자동 위임
프로젝트의 `CLAUDE.md`에 규칙을 심으면, 리뷰 요청 시 자동으로 read-only subagent가 동작한다.
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md

Return findings as a prioritized list with file:line references.
```

#### D. Skill 기반 슬래시 명령
`.claude/skills/deep-review/SKILL.md` 식으로 스킬을 만들고 `/deep-review`로 호출.
```markdown
---
name: deep-review
description: Comprehensive code review that checks security, performance, and style in parallel. Use when reviewing staged changes before a commit or PR.
---

Run three parallel subagent reviews on the staged changes:

1. Security review - check for vulnerabilities, injection risks, authentication issues, and sensitive data exposure
2. Performance review - check for N+1 queries, unnecessary iterations, memory leaks, and blocking operations
3. Style review - check for consistency with project patterns documented in /docs/style-guide.md

Synthesize findings into a single summary with priority-ranked issues.
Each issue should include the file, line number, and recommended fix.
```

### 실전 패턴 4가지
1. **Research-before-implement**
   ```
   Before I implement user notifications, use a subagent to research:
   - How are emails currently sent in this codebase?
   - Which libraries are available?
   - Is there an existing notification abstraction?
   ```
2. **Parallel edits** — 독립 파일의 같은 문제 고치기
3. **Fresh-eyes review** — 구현을 끝낸 뒤 read-only subagent로 검증
4. **Pipeline** — 설계 / 구현 / 테스트를 각각 다른 subagent에 위임

### 운영 팁
- `Ctrl+B` 로 subagent를 백그라운드로 보내고 메인 작업을 계속한다.
- `/tasks` 로 진행 중인 subagent 상태를 확인한다.
- 전문 에이전트를 과하게 만들면 자동 위임 판단이 흔들린다 — 꼭 필요한 역할만.
- Subagent 사이엔 직접 통신이 없으니, 협력이 필요하면 Agent Teams를 쓴다.

---

## 🇺🇸 English

### One-liner
A subagent is a **separate Claude instance with its own context window**. Delegate research, parallel work, or fresh reviews to subagents so your main session stays focused.

### When to use (strong signals)
- Research-heavy tasks (10+ files)
- 3+ independent subtasks
- Need for a fresh perspective
- Verification before committing
- Pipeline workflows (design → implement → test)

### When NOT to use
- Sequential / dependent work
- Simultaneous edits to the same file
- Small tasks where overhead > benefit
- When agents must coordinate (subagents can't talk to each other — use Agent Teams)

### Four ways to invoke
#### A. Conversational
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

#### B. Custom subagent file (`.claude/agents/`)
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
Invoke: `Have the security-reviewer look at the staged changes.`

#### C. CLAUDE.md policy
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md
```

#### D. Skills (slash command)
`.claude/skills/deep-review/SKILL.md` → run with `/deep-review`.

### Four practical patterns
1. Research-before-implement
2. Parallel edits on independent files
3. Fresh-eyes review (read-only)
4. Design / implement / test pipeline

### Operational tips
- `Ctrl+B` — send a subagent to the background.
- `/tasks` — inspect running subagents.
- Don't over-populate specialists: it destabilizes auto-delegation.
- Subagents can't communicate — use Agent Teams when they must.

---

## 주의 / Notes
- 본 문서는 원문 요약이며, 공식 가이드는 [원문](https://claude.com/blog/subagents-in-claude-code)을 참조하세요.
- Distilled summary. See the [original post](https://claude.com/blog/subagents-in-claude-code) for the authoritative version.
