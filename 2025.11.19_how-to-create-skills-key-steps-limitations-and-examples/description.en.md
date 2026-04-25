**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?

This post is a practical guide to writing Skills for Claude, including what makes a Skill trigger reliably, how to structure SKILL.md, and how to test and iterate.

## When is it useful?

Use it when you want to create a reusable Skill (for Claude apps, Claude Code, or the Skills API) and need guidance on naming, description writing (triggering), instruction structure, testing, and keeping the context size manageable.

## Key points

- A Skill has three core components: name, description (drives triggering), and instructions.
- Descriptions should be specific: what the skill does, when it should activate, and what it should not be used for.
- Keep SKILL.md scannable with clear phases, prerequisites, error handling, and examples.
- Use companion files to avoid bloating context (a “menu” approach that links to additional files).
- Test with a matrix: normal, edge cases, and out-of-scope requests; iterate based on real usage.

## Bundled resources

- A ready-to-adapt skill authoring template: `skills/skill-authoring-guide/templates/skill-template.md`
- A test matrix template for skill validation: `skills/skill-authoring-guide/templates/test-matrix.md`
- Example excerpts derived from the post’s SKILL.md examples: `skills/skill-authoring-guide/examples/skill-examples.md`

## Source

- https://claude.com/blog/how-to-create-skills-key-steps-limitations-and-examples
