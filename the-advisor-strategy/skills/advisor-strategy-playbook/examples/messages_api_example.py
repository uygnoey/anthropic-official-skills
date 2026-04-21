# Source: https://claude.com/blog/the-advisor-strategy
# Note: This is the snippet as published in the blog post.

response = client.messages.create(
    model="claude-sonnet-4-6",  # executor
    tools=[
        {
            "type": "advisor_20260301",
            "name": "advisor",
            "model": "claude-opus-4-6",
            "max_uses": 3,
        },
        # ... your other tools
    ],
    messages=[...],
)

# Advisor tokens reported separately
# in the usage block.
