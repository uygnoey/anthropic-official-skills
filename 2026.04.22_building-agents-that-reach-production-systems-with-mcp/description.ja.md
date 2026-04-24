[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Building agents that reach production systems with MCP

## この記事について
この記事は、Claude ベースのエージェントを実運用（プロダクション）のシステムやワークフローに接続する方法と、制約条件に応じてどの統合方式を選ぶべきかを整理します。

## どんなときに役立つか
課題管理、データウェアハウス、インフラなどの内部/外部システムへ、エージェントから**安全かつ信頼性高く**アクセスさせたいとき（特にクラウド/プロダクション環境）に役立ちます。

## 主なポイント
- 直接 API 呼び出し、CLI 自動化、MCP ベースのツールサーバーという 3 つの統合手法を比較します。
- プロダクションでは、リモート MCP サーバーが多様なクライアント/環境で再利用可能な統合レイヤーになります。
- ツールは API エンドポイントの鏡ではなく、ユーザーの意図（やりたい作業）単位で設計し、表面積を小さく保ちます。
- ツール定義を必要なときだけ読み込み、大きなツール結果はコードで処理してコンテキスト効率を改善します。
- OAuth などの標準認証とトークン保管パターンを使い、プロダクション運用に備えます。

## 同梱リソース
- Agent Skill: `skills/mcp-production-integration-patterns/SKILL.md`

## 出典
- https://claude.com/blog/building-agents-that-reach-production-systems-with-mcp
