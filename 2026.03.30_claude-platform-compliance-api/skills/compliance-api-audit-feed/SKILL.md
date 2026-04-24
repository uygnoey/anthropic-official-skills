---
name: compliance-api-audit-feed
description: Enable and use the Claude Platform Compliance API to retrieve and filter organization audit activity (by time range, user, or API key) for security and compliance workflows.
---

## Instructions
You are helping an admin or security/compliance team audit Claude Platform activity using the Compliance API.

1) Confirm the Compliance API is enabled for the organization.
- If it is not enabled, instruct the user to contact their account team to enable it.

2) Confirm an admin API key exists.
- If not, instruct the user to create an admin API key in the Claude Platform.

3) Define what audit view the user needs.
- Time range
- Specific user(s)
- Specific API key(s)

4) Query the activity feed endpoint using the admin API key.
- If the user needs a single feed across multiple Claude organizations under a parent organization, instruct them to add the relevant Claude API organization(s) to the same parent organization and filter the unified feed accordingly.

5) Output a concise audit report.
- Summarize the filters used and the time window.
- List notable events and any follow-up questions.

## Examples
### Example: Setup checklist
User: We need to audit our Claude API usage for the last 30 days.
Assistant:
- Verify the Compliance API is enabled (contact your account team if not).
- Create or locate an admin API key.
- Use the activity feed endpoint to pull events for the last 30 days and review by user and API key.

### Example: Multi-org feed
User: We have multiple Claude organizations and want one activity feed.
Assistant:
- Add the Claude API organization to the same parent organization you use for Claude Enterprise.
- Use the Compliance API activity feed and filter for the organizations you need.
