---
name: enterprise-workspace-security-basics
description: Establish baseline administrative and security practices for rolling out Claude in an organization, based on capabilities highlighted in the Claude for Enterprise announcement.
---

## Instructions
Use this skill to translate enterprise rollout requirements into a clear checklist of workspace controls and rollout steps.

1) Confirm identity and access controls
- Plan for SSO and domain capture.
- Define role-based permissions, including a designated primary owner for the workspace.

2) Plan for compliance visibility
- Decide how you will review and retain audit logs once available.
- Document who is responsible for periodic access reviews.

3) Plan for provisioning automation
- If you need automated onboarding/offboarding, plan for SCIM when available.

4) Plan for engineering workflow integration
- If engineering teams need repository context, evaluate native GitHub integration availability and rollout sequence.

5) Communicate data-handling expectations
- Align internal guidance with the statement that Anthropic does not train on customer conversations/content.

## Examples
### Example: Turn requirements into a rollout checklist
Input:
- We need SSO, strict access control, and an audit trail.

Output:
- Access controls: enable SSO + domain capture; define roles; assign a primary owner.
- Compliance: set an audit log review cadence and retention policy (when audit logs are available).
- Provisioning: plan SCIM integration for joiner/mover/leaver automation (when available).
- Engineering: decide whether to enable GitHub integration for repo context.

## Source
- https://claude.com/blog/claude-for-enterprise
