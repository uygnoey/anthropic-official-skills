# Example: Context protection (OrderLookupAgent + SupportAgent)

This pattern uses a subagent to fetch and summarize large order details so the main support agent’s context stays clean.

```python
# Sketch based on the blog post
from anthropic import Anthropic

client = Anthropic()

class OrderLookupAgent:
    def lookup_order(self, order_id: str) -> dict:
        messages = [{"role": "user", "content": f"Get essential details for order {order_id}"}]
        response = client.messages.create(
            model="claude-sonnet-4-5",
            max_tokens=1024,
            messages=messages,
            tools=[get_order_details_tool],
        )
        return extract_summary(response)

class SupportAgent:
    def handle_issue(self, user_message: str):
        if needs_order_info(user_message):
            order_id = extract_order_id(user_message)
            order_summary = OrderLookupAgent().lookup_order(order_id)
            context = f"Order {order_id}: {order_summary['status']}, purchased {order_summary['date']}"

            messages = [{"role": "user", "content": f"{context}\n\nUser issue: {user_message}"}]
            return client.messages.create(
                model="claude-sonnet-4-5",
                max_tokens=2048,
                messages=messages,
            )
```
