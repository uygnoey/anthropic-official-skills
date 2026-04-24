[English](./README.md) · [한국어](./README.ko.md) · [Español](./README.es.md) · **日本語**

# skills-from-claude-blog

> [claude.com/blog](https://www.claude.com/blog) の記事を、Claude Code 公式拡張スペックに沿って整理した成果物集。
> Anthropic とは無関係の第三者まとめプロジェクトです。

Claude 公式ブログの記事を、**記事の性格に合わせた Claude Code 公式スペック**へ変換してまとめたリポジトリです。4 時間ごとのバッチで新着記事と未処理記事を取り込みます。

## 構成（記事 1 本ごと）

ブログ記事 1 本 = リポジトリルート直下の `<YYYY.MM.DD>_<blog-slug>/` フォルダ 1 つ。日付のプレフィックスは記事の `published_date` を `YYYY.MM.DD` に変換したもの、`<blog-slug>` は URL の最後のセグメントです。GitHub 上で新しいものから古いものへ自然に並びます。サブフォルダは記事の性格に応じて条件付きで追加されます。

```
<YYYY.MM.DD>_<blog-slug>/
├── description.en.md               # 英語の解説（常時）
├── description.ko.md               # 韓国語の解説（常時）
├── description.es.md               # スペイン語の解説（常時）
├── description.ja.md               # 日本語の解説（常時）
├── source.json                     # 原文メタデータ（常時）
│
├── skills/<name>/SKILL.md          # A. Agent Skills スペック
├── agents/<name>.md                # B. Claude Code Subagent スペック
├── guides/<name>.{en,ko,es,ja}.md  # C. 自由形式の多言語ガイド
├── hooks/<name>.json +.md          # D. Claude Code Hooks JSON + 解説
├── output-styles/<name>.md         # E. Output Style
└── plugin/                         # G. Plugin バンドル（まれ）
    ├── .claude-plugin/plugin.json
    └── skills|agents|hooks|output-styles/...
```

### 公式ドキュメント
- [Agent Skills](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview) — `SKILL.md`
- [Claude Code Subagents](https://code.claude.com/docs/en/sub-agents) — `agents/<name>.md`
- [Claude Code Hooks](https://code.claude.com/docs/en/hooks) — `hooks/<name>.json`
- [Output Styles](https://code.claude.com/docs/en/output-styles) — `output-styles/<name>.md`
- [Plugins](https://code.claude.com/docs/en/plugins) — `plugin/` バンドル

### スペック選定マトリクス

| 判定 | 判断のトリガー | 成果物 |
|---|---|---|
| **A. Skill** | 読者が再利用できる **パターン／原則／フレームワーク／how-to** があるか？ | `skills/<name>/SKILL.md` |
| **B. Subagent** | 記事内に **名前付きエージェントの役割が 2 つ以上** 明記されているか？ | それぞれ `agents/<name>.md` |
| **C. Guide** | 記事が **デプロイ／アーキテクチャ／方法論／調査** 寄りか？ | `guides/<name>.{en,ko,es,ja}.md` |
| **D. Hook** | **PreToolUse／PostToolUse／Stop／SessionStart** など lifecycle イベントの自動化を扱っているか？ | `hooks/<name>.json` + 解説 `.md` |
| **E. Output Style** | **system prompt の トーン／役割／フォーマットを丸ごと変更** する話か（一言のコツではない） | `output-styles/<name>.md` |
| **G. Plugin** | **複数の成果物をひとつのバンドルとして配布** する話が中心か？ | `plugin/` バンドル全体 |

- **F. Slash Command は作りません。** 公式ドキュメントで `.claude/commands/` が legacy 扱いになり、`.claude/skills/` が推奨されているため、slash command を扱う記事は **Skill へ変換** します。
- 複数の判定が同時に当てはまるのは正常。すべて生成します。
- 判定に迷ったら **A を含める** のがデフォルト。読者視点で Skill が最も実用的だからです。
- **原文にない役割・パターン・スクリプトは創作しません。** 不確かなら原文への参照でとどめます。

## そのまま使う

各成果物はそのまま自分のプロジェクトにコピーできます。

| 成果物 | 置き場所 |
|---|---|
| `skills/<name>/` | `.claude/skills/<name>/` または `~/.claude/skills/<name>/` |
| `agents/<name>.md` | `.claude/agents/<name>.md` または `~/.claude/agents/<name>.md` |
| `hooks/<name>.json` の内容 | `.claude/settings.json` の `hooks` フィールドへマージ |
| `output-styles/<name>.md` | `.claude/output-styles/<name>.md` |
| `plugin/` | `--plugin-dir ./plugin` で読み込み |

## インデックス

| ブログ記事 | 公開日 | 成果物 |
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
| [Code with Claude comes to San Francisco, London, and Tokyo](https://claude.com/blog/code-with-claude-san-francisco-london-tokyo) | 2026-03-18 | 1 skill + 1 guide |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [Advancing Claude for Excel and PowerPoint](https://claude.com/blog/claude-excel-powerpoint-updates) | 2026-03-11 | 1 skill + 1 guide |
| [Common workflow patterns for AI agents](https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them) | 2026-03-05 | 1 skill + 1 guide |
| [Behind the model launch: What customers discovered testing Claude Opus 4.6 early](https://claude.com/blog/behind-model-launch-what-customers-discovered-testing-claude-opus-4-6-early) | 2026-02-09 | 1 skill |
| [A complete guide to building skills for Claude](https://claude.com/blog/complete-guide-to-building-skills-for-claude) | 2026-01-29 | 1 skill + 1 guide |
| [Updates to Claude Team](https://claude.com/blog/claude-team-updates) | 2026-01-28 | 1 skill |
| [Building multi-agent systems: When and how to use them](https://claude.com/blog/building-multi-agent-systems-when-and-how-to-use-them) | 2026-01-23 | 1 skill |
| [Building agents with Skills: Equipping agents for specialized work](https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work) | 2026-01-22 | 1 skill + 1 guide |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [Claude Code and Slack](https://claude.com/blog/claude-code-and-slack) | 2025-12-08 | 1 skill |
| [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [How three YC startups built their companies with Claude Code](https://claude.com/blog/building-companies-with-claude-code) | 2025-11-17 | 1 skill + 1 guide |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for startups](https://claude.com/blog/building-ai-agents-for-startups) | 2025-11-03 | 1 skill |
| [Building AI agents in healthcare and life sciences](https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences) | 2025-10-30 | 1 skill + 1 guide |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agent + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |
| [Build responsive web layouts](https://claude.com/blog/build-responsive-web-layouts) | 2025-10-10 | 1 skill |
| [Customize Claude Code with plugins](https://claude.com/blog/claude-code-plugins) | 2025-10-09 | 1 skill + 1 guide + 1 plugin |
| [Beyond permission prompts: making Claude Code more secure and autonomous](https://claude.com/blog/beyond-permission-prompts-making-claude-code-more-secure-and-autonomous) | 2025-10-08 | 1 skill |
| [Claude and Slack](https://claude.com/blog/claude-and-slack) | 2025-10-01 | 1 skill + 1 guide |
| [Building agents with the Claude Agent SDK](https://claude.com/blog/building-agents-with-the-claude-agent-sdk) | 2025-09-29 | 1 skill |
| [Claude is now available in Microsoft 365 Copilot](https://claude.com/blog/claude-now-available-in-microsoft-365-copilot) | 2025-09-24 | 1 skill + 1 guide |
| [Piloting Claude in Chrome](https://claude.com/blog/claude-for-chrome) | 2025-08-25 | 1 skill + 1 guide |
| [Claude Code and new admin controls for business plans](https://claude.com/blog/claude-code-and-new-admin-controls-for-business-plans) | 2025-08-20 | 1 skill |
| [Claude Sonnet 4 now supports 1M tokens of context](https://claude.com/blog/1m-context) | 2025-08-12 | 1 skill |
| [Automate security reviews with Claude Code](https://claude.com/blog/automate-security-reviews-with-claude-code) | 2025-08-06 | 1 skill |
| [Build and share AI-powered apps with Claude](https://claude.com/blog/claude-powered-artifacts) | 2025-07-25 | 1 skill |
| [Turn ideas into interactive AI-powered apps](https://claude.com/blog/build-artifacts) | 2025-06-25 | 1 skill |
| [Remote MCP support in Claude Code](https://claude.com/blog/claude-code-remote-mcp) | 2025-06-18 | 1 skill + 1 guide |
| [Mcp Connector](https://claude.com/blog/agent-capabilities-api) | 2025-05-22 | 1 skill |
| [Claude on Google Cloud’s Vertex AI: FedRAMP High and IL2 Authorized](https://claude.com/blog/claude-on-google-cloud-fedramp-high) | 2025-04-02 | 1 skill |
| [Introducing the analysis tool in Claude.ai](https://claude.com/blog/analysis-tool) | 2024-10-24 | 1 skill |
| [Claude for Enterprise](https://claude.com/blog/claude-for-enterprise) | 2024-09-10 | 1 skill + 1 guide |
| [Claude Android app](https://claude.com/blog/android-app) | 2024-07-16 | 1 skill |
| [Long context prompting for Claude 2.1](https://claude.com/blog/claude-2-1-prompting) | 2023-12-06 | 1 skill |
| [Claude on Amazon Bedrock now available to every AWS customer](https://claude.com/blog/amazon-bedrock-general-availability) | 2023-09-28 | 1 skill |
| [Claude 2 on Amazon Bedrock](https://claude.com/blog/claude-2-amazon-bedrock) | 2023-08-23 | 1 skill |


すべてのガイドと解説は英語・韓国語・スペイン語・日本語で提供されています。各ファイル先頭の言語スイッチャから切り替えてください。

## バッチ運用

- Perplexity Computer の cron が 4 時間ごとに実行
- 記事一覧は `https://www.claude.com/sitemap.xml` と `/blog` インデックスから収集
- 優先順位: 前回実行以降の新着（新→旧）→ 未処理の既存記事（旧→新）→ 公開日不明
- 1 回の実行で最大 2 記事

## 執筆ガイドライン

1. `SKILL.md` と `agents/*.md` は公式スペックが英語ベースなので **英語** で書く。
2. Hook JSON は原文の挙動を忠実に反映。シェルコマンドはコメントで出典を明示。
3. Output Style は記事で指定されたトーン／役割／フォーマットをそのまま写す。迷ったら guide に落とす。
4. `name` フィールド（Skill／Subagent／Output Style／Plugin）は `^[a-z0-9-]+$`、64 文字以内、予約語 `claude`・`anthropic` 禁止。
5. `description` は三人称・1024 文字以内（Skill／Subagent）。
6. `guides/` は `.en.md` · `.ko.md` · `.es.md` · `.ja.md` の 4 言語で書き、先頭に言語スイッチャを置く。
7. 人向けの解説 (`description.*.md`) も同じ 4 言語で書き、先頭に言語スイッチャを置く。
8. **原文にない内容を創作しない。** 不確かなら「原文参照」で置く。
9. **アーティファクトはセルフコンテインド。** `SKILL.md`、`agents/*.md`、`hooks/*.md`、`output-styles/*.md` は自身のフォルダの外を参照してはいけません — `../` パス、他のアーティファクトへのリンク、`description.*.md` や `guides/` へ戻るリンクはすべて禁止。外部の素材が必要ならローカルのコンパニオンファイル（`references/`、`examples/`、`templates/`、`scripts/`、`prompts/`、`assets/` または兄弟の `.md`）にコピーしてください。

## ファイル

```
.
├── <YYYY.MM.DD>_<blog-slug>/           # 記事 1 本ごとに 1 フォルダ、日付プレフィックス付き
├── scripts/
│   ├── list_pending.py          # 未処理 URL の一覧
│   ├── mark_processed.py        # URL を処理済みに記録
│   ├── update_last_run.py       # バッチ時刻の押印
│   └── validate.py              # 全スペックの pre-commit 検証
└── state/
    └── processed.json           # 処理済み URL + last_run_at
```

## ライセンス

- 原文（Claude ブログ記事）の著作権は Anthropic に帰属。本リポジトリは学習・参照目的の要約と引用のみを含みます。
- リポジトリコード: MIT License。
