---
name: code-plugin-basics
description: Package and share Claude Code customizations using plugins, with a focus on when to use plugins and how to install them from Claude Code.
---

## Instructions
You help the user package and share Claude Code customizations as a plugin.

- Treat a plugin as a lightweight bundle that can include any combination of:
  - slash commands
  - subagents
  - MCP servers
  - hooks
- Prefer enabling plugins only when needed to reduce prompt context and complexity.
- If the user asks about distribution, explain marketplaces at a high level and point them to the plugin marketplace mechanism.
- If the user asks for “how to install”, provide the in-product `/plugin` commands.

### Installation workflow
- Add a marketplace: `/plugin marketplace add <user-or-org>/<repo-name>`
- Install a plugin: `/plugin install <plugin-name>`

## Examples
### Install a plugin from a marketplace
```
/plugin marketplace add user-or-org/repo-name
/plugin install feature-dev
```

### Minimal plugin bundle skeleton
See: `templates/plugin.json`
