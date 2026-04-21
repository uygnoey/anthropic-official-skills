---
name: security-review-automation
description: Automate security review workflows with Claude Code by running ad-hoc checks before commits and adding pull-request reviews via GitHub Actions.
---

## Instructions
Use this skill to set up a lightweight security review loop around Claude Code.

1. **Run an ad-hoc review before committing**
   - Update Claude Code to the latest version.
   - In your repository, run the built-in command: `/security-review`.
   - Review the findings and (optionally) ask Claude Code to implement fixes.

2. **Add automated pull request reviews**
   - Install the Claude Code GitHub Action (see the post for the installation and configuration documentation).
   - Configure rules to reduce false positives and align with your team’s security policy.
   - Have the action comment on PR diffs with issues and recommended fixes.

3. **Focus areas to request/check**
   - SQL injection risks
   - Cross-site scripting (XSS)
   - Authentication and authorization flaws
   - Insecure data handling
   - Dependency vulnerabilities

## Examples
### Example: Pre-commit check
- Run: `/security-review`
- Then ask Claude Code: “Fix the highest severity issues you found, and explain each change.”

### Example: Pull request automation
- Add the GitHub Action and have it run on every PR.
- Tune rules to reduce noise.

## Notes
- This skill is based on the Claude blog post (see `source.json` at the artifact root).
- The post references customization and installation documentation, but does not include a full workflow file or configuration snippet.
