[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# CLAUDE.mdでClaude Codeをカスタマイズする

## この記事について
Claude Codeにプロジェクト構造・コーディングスタイル・よく使うコマンドをセッションのたびに説明し直す手間をなくします。プロジェクトルートに`CLAUDE.md`を置くだけで、**すべての会話の開始時にその内容がClaudeのシステムプロンプトとして自動的に読み込まれます**。

## どんなときに役立つか
- チームが共有リポジトリで一貫したClaudeの動作を望むとき（ファイルをコミットする）
- 複数のサブプロジェクトがルールを共有するモノレポ（親ディレクトリに配置）
- 個人のグローバルなデフォルト設定（`~/CLAUDE.md`）
- 毎セッション同じ指示を繰り返している自分に気づいたとき

## 基本原則
1. **`/init`から始める** — Claudeにコードベースを分析させてファイルの草案を作成させる。
2. **3つの軸で整理する**: (1) プロジェクトマップ、(2) ツール連携、(3) 標準ワークフロー。
3. **実際の問題だけを記録する。** 理論的な懸念事項は省く。
4. **秘密情報は含めない。** APIキー、認証情報、脆弱性の詳細は絶対に記載しないこと。

## 推奨セクション
| セクション | 目的 | 内容 |
|---|---|---|
| Project map | プロジェクト概要 | 一行説明、ディレクトリツリー、主要な依存関係、アーキテクチャパターン |
| Tool connections | カスタムコマンド / MCP | カスタムコマンドの呼び出し方、MCPサーバーのルール |
| Workflows | 標準手順 | 作業前の確認事項、explore→plan→code→commit、TDDルール |

## 例: FastAPIプロジェクト

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

## 例: MCPツールのルール（Slack）

```markdown
## Slack MCP usage

- Posts to `#dev-notifications` channel only
- Use for deployment notifications and build failures
- Do not use for individual PR updates
- Rate limited to 10 messages per hour
```

## 作成チェックリスト
- [ ] `/init`から開始したか
- [ ] ディレクトリマップが実際の構造と一致しているか
- [ ] よく使うbashコマンドが記載されているか
- [ ] APIキー・認証情報が含まれていないか
- [ ] チームのワークフロー（テスト、PR）が反映されているか
- [ ] 実際に繰り返し発生する問題を背景に持つルールのみ記載されているか

## メンテナンスのヒント
- チャット中に繰り返しの指示が必要になったら、バックティック3つのキーを押してCLAUDE.mdに直接追記できる。
- 繰り返し行う作業は`.claude/commands/`配下にカスタムスラッシュコマンド（MDファイル、`$ARGUMENTS` / `$1`を使用）として登録する。
- `/clear`でコンテキストをリセットし、独立したタスクはサブエージェントに委任する。
- 長大なガイダンスは別の`.md`ファイルに分割し、CLAUDE.mdから参照する。

## 出典
〜をもとに整理しました: [Using CLAUDE.MD files: Customizing Claude Code for your codebase](https://claude.com/blog/using-claude-md-files) （公開: 2025-11-25）。権威ある情報は必ず原文を参照してください。
