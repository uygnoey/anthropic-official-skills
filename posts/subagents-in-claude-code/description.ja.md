[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude Codeでサブエージェントを使う

## この記事について
サブエージェントとは、**独自のコンテキストウィンドウを持つ独立したClaudeインスタンス**です。このスキルは、調査作業・並行作業・フレッシュな視点でのレビューをサブエージェントに委任することで、メインセッションに集中できるようにするためのパターンをまとめています。

## どんなときに役立つか（強いシグナル）
- 調査量の多いタスク（10ファイル以上）
- 独立したサブタスクが3つ以上ある場合
- フレッシュな視点が必要なとき
- コミット前の検証
- パイプラインワークフロー（設計 → 実装 → テスト）

## 使わないほうがよい場合
- 順序依存・逐次処理の作業
- 同じファイルへの同時編集
- オーバーヘッドがメリットを上回る小規模タスク
- エージェント同士が連携する必要がある場合 — サブエージェントは互いに通信できないため、Agent Teamsを使うこと

## 4つの呼び出し方法

### A. 会話形式
```
Use subagents to explore this codebase in parallel:

1. Find all API endpoints and summarize their purposes
2. Identify the database schema and relationships
3. Map out the authentication flow

Return a summary of each, not the full file contents.
```

### B. カスタムサブエージェントファイル（`.claude/agents/`）
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
呼び出し方: `Have the security-reviewer look at the staged changes.`

### C. CLAUDE.mdのポリシーとして定義
```markdown
## Code review standards

When asked to review code, ALWAYS use a subagent with READ-ONLY access (Glob, Grep, Read only).
The review should ALWAYS check for:
- Security vulnerabilities
- Performance issues
- Adherence to project patterns in /docs/architecture.md
```

### D. スラッシュコマンドスキル
`.claude/skills/deep-review/SKILL.md` → `/deep-review`で実行。

## 4つの実践パターン
1. **Research-before-implement** — まず対象領域を調査してから実装する
2. **Parallel edits** — 独立したファイルを同時に修正する
3. **Fresh-eyes review** — 実装後、読み取り専用のサブエージェントで検証する
4. **Pipeline** — 設計・実装・テストをそれぞれ別のサブエージェントが担当する

## 運用上のヒント
- `Ctrl+B` — サブエージェントをバックグラウンドに送る。
- `/tasks` — 実行中のサブエージェントを確認する。
- 専門エージェントを増やしすぎないこと。候補が多すぎると自動委任の判断が不安定になる。
- サブエージェント同士は通信できない。連携が必要な場合はAgent Teamsを使うこと。

## 同梱リソース
- Skills (2): `skills/using-subagents/SKILL.md`, `skills/deep-review/SKILL.md`
- Agent (1): `agents/security-reviewer.md`
- Hook (1): `hooks/check-tests.json` / `hooks/check-tests.md`

## 出典
〜をもとに整理しました: [How and when to use subagents in Claude Code](https://claude.com/blog/subagents-in-claude-code) （公開: 2026-04-07）。権威ある情報は原文を参照してください。
