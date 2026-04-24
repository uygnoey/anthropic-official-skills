[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Claude Code: セッション管理と1Mコンテキスト

## この記事について

Claude Codeチームによる、セッションとコンテキストウィンドウ(最大100万トークンに拡張)の管理方法についての実践ガイドです。新しいスラッシュコマンド `/usage` を紹介し、context rot(コンテキスト劣化)とコンパクションを説明しつつ、各ターンを continue / `/rewind` / `/clear` / `/compact` / サブエージェントの5つに分岐する決定点として整理しています。

## どんなときに役立つか

- Claude Code のセッションを長く使っていて、出力の質が徐々に落ちると感じるとき
- `/compact`、`/clear`、rewind、サブエージェントのどれを使うか迷うとき
- コンテキストがまだ「有用」なのか、削ぎ落とすべきなのかを判断する指針が欲しいとき
- 自動コンパクションが悪さをした経験があり、その原因を理解したいとき
- サブエージェントへ作業を委譲する具体的なプロンプト例が欲しいとき

## 主なポイント

- コンテキストウィンドウにはシステムプロンプト、会話全体、ツール呼び出しと出力、読んだ全ファイルが含まれ、ハードカットオフです。
- **Context rot**:コンテキストが膨らむと注意が分散し、古い内容が現在のタスクを邪魔して性能が劣化します。
- **コンパクション**はウィンドウが埋まると履歴をモデル生成の要約に置き換えます。`/compact <hint>` で自分からも発火できます。
- 各ターンは分岐点:Continue、`/rewind`(Escを2回)、`/clear`、`/compact`、サブエージェント。
- 原則:**新しいタスク ⇒ 新しいセッション**。ただし、実装した機能のドキュメント化など続きの作業はコンテキストを保つ方が速く安価です。
- **修正より巻き戻し**:Claudeが誤った方向に行ったときは「うまくいかなかった」と伝えるより、有用なファイル読み込み直後まで `/rewind` して学んだ内容で再プロンプトします。
- **Compact vs Clear**:compact は情報が失われるが手軽、clear は手間がかかるが何を持ち越すかを自分で決められます。
- **悪い自動コンパクション**はモデルがあなたの次の方向を予測できないときに起きます。ウィンドウが埋まる前にヒント付きで先回りして compact しましょう。
- **サブエージェント**:次の作業が結論だけ必要で中間出力が大量になるときに最適。判断基準:*そのツール出力をまた使うのか、結論だけで十分か?*

## 同梱リソース

- `skills/context-window-management/SKILL.md` — continue / rewind / compact / clear / subagent を選ぶ決定フレームワーク
- `skills/context-window-management/references/decision-table.md` — 記事の「状況 → ツール」決定表
- `skills/context-window-management/examples/subagent-prompts.md` — 記事中のサブエージェント委譲プロンプト
- `guides/session-management-1m-context.{en,ko,es,ja}.md` — 4言語の解説ガイド

## 出典

- [Using Claude Code: session management and 1M context](https://claude.com/blog/using-claude-code-session-management-and-1m-context) — 2026年4月15日公開。
