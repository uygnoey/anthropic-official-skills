# CLAUDE.md 파일로 Claude Code 커스터마이즈하기 / Customizing Claude Code with CLAUDE.md

> **출처 / Source**: [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files)
> **게시일 / Published**: 2025-11-25

---

## 🇰🇷 한국어

### 이 스킬이 해결하는 문제
Claude Code에 매번 프로젝트 구조, 코딩 스타일, 사용하는 명령을 반복해서 설명하는 일을 없애고 싶을 때. `CLAUDE.md` 파일을 두면 그 내용이 **모든 대화의 시스템 프롬프트에 자동으로 포함**됩니다.

> "CLAUDE.md files solve this by giving Claude persistent context about your project. Think of it as a configuration file that Claude automatically incorporates into every conversation."

### 언제 쓰는가
- 팀이 같은 코드베이스에서 작업하며 일관된 Claude 동작을 원할 때 (repo 루트에 커밋)
- 모노레포에서 하위 프로젝트별 규칙을 분리하고 싶을 때 (parent directory)
- 개인 전역 선호도를 적용하고 싶을 때 (`~/CLAUDE.md`)

### 핵심 원칙
1. **`/init`로 시작하라.** 기존 코드베이스를 분석해 초안을 만들어 줍니다.
2. **세 축으로 구성하라**: (1) 프로젝트 맵 (2) 도구 연결 (3) 표준 워크플로.
3. **간결하게, 실제 문제 중심으로.** "Start simple, expand deliberately."
4. **민감 정보 금지.** API 키, 자격증명, 보안 취약점 세부사항은 절대 넣지 말 것.

### 권장 구조 (섹션)
| 섹션 | 목적 | 넣을 것 |
|---|---|---|
| Give Claude a map | 프로젝트 개요 | 한 줄 요약, 디렉토리 트리, 주요 의존성, 아키텍처 패턴 |
| Connect to tools | 커스텀 도구/MCP | 커스텀 명령 사용법, MCP 서버 사용 규칙 |
| Define workflows | 표준 절차 | 작업 전 조사 질문, explore→plan→code→commit, TDD 규칙 |

### 예시: FastAPI 프로젝트용 CLAUDE.md
```markdown
# Project Context

When working with this codebase, prioritize readability over cleverness.
Ask clarifying questions before making architectural changes.

## About This Project

FastAPI REST API for user authentication and profiles.
Uses SQLAlchemy for database operations and Pydantic for validation.

## Key Directories

- `app/models/` - database models
- `app/api/` - route handlers
- `app/core/` - configuration and utilities

## Standards

- Type hints required on all functions
- pytest for testing (fixtures in `tests/conftest.py`)
- PEP 8 with 100 character lines

## Common Commands
​```bash
uvicorn app.main:app --reload  # dev server
pytest tests/ -v               # run tests
​```

## Notes

All routes use `/api/v1` prefix. JWT tokens expire after 24 hours.
```

### 예시: MCP 도구 사용 규칙 (Slack)
```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

### 체크리스트
- [ ] `/init`로 초안 생성했는가?
- [ ] 디렉토리 맵이 실제 구조와 일치하는가?
- [ ] 자주 쓰는 bash 명령이 들어있는가?
- [ ] API 키/비밀이 포함되지 않았는가?
- [ ] 팀 워크플로(테스트 규칙, PR 규칙)가 반영되어 있는가?

### 팁
- 대화 중 반복 지시가 필요하면 ` ``` ` 키로 바로 CLAUDE.md에 추가할 수 있다.
- 대형 지시사항은 별도 `.md`로 분리하고 CLAUDE.md에서 참조한다.
- 컨텍스트가 오염되면 `/clear`로 리셋, 분리된 작업은 subagent로 격리한다.
- 반복 작업은 `.claude/commands/` 아래에 커스텀 슬래시 명령(MD 파일, `$ARGUMENTS`/`$1` 활용)으로 만든다.

---

## 🇺🇸 English

### Problem this skill solves
You keep re-explaining project structure, style, and commands to Claude Code every session. `CLAUDE.md` puts that context into Claude's **system prompt automatically on every conversation**.

### When to use
- Teams that want consistent Claude behavior across a shared repo (commit the file)
- Monorepos where a parent directory defines rules for all sub-projects
- Personal global defaults (`~/CLAUDE.md`)

### Core principles
1. **Start with `/init`** — let Claude analyze the codebase and draft the file.
2. **Organize around three axes**: (1) project map, (2) tool connections, (3) standard workflows.
3. **Keep it concise and problem-driven.** "Each addition should solve a real problem you have encountered, not theoretical concerns."
4. **No secrets.** Never include API keys, credentials, or detailed security vulnerability information.

### Recommended sections
| Section | Purpose | Contents |
|---|---|---|
| Give Claude a map | Project overview | One-liner, directory tree, key dependencies, architecture patterns |
| Connect to tools | Custom commands / MCP | How to call custom commands, rules for MCP servers |
| Define workflows | Standard procedures | Pre-work questions, explore→plan→code→commit, TDD rules |

### Example: FastAPI project CLAUDE.md
(see the Korean section above — same content)

### Example: MCP tool rules (Slack)
```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

### Checklist
- [ ] Did you start from `/init`?
- [ ] Does the directory map match reality?
- [ ] Are common bash commands listed?
- [ ] Zero secrets / credentials?
- [ ] Team workflows (tests, PRs) captured?

### Tips
- During chat, press the ` ``` ` key to append a repeated instruction directly to CLAUDE.md.
- Split very long guidance into separate `.md` files and reference them from CLAUDE.md.
- Use `/clear` to reset context, and delegate isolated tasks to subagents.
- Put repeated workflows under `.claude/commands/` as custom slash commands (MD files, use `$ARGUMENTS` / `$1`).

---

## 주의 / Notes
- 본 문서는 원문 요약이며, 권위 있는 사용법은 반드시 [원문](https://claude.com/blog/using-claude-md-files)을 확인하세요.
- This is a distilled summary. Always defer to the [original post](https://claude.com/blog/using-claude-md-files) for authoritative guidance.
