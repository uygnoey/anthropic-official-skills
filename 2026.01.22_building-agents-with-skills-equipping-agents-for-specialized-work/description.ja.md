[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Skillsでエージェントを作る：専門的な仕事のための能力付与

## この記事について
この記事は、Agent Skillsとは何か、ドメイン知識をどのようにファイルとしてパッケージするか、そして段階的な公開（メタデータ → SKILL.md → references）が多数のスキルをスケールさせる理由を説明します。

## どんなときに役立つか
- ルール/標準/ワークフローを毎回説明しなくても、エージェントに一貫して適用させたいとき。
- 多数のスキルを扱いつつ、コンテキスト使用量を抑えたいとき。

## 主なポイント
- まずYAMLフロントマター（name + description）が提示され、必要になったときにのみSKILL.md全文やより深い参照ファイルを読み込みます。
- 記事は3層構造を強調します：メタデータ（約50トークン）、SKILL.md（約500トークン）、参照ファイル（2,000+トークン、必要時のみ）。
- スキルは補助ファイル（例：ドキュメント、スライドのガイダンス、スクリプト）を同梱し、SKILL.mdから参照できます。

## 同梱リソース
- Skill: `skills-packaging-principles`（構造ガイド＋テンプレート）
- Guide: `skills-packaging-guide`（概要、推奨レイアウト）

## 出典
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
