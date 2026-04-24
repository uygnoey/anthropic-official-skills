[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は Claude Code のプラグインを紹介します。プラグインは、Claude Code のカスタマイズ（拡張ポイント）をまとめて配布できる軽量な仕組みで、Claude Code 内からインストールしてオン／オフを切り替えられます。

## どんなときに役立つか
チームやプロジェクトで同じ Claude Code 環境（例: テスト用ハーネス、コードレビュー用フック、ツール連携）を標準化・共有したいときに役立ちます。手作業で設定をコピーする必要が減ります。

## 主なポイント
- プラグインは、スラッシュコマンド、サブエージェント、MCP サーバー、フックなどの拡張ポイントを任意に組み合わせて同梱できます。
- 必要なときだけ有効化する設計で、システムプロンプトのコンテキストと複雑さを抑えられます。
- マーケットプレイスで配布・発見できます。
- Claude Code から `/plugin` コマンドでインストールできます（パブリックベータ）。

## 同梱リソース
- スキル: `skills/code-plugin-basics/SKILL.md`
- ガイド: `guides/claude-code-plugins-overview.ja.md`（および翻訳）
- プラグインバンドル例: `plugin/.claude-plugin/plugin.json`

## 出典
- https://claude.com/blog/claude-code-plugins
