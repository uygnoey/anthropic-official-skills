[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## この記事について
Claude CodeでのOpus 4.7の挙動と、プロンプトや設定（effortレベル、adaptive thinking、セッション構成）を調整して品質とトークン効率を高める方法を解説します。

## どんなときに役立つか
Opus 4.6から4.7へ移行（または新規セットアップ）する際に、挙動の予測可能性やトークン使用量の管理、effortレベルの使い分け指針が必要なときに役立ちます。

## 主なポイント
- 最初のターンで意図・制約・受け入れ基準・関連ファイル位置をまとめて伝えると、ターンをまたぐ追加推論を減らし品質を高めやすくなります。
- 対話型セッションではユーザーのターンごとに推論オーバーヘッドが増えるため、質問をまとめ、必要なやり取りを減らすのが有利です。
- Claude CodeでのOpus 4.7の既定effortは`xhigh`（`high`と`max`の間）で、多くのagenticなコーディング作業に推奨されます。タスク中にeffortを切り替えてコスト/レイテンシと性能を調整できます。
- Opus 4.7は固定予算のExtended Thinkingではなくadaptive thinkingを採用しており、必要に応じて「もっと/少なく考える」よう明示的に促せます。
- 挙動の変更点: 返答の長さは複雑さに合わせて調整され、ツール呼び出しは減って推論が増え、既定ではsubagent生成も減ります。より多くのツール利用や並列subagentが必要なら明示してください。

## 同梱リソース
- 1 skill (opus-4-7-code-best-practices)
- 1 guide set (opus-4-7-code-best-practices)

## 出典
- Best practices for using Claude Opus 4.7 with Claude Code (2026-04-16): https://claude.com/blog/best-practices-for-using-claude-opus-4-7-with-claude-code
