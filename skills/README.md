# Skills Index

Claude 공식 블로그 글을 **글의 성격에 맞는 Claude 공식 규격**으로 정리한 모음. 4시간마다 배치가 돌며 새 글을 추가합니다.

## 각 폴더 구성

블로그 글 하나 = 폴더 하나. 폴더 안에는 항상 아래 네 파일이 있고, 글의 성격에 따라 `agents/` 또는 `guides/` 하위 폴더가 추가됩니다.

| 항목 | 항상? | 규격 | 설명 |
|---|---|---|---|
| `SKILL.md` | 항상 | [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) | 진입점. YAML frontmatter(name, description) + Instructions + Examples |
| `description.ko.md` / `description.en.md` | 항상 | 자유 | 사람용 한·영 해설 |
| `source.json` | 항상 | — | 원문 메타데이터 |
| `agents/<name>.md` | 조건부 | [Claude Code Subagent](https://code.claude.com/docs/en/sub-agents) | 원문에 명시된 에이전트 역할들을 Subagent 규격으로 정의. `.claude/agents/`에 바로 복사해 사용 가능 |
| `guides/<name>.md` | 조건부 | 자유 형식 | 원문이 방법론·배포·아키텍처 성격일 때 상세 참고 문서 |

### 규격 선택 기준
- **재사용 능력형 글** (문서 처리, 코드 작업, 특정 워크플로우 사용법) → SKILL.md만
- **에이전트 역할이 명시된 글** (named 역할 2개 이상) → SKILL.md + `agents/*.md`
- **배포·아키텍처·방법론 성격 글** → SKILL.md + `guides/<slug>.md`

## 목록

| Skill | 주제 | 규격 | 원문 게시일 |
|---|---|---|---|
| [using-subagents](./using-subagents/SKILL.md) | How and when to use subagents in Claude Code | SKILL | 2026-04-07 |
| [project-context-files](./project-context-files/SKILL.md) | Using CLAUDE.MD files to customize Claude Code | SKILL | 2025-11-25 |
| [prompt-engineering-techniques](./prompt-engineering-techniques/SKILL.md) | Prompt engineering best practices | SKILL | 2025-11-10 |
| [financial-services-agent-deployment](./financial-services-agent-deployment/SKILL.md) | Building and deploying AI agents safely in financial services | SKILL + 3 agents + guide | 2025-10-30 |
| [browser-based-code-delegation](./browser-based-code-delegation/SKILL.md) | Delegating coding tasks from a web UI connected to GitHub | SKILL | 2025-10-20 |
