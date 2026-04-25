# Example spec: /submit-pr (context-aware command)

This spec mirrors the post’s example of a custom command that loads context and gathers repository state before proceeding.

## Goal
Reduce friction and mistakes when submitting a pull request.

## Inputs
- Current working branch
- Current working directory (to infer relevant domain context)

## Command behavior
1. Load relevant context (e.g., nearest `CLAUDE.md` up the directory tree).
2. Gather repository state:
   - `git status`
   - recent changes (diff summary)
   - related PR information (if your tooling can link commits/branches to PRs)
3. Present a short plan for the PR:
   - What changed
   - Why it changed
   - Risk assessment
   - Tests run / to run
4. Draft PR title and description for review.

## Source
- https://claude.com/blog/how-brex-improves-code-quality-and-productivity-with-claude-code
