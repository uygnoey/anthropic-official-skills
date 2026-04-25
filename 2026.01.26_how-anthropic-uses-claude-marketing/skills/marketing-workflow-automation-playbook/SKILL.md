---
name: marketing-workflow-automation-playbook
description: Build lightweight Claude Code workflows that remove repetitive marketing busywork—generating creative variations (e.g., via Figma plugins) and producing upload-ready ad copy (e.g., RSA headlines) with Skills for brand/accuracy/best practices.
---

## Instructions
Use this skill to translate common growth marketing workflows into small, repeatable tools.

### Principles from the post
- Start small: pick a simple, repetitive task to prove the tool works (e.g., a “calculator app” experiment).
- Describe the problem in natural language: explain the friction, the desired outcome, and the constraints.
- Reuse existing resources: point to relevant docs (e.g., API documentation) and build incrementally.
- Encode guidance as Skills: keep brand tone/voice, product accuracy constraints, and channel-specific best practices in reusable files.
- Produce operational outputs: ensure the workflow ends with something the team can directly use (e.g., a CSV ready for Google Ads upload).

### Workflow pattern 1: Creative variations with a Figma plugin
- Goal: avoid repeated copy/paste across frames and aspect ratios.
- High-level behavior: select a frame, provide copy variations once, click a button to generate permutations.
- Template prompt: see [templates/figma-plugin-build-prompt.md](./templates/figma-plugin-build-prompt.md).

### Workflow pattern 2: Responsive Search Ads (RSA) copy → upload-ready CSV
- Goal: quickly brainstorm, refine, validate character limits, and export.
- Inputs: campaign data, existing copy, keywords.
- Guardrails: brand tone/voice, product accuracy, RSA best practices.
- Template prompt: see [templates/rsa-workflow-spec.md](./templates/rsa-workflow-spec.md).
- Output: CSV ready for upload.

## Examples
- [examples/figma-plugin-outcome.md](./examples/figma-plugin-outcome.md)
- [examples/rsa-slash-command.md](./examples/rsa-slash-command.md)
