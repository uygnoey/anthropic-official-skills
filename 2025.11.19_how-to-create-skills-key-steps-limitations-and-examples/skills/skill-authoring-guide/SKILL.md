---
name: skill-authoring-guide
description: "Write and refine Claude Skills (SKILL.md): naming, description writing for reliable triggering, instruction structure, testing/validation, and context-size management via companion files. Use when creating or reviewing a Skill, or when debugging why a Skill triggers incorrectly."
---

# Skill authoring guide

## Instructions

Help the user create or improve a Skill (SKILL.md) by applying the process and constraints described in the source post.

### 1) Clarify the core requirements

- Define the specific task the skill accomplishes.
- Identify triggers: when should the skill activate?
- Define success criteria and expected outputs.
- List edge cases and limitations.

Use the template at:

- [templates/skill-template.md](./templates/skill-template.md)

### 2) Name the skill

- Use lowercase with hyphens.
- Keep it short, clear, and descriptive.

### 3) Write the description (most important for triggering)

Write from Claude’s perspective.

Include:

- Specific capabilities
- Clear activation triggers / use cases
- Relevant context
- Boundaries (what not to use it for)

### 4) Write the main instructions

- Keep instructions structured and scannable (headers, bullets, phases).
- Include prerequisites, execution steps, error handling, and limitations.
- Provide concrete examples.
- Prefer a “menu” approach: keep SKILL.md lightweight and link to detailed companion files so only the relevant file needs to be loaded.

### 5) Test, validate, and iterate

Create a test matrix with:

- Normal operations
- Edge cases
- Out-of-scope requests

Use:

- [templates/test-matrix.md](./templates/test-matrix.md)

Then iterate based on real usage:

- Update descriptions if triggering is inconsistent.
- Clarify instructions if outputs vary.

## Examples

See:

- [examples/skill-examples.md](./examples/skill-examples.md)

## References

- [references/post-notes.md](./references/post-notes.md)
