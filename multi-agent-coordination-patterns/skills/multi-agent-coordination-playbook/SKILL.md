---
name: multi-agent-coordination-playbook
description: A practical playbook for choosing and evolving between five multi-agent coordination patterns (generator-verifier, orchestrator-subagent, agent teams, message bus, shared state) based on task structure, context boundaries, and information flow.
---

## Instructions

Use this skill when you need to choose a multi-agent coordination architecture (or decide how to evolve your current one) after deciding that multiple agents are appropriate.

### 1) Start with the simplest pattern that could work

- Prefer a simple coordination pattern first.
- Observe where it struggles in your real workload.
- Evolve toward a more complex pattern only when the failure mode is clear.

### 2) Choose a pattern based on structure (not “sophistication”)

Use these quick-fit rules:

- **Generator-verifier**: choose when output quality is critical and you can make evaluation criteria explicit.
- **Orchestrator-subagent**: choose when task decomposition is clear and subtasks are bounded and mostly independent.
- **Agent teams**: choose when subtasks are independent and benefit from long-running, multi-step work with persistent worker context.
- **Message bus**: choose when work is event-driven, the workflow structure varies by event, and you expect your agent ecosystem to grow.
- **Shared state**: choose when work is collaborative and agents need to build on each other’s findings continuously.

### 3) Plan for each pattern’s primary failure mode

- **Generator-verifier**: define verification criteria; add an iteration limit and a fallback strategy.
- **Orchestrator-subagent**: mitigate the orchestrator becoming an information bottleneck (important findings may be summarized away).
- **Agent teams**: ensure true independence; partition work and plan conflict resolution when workers touch shared resources.
- **Message bus**: invest in logging/correlation; ensure routing accuracy (misroutes can fail silently).
- **Shared state**: implement strong termination conditions to avoid reactive loops (e.g., time budgets, convergence thresholds, or a designated “done” agent).

### 4) Evolve between patterns when your constraints change

- **Orchestrator-subagent → Agent teams** when workers must retain state across many assignments.
- **Orchestrator-subagent → Message bus** when conditional routing logic grows and workflow becomes event-driven.
- **Agent teams → Shared state** when workers need each other’s findings in real time.
- **Message bus → Shared state** when the “events” are mostly about sharing findings rather than triggering actions.

## Examples

### Example: quality-critical generation

Use **generator-verifier** when you can explicitly describe what the verifier should check (accuracy, tone, completeness), and you can cap iterations with a safe fallback.

### Example: multi-check code review

Use **orchestrator-subagent** when checks are distinct, require different context, and return a clear output that an orchestrator can synthesize.

### Example: migrating a large codebase

Use **agent teams** when each worker can own an independent partition for a long time, accumulating domain context across multiple steps.

### Example: security operations pipeline

Use **message bus** when alerts are event-driven, routing needs to expand over time, and new agent types should be pluggable.

### Example: collaborative research synthesis

Use **shared state** when agents should immediately see and build on each other’s discoveries in a shared store.

## Source

- https://claude.com/blog/multi-agent-coordination-patterns
