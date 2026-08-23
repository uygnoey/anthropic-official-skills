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
| [The AI-Native SDLC playbook](https://claude.com/blog/the-ai-native-sdlc-playbook) | 2026-08-21 | 1 skill + 3 agent + 2 hook + 1 guide |
| [Bringing the cybersecurity capabilities of Claude Mythos 5 to more defenders](https://claude.com/blog/bringing-claude-mythos-5-to-more-defenders) | 2026-08-21 | 1 skill + 1 guide |
| [How monday.com transformed its platform into an agent-first product where humans and agents collaborate](https://claude.com/blog/how-monday-com-transformed-its-platform-into-an-agent-first-product-where-humans-and-agents-collaborate) | 2026-08-20 | 1 skill + 5 agent + 1 guide |
| [Build production agents with computer use, the Skills API, and the Files API](https://claude.com/blog/computer-use-skills-api-files-api) | 2026-08-20 | 1 skill + 1 guide |
| [The Claude Code guide for startups](https://claude.com/blog/claude-code-guide-for-startups) | 2026-08-20 | 1 skill + 4 agent + 1 guide |
| [Anthropic's approach to teaching and learning AI](https://claude.com/blog/anthropics-approach-to-teaching-and-learning-ai) | 2026-08-20 | 1 skill + 1 guide |
| [Turning conversation into knowledge: how Slack builds human-agent teams](https://claude.com/blog/turning-conversation-into-knowledge-how-slack-builds-human-agent-teams) | 2026-08-19 | 1 skill + 1 guide |
| [The Claude Science product guide](https://claude.com/blog/the-claude-science-product-guide) | 2026-08-18 | 1 skill + 1 guide |
| [Claude on call: How Claude Tag serves as Anthropic's first responder for CI/CD failures](https://claude.com/blog/ai-ci-cd-on-call) | 2026-08-18 | 1 skill + 3 agent + 1 guide |
| [How ABC Legal turned every employee into a builder with Claude Managed Agents](https://claude.com/blog/how-abc-legal-turned-every-employee-into-a-builder-with-claude-managed-agents) | 2026-08-17 | 1 skill + 4 agent + 1 guide |
| [Maximizing the value of your Claude Code sessions](https://claude.com/blog/maximizing-the-value-of-your-claude-code-sessions) | 2026-08-14 | 1 skill + 1 guide |
| [Self-service data analytics in Slack: how Anthropic deploys Claude Tag for ad hoc questions](https://claude.com/blog/self-service-data-analytics-in-slack-how-anthropic-deploys-claude-tag-for-ad-hoc-questions) | 2026-08-13 | 1 skill + 1 guide |
| [Securing the frontier: How JetBrains evaluates and deploys Claude Fable 5](https://claude.com/blog/how-jetbrains-evaluates-and-deploys-claude-fable-5) | 2026-08-13 | 1 skill + 1 guide |
| [Claude Tag now reads even more of the room](https://claude.com/blog/claude-tag-now-reads-even-more-of-the-room) | 2026-08-13 | 1 skill |
| [The Claude in Chrome side panel is now Claude Cowork](https://claude.com/blog/cowork-chrome-side-panel) | 2026-08-12 | 1 skill + 1 guide |
| [Compliance API coverage extends to Claude Cowork and Claude Code](https://claude.com/blog/compliance-api-cowork-and-claude-code) | 2026-08-11 | 1 skill |
| [How Anthropic's business development team uses Claude to run inbound and outbound at scale](https://claude.com/blog/how-anthropics-business-development-team-uses-claude-to-run-inbound-and-outbound-at-scale) | 2026-08-07 | 4 skill + 1 guide |
| [Running auto mode in production](https://claude.com/blog/auto-mode-in-production) | 2026-08-07 | 1 skill + 1 guide |
| [Auto mode is now the default in Claude Code for Pro, Max, and Team plans](https://claude.com/blog/auto-mode-default-in-claude-code) | 2026-08-07 | 1 skill + 1 guide |
| [Run Claude Code sessions on your own compute](https://claude.com/blog/run-claude-code-sessions-on-your-own-compute) | 2026-08-06 | 1 skill + 1 guide |
| [Millennium and Anthropic are building a digital risk analyst with Claude](https://claude.com/blog/millennium-and-anthropic-are-building-a-digital-risk-analyst-with-claude) | 2026-08-06 | 1 skill |
| [Inference hooks: inline data loss prevention for Claude Enterprise](https://claude.com/blog/claude-enterprise-inference-hooks) | 2026-08-05 | 1 skill + 1 guide |
| [A Guide to Cost Visibility and Control in Claude](https://claude.com/blog/a-guide-to-cost-visibility-and-control-in-claude) | 2026-08-04 | 1 skill + 1 guide |
| [Bringing MCP 2026-07-28 to Claude](https://claude.com/blog/bringing-mcp-2026-07-28-to-claude) | 2026-07-28 | 1 skill + 1 guide |
| [The new rules of context engineering for Claude 5 generation models](https://claude.com/blog/the-new-rules-of-context-engineering-for-claude-5-generation-models) | 2026-07-24 | 1 skill + 1 guide |
| [How the product designer who built Claude Design uses it to explore ideas before building them](https://claude.com/blog/how-the-product-designer-who-built-claude-design-uses-it-to-explore-ideas-before-building-them) | 2026-07-24 | 1 skill + 1 guide |
| [Claude models explained: choosing the best model for your use case](https://claude.com/blog/claude-models-explained-choosing-the-best-model-for-your-use-case) | 2026-07-24 | 1 skill + 2 agent + 1 guide |
| [Think through hard problems in voice mode](https://claude.com/blog/think-through-hard-problems-in-voice-mode) | 2026-07-23 | 1 skill + 1 guide |
| [Four role-based certifications for the people who put Claude to work for customers](https://claude.com/blog/four-role-based-claude-certifications) | 2026-07-23 | 2 skill + 1 guide |
| [How Outtake built a cyber investigator on Claude](https://claude.com/blog/how-outtake-built-a-cyber-investigator-on-claude) | 2026-07-22 | 1 skill + 2 agent + 1 guide |
| [Building verification loops in Claude Code with skills](https://claude.com/blog/building-verification-loops-in-claude-code-with-skills) | 2026-07-22 | 1 skill + 1 guide |
| [How Datadog built a "universal machine tool" for Claude Code](https://claude.com/blog/how-datadog-built-a-universal-machine-tool-for-claude-code) | 2026-07-21 | 1 skill + 1 guide |
| [How Anthropic secures its AI-native software development lifecycle](https://claude.com/blog/how-anthropic-secures-its-ai-native-software-development-lifecycle) | 2026-07-21 | 1 skill + 2 agent + 1 hook + 1 guide |
| [Working at the frontier: How Cursor knew Claude Fable 5 was ready for the hardest 1% of problems](https://claude.com/blog/working-at-the-frontier-cursor) | 2026-07-17 | 2 skill + 1 guide |
| [Zero risk isn't the job: a CISO's guide to agentic AI](https://claude.com/blog/ciso-guide-to-agentic-ai) | 2026-07-17 | 1 skill + 2 agent + 1 guide |
| [How Anthropic Runs Large-Scale Code Migrations with Claude Code](https://claude.com/blog/ai-code-migration) | 2026-07-16 | 1 skill + 5 agent + 1 guide |
| [Working at the frontier: How Cognition trusts Claude Fable 5 to work through the night](https://claude.com/blog/working-at-the-frontier-how-cognition-trusts-claude-fable-5-to-work-through-the-night) | 2026-07-10 | 2 skill + 1 guide |
| [How Anthropic's marketing operations team uses Claude Cowork to automate reporting and campaign builds](https://claude.com/blog/how-anthropics-marketing-operations-team-uses-claude-cowork-to-automate-reporting-and-campaign-builds) | 2026-07-08 | 4 skill + 2 agent + 1 guide |
| [How people are using Claude Cowork](https://claude.com/blog/how-people-are-using-claude-cowork) | 2026-07-07 | 1 skill + 1 guide |
| [Claude Cowork is coming to mobile and web](https://claude.com/blog/cowork-web-mobile) | 2026-07-07 | 1 skill + 1 guide |
| [Choosing a Claude model and effort level in Claude Code](https://claude.com/blog/claude-model-and-effort-level-in-claude-code) | 2026-07-07 | 1 skill + 1 guide |
| [Bringing Claude Code and Claude Cowork to government](https://claude.com/blog/bringing-claude-code-and-claude-cowork-to-government) | 2026-07-07 | 1 skill + 1 guide |
| [A Field Guide to Claude Fable 5: Finding Your Unknowns](https://claude.com/blog/a-field-guide-to-claude-fable-finding-your-unknowns) | 2026-07-06 | 1 skill + 1 guide |
| [Giving admins more visibility and control over Claude spend](https://claude.com/blog/giving-admins-more-visibility-and-control-over-claude-usage-and-spend) | 2026-07-02 | 1 skill + 1 guide |
| [Getting started with loops](https://claude.com/blog/getting-started-with-loops) | 2026-06-30 | 2 skill |
| [Introducing the Claude apps gateway for Amazon Bedrock and Google Cloud](https://claude.com/blog/introducing-the-claude-apps-gateway) | 2026-06-29 | 1 skill + 1 guide |
| [Claude in Microsoft Foundry is now generally available](https://claude.com/blog/claude-in-microsoft-foundry) | 2026-06-29 | 1 skill |
| [Lessons from Anthropic on building effective human-agent teams](https://claude.com/blog/building-effective-human-agent-teams) | 2026-06-24 | 1 skill + 1 guide |
| [Agent identity: a new access model for autonomous, team-wide AI \| Claude](https://claude.com/blog/agent-identity-access-model) | 2026-06-24 | 1 skill |
| [The full Claude Desktop experience on AWS, Google Cloud, and Microsoft Foundry](https://claude.com/blog/the-full-claude-desktop-experience-on-aws-google-cloud-and-microsoft-foundry) | 2026-06-22 | 1 skill |
| [Steering Claude Code: skills, hooks, subagents and more](https://claude.com/blog/steering-claude-code-skills-hooks-rules-subagents-and-more) | 2026-06-18 | 1 skill + 1 agent + 1 guide |
| [Centrally manage authorization for MCP connectors](https://claude.com/blog/enterprise-managed-auth) | 2026-06-18 | 1 skill + 1 guide |
| [Claude Code now supports artifacts](https://claude.com/blog/artifacts-in-claude-code) | 2026-06-18 | 1 skill + 1 guide |
| [Secure access to the Claude Platform with Workload Identity Federation](https://claude.com/blog/workload-identity-federation) | 2026-06-17 | 1 skill |
| [Meet the winners of our Claude Opus 4.8 Build Day hackathon](https://claude.com/blog/meet-the-winners-of-our-claude-opus-4-8-build-day-hackathon) | 2026-06-17 | 1 skill + 1 guide |
| [Claude Design now stays on brand for daily work](https://claude.com/blog/claude-design-stays-on-brand-for-daily-work) | 2026-06-17 | 1 skill + 1 guide |
| [Meet the winners of Built with Opus 4.7 Claude Code hackathon](https://claude.com/blog/meet-the-winners-of-built-with-opus-4-7-claude-code-hackathon) | 2026-06-15 | 1 skill + 1 guide |
| [The evolution of agentic surfaces: building with Claude Managed Agents](https://claude.com/blog/building-with-claude-managed-agents) | 2026-06-10 | 1 skill + 1 guide |
| [New in Claude Managed Agents: run agents on a schedule and store environment variables in vaults](https://claude.com/blog/whats-new-in-claude-managed-agents) | 2026-06-09 | 1 skill |
| [Observability for developers building connectors](https://claude.com/blog/observability-for-developers-building-connectors) | 2026-06-08 | 1 skill + 1 guide |
| [Building intelligent apps for Apple platforms with Claude in the Foundation Models framework](https://claude.com/blog/claude-for-foundation-models) | 2026-06-08 | 1 skill + 1 guide + 1 plugin |
| [The Claude Cowork product guide](https://claude.com/blog/the-claude-cowork-product-guide) | 2026-06-05 | 1 skill + 1 guide |
| [How one Anthropic seller rebuilt his team's workflows with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-gtm-engineering) | 2026-06-05 | 1 skill + 1 guide + 1 style |
| [Running an AI-native engineering org](https://claude.com/blog/running-an-ai-native-engineering-org) | 2026-06-03 | 1 skill |
| [Lessons from building Claude Code: How we use skills](https://claude.com/blog/lessons-from-building-claude-code-how-we-use-skills) | 2026-06-03 | 1 skill |
| [How Anthropic enables self-service data analytics with Claude](https://claude.com/blog/how-anthropic-enables-self-service-data-analytics-with-claude) | 2026-06-03 | 1 skill |
| [Best practices for getting started with Claude Cowork](https://claude.com/blog/best-practices-for-getting-started-with-claude-cowork) | 2026-06-03 | 1 skill + 1 guide |
| [A harness for every task: dynamic workflows in Claude Code](https://claude.com/blog/a-harness-for-every-task-dynamic-workflows-in-claude-code) | 2026-06-02 | 1 skill + 1 guide |
| [Introducing dynamic workflows in Claude Code](https://claude.com/blog/introducing-dynamic-workflows-in-claude-code) | 2026-05-28 | 1 skill + 1 guide |
| [How CodeRabbit Used Claude to Build an Agent Orchestration System](https://claude.com/blog/how-coderabbit-used-claude-to-build-an-agent-orchestration-system) | 2026-05-27 | 1 skill |
| [Code w/ Claude London 2026: Rethinking how we build](https://claude.com/blog/code-w-claude-london-2026-rethinking-how-we-build) | 2026-05-26 | 1 skill + 1 guide |
| [How Anthropic's finance team uses Claude to shape the narrative behind the numbers](https://claude.com/blog/how-anthropics-finance-team-uses-claude-to-shape-the-narrative-behind-the-numbers) | 2026-05-22 | 1 skill + 1 guide |
| [How our partners are putting Opus to work for cybersecurity](https://claude.com/blog/how-our-partners-are-putting-opus-to-work-for-cybersecurity) | 2026-05-21 | 1 skill |
| [Claude now works with more security and compliance tools](https://claude.com/blog/compliance-api-security-partners) | 2026-05-21 | 1 skill |
| [Using Claude Code: The unreasonable effectiveness of HTML](https://claude.com/blog/using-claude-code-the-unreasonable-effectiveness-of-html) | 2026-05-20 | 1 skill + 1 guide |
| [How an Anthropic sales leader uses Claude Cowork to run a 4,000-account book](https://claude.com/blog/how-an-anthropic-sales-leader-uses-claude-cowork-to-run-a-4-000-account-book) | 2026-05-20 | 1 skill + 1 guide |
| [New in Claude Managed Agents: self-hosted sandboxes and MCP tunnels](https://claude.com/blog/claude-managed-agents-updates) | 2026-05-19 | 1 skill + 1 guide |
| [Deploying Claude across the legal industry](https://claude.com/blog/deploying-claude-across-the-legal-industry) | 2026-05-15 | 1 skill + 1 guide |
| [The founder's playbook: Building an AI-native startup](https://claude.com/blog/the-founders-playbook) | 2026-05-14 | 1 skill + 1 guide |
| [How Claude Code works in large codebases: Best practices and where to start](https://claude.com/blog/how-claude-code-works-in-large-codebases-best-practices-and-where-to-start) | 2026-05-14 | 1 skill + 1 guide |
| [Best practices for computer and browser use with Claude](https://claude.com/blog/best-practices-for-computer-and-browser-use-with-claude) | 2026-05-13 | 1 skill + 1 guide |
| [Code w/ Claude SF 2026: Building on the AI exponential](https://claude.com/blog/code-w-claude-sf-2026-sf) | 2026-05-12 | 1 skill |
| [Claude for the legal industry](https://claude.com/blog/claude-for-the-legal-industry) | 2026-05-12 | 1 skill + 1 guide + 1 style + 1 plugin |
| [How Anthropic's cybersecurity team built a threat detection platform with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-cybersecurity) | 2026-05-11 | 1 skill |
| [Agent view in Claude Code](https://claude.com/blog/agent-view-in-claude-code) | 2026-05-11 | 1 skill + 1 guide |
| [Collaborate with Claude across Excel, PowerPoint, Word and Outlook](https://claude.com/blog/collaborate-with-claude-across-excel-powerpoint-word-and-outlook) | 2026-05-07 | 1 skill + 1 guide |
| [Claude Platform on AWS](https://claude.com/blog/claude-platform-on-aws) | 2026-05-07 | 1 skill + 1 guide |
| [New in Claude Managed Agents: dreaming, outcomes, and multiagent orchestration](https://claude.com/blog/new-in-claude-managed-agents) | 2026-05-06 | 1 skill + 1 guide |
| [Deploying Claude across financial services](https://claude.com/blog/deploying-claude-across-financial-services) | 2026-05-05 | 1 skill |
| [How a non-technical project manager built and shipped a stress management app with Claude Code in six weeks](https://claude.com/blog/how-a-non-technical-project-manager-built-and-shipped-a-stress-management-app-with-claude-code-in-six-weeks) | 2026-05-01 | 1 skill + 4 agent + 1 guide |
| [Lessons from building Claude Code: Prompt caching is everything](https://claude.com/blog/lessons-from-building-claude-code-prompt-caching-is-everything) | 2026-04-30 | 1 skill |
| [How Kepler built verifiable AI for financial services with Claude](https://claude.com/blog/how-kepler-built-verifiable-ai-for-financial-services-with-claude) | 2026-04-30 | 1 skill + 1 guide |
| [Claude Security is now in public beta](https://claude.com/blog/claude-security-public-beta) | 2026-04-30 | 1 skill |
| [Building AI agents for the enterprise](https://claude.com/blog/building-ai-agents-for-the-enterprise) | 2026-04-30 | 1 skill + 1 guide |
| [Product development in the agentic era](https://claude.com/blog/product-development-in-the-agentic-era) | 2026-04-29 | 1 skill |
| [New guide: Deploying Claude across the enterprise with Claude Cowork](https://claude.com/blog/new-guide-deploying-claude-across-the-enterprise-with-claude-cowork) | 2026-04-29 | 1 skill |
| [Claude API skill now in CodeRabbit, JetBrains, Resolve AI, and Warp](https://claude.com/blog/claude-api-skill) | 2026-04-29 | 1 skill |
| [Onboarding Claude Code like a new developer: Lessons from 17 years of development](https://claude.com/blog/onboarding-claude-code-like-a-new-developer-lessons-from-17-years-of-development) | 2026-04-28 | 1 skill |
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
| [Product management on the AI exponential](https://claude.com/blog/product-management-on-the-ai-exponential) | 2026-03-19 | 1 skill |
| [Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo) | 2026-03-18 | 1 skill + 1 guide |
| [1M context is now generally available for Opus 4.6 and Sonnet 4.6](https://claude.com/blog/1m-context-ga) | 2026-03-13 | 1 skill |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates) | 2026-03-11 | 1 skill + 1 guide |
| [Bringing Code Review to Claude Code](https://claude.com/blog/code-review) | 2026-03-09 | 1 skill |
| [Common workflow patterns for AI agents](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them) | 2026-03-05 | 1 skill + 1 guide |
| [Improving skill-creator: Test, measure, and refine Agent Skills](https://claude.com/blog/improving-skill-creator-test-measure-and-refine-agent-skills) | 2026-03-03 | 1 skill |
| [Cowork and plugins for finance](https://claude.com/blog/cowork-plugins-finance) | 2026-02-24 | 1 guide |
| [Cowork and plugins for teams across the enterprise](https://claude.com/blog/cowork-plugins-across-enterprise) | 2026-02-24 | 1 guide |
| [How AI helps break the cost barrier to COBOL modernization](https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization) | 2026-02-23 | 1 skill |
| [Preview, review, and merge with Claude Code](https://claude.com/blog/preview-review-and-merge-with-claude-code) | 2026-02-20 | 1 skill |
| [Increase web search accuracy and efficiency with dynamic filtering](https://claude.com/blog/improved-web-search-with-dynamic-filtering) | 2026-02-17 | 1 skill |
| [Claude Enterprise, now available self-serve](https://claude.com/blog/self-serve-enterprise) | 2026-02-12 | 1 skill |
| [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early) | 2026-02-09 | 1 skill |
| [Advancing finance with Claude Opus 4.6](https://claude.com/blog/opus-4-6-finance) | 2026-02-05 | 1 skill + 1 guide |
| [Customize Cowork with plugins - Claude.ai](https://claude.com/blog/cowork-plugins) | 2026-01-30 | 1 guide |
| [Measure Claude Code's impact with contribution metrics](https://claude.com/blog/contribution-metrics) | 2026-01-29 | 1 skill |
| [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) | 2026-01-29 | 1 skill + 1 guide |
| [How leading retailers are turning AI pilots into enterprise-wide transformation](https://claude.com/blog/how-leading-retailers-are-turning-ai-pilots-into-enterprise-wide-transformation) | 2026-01-28 | 1 skill + 1 guide |
| [Updates to Claude Team](https://claude.com/blog/claude-team-updates) | 2026-01-28 | 1 skill |
| [Interactive connectors and MCP Apps](https://claude.com/blog/interactive-tools-in-claude) | 2026-01-26 | 1 skill + 1 guide |
| [How Anthropic's Growth Marketing team cut ad creation time from 30 minutes to 30 seconds with Claude Code](https://claude.com/blog/how-anthropic-uses-claude-marketing) | 2026-01-26 | 1 skill |
| [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) | 2026-01-23 | 1 skill |
| [Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work) | 2026-01-22 | 1 skill + 1 guide |
| [Eight trends defining how software gets built in 2026](https://claude.com/blog/eight-trends-defining-how-software-gets-built-in-2026) | 2026-01-21 | 1 skill |
| [Extending Claude's capabilities with skills and MCP servers](https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers) | 2025-12-19 | 1 skill |
| [Skills for organizations, partners, the ecosystem](https://claude.com/blog/organization-skills-and-directory) | 2025-12-18 | 1 skill + 1 guide |
| [Making Claude a better electrical engineer](https://claude.com/blog/making-claude-a-better-electrical-engineer) | 2025-12-12 | 1 skill |
| [Claude Code power user customization: How to configure hooks](https://claude.com/blog/how-to-configure-hooks) | 2025-12-11 | 1 skill + 9 hook |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [How Anthropic's legal team cut review times from days to hours with Claude](https://claude.com/blog/how-anthropic-uses-claude-legal) | 2025-12-08 | 1 skill |
| [Claude Code and Slack](https://claude.com/blog/claude-code-and-slack) | 2025-12-08 | 1 skill |
| [What are the key benefits of transitioning to agentic coding for software development?](https://claude.com/blog/key-benefits-transitioning-agentic-coding) | 2025-12-01 | 1 skill + 1 guide |
| [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [What's new in Claude: Turning Claude into your thinking partner](https://claude.com/blog/your-thinking-partner) | 2025-11-20 | 1 skill |
| [How to create Skills for Claude: steps and examples](https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples) | 2025-11-19 | 1 skill |
| [How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code) | 2025-11-17 | 1 skill + 1 guide |
| [Structured outputs on the Claude Developer Platform](https://claude.com/blog/structured-outputs-on-the-claude-developer-platform) | 2025-11-14 | 1 skill |
| [How Skills compares to prompts, Projects, MCP, and subagents](https://claude.com/blog/skills-explained) | 2025-11-13 | 1 skill + 3 agent + 4 guide |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for startups](https://claude.com/blog/building-ai-agents-for-startups) | 2025-11-03 | 1 skill |
| [What is Model Context Protocol? Connect AI to your world](https://claude.com/blog/what-is-model-context-protocol) | 2025-10-31 | 1 skill + 1 guide |
| [Introduction to agentic coding](https://claude.com/blog/introduction-to-agentic-coding) | 2025-10-30 | 1 skill + 1 guide |
| [How Brex improves code quality and productivity with Claude Code](https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code) | 2025-10-30 | 1 skill |
| [Building AI agents in healthcare and life sciences](https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences) | 2025-10-30 | 1 skill + 1 guide |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agent + 1 guide |
| [Fix software bugs faster with Claude](https://claude.com/blog/fix-software-bugs-faster-with-claude) | 2025-10-28 | 1 skill |
| [How to integrate APIs seamlessly](https://claude.com/blog/integrate-apis-seamlessly) | 2025-10-27 | 1 skill + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Introducing Agent Skills](https://claude.com/blog/skills) | 2025-10-16 | 1 skill |
| [Claude and your productivity platforms](https://claude.com/blog/productivity-platforms) | 2025-10-16 | 1 skill + 1 guide |
| [How to scale agentic coding across your engineering organization](https://claude.com/blog/scaling-agentic-coding) | 2025-10-15 | 1 skill |
| [Build responsive web layouts](https://claude.com/blog/build-responsive-web-layouts) | 2025-10-10 | 1 skill |
| [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins) | 2025-10-09 | 1 skill + 1 guide + 1 plugin |
| [Beyond permission prompts: making Claude Code more secure and autonomous](https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous) | 2025-10-08 | 1 skill |
| [Optimize code performance quickly](https://claude.com/blog/optimize-code-performance-quickly) | 2025-10-06 | 1 skill |
| [How enterprises are driving AI transformation with Claude](https://claude.com/blog/driving-ai-transformation-with-claude) | 2025-10-01 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |
| [Managing context on the Claude Developer Platform](https://claude.com/blog/context-management) | 2025-09-29 | 1 skill |
| [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | 2025-09-29 | 1 skill |
| [Claude is now available in Microsoft 365 Copilot](https://claude.com/blog/claude-now-available-in-microsoft-365-copilot) | 2025-09-24 | 1 skill + 1 guide |
| [Bringing memory to teams](https://claude.com/blog/memory) | 2025-09-11 | 1 skill |
| [Claude can now create and edit files](https://claude.com/blog/create-files) | 2025-09-09 | 1 skill |
| [Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) | 2025-08-25 | 1 skill + 1 guide |
| [Claude Code and new admin controls for business plans](https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans) | 2025-08-20 | 1 skill |
| [Prompt caching with Claude](https://claude.com/blog/prompt-caching) | 2025-08-14 | 1 skill |
| [Claude Sonnet 4 now supports 1M tokens of context](https://claude.com/blog/1m-context) | 2025-08-12 | 1 skill |
| [Automate security reviews with Claude Code](https://claude.com/blog/automate-security-reviews-with-claude-code) | 2025-08-06 | 1 skill |
| [Build and share AI-powered apps with Claude](https://claude.com/blog/claude-powered-artifacts) | 2025-07-25 | 1 skill |
| [How Anthropic teams use Claude Code](https://claude.com/blog/how-anthropic-teams-use-claude-code) | 2025-07-24 | 1 skill |
| [Discover tools that work with Claude](https://claude.com/blog/connectors-directory) | 2025-07-14 | 1 skill |
| [Turn ideas into interactive AI-powered apps](https://claude.com/blog/build-artifacts) | 2025-06-25 | 1 skill |
| [Introducing Citations on the Anthropic API](https://claude.com/blog/introducing-citations-api) | 2025-06-23 | 1 skill + 1 guide |
| [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) | 2025-06-18 | 1 skill + 1 guide |
| [Mcp Connector](https://claude.com/blog/agent-capabilities-api) | 2025-05-22 | 1 skill |
| [Introducing web search on the Anthropic API](https://claude.com/blog/web-search-api) | 2025-05-07 | 1 skill + 1 guide |
| [Claude can now connect to your world](https://claude.com/blog/integrations) | 2025-05-01 | 1 skill + 1 guide |
| [Claude takes research to new places](https://claude.com/blog/research) | 2025-04-15 | 1 skill |
| [Introducing the Max Plan](https://claude.com/blog/max-plan) | 2025-04-09 | 1 skill |
| [Claude on Google Cloud’s Vertex AI: FedRAMP High and IL2 Authorized](https://claude.com/blog/claude-on-google-cloud-fedramp-high) | 2025-04-02 | 1 skill |
| [Claude can now search the web](https://claude.com/blog/web-search) | 2025-03-20 | 1 skill |
| [Token-saving updates on the Anthropic API](https://claude.com/blog/token-saving-updates) | 2025-03-13 | 1 skill |
| [Get to production faster with the upgraded Anthropic Console](https://claude.com/blog/upgraded-anthropic-console) | 2025-03-06 | 1 skill |
| [Claude 3.5 Haiku on AWS Trainium2 and model distillation in Amazon Bedrock](https://claude.com/blog/trainium2-and-distillation) | 2024-12-03 | 1 skill |
| [Introducing the analysis tool in Claude.ai](https://claude.com/blog/analysis-tool) | 2024-10-24 | 1 skill |
| [Improve your prompts in the developer console](https://claude.com/blog/prompt-improver) | 2024-10-14 | 1 skill |
| [Introducing the Message Batches API](https://claude.com/blog/message-batches-api) | 2024-10-08 | 1 skill |
| [Workspaces in the Anthropic API Console](https://claude.com/blog/workspaces) | 2024-09-10 | 1 skill + 1 guide |
| [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) | 2024-09-10 | 1 skill + 1 guide |
| [Artifacts are now generally available](https://claude.com/blog/artifacts) | 2024-08-27 | 1 skill |
| [Claude Android app](https://claude.com/blog/android-app) | 2024-07-16 | 1 skill |
| [Fine-tune Claude 3 Haiku in Amazon Bedrock](https://claude.com/blog/fine-tune-claude-3-haiku) | 2024-07-10 | 1 skill |
| [Evaluate prompts in the developer console](https://claude.com/blog/evaluate-prompts) | 2024-07-09 | 1 skill |
| [Claude can now use tools](https://claude.com/blog/tool-use-ga) | 2024-05-30 | 1 skill |
| [Generate better prompts in the developer Console](https://claude.com/blog/prompt-generator) | 2024-05-20 | 1 skill |
| [Introducing the Claude Team plan and iOS app](https://claude.com/blog/team-plan-and-ios) | 2024-05-01 | 1 guide |
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
