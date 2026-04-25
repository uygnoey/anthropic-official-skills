[English](./README.md) · **한국어** · [Español](./README.es.md) · [日本語](./README.ja.md)

# skills-from-claude-blog

> [claude.com/blog](https://www.claude.com/blog)의 글을 Claude Code 공식 확장 규격에 맞춰 정리한 저장소.
> Anthropic과 무관한 제3자 요약 프로젝트입니다.

Claude 공식 블로그 글을 **글의 성격에 맞는 Claude Code 공식 규격**으로 변환해 모은 저장소입니다. 4시간마다 배치가 돌며 신규 글과 미처리 글을 반영합니다.

## 폴더 구조 (블로그 글 하나당)

블로그 글 하나 = 리포지토리 루트 아래 `<YYYY.MM.DD>_<blog-slug>/` 폴더 하나. 앞 날짜 접두어는 글의 `published_date`를 `YYYY.MM.DD`로 변환한 값, `<blog-slug>`는 URL 마지막 세그먼트입니다. GitHub에서 최신글부터 자연스럽게 정렬됩니다. 글의 성격에 따라 아래 폴더들이 선택적으로 들어갑니다.

```
<YYYY.MM.DD>_<blog-slug>/
├── description.en.md               # 영어 해설 (항상)
├── description.ko.md               # 한국어 해설 (항상)
├── description.es.md               # 스페인어 해설 (항상)
├── description.ja.md               # 일본어 해설 (항상)
├── source.json                     # 원문 메타 (항상)
│
├── skills/<name>/SKILL.md          # A. Agent Skills 규격
├── agents/<name>.md                # B. Claude Code Subagent 규격
├── guides/<name>.{en,ko,es,ja}.md  # C. 자유 형식 4개 언어 가이드
├── hooks/<name>.json +.md          # D. Claude Code Hooks JSON + 설명
├── output-styles/<name>.md         # E. Output Style 규격
└── plugin/                         # G. Plugin 번들 (드묾)
    ├── .claude-plugin/plugin.json
    └── skills|agents|hooks|output-styles/...
```

### 공식 규격 문서
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — `SKILL.md`
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — `agents/<name>.md`
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) — `hooks/<name>.json`
- [Output Styles](https://code.claude.com/docs/en/output-styles) — `output-styles/<name>.md`
- [Plugins](https://code.claude.com/docs/en/plugins) — `plugin/` 전체 번들

### 규격 선택 매트릭스

| 판정 | 트리거 질문 | 결과물 |
|---|---|---|
| **A. Skill** | 독자가 재사용할 수 있는 **패턴·원칙·프레임워크·how-to**가 있는가? | `skills/<name>/SKILL.md` |
| **B. Subagent** | 글에 **named agent 역할**이 2개 이상 명시되어 있는가? | `agents/<name>.md` 각각 |
| **C. Guide** | 글이 **배포·아키텍처·방법론·서베이** 성격인가? | `guides/<name>.{en,ko,es,ja}.md` |
| **D. Hook** | 글이 **PreToolUse/PostToolUse/Stop/SessionStart 등 lifecycle event**에서의 자동화를 설명하는가? | `hooks/<name>.json` + `hooks/<name>.md` 설명 |
| **E. Output Style** | 글이 **시스템 프롬프트 톤/역할/포맷 전체 변경**을 설명하는가? (한두 문장 팁이 아닌 전체 스타일 정의) | `output-styles/<name>.md` |
| **G. Plugin** | 글이 **여러 artifact를 하나의 번들로 배포**하는 방법을 중심으로 다루는가? | `plugin/` 번들 전체 |

- **F. Slash Command은 만들지 않음.** 공식 문서가 `.claude/commands/`를 legacy로 표기하고 `.claude/skills/`를 권장 중이라, 글이 slash command를 다루면 **Skill로 변환**합니다.
- 여러 판정이 동시에 해당되는 게 정상. 전부 생성.
- 판정 불확실 시 기본값은 **A 포함**. 독자 관점에서 Skill이 가장 실용적이기 때문.
- **원문에 없는 역할·패턴·스크립트를 지어내지 않습니다.** 불확실하면 원문 인용으로 대체.

## 바로 쓰는 법

각 artifact는 그대로 해당 위치에 복사해 쓸 수 있습니다.

| Artifact | 목적지 |
|---|---|
| `skills/<name>/` | `.claude/skills/<name>/` 또는 `~/.claude/skills/<name>/` |
| `agents/<name>.md` | `.claude/agents/<name>.md` 또는 `~/.claude/agents/<name>.md` |
| `hooks/<name>.json` 내용 | `.claude/settings.json`의 `hooks` 필드에 병합 |
| `output-styles/<name>.md` | `.claude/output-styles/<name>.md` |
| `plugin/` | `--plugin-dir ./plugin` 로 로드 |

## 색인

| 블로그 글 | 게시일 | Artifacts |
|---|---|---|
| [New connectors in Claude for everyday life](https://claude.com/blog/connectors-for-everyday-life) | 2026-04-23 | 1 skill |
| [Built-in memory for Claude Managed Agents](https://claude.com/blog/claude-managed-agents-memory) | 2026-04-23 | 1 skill + 1 guide |
| [Building agents that reach production systems with MCP](https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp) | 2026-04-22 | 1 skill |
| [Meet the winners of our Built with Opus 4.6 Claude Code hackathon](https://claude.com/blog/meet-the-winners-of-our-built-with-opus-4-6-claude-code-hackathon) | 2026-04-20 | 1 skill |
| [Best practices for using Claude Opus 4.7 with Claude Code](https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code) | 2026-04-16 | 1 skill + 1 guide |
| [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) | 2026-04-15 | 1 skill + 1 guide |
| [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) | 2026-04-14 | 1 skill + 1 guide |
| [Redesigning Claude Code on desktop for parallel agents](https://claude.com/blog/claude-code-desktop-redesign) | 2026-04-14 | 1 skill |
| [Seeing like an agent: how we design tools in Claude Code](https://claude.com/blog/seeing-like-an-agent) | 2026-04-10 | 1 skill |
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skill + 3 agent + 1 guide |
| [Multi-agent coordination patterns: Five approaches and when to use them](https://claude.com/blog/multi-agent-coordination-patterns) | 2026-04-10 | 1 skill + 1 guide |
| [The advisor strategy: Give agents an intelligence boost](https://claude.com/blog/the-advisor-strategy) | 2026-04-09 | 1 skill |
| [Making Claude Cowork ready for enterprise](https://claude.com/blog/cowork-for-enterprise) | 2026-04-09 | 1 skill |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [How Carta Healthcare gets AI to reason like a clinical abstractor](https://claude.com/blog/carta-healthcare-clinical-abstractor) | 2026-04-08 | 1 skill |
| [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skill + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence: 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Audit Claude Platform activity with the Compliance API](https://claude.com/blog/claude-platform-compliance-api) | 2026-03-30 | 1 skill |
| [Auto mode for Claude Code](https://claude.com/blog/auto-mode) | 2026-03-24 | 1 skill |
| [Put Claude to work on your computer](https://claude.com/blog/dispatch-and-computer-use) | 2026-03-23 | 1 skill |
| [Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo) | 2026-03-18 | 1 skill + 1 guide |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates) | 2026-03-11 | 1 skill + 1 guide |
| [Common workflow patterns for AI agents](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them) | 2026-03-05 | 1 skill + 1 guide |
| [Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance) | 2026-02-24 | 1 guide |
| [Cowork and plugins for teams across the enterprise](https://claude.com/blog/cowork-plugins-across-enterprise) | 2026-02-24 | 1 guide |
| [How AI helps break the cost barrier to COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) | 2026-02-23 | 1 skill |
| [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early) | 2026-02-09 | 1 skill |
| [Customize Cowork with plugins - Claude.ai](https://claude.com/blog/cowork-plugins) | 2026-01-30 | 1 guide |
| [Measure Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics) | 2026-01-29 | 1 skill |
| [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) | 2026-01-29 | 1 skill + 1 guide |
| [Updates to Claude Team](https://claude.com/blog/claude-team-updates) | 2026-01-28 | 1 skill |
| [How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-marketing) | 2026-01-26 | 1 skill |
| [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) | 2026-01-23 | 1 skill |
| [Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work) | 2026-01-22 | 1 skill + 1 guide |
| [Eight trends defining how software gets built in 2026](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026) | 2026-01-21 | 1 skill |
| [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) | 2025-12-19 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [How Anthropic's legal team cut review times from days to hours with Claude](https://claude.com/blog/how-anthropic-uses-claude-legal) | 2025-12-08 | 1 skill |
| [Claude Code and Slack](https://claude.com/blog/claude-code-and-slack) | 2025-12-08 | 1 skill |
| [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code) | 2025-11-17 | 1 skill + 1 guide |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for startups](https://claude.com/blog/building-ai-agents-for-startups) | 2025-11-03 | 1 skill |
| [Building AI agents in healthcare and life sciences](https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences) | 2025-10-30 | 1 skill + 1 guide |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agent + 1 guide |
| [Fix software bugs faster with Claude](https://claude.com/blog/fix-software-bugs-faster-with-claude) | 2025-10-28 | 1 skill |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Build responsive web layouts](https://claude.com/blog/build-responsive-web-layouts) | 2025-10-10 | 1 skill |
| [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins) | 2025-10-09 | 1 skill + 1 guide + 1 plugin |
| [Beyond permission prompts: making Claude Code more secure and autonomous](https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous) | 2025-10-08 | 1 skill |
| [How enterprises are driving AI transformation with Claude](https://claude.com/blog/driving-ai-transformation-with-claude) | 2025-10-01 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |
| [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management) | 2025-09-29 | 1 skill |
| [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | 2025-09-29 | 1 skill |
| [Claude is now available in Microsoft 365 Copilot](https://claude.com/blog/claude-now-available-in-microsoft-365-copilot) | 2025-09-24 | 1 skill + 1 guide |
| [Claude can now create and edit files](https://claude.com/blog/create-files) | 2025-09-09 | 1 skill |
| [Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) | 2025-08-25 | 1 skill + 1 guide |
| [Claude Code and new admin controls for business plans](https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans) | 2025-08-20 | 1 skill |
| [Claude Sonnet 4 now supports 1M tokens of context](https://claude.com/blog/1m-context) | 2025-08-12 | 1 skill |
| [Automate security reviews with Claude Code](https://claude.com/blog/automate-security-reviews-with-claude-code) | 2025-08-06 | 1 skill |
| [Build and share AI-powered apps with Claude](https://claude.com/blog/claude-powered-artifacts) | 2025-07-25 | 1 skill |
| [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | 2025-07-24 | 1 skill |
| [Discover tools that work with Claude](https://claude.com/blog/connectors-directory) | 2025-07-14 | 1 skill |
| [Turn ideas into interactive AI-powered apps](https://claude.com/blog/build-artifacts) | 2025-06-25 | 1 skill |
| [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) | 2025-06-18 | 1 skill + 1 guide |
| [Mcp Connector](https://claude.com/blog/agent-capabilities-api) | 2025-05-22 | 1 skill |
| [Claude on Google Cloud’s Vertex AI: FedRAMP High and IL2 Authorized](https://claude.com/blog/claude-on-google-cloud-fedramp-high) | 2025-04-02 | 1 skill |
| [Introducing the analysis tool in Claude.ai](https://claude.com/blog/analysis-tool) | 2024-10-24 | 1 skill |
| [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) | 2024-09-10 | 1 skill + 1 guide |
| [Claude Android app](https://claude.com/blog/android-app) | 2024-07-16 | 1 skill |
| [Fine-tune Claude 3 Haiku in Amazon Bedrock](https://claude.com/blog/fine-tune-claude-3-haiku) | 2024-07-10 | 1 skill |
| [Evaluate prompts in the developer console](https://claude.com/blog/evaluate-prompts) | 2024-07-09 | 1 skill |
| [Long context prompting for Claude 2.1](https://claude.com/blog/claude-2-1-prompting) | 2023-12-06 | 1 skill |
| [Claude on Amazon Bedrock now available to every AWS customer](https://claude.com/blog/amazon-bedrock-general-availability) | 2023-09-28 | 1 skill |
| [Claude 2 on Amazon Bedrock](https://claude.com/blog/claude-2-amazon-bedrock) | 2023-08-23 | 1 skill |


모든 가이드와 해설은 영어·한국어·스페인어·일본어로 제공되며, 각 파일 상단의 언어 선택 링크로 전환할 수 있습니다.

## 배치 운영

- Perplexity Computer 크론이 4시간마다 실행
- `https://www.claude.com/sitemap.xml`과 `/blog` 인덱스에서 글 목록 수집
- 우선순위: 마지막 배치 이후 신규 글 (최신→과거) → 미처리 기존 글 (오래된→최신) → 게시일 미상
- 한 번에 최대 2개 글 처리

## 작성 지침

1. `SKILL.md`와 `agents/*.md`는 공식 규격이 영문 기반이므로 **영문**으로 작성.
2. Hook JSON은 원문의 동작을 정확히 반영. 셸 명령은 주석으로 출처 명시.
3. Output Style은 글에 명시된 톤·역할·포맷을 그대로 옮김. 확신 없으면 guide로 돌림.
4. `name` 필드(Skill, Subagent, Output Style, Plugin)는 `^[a-z0-9-]+$`, 64자 이하, `claude`·`anthropic` 예약어 금지.
5. `description`은 3인칭, 1024자 이하 (Skill·Subagent).
6. `guides/`는 `.en.md` · `.ko.md` · `.es.md` · `.ja.md` 네 개 언어로 작성, 상단에 언어 선택 링크.
7. 사람용 해설(`description.*.md`)도 네 개 언어로 작성, 상단에 언어 선택 링크.
8. **원문에 없는 내용 창작 금지.** 불확실하면 "원문 참고"로 처리.
9. **artifact는 self-contained.** `SKILL.md`, `agents/*.md`, `hooks/*.md`, `output-styles/*.md`는 자기 폴더 밖을 참조하지 않습니다. `../` 경로, 다른 artifact 간 링크, `description.*.md`나 `guides/`로 돌아가는 링크 모두 금지. 외부 자료가 필요하면 로컬 컴패니언 파일(`references/`, `examples/`, `templates/`, `scripts/`, `prompts/`, `assets/` 또는 형제 `.md`)로 복사해서 쓰세요.

## 파일

```
.
├── <YYYY.MM.DD>_<blog-slug>/           # 블로그 글 하나당 폴더 하나, 날짜 접두어 포함
├── scripts/
│   ├── list_pending.py          # 대기 목록 조회
│   ├── mark_processed.py        # 처리 완료 기록
│   ├── update_last_run.py       # 배치 타임스탬프
│   └── validate.py              # 전 규격 검증 (pre-commit)
└── state/
    └── processed.json           # 처리된 URL + last_run_at
```

## 라이선스

- 원문(Claude 블로그 글) 저작권은 Anthropic. 이 저장소는 학습·참고 목적의 요약·인용만 포함.
- 저장소 코드는 MIT License.
