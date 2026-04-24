[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Code に routines を導入

## この記事について

2026年4月14日にリサーチプレビューとして登場した Claude Code **routines** のアナウンス。routine は、プロンプト・リポジトリ・コネクタをまとめて一度設定すれば、スケジュール、API 呼び出し、イベント駆動で実行できる Claude Code 自動化です。Claude Code のウェブインフラ上で動くので、ノートPCを開けておく必要はありません。

## どんなときに役立つか

- 開発サイクル自動化に Claude Code を使っているが、cron ジョブ・インフラ・追加の MCP ツールを自分で面倒見ているとき
- アラート、デプロイフック、社内ツールと Claude Code を HTTP 経由でつなげたいとき
- GitHub PR イベントを起点に Claude Code セッションを自動で立ち上げたいとき
- 夜間バックログトリアージや週次ドキュメントドリフトスキャンなどスケジュールタスクが必要なとき
- CI/CD 上でデプロイ検証・アラートトリアージ・フィードバック→PR ワークフローを Claude Code に任せたいとき

## 主なポイント

- リサーチプレビューで **3種類のトリガー**:スケジュール(時間/夜間/週次)、API(routine ごとにエンドポイントと認証トークン)、Webhook(まずは GitHub リポジトリイベント)
- スケジュール routines は CLI の `/schedule` フローを置き換えます。既存の `/schedule` タスクは routines になります。
- API routine はそれぞれ固有のエンドポイントとトークンを持ちます。メッセージを POST するとセッション URL が返ります。
- GitHub Webhook routine はフィルタに一致する PR ごとに Claude セッションを1つ開き、その PR のコメントや CI 失敗といった更新をセッションに流し続けます。
- 早期ユーザーに見られるパターン:バックログトリアージ、ドキュメントドリフト検出、デプロイ検証、アラートトリアージ、フィードバック解決、SDK 間ライブラリポート、チーム独自のコードレビュー
- 提供範囲:Pro、Max、Team、Enterprise(Claude Code on the web 有効化)。claude.ai/code または CLI の `/schedule` から作成。
- 1日の上限:Pro 最大5、Max 最大15、Team/Enterprise 最大25 routines。超過分は extra usage で実行可能。routines はインタラクティブセッションと同様にサブスクリプションの利用量を消費。

## 同梱リソース

- `skills/code-routines/SKILL.md` — トリガー種別の選び方と良い routine プロンプトの書き方
- `skills/code-routines/examples/prompts.md` — 記事中のスケジュール/API/GitHub Webhook プロンプト例
- `skills/code-routines/references/patterns.md` — 記事に出てくる早期利用パターン一覧
- `guides/routines-overview.{en,ko,es,ja}.md` — 4言語の解説ガイド

## 出典

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — 2026年4月14日公開。
