---
name: healthcare-agent-implementation
description: A practical framework for implementing AI agents in healthcare and life sciences, focusing on interoperability, latency, compliance, and maintaining human clinical authority.
---

## Instructions
Use this skill to plan and review a healthcare/life-sciences agent initiative.

1) Decide interoperability requirements
- Connectivity approach: direct integration, custom connectors (e.g., via APIs or MCP), or middleware.
- Data formatting: standardize ingestion, convert between incompatible formats, and explicitly handle unstructured clinical text vs structured fields.
- Synchronization: define what must be real-time vs what can be batch, based on clinical urgency.

2) Design for regulation and safety
- Define the compliance boundary (e.g., HIPAA) and data governance requirements.
- Build evidence-based validation for any clinical impact claims.
- Require audit trails for agent decisions/actions and operational observability.

3) Preserve human clinical authority
- Make reasoning and recommendations transparent enough for clinicians to validate.
- Define escalation paths for ambiguity and higher-risk conditions.
- Provide clear override controls.
- Prefer fail-safe defaults that prioritize patient safety over efficiency.

4) Start with appropriate use cases
- Prefer high-visibility workflows with measurable outcomes (e.g., documentation efficiency, patient engagement).
- Consider lower-risk starter tasks such as abnormal lab flagging, drug interaction checks, and guideline reminders.

5) Plan for scale
- Invest in shared infrastructure (e.g., a unified NLP engine and integration layer) before proliferating point solutions.

## Examples
### Example: selecting an initial use case
- Choose a workflow with clear success metrics (time-to-document, error rates, clinician satisfaction).
- Validate data access pathways across EHR and departmental systems.
- Define required latency and escalation triggers.

### Example: governance checklist
See `references/healthcare-agent-checklist.md`.
