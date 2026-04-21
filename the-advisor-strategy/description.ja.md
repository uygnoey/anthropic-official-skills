[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について
この記事は「アドバイザー戦略（advisor strategy）」を紹介します。強力なモデル（Opus）をアドバイザー、より低コストなモデル（Sonnet または Haiku）を実行役（executor）として組み合わせ、必要な場面だけ高品質な助言を得て全体コストを抑える考え方です。

## どんなときに役立つか
通常はツールを使ってエンドツーエンドで進められる一方、難しい判断の局面でだけ上位の推論が必要になるエージェント的ワークフローに向いています。最上位モデルを常時使わずに性能とコストのバランスを取れます。

## 主なポイント
- 実行役（Sonnet/Haiku）がタスクを最後まで実行します（ツール呼び出し、結果の読み取り、反復）。
- 必要に応じて実行役がアドバイザー（Opus）に相談し、アドバイザーは計画／修正／停止シグナルを返しますが、ツール呼び出しやユーザー向け最終出力は行いません。
- Claude Platform の「advisor tool」により、Messages API リクエストの小さな変更で単一リクエスト内のモデル切り替えが可能になります。
- `max_uses` でアドバイザー呼び出し回数を制限でき、使用量（トークン）は別枠で報告されます。

## 同梱リソース
- アドバイザー戦略を整理し、記事中の API スニペットをそのまま含むスキル: `skills/advisor-strategy-playbook/SKILL.md`。
- API スニペットを含む実行可能な例: `skills/advisor-strategy-playbook/examples/messages_api_example.py`。

## 出典
- https://claude.com/blog/the-advisor-strategy
