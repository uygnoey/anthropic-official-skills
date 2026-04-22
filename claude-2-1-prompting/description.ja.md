[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は、Claude 2.1の長文コンテキストで「needle-in-a-haystack」型の検索精度を上げる簡単なプロンプト修正を紹介します。

## どんなときに役立つか
非常に長い文書（最大約200Kトークン）を渡し、文書内の特定の一文（特に文脈から外れている/挿入された一文）に基づいて回答させたいときに役立ちます。

## 主なポイント
- Claude 2.1は200Kトークンのコンテキスト窓を持ち、長文検索が得意。
- 単独の一文（特に文脈外の一文）に基づく回答を渋る場合がある。
- 返答を「Here is the most relevant sentence in the context:」で始めるよう指示すると精度が大きく改善する。

## 同梱リソース
- Skill: long-context-needle-finding
- プロンプトテンプレート: needle探索のための先頭文

## 出典
- https://claude.com/blog/claude-2-1-prompting
