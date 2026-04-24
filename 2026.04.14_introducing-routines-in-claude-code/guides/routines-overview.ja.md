[English](./routines-overview.en.md) · [한국어](./routines-overview.ko.md) · [Español](./routines-overview.es.md) · **日本語**

# Claude Code の routines 概要

*Introducing routines in Claude Code*(2026年4月14日、リサーチプレビュー)を読み物として整理しました。

## routines とは

routine は、プロンプト・リポジトリ・コネクタをまとめて一度設定すれば、スケジュール、API 呼び出し、イベント駆動で実行できる Claude Code の自動化です。Claude Code のウェブインフラ上で動くため、ノートPCを開いておく必要はありません。

開発者はすでに Claude Code でソフトウェア開発サイクルを自動化していますが、これまでは cron ジョブ、インフラ、追加の MCP ツーリングを自分で面倒見る必要がありました。routines はリポジトリとコネクタが繋がった状態で出荷されるので、自動化を一度パッケージ化しておけば済みます。

## 3種類のトリガー

### スケジュール routines

プロンプトとカデンス(時間/夜間/週次)を渡せば、その予定で実行されます。公式の例:

> Every night at 2am: pull the top bug from Linear, attempt a fix, and open a draft PR.

CLI で `/schedule` を使っていたなら、そのタスクはすでにスケジュール routines です。

### API routines

各 routine は固有のエンドポイントと認証トークンを受け取ります。エンドポイントにメッセージを POST するとセッション URL が返ります。アラート、デプロイフック、社内ツール — HTTP リクエストを送れる場所ならどこからでも Claude Code を起動できます。例:

> Read the alert payload, find the owning service, and post a triage summary to #oncall with a proposed first step.

### Webhook routines(GitHub から開始)

GitHub リポジトリイベントに対して routine を自動起動できます。フィルタに一致する PR ごとに Claude が新しいセッションを作成し、routine を実行します。例:

> Please flag PRs that touch the /auth-provider module. Any changes to this module need to be summarized and posted to #auth-changes.

Claude は PR ごとに1つのセッションを開き、その PR のコメントや CI 失敗などの更新をセッションに流し続けるので、フォローアップにも対応できます。今後、Webhook routines をより多くのイベントソースに拡張する予定だと言及されています。

## チームが作っているもの

### スケジュール
- **バックログ管理**:夜間に新規 issue をトリアージ、ラベル付け、アサインし、Slack にサマリ投稿
- **ドキュメントドリフト**:週次でマージ済み PR を走査し、変更された API を参照しているドキュメントを検出、更新 PR を開く

### API
- **デプロイ検証**:CD パイプラインがデプロイごとに呼び出し → Claude が新ビルドに対してスモークチェックを実行、エラーログからリグレッションを探し、リリースチャンネルに go/no-go を投稿
- **アラートトリアージ**:Datadog を routine のエンドポイントに向ける → Claude がトレースを取得し最近のデプロイと相関を取り、on-call がページを開く前に修正ドラフトを準備
- **フィードバック解決**:ドキュメントフィードバックウィジェットや社内ダッシュボードがレポートを投稿 → Claude が該当リポに対してセッションを開き、issue を文脈にして変更ドラフトを作成

### GitHub
- **ライブラリポート**:Python SDK に PR がマージされるたびに、並行する Go SDK へ変更をポートして対応 PR を開く
- **独自コードレビュー**:PR が開かれたら、チーム独自のセキュリティ・パフォーマンスチェックリストを走らせ、人間レビュアーの前にインラインコメントを残す

## はじめ方

routines は Claude Code on the web を有効化した Pro、Max、Team、Enterprise プランで利用できます。claude.ai/code から最初の routine を作成するか、CLI で `/schedule` と入力してください。

routines はインタラクティブセッションと同じくサブスクリプションの使用量を消費します。1日の上限:

- Pro:1日最大5個
- Max:1日最大15個
- Team/Enterprise:1日最大25個

これを超える場合は extra usage で実行可能です。詳細はドキュメントを参照してください。

## 出典

- [Introducing routines in Claude Code](https://claude.com/blog/introducing-routines-in-claude-code) — 2026年4月14日。
