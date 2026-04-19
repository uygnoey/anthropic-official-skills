# CLAUDE.md로 Claude Code 커스터마이즈

## 이 스킬이 뭔가요
Claude Code에 매번 프로젝트 구조·코딩 스타일·자주 쓰는 명령을 반복 설명하는 일을 없애줍니다. 프로젝트 루트에 `CLAUDE.md` 파일 하나 두면 Claude가 **모든 대화 시작 시점에 그 내용을 시스템 프롬프트로 자동 로드**합니다.

## 언제 써야 하나요
- 같은 코드베이스에서 팀이 일관된 Claude 동작을 원할 때 (repo에 커밋)
- 모노레포에서 여러 하위 프로젝트가 규칙을 공유할 때 (상위 디렉토리에 배치)
- 개인 전역 선호를 걸고 싶을 때 (`~/CLAUDE.md`)
- 세션마다 같은 지시를 반복하는 자신을 발견할 때

## 핵심 원칙
1. **`/init`으로 시작하라.** 기존 코드베이스를 분석해 초안을 만들어 줍니다.
2. **세 축으로 구성하라**: (1) 프로젝트 맵 (2) 도구 연결 (3) 표준 워크플로.
3. **실제 문제만 담아라.** 이론적·가상의 규칙은 빼라.
4. **민감 정보 금지.** API 키, 자격증명, 보안 취약점 세부사항은 절대 넣지 말 것.

## 권장 구조
| 섹션 | 목적 | 넣을 것 |
|---|---|---|
| Project map | 프로젝트 개요 | 한 줄 요약, 디렉토리 트리, 주요 의존성, 아키텍처 패턴 |
| Tool connections | 커스텀 도구/MCP | 커스텀 명령 사용법, MCP 서버 사용 규칙 |
| Workflows | 표준 절차 | 작업 전 조사 질문, explore→plan→code→commit, TDD 규칙 |

## 예시: FastAPI 프로젝트용 CLAUDE.md

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

## 예시: MCP 도구 사용 규칙 (Slack)

```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

## 작성 체크리스트
- [ ] `/init`로 초안을 만들었는가?
- [ ] 디렉토리 맵이 실제 구조와 일치하는가?
- [ ] 자주 쓰는 bash 명령이 들어있는가?
- [ ] API 키/비밀이 포함되지 않았는가?
- [ ] 팀 워크플로(테스트 규칙, PR 규칙)가 반영되어 있는가?

## 유지 관리 팁
- 대화 중 반복 지시가 필요하면 ` ``` ` (백틱 3개)로 바로 CLAUDE.md에 추가한다.
- 반복 작업은 `.claude/commands/` 아래에 커스텀 슬래시 명령(MD 파일, `$ARGUMENTS`/`$1` 활용)으로 만든다.
- 컨텍스트가 오염되면 `/clear`로 리셋, 분리된 작업은 subagent로 격리한다.
- 대형 지시사항은 별도 `.md`로 분리하고 CLAUDE.md에서 참조한다.

## 출처
[Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) (2025-11-25) 요약. 권위 있는 사용법은 반드시 원문을 확인하세요.
