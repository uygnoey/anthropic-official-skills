[English](./skills-packaging-guide.en.md) · [한국어](./skills-packaging-guide.ko.md) · [Español](./skills-packaging-guide.es.md) · **日本語**

# Skillsパッケージングガイド

## 概要
このガイドは、段階的な公開を用いてAgent Skillsを構造化するための、記事の推奨アプローチを要約します。

## 推奨構造
- YAMLフロントマターは最小限（name + description）。
- 実行可能な手順は `SKILL.md` に。
- 長文資料は `references/` に分離し、`SKILL.md` からリンク。

## なぜ役立つか
段階的な公開により、大規模なスキルライブラリでも使いやすくなります。モデルは低コストで多くのスキル「一覧」を把握し、必要なときだけ詳細を読み込みます。

## 出典
- https://claude.com/blog/building-agents-with-skills-equipping-agents-for-specialized-work
