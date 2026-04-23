[English](./remote-mcp-overview.en.md) · [한국어](./remote-mcp-overview.ko.md) · [Español](./remote-mcp-overview.es.md) · **日本語**

## Claude Code のリモート MCP とは？
リモート MCP 対応により、Claude Code はベンダーが運用する MCP サーバーに接続し、サードパーティのツールとリソースを開発ワークフローの中で直接利用できます。

## 重要な理由
- ローカルサーバーより低メンテナンス（更新・スケーリング・可用性はベンダーが管理）。
- ネイティブ OAuth による安全な接続。
- 外部システム（例: イシュートラッカー、エラーモニタリング）から構造化コンテキストを取り込める。

## 一般的な流れ
1. ベンダーの MCP サーバーを選ぶ。
2. Claude Code にベンダー URL を追加する。
3. 一度だけ認証する（OAuth）。
4. 公開されるツール／リソースをワークフローで使う。

## 出典
- https://claude.com/blog/claude-code-remote-mcp
