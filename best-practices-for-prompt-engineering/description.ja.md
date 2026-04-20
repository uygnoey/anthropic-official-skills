[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude のプロンプトエンジニアリング ベストプラクティス

## このスキルについて
Anthropic 公式のプロンプトエンジニアリングガイドをもとに整理したクイックリファレンスです。基本5技法（明確さ・文脈・具体性・例示・「わからない」の許可）と応用4技法（プリフィル・思考の連鎖・出力フォーマット制御・プロンプトチェーン）を収録しています。モデル世代別の推奨事項も反映しており、Claude 4.x では旧モデルと比べて XML タグの多用やロールプレイが不要になっています。

## どんなときに役立つか
- プロンプトへの回答が汎用的すぎたり、的外れだったりするとき
- Claude が情報を捏造している（ハルシネーション）と思われるとき
- 出力フォーマット（JSON・散文・リスト）が一定しないとき
- 複雑なタスクが一度で解決しないとき
- プロンプトを見直して API コストや遅延を最適化したいとき

## 基本5技法

### 1. 明確かつ直接的に伝える
- Vague: `Create an analytics dashboard`
- Explicit: `Create an analytics dashboard. Include as many relevant features and interactions as possible. Go beyond the basics to create a fully-featured implementation.`

### 2. 文脈と理由を提供する
- Less effective: `NEVER use bullet points`
- More effective: `I prefer responses in natural paragraph form rather than bullet points because I find flowing prose easier to read and more conversational.`

### 3. 具体的に指定する
- Vague: `Create a meal plan for a Mediterranean diet`
- Specific: `Design a Mediterranean diet meal plan for pre-diabetic management. 1,800 calories daily, emphasis on low glycemic foods. List breakfast, lunch, dinner, and one snack with complete nutritional breakdowns.`

### 4. 例を使う
まず1例から始め、必要に応じて複数例に増やします。フォーマット・トーン・微妙なパターンが重要な場合に特に効果的です。
```
Here's an example of the summary style I want:

Article: [link]
Summary: EU passes comprehensive AI Act targeting high-risk systems. Key provisions include transparency requirements and human oversight mandates. Takes effect 2026.

Now summarize this article in the same style: [new link]
```

### 5. 不確実性を表現する余地を与える
```
Analyze this financial data and identify trends. If the data is insufficient to draw conclusions, say so rather than speculating.
```

## 応用4技法

### 1. レスポンスのプリフィル
```python
messages=[
    {"role": "user", "content": "Extract the name and price from this product description into JSON."},
    {"role": "assistant", "content": "{"}
]
```

### 2. 思考の連鎖 — 基本 / ガイド付き / 構造化
構造化の例:
```
Think before you write the email in <thinking> tags.
First, analyze what messaging would appeal to this donor.
Then, identify relevant program aspects.
Finally, write the personalized donor email in <email> tags, using your analysis.
```

### 3. 出力フォーマットを制御する
希望する散文・マークダウン・リストの方針を明示的に記述します。

### 4. プロンプトチェーン
複雑なタスクを連続したステップに分解し、各出力を次のプロンプトの入力として使います。

## 技法の選び方

| 目的 | 使う技法 |
|---|---|
| 特定の出力フォーマット | 例示・プリフィル・明示的なフォーマット指示 |
| ステップごとの推論 | Extended thinking（Claude 4.x）または思考の連鎖 |
| 複雑な多段階タスク | プロンプトチェーン |
| 透明性のある推論 | 構造化出力を伴う思考の連鎖 |
| ハルシネーション防止 | 「わからない」を許可する文言 |

## アンチパターン
- 過度なエンジニアリングは避ける。
- 基本を軽視しない。
- AI が意図を読めると思い込まない。
- すべての技法を同時に使わない。
- 反復改善を怠らない。
- 古い技法（XML 多用 / ロールプレイ）に頼らない。

## トラブルシューティング

| 症状 | 対処 |
|---|---|
| 回答が汎用的すぎる | 具体性・例示を追加 |
| 的外れ | 目的・文脈をより明示 |
| フォーマットが一定しない | 例示またはプリフィル |
| 複雑すぎて不安定 | チェーンに分解 |
| 不要な前置きが多い | プリフィル ／「省略して」と明示 |
| 情報を捏造する | 「わからない」を許可する文言 |
| 提案するだけで実装しない | 行動を表す動詞を明示 |

## 出典
〜をもとに整理しました: [Best practices for prompt engineering](https://claude.com/blog/best-practices-for-prompt-engineering)（公開: 2025-11-10）。権威ある指針は原文をご参照ください。
