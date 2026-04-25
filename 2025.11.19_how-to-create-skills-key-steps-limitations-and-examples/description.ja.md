[English](./description.en.md) · [한국어](./description.ko.md) · [Español](./description.es.md) · **日本語**

## この記事について

この記事は、Claude の Skills を実務的に作るためのガイドです。Skill が安定して発火するための要点、SKILL.md の構成、テストと改善の進め方を解説します。

## どんなときに役立つか

Claude アプリ（claude.ai）、Claude Code、または Skills API で再利用可能な Skill を作りたいときに、命名、description（発火条件）、指示の構造、テスト、コンテキスト量の管理の指針が必要な場合に役立ちます。

## 主なポイント

- Skill の中核は name / description（発火に最重要）/ instructions の 3 要素です。
- description は「何ができるか」「いつ使うべきか」「何には使わないか」を具体的に書きます。
- SKILL.md はフェーズ、前提条件、エラーハンドリング、例を含め、読み流しやすい構造にします。
- コンテキストを肥大化させないため、追加ファイルへのリンクを使う「メニュー」方式を推奨します。
- 通常ケース／エッジケース／スコープ外の要求でテストマトリクスを作り、実利用から反復改善します。

## 同梱リソース

- すぐに流用できる Skill 作成テンプレート: `skills/skill-authoring-guide/templates/skill-template.md`
- Skill 検証用のテストマトリクステンプレート: `skills/skill-authoring-guide/templates/test-matrix.md`
- 記事の SKILL.md 例から整理した抜粋: `skills/skill-authoring-guide/examples/skill-examples.md`

## 出典

- https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
