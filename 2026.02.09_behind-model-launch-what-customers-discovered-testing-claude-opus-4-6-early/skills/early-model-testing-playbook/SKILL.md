---
name: early-model-testing-playbook
description: A practical playbook for running a short pre-launch model evaluation window that blends automated evals with hands-on “vibe checks.”
---

## Instructions
Use this skill to plan and run a focused early-access evaluation of a new Claude model (or any LLM) during a short pre-release window.

1. **Prepare the evaluation window**
   - Clear calendars and set up a dedicated coordination channel (e.g., Slack).
   - Create a shared space for notes, observations, and test artifacts.
   - Avoid sharing early impressions too soon if you want to reduce team bias.

2. **Start with the hardest workloads**
   - Prioritize the real production-like tasks that matter most to your team.
   - Run both automated evals/benchmarks and hands-on stress tests.

3. **Collect two kinds of signals**
   - **Quantitative:** benchmark/eval scores.
   - **Qualitative:** how the model feels in real workflows (e.g., whether it behaves like a collaborator, how far it can go before stalling).

4. **Mix testing modes (examples from the post)**
   - Automated eval platform + hands-on stress testing.
   - Benchmarks + domain expert qualitative review (e.g., lawyers for legal tasks).
   - Iterative planning loops in existing engineering workflows.
   - Benchmarks + “vibe checks” (engineers building apps with the model).

5. **Document discoveries (strengths and rough edges)**
   - Capture what improved, what broke, and what patterns you’d want the model provider to iterate on.

## Examples
### Example: Minimal early access checklist
- Set up: channel + shared doc + owner.
- Run: top 5 hardest tasks + one benchmark suite.
- Record: failures, surprising wins, and clear go/no-go criteria.

## Notes
- This skill is derived from qualitative descriptions in the Claude blog post and does not include code or configuration snippets.
- Source: see `source.json` at the artifact root.
