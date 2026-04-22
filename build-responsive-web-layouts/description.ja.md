[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# レスポンシブなWebレイアウトを作る

## この記事について
この記事は、Claude（特にClaude Code）を使ってレスポンシブなWebレイアウトを生成したり、既存CSSをリファクタリングして幅広いビューポートサイズで安定して動作させる方法を紹介します。

## どんなときに役立つか
- 固定幅や硬いレイアウト規則が原因で、スマホ/タブレットでオーバーフローや可読性低下が起きるとき。
- ブレークポイントの手作業による試行錯誤から、テストで裏付けされた体系的な改善に移行したいとき。

## 主なポイント
- Claude Codeはスタイルシートを読み、硬直した制約を見つけて `max-width`、`flex-basis`、`auto-fit` のグリッドなど柔軟な代替案へ置き換えるのを支援できます。
- ブレークポイントごとのメディアクエリを追加し、320px・512px など小さなビューポートで横方向のオーバーフローがないか確認します。
- Playwrightテストを生成して、iPhone/iPad/デスクトップなど代表的なデバイスサイズで挙動を検証できます。

## 同梱リソース
- Skill: `responsive-layout-refactor`（手順、プロンプト例、スニペット例）

## 出典
- https://claude.com/blog/build-responsive-web-layouts
