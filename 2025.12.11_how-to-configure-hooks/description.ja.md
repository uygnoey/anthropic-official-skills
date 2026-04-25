[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について

この記事では、Claude Code の hooks を設定して、繰り返し作業の自動化、プロジェクト規約の強制、コーディングセッションへの動的コンテキスト注入を行う方法を解説します。

## どんなときに役立つか

ツール実行の前後、セッション開始/終了、コンパクト前後、Stop などのライフサイクルイベントで、コマンド実行やプロンプトによるチェックを自動化したいときに役立ちます。

## 主なポイント

- hooks は JSON で設定し、ライフサイクルイベント（例: PreToolUse, PostToolUse, SessionStart, Stop）に 1 つ以上のアクションを割り当てます。
- アクションはコマンド実行や、プロンプト型のチェックを行えます。
- matcher は大文字/小文字を区別し、複数の一致した hooks が並列に実行されることがあります。
- hooks はユーザー権限で任意のシェルコマンドを実行するため、stdin の入力検証/サニタイズや機密ファイルの扱いに注意が必要です。
- 既定のタイムアウト（60 秒）があり、hook ごとに設定できます。

## 同梱リソース

- hook の入出力をログに残すための再利用可能なラッパースクリプト: `hooks/log-wrapper.sh`
- よくあるパターンの例:
  - Write 前にパスを検証 (`hooks/pretooluse-validate-write-path.json`)
  - PermissionRequest でテストコマンドを制限 (`hooks/permissionrequest-validate-tests.json`)
  - Write/Edit 後に自動整形 (`hooks/posttooluse-format-written-files.json`)
  - compact 前にトランスクリプトをバックアップ (`hooks/precompact-backup-transcript.json`)
  - SessionStart にプロジェクト文脈を表示 (`hooks/sessionstart-show-context.json`)
  - SessionStart にセッションログを記録 (`hooks/sessionstart-log-session.json`)
  - Stop 時に完了チェックを必須化 (`hooks/stop-completion-check.json`)
  - SubagentStop でサブエージェント出力をレビュー (`hooks/subagentstop-review.json`)
  - UserPromptSubmit でスプリント文脈を注入 (`hooks/userpromptsubmit-inject-context.json`)

## 出典

- https://claude.com/blog/how-to-configure-hooks
