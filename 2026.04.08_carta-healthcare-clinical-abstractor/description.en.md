**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Carta Healthcare gets AI to reason like a clinical abstractor

## What is this post?
This post explains how Carta Healthcare built Lighthouse, a clinical data abstraction platform that uses Claude to reason over medical records and reach high accuracy at scale.

## When is it useful?
Useful if you are building an AI system that must make defensible, time-bounded decisions from messy domain documents (especially when humans must review and trust the outputs).

## Key points
- Context engineering matters as much as the model: decide what evidence to include/exclude and in what order, and assemble patient-specific context at runtime.
- Use explicit temporal anchors (e.g., procedure start time) when asking for “pre‑procedure” values so the model can apply correct time logic.
- Build an evaluation framework early and make it granular enough to pinpoint whether failures come from prompt wording, missing context, or retrieval gaps.
- Close the loop with domain experts: incorporate abstractor feedback into prompt/context updates quickly.
- Prioritize transparency: show the evidence and the model’s rationale so abstractors can validate results.

## Bundled resources
- A Claude Code skill for “context engineering for time-bounded extraction” with reusable templates and evaluation checklist.

## Source
- https://claude.com/blog/carta-healthcare-clinical-abstractor
