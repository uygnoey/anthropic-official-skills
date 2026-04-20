[English](./coordination-patterns.en.md) · [한국어](./coordination-patterns.ko.md) · [Español](./coordination-patterns.es.md) · **日本語**

# マルチエージェント協調パターン：選定ガイド

## このガイドについて
この記事で紹介された5つのマルチエージェント協調パターンを選び、必要に応じて進化させるための要約ガイドです。

## どんなときに役立つか
マルチエージェントが必要だと判断したあと、タスク構造と運用上の制約に合うアーキテクチャを選ぶときに使います。

## クイック選定表

| 状況 | パターン |
| --- | --- |
| 品質重視の成果物 + 明示的な評価基準 | Generator-verifier |
| 明確なタスク分解 + 境界のあるサブタスク | Orchestrator-subagent |
| 並列・独立・長時間のサブタスク | Agent teams |
| イベント駆動パイプライン + 拡大するエージェント生態系 | Message bus |
| 共有された発見に基づき協働する作業 | Shared state |
| 単一障害点の回避が重要 | Shared state |

## 進化の考え方
- まずは動く可能性のある最も単純なパターンから始めます。
- 主な失敗モードを観察します。
- 失敗が継続的かつ構造的な場合にのみ、より複雑なパターンへ進化させます。

## 出典
- https://claude.com/blog/multi-agent-coordination-patterns
