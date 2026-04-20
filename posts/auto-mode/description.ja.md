[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## この記事について
Claude CodeのAuto mode（自動モード）を紹介します。Claudeが多くのツール操作を自動承認しつつ、安全策でリスクの高い操作をブロックします。

## どんなときに役立つか
承認の中断を減らして長時間タスクを走らせたい一方で、--dangerously-skip-permissionsで権限確認を完全に外すのは避けたいときに役立ちます。

## 主なポイント
- Claude Codeの既定の権限はファイル書き込みやbashコマンドごとに承認を求めますが、Auto modeはその中断を減らすための仕組みです。
- 各ツール呼び出しの前に、分類器が破壊的になり得る操作（大量削除、機密データの持ち出し、悪意あるコード実行など）を確認します。
- 安全と判断された操作は自動実行され、危険な操作はブロックされて別の手段を試すよう促されます。ブロックが続く場合は最終的にユーザー承認が求められます。
- 権限チェックの完全スキップよりはリスクを下げますが、リスクをゼロにはできないため、隔離環境での利用が推奨されます。
- `claude --enable-auto-mode`で有効化し（Shift+Tabでモード切替）、管理者はマネージド設定の`disableAutoMode`で無効化できます。

## 同梱リソース
- 1 skill (auto-mode-permissions)

## 出典
- Auto mode for Claude Code (2026-03-24): https://claude.com/blog/auto-mode
