# skills-from-claude-blog

> Agent Skills distilled from posts on [claude.com/blog](https://www.claude.com/blog).
> Not affiliated with Anthropic — this is a third-party summary project.

Anthropic의 공식 블로그 글을 읽어, Claude Code/API에서 바로 쓸 수 있는 [Agent Skills](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview) 형식의 `SKILL.md`로 정리하는 저장소입니다. 4시간마다 배치가 돌면서 신규 글과 미정리 글을 찾아 반영합니다.

## Skill layout (per folder)

```
skills/<skill-name>/
├── SKILL.md           # Anthropic Skills spec: YAML frontmatter + English instructions + examples
├── description.ko.md  # 한국어 해설 (이 스킬 소개, 사용 시점, 예시)
├── description.en.md  # English explainer (overview, when to use, examples)
└── source.json        # original blog URL, title, published date
```

`SKILL.md`는 [Anthropic Agent Skills 규격](https://docs.claude.com/en/docs/agents-and-tools/agent-skills/overview)을 따릅니다.
- `name`: 소문자/숫자/하이픈, 최대 64자, `anthropic`/`claude` 예약어 금지
- `description`: 3인칭, 1024자 이내, 스킬이 하는 일 + 언제 쓰는지 포함
- 본문: 500줄 이내, Instructions + Examples 구조

## Batch operation

- Perplexity Computer cron이 4시간마다 실행
- `https://www.claude.com/sitemap.xml`과 `/blog` 인덱스에서 글 목록 수집
- 우선순위: (1) 마지막 배치 이후 신규 글 (최신순) → (2) 미처리 기존 글 (오래된순) → (3) 게시일 미상
- 한 번에 최대 2개 글을 처리. 처리 결과는 `git commit && push`로 자동 반영.

## Files / 디렉토리

```
.
├── skills/           # 정제된 스킬 모음
│   ├── README.md     # 인덱스
│   └── <skill>/
├── scripts/          # 대기 목록 조회, 상태 기록, 배치 타임스탬프
└── state/
    └── processed.json  # 처리된 URL과 last_run_at
```

## Authoring guidelines

1. **SKILL.md는 영어**로 작성하고 Anthropic 공식 규격을 따른다.
2. 스킬명(폴더명)에 `claude` 또는 `anthropic` 넣지 않는다.
3. description은 "무엇을 한다" + "언제 사용하는지" 둘 다 포함해야 한다.
4. 본문은 Instructions → Examples → (선택) Anti-patterns → Source 순을 권장.
5. 한국어 해설은 `description.ko.md`, 영문 해설은 `description.en.md`로 분리.
6. 원문에 없는 내용은 지어내지 않는다 — 출처 명시 필수.

## License

- 원문(Anthropic 블로그 글)의 저작권은 Anthropic에 있습니다. 이 저장소는 학습·참고 목적의 요약·인용만 포함합니다.
- 저장소 자체 코드(스크립트, 구조)는 MIT License.
