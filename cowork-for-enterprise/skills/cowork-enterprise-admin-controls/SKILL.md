---
name: cowork-enterprise-admin-controls
description: A checklist-style reference of the enterprise admin controls described for Claude Cowork (RBAC, spend limits, usage analytics, and OpenTelemetry observability).
---

## Overview
This skill converts the Claude blog post into a reusable checklist you can apply when deploying Claude Cowork in an enterprise environment.

## Instructions
Use this as an admin/operator checklist:

1. **Access controls**
   - Create user groups (manually or via SCIM).
   - Define custom roles that specify which Claude capabilities are allowed.
   - Enable Claude Cowork for the appropriate teams.

2. **Spend controls**
   - Set per-group (team) spend limits from the admin console.

3. **Usage analytics**
   - Use the admin dashboard to track sessions and active users.
   - Use the Analytics API to review:
     - per-user activity
     - skill invocations
     - connector invocations
     - DAU/WAU/MAU metrics (alongside Chat and Claude Code)

4. **Observability and auditability**
   - Enable expanded OpenTelemetry emission to capture events such as:
     - tool and connector calls
     - files read or modified
     - skills used
     - whether AI-initiated actions were approved manually or automatically
   - Route telemetry to your observability/SIEM stack (e.g., Splunk, Cribl).

5. **Connector governance**
   - Configure per-connector action controls (e.g., allow read actions but disable write actions across the organization).

6. **Connector enablement**
   - If relevant, add the Zoom MCP connector from the connector directory in settings.

## Examples
- Example deployment plan: roll out to one group, set an initial spend limit, enable telemetry, then expand group-by-group as adoption grows.

## Source
- https://claude.com/blog/cowork-for-enterprise
