# Example: Specialization via toolsets and prompts

This pattern creates specialized agents (e.g., CRM vs marketing) and routes requests via an orchestrator.

```python
# Sketch based on the blog post
from anthropic import Anthropic

client = Anthropic()

class CRMAgent:
    """Handles customer relationship management operations"""
    system_prompt = (
        "You are a CRM specialist. You manage contacts, opportunities, and account records. "
        "Always verify record ownership before updates and maintain data integrity across related records."
    )
    tools = [crm_get_contacts, crm_create_opportunity]

class MarketingAgent:
    """Handles marketing automation operations"""
    system_prompt = (
        "You are a marketing automation specialist. You manage campaigns, lead scoring, and email sequences. "
        "Prioritize data hygiene and respect contact preferences."
    )
    tools = [marketing_get_campaigns, marketing_create_lead]

class OrchestratorAgent:
    """Routes requests to specialized agents"""
    def execute(self, user_request: str):
        return client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            system=(
                "You coordinate platform integrations. Route requests to the appropriate specialist:\n"
                "- CRM: Contact records, opportunities, accounts, sales pipeline\n"
                "- Marketing: Campaigns, lead nurturing, email sequences, scoring\n"
                "- Messaging: Notifications, alerts, team communication"
            ),
            messages=[{"role": "user", "content": user_request}],
            tools=[delegate_to_crm, delegate_to_marketing, delegate_to_messaging],
        )
```
