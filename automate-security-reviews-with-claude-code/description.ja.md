[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude Code におけるセキュリティレビューの自動化を紹介します。ターミナルから即時に実行できる `/security-review` コマンドと、Pull Request を自動レビューする GitHub Actions 連携が含まれます。

## どんなときに役立つか
- コミット前に、よくある脆弱性を早期に検出したいとき
- PR ごとに自動で問題を指摘し、修正提案を残す CI ワークフローを組み込みたいとき

## 主なポイント
- `/security-review` コマンドは、SQL インジェクション、クロスサイトスクリプティング（XSS）、認証/認可の不備、安全でないデータ取り扱い、依存関係の脆弱性などをチェックできます。
- GitHub Action は PR の差分にコメントでき、カスタムルールで誤検知を減らすよう設定できます。
- 問題を特定した後、Claude Code に修正実装を依頼できます。

## 同梱リソース
- Skill: `skills/security-review-automation/SKILL.md`

## 出典
- https://claude.com/blog/automate-security-reviews-with-claude-code
