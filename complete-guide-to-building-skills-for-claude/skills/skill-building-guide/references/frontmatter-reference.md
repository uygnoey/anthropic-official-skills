# SKILL.md frontmatter reference

## Minimal required frontmatter
```yaml
---
name: your-skill-name
description: What it does. Use when user asks to [specific phrases].
---
```

## Optional fields (example)
```yaml
---
name: skill-name-in-kebab-case
description: What it does and when to use it. Include specific trigger phrases.
license: MIT
allowed-tools: "Bash(python:*) Bash(npm:*) WebFetch"
metadata:
  author: Company Name
  version: 1.0.0
  mcp-server: server-name
  category: productivity
  tags: [project-management, automation]
  documentation: https://example.com/docs
  support: support@example.com
---
```

## Notes
- `name` must be kebab-case and should match the skill folder name.
- `description` must include both what the skill does and when it should trigger, and must be under 1024 characters.
- Avoid XML tags (`<` and `>`) anywhere in SKILL.md.

## Source
- https://resources.anthropic.com/hubfs/The-Complete-Guide-to-Building-Skill-for-Claude.pdf
