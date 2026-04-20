[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、マルチエージェントの代表的な協調パターン5つ（Generator-verifier、Orchestrator-subagent、Agent teams、Message bus、Shared state）を概観し、仕組み・トレードオフ・選び方を解説します。

## どんなときに役立つか
マルチエージェントが適切だと判断したあと、タスク分解、コンテキスト境界、情報の流れ、運用上の制約に基づいて協調アーキテクチャを選択（または進化）するときに役立ちます。

## 主なポイント
- まずは動く可能性のある最も単純なパターンから始め、うまくいかない点を観察して進化させます。
- Generator-verifierは評価基準を明示できる品質重視の成果物に適し、反復回数制限とフォールバックが重要です。
- Orchestrator-subagentは分解が明確で境界のあるサブタスクに適しますが、オーケストレーターが情報ボトルネックになり得ます。
- Agent teamsは長時間の独立サブタスクに適し、ワーカーがコンテキストを保持しますが、適切な分割が必要です。
- Message busはイベント駆動パイプラインや拡大するエコシステムに適しますが、ルーティング/デバッグが難しくなります。
- Shared stateは発見を直接共有する協調作業に適しますが、リアクティブループを避けるため強い終了条件が必要です。

## 同梱リソース
- Skill: マルチエージェント協調パターンの選定と適用（クイック表 + 進化ガイド）

## 出典
- https://claude.com/blog/multi-agent-coordination-patterns
