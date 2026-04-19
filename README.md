# skills-from-claude-blog

> Artifacts distilled from posts on [claude.com/blog](https://www.claude.com/blog),
> organized by Claude's official specs.
> Not affiliated with Anthropic — this is a third-party summary project.

Claude 공식 블로그의 글 하나하나를 **글의 성격에 맞는 공식 규격**으로 변환해 모은 저장소입니다. 4시간마다 배치가 돌며 신규 글과 미처리 글을 찾아 반영합니다.

## Layout (per blog post)

블로그 글 하나 = `posts/<blog-slug>/` 폴더 하나. 글의 성격에 따라 안에 들어가는 artifact가 달라집니다.

```
posts/<blog-slug>/
├── description.ko.md             # 사람용 한국어 해설 (항상)
├── description.en.md             # 사람용 영어 해설 (항상)
├── source.json                   # 원문 URL·제목·게시일 (항상)
│
├── skills/<skill-name>/          # Agent Skills 규격 — 재사용 능력형 글이면 생성
│   └── SKILL.md
│
├── agents/<agent-name>.md        # Claude Code Subagent 규격 — 글에 에이전트 역할이 명시되면 생성
│
└── guides/<name>.en.md           # 자유 형식 — 배포·방법론·아키텍처 성격 글이면 생성
    <name>.ko.md
```

### 규격별 공식 문서
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — `SKILL.md`는 이 규격
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — `agents/*.md`는 이 규격

### 규격 선택 기준
각 블로그 글을 읽고 아래 중 해당되는 것을 **모두** 선택:
- **A. 재사용 능력형** (문서 처리, 코드 작업, 특정 워크플로우 설명) → `skills/<name>/SKILL.md`
- **B. 에이전트 역할이 명시된 글** (named 역할 2개 이상) → `agents/<name>.md` 파일들 추가
- **C. 배포·아키텍처·방법론 성격** (스테이지, 프레임워크, 체크리스트, 사례) → `guides/<name>.{en,ko}.md` 추가

원문에 없는 역할·가이드를 지어내지 않습니다.

## Drop-in usage

이 저장소의 artifact들은 그대로 `.claude/` 아래 해당 위치에 복사해 사용할 수 있습니다.

- Skill을 쓰려면: `posts/<blog>/skills/<name>/` → `.claude/skills/<name>/` 또는 `~/.claude/skills/<name>/`
- Subagent를 쓰려면: `posts/<blog>/agents/<name>.md` → `.claude/agents/<name>.md` 또는 `~/.claude/agents/<name>.md`

## Index

| Blog post | Artifacts |
|---|---|
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide (en/ko) |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide (en/ko) |
| [claude-code-on-the-web](posts/claude-code-on-the-web/) (2025-10-20) | 1 skill |
| [building-ai-agents-in-financial-services](posts/building-ai-agents-in-financial-services/) (2025-10-30) | 1 skill + 3 agents + 1 guide (en/ko) |
| [best-practices-for-prompt-engineering](posts/best-practices-for-prompt-engineering/) (2025-11-10) | 1 skill |
| [using-claude-md-files](posts/using-claude-md-files/) (2025-11-25) | 1 skill |
| [subagents-in-claude-code](posts/subagents-in-claude-code/) (2026-04-07) | 1 skill |


## Batch operation

- Perplexity Computer cron이 4시간마다 실행
- `https://www.claude.com/sitemap.xml`과 `/blog` 인덱스에서 글 목록 수집
- 우선순위: (1) 마지막 배치 이후 신규 글 (최신순) → (2) 미처리 기존 글 (오래된순) → (3) 게시일 미상
- 한 번에 최대 2개 글을 처리. 결과는 `git commit && push`로 자동 반영.

## Authoring guidelines

1. `SKILL.md`와 `agents/*.md`는 공식 규격이 영문 기반이므로 **영문**으로 작성.
2. `name` 필드에 `claude`, `anthropic` 예약어 금지. 소문자·숫자·하이픈만, 64자 이하.
3. `description`은 3인칭, 1024자 이하, "무엇을 한다 + 언제 사용해야 한다" 둘 다 포함.
4. `guides/`는 사람용이므로 `.en.md`와 `.ko.md` 두 언어로 작성.
5. 사람용 해설은 post 루트의 `description.ko.md` / `description.en.md`에 작성.
6. **원문에 없는 내용은 지어내지 않는다.** 확신 없으면 "원문 참고"로 넘긴다.

## Files

```
.
├── posts/                       # 블로그 글 하나당 폴더 하나
├── scripts/
│   ├── list_pending.py          # 대기 목록 조회 (우선순위 반영)
│   ├── mark_processed.py        # 처리 완료 기록
│   └── update_last_run.py       # 배치 실행 타임스탬프
└── state/
    └── processed.json           # 처리된 URL 기록 + last_run_at
```

## License

- 원문(Claude 블로그 글)의 저작권은 Anthropic에 있습니다. 이 저장소는 학습·참고 목적의 요약·인용만 포함합니다.
- 저장소 자체 코드(스크립트, 구조)는 MIT License.
