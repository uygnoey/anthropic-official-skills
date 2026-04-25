# Team patterns (examples catalog)

This file catalogs the concrete usage examples described in the post.

## Codebase navigation and understanding
- Infrastructure onboarding: new data scientists provide the repository; Claude Code reads CLAUDE.md files and explains data pipeline dependencies.
- Product Engineering: ask Claude Code to identify relevant files for bug fixes, feature work, or analysis.

## Testing and code review
- Product Design: ask Claude Code to write comprehensive tests; integrate automated pull request comments via GitHub Actions; use Claude to refactor tests when they fail due to formatting issues.
- Security Engineering: ask for pseudocode and guidance through test-driven development; periodically check in; translate testing guidance to other languages (e.g., Rust).

## Debugging and troubleshooting
- Security Engineering incidents: provide stack traces and documentation to trace control flow.
- Data Infrastructure troubleshooting: provide dashboard screenshots; Claude guides through Google Cloud UI step-by-step to diagnose issues and gives commands to fix (e.g., create new IP pool and add to cluster).
- Product Engineering: describe observed behavior; Claude proposes a fix; humans review and ship.

## Prototyping and feature development
- Product Design: set up autonomous loops (write code → run tests → iterate); map error states and system statuses to identify edge cases; even build editor keybindings.
- Data science: one-shot prompting to build a React app to visualize RL model performance, then iterate with small tweaks.
- Inference: ask Claude to explain model-specific functions.

## Documentation and knowledge management
- Security Engineering: synthesize multiple documentation sources into markdown runbooks and troubleshooting guides.

## Automation and workflow optimization
- Growth Marketing: agentic workflow processes CSVs of ads, identifies underperformers, generates new variations within strict character limits; uses two specialized subagents.
- Growth Marketing: a Figma plugin identifies frames and generates up to 100 ad variations by swapping headlines and descriptions.
- Legal: prototypes "phone tree" systems.

## Source
- https://claude.com/blog/how-anthropic-teams-use-claude-code
