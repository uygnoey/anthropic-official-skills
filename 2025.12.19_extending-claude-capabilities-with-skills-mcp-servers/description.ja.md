[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Extending Claude's capabilities with skills and MCP servers

## この記事について
この記事は、エージェント構築において Skills と Model Context Protocol（MCP）サーバーがどのように補完し合うかを説明します。

## どんなときに役立つか
複数ステップのワークフローで、再利用可能な手順知（Skill）とライブなツール接続（MCP）のどちらに何を持たせるか判断したいときに役立ちます。

## 主なポイント
- MCP は外部システムへの安全で標準化されたアクセス（接続性）を提供し、Skill はそれをどう使うかという手順知（専門性）を提供します。
- Skill は複数ステップのワークフロー、一貫性、ドメイン知、組織知の共有に向いています。
- MCP はリアルタイムデータ取得、外部システムでの操作、ファイル操作、API 連携が必要な場合に向いています。
- 組み合わせる際は、JSON 返却など MCP の指示と Skill の出力指示が衝突しないよう注意します。

## 同梱リソース
- Skill: `skills-and-mcp-architecture-playbook` (Agent Skills)

## 出典
- https://claude.com/blog/extending-claude-capabilities-with-skills-mcp-servers
