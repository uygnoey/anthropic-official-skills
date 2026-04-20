[English](./README.md) · [한국어](./README.ko.md) · [Español](./README.es.md) · [日本語](./README.ja.md)

# skills-from-claude-blog

> [claude.com/blog](https://www.claude.com/blog) の記事を、Claude Code 公式拡張スペックに沿って整理した成果物集。
> Anthropic とは無関係の第三者まとめプロジェクトです。

Claude 公式ブログの記事を、**記事の性格に合わせた Claude Code 公式スペック**へ変換してまとめたリポジトリです。4 時間ごとのバッチで新着記事と未処理記事を取り込みます。

## 構成（記事 1 本ごと）

ブログ記事 1 本 = `posts/<blog-slug>/` フォルダ 1 つ。サブフォルダは記事の性格に応じて条件付きで追加されます。

```
posts/<blog-slug>/
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
| [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) | 2026-04-10 | 2 skills + 3 agents + 1 guide |
| [Claude Managed Agents: get to production 10x faster](https://claude.com/blog/claude-managed-agents) | 2026-04-08 | 1 guide |
| [Subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) | 2026-04-07 | 2 skills + 1 agent + 1 hook |
| [Harnessing Claude's Intelligence \| 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence) | 2026-04-02 | 1 skill + 1 guide |
| [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) | 2026-03-12 | 1 skill |
| [How enterprises are building AI agents in 2026](https://claude.com/blog/how-enterprises-are-building-ai-agents-in-2026) | 2025-12-09 | 1 guide |
| [Using CLAUDE.md files](https://claude.com/blog/using-claude-md-files) | 2025-11-25 | 1 skill |
| [Improving frontend design through Skills](https://claude.com/blog/improving-frontend-design-through-skills) | 2025-11-12 | 1 skill + 1 guide |
| [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering) | 2025-11-10 | 1 skill |
| [Building AI agents for financial services](https://claude.com/blog/building-ai-agents-in-financial-services) | 2025-10-30 | 1 skill + 3 agents + 1 guide |
| [Claude Code on the web](https://claude.com/blog/claude-code-on-the-web) | 2025-10-20 | 1 skill |

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

## ファイル

```
.
├── posts/                       # 記事 1 本ごとに 1 フォルダ
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
