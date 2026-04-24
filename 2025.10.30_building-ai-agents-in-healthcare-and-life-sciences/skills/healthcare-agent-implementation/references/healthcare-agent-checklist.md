# Healthcare agent implementation checklist

This checklist is derived from the post “Building AI agents in healthcare and life sciences”.

## Interoperability
- Connectivity: direct integration vs custom connectors (APIs/MCP) vs middleware.
- Data formatting: standardized ingestion, format conversion, unstructured vs structured handling.
- Synchronization: real-time vs batch based on clinical urgency.

## Compliance and safety
- Define HIPAA (or other) compliance requirements for data processing.
- Evidence-based validation that the agent improves patient outcomes (when relevant).
- Audit trails for decisions and actions.
- Observability and risk management.

## Human authority
- Transparent reasoning clinicians can understand and validate.
- Escalation pathways for complex/ambiguous cases.
- Override capabilities.
- Fail-safe defaults prioritizing patient safety.

## Source
- https://claude.com/blog/building-ai-agents-in-healthcare-and-life-sciences
