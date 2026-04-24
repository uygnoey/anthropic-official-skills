[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Harnessing Claude's Intelligence | アプリ構築のための3つの主要パターン

## この記事について
この記事では、Claude Platform 上でアプリケーションを構築する際に、モデルの能力向上に追従しながらレイテンシとコストのバランスを保つための3つのパターンを紹介しています。

## どんなときに役立つか
エージェントハーネス（プロンプト・ツール・コンテキスト・メモリの境界設計）を設計する際に、何を Claude に委任し、何をインフラ側で固定すべきかの指針が必要なときに役立ちます。

## 主なポイント
- Claude がすでによく理解しているツール（例: bash やテキストエディタ）を優先して活用し、高レベルのパターンはそこから自然に生まれるよう設計する。
- Claude の能力が向上するにつれてハーネスの前提が古くなる可能性があるため、「今、何をやめられるか？」と自問しながら継続的に見直す。
- 境界は慎重に設定する: キャッシュ効率を高めるコンテキスト設計を行い、セキュリティ・UX・オブザーバビリティのために高リスクな操作は宣言型ツールに昇格させる。

## 同梱リソース
- スキル 1 件: `skills/building-on-evolving-models/SKILL.md` — 3つのパターンとキャッシュヒット原則を Agent Skills 形式でまとめたもの
- ガイド 1 件（英語/韓国語）: `guides/three-patterns-app-harness.en.md`, `guides/three-patterns-app-harness.ko.md`

## 出典
〜をもとに整理しました: [Harnessing Claude's Intelligence: 3 Key Patterns for Building Apps](https://claude.com/blog/harnessing-claudes-intelligence)（公開: 2026-04-02）。
