**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post introduces automated security reviews in Claude Code, including an ad-hoc `/security-review` command and a GitHub Actions integration that reviews pull requests.

## When is it useful?
- Before committing changes, to catch common vulnerabilities early.
- On every pull request, to continuously flag issues and suggest fixes as part of your existing CI workflow.

## Key points
- The `/security-review` command can check for SQL injection, cross-site scripting (XSS), authentication/authorization flaws, insecure data handling, and dependency vulnerabilities.
- The GitHub Action can comment on PR diffs, and is configurable to reduce false positives via custom rules.
- Claude Code can be asked to implement fixes after issues are identified.

## Bundled resources
- Skill: `skills/security-review-automation/SKILL.md`

## Source
- https://claude.com/blog/automate-security-reviews-with-claude-code
