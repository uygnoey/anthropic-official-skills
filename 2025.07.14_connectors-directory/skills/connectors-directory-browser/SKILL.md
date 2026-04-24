---
name: connectors-directory-browser
description: Use a lightweight checklist and prompt templates to evaluate a Claude connector from a directory, clarify required permissions, and define safe success criteria before you connect it.
---

## Instructions
Use this skill when you are about to connect a third-party tool to Claude from a connector directory.

1. **State the workflow goal** in one sentence.
2. **Identify the connector** (name + whether it is remote SaaS vs local desktop extension).
3. **Ask for access boundaries**: what data it can read, what it can write or trigger, and what it cannot do.
4. **Define success criteria**: what output you expect from the connector-enabled workflow.
5. **Define safety constraints** (red lines): sensitive data to avoid, irreversible actions to prohibit, environments to restrict (prod vs sandbox).
6. **Run a minimal test** with non-sensitive data.
7. **Review and iterate**: expand scope only after the minimal test passes.

Use the prompt templates in:
- templates/permission-audit.md
- templates/minimal-test-plan.md

## Examples
### Example: connecting Linear to draft release notes
1) Fill out `templates/permission-audit.md` for the Linear connector.
2) Create a small test plan using `templates/minimal-test-plan.md`.
3) Run the workflow on a single public or low-risk issue.

### Example: installing a local desktop extension
Follow the same steps, but explicitly note what local resources the extension can access (files, projects, local APIs) and what it sends to remote services.
