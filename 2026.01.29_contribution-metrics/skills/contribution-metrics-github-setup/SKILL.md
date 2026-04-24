---
name: contribution-metrics-github-setup
description: Enable Claude Code contribution metrics by connecting your organization to GitHub, then verify the analytics dashboard is populating PR and commit attribution.
---

## Instructions

Use this skill to guide a workspace admin through enabling Claude Code contribution metrics (public beta) via GitHub integration.

### Preconditions
- You are a Claude Code workspace admin/owner.
- Your organization can install and authorize the Claude GitHub App.

### Steps
1. Install the Claude GitHub App for your organization.
2. In Claude, go to **Admin settings → Claude Code**.
3. Toggle on **GitHub Analytics**.
4. Authenticate to your GitHub organization when prompted.
5. After your team uses Claude Code, confirm metrics begin populating in the Claude Code analytics dashboard.

### Interpretation notes
- Treat these as directional adoption/impact signals alongside your existing engineering KPIs (e.g., PR throughput, sprint metrics).
- Expect conservative attribution: only high-confidence matches between Claude Code session activity and GitHub PR/commit activity are counted.

## Examples

### Example: Admin enablement checklist
- [ ] Claude GitHub App installed
- [ ] GitHub Analytics enabled in Admin settings
- [ ] GitHub org authentication completed
- [ ] Dashboard shows PRs merged and code committed with attribution
