[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

# Cowork に専用ブラウザが追加

## この記事について

製品アナウンスです。デスクトップアプリの Claude Cowork に、専用のブラウザが組み込まれました。タスク
に Web サイトが必要になると、サイドパネルにブラウザが開き、Claude がページを移動し、読み、クリック
し、入力します。この記事では、このブラウザが Claude in Chrome とどう違うのか、どの場面でどちらを
使うのか、ログインをサイト単位でどう取り込むのか、プロンプトインジェクションからセッションを何が
守るのか、有料プランと法人管理者向けの提供がどう進むのかを説明しています。

## どんなときに役立つか

- 別のウィンドウで作業を続けながら、Web タスクを単独で走らせたいとき。
- ある作業に対して、内蔵ブラウザと Claude in Chrome のどちらを使うか決めたいとき。
- 自分のタブ・ブックマーク・パスワードを見せずに、エージェントにサイトへアクセスさせたいとき。
- 組織で内蔵ブラウザを有効化する必要がある法人管理者のとき。

## 主なポイント

- **デスクトップアプリの中のブラウザ。** タスクに Web サイトが必要になると、サイドパネルにブラウザ
  が開き、Claude がページを移動し、読み、クリックし、入力します。
- **個人のブラウジングとは分離されています。** Claude がユーザーのタブ、ブックマーク、パスワードを
  見ることはありません。
- **ログインはサイト単位で取り込みます。** macOS では Chrome、Edge、Firefox から、Windows と Linux
  では Firefox から取り込めます。金融・メール・SSO のサイトは、明示的に含めない限り既定で除外され
  ます。
- **内蔵ブラウザ**は、別の作業を続けている間に進めたい Web 作業に使います — リサーチの収集、ベンダー
  ポータルからの請求書のとりまとめなど。
- **Claude in Chrome** は、すでに開いていてログイン済みのページに使います — CRM の更新、受信トレイ
  の処理、ドキュメントの編集など。
- **既定値は利用状況によって変わります。** すでに Claude in Chrome を使っているかどうかで切り替わり、
  Settings → Cowork → Preferred browser から手動で選べます。
- **リスクはプロンプトインジェクションです。** ページに隠された指示が Claude の動きをそらそうとしま
  す。内蔵ブラウザには Claude in Chrome と同じ safeguards が適用され、ユーザーの依頼内容と実際の
  操作が一致しているかの確認も含まれます。これらはリスクを有意に減らしますが、完全にはなくせない
  ため、信頼できるサイトから始めてください。
- **提供。** Pro、Max、Team 向けに 1 週間かけて macOS、Windows、Linux（ベータ）へ展開されます。
  Claude に Web タスクを任せる以外の設定は不要です。法人管理者は Organization settings → Cowork →
  Built-in browser からすぐに有効化できます。
- **ブラウザはデスクトップにあります。** デスクトップアプリが開いていて接続されていれば Web と
  モバイルからも利用でき、デスクトップアプリのない Web のみの利用者は引き続き Claude in Chrome を
  使います。

## 同梱リソース

- `skills/desktop-browser-routing/SKILL.md` — 内蔵ブラウザと Claude in Chrome の選び分けと、
  どちらでも安全に作業するための指針。
- `skills/desktop-browser-routing/references/browser-choice.md` — 2 つのブラウザの比較。
- `skills/desktop-browser-routing/references/logins-and-safety.md` — ログイン取り込みの範囲と
  プロンプトインジェクションへの姿勢。
- `guides/built-in-browser-rollout.{en,ko,es,ja}.md` — 提供状況、管理者による有効化、セットアップ。

## 出典

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
