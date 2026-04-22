# Example: Parallel research subagents

This pattern decomposes a query into facets, runs each facet in parallel subagents, then synthesizes results.

```python
# Sketch based on the blog post
import asyncio
from anthropic import AsyncAnthropic

client = AsyncAnthropic()

async def research_topic(query: str) -> dict:
    facets = await lead_agent.decompose_query(query)
    tasks = [research_subagent(facet) for facet in facets]
    results = await asyncio.gather(*tasks)
    return await lead_agent.synthesize(results)

async def research_subagent(facet: str) -> dict:
    messages = [{"role": "user", "content": f"Research: {facet}"}]
    response = await client.messages.create(
        model="claude-sonnet-4-5",
        max_tokens=4096,
        messages=messages,
        tools=[web_search, read_document],
    )
    return extract_findings(response)
```
