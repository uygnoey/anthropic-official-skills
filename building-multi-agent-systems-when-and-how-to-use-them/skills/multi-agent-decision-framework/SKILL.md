---
name: multi-agent-decision-framework
description: Decide when to use multi-agent architectures (context protection, parallelization, specialization), how to decompose work by context boundaries, and how to add a verification subagent pattern with explicit pass/fail criteria.
---

## Instructions
You should help the user decide whether a multi-agent system is warranted, and if so, propose a practical architecture.

1. Start by attempting a single-agent solution.
2. Only recommend multi-agent if at least one strong driver applies:
   - Context protection (avoid context pollution)
   - Parallelization (explore in parallel; thoroughness over speed)
   - Specialization (focused toolsets, prompts, or deep domain expertise)
3. Use context-centric decomposition:
   - Prefer boundaries that keep related context together (e.g., feature + tests).
   - Avoid boundaries that require heavy shared state or sequential handoffs.
4. If adopting multi-agent, propose:
   - Orchestrator responsibilities
   - Subagent responsibilities and context boundaries
   - What minimal artifacts flow between them (summaries, diffs, checklists)
5. Add a verification subagent when independent validation is valuable.
   - Require explicit acceptance criteria.
   - Guard against “early victory” by forcing comprehensive checks (including negative tests).

Refer to the companion reference for decision criteria and the companion examples for implementation sketches.

## Examples
- Decision & architecture proposal: see [references/decision-framework.md](./references/decision-framework.md)
- Context protection pattern: see [examples/context-protection.md](./examples/context-protection.md)
- Parallel research pattern: see [examples/parallel-research.md](./examples/parallel-research.md)
- Specialization routing pattern: see [examples/specialization-routing.md](./examples/specialization-routing.md)
- Verification subagent loop: see [examples/verification-subagent.md](./examples/verification-subagent.md)
