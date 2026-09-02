# Skills, not subagents

## The default

One model in a standard agent loop: reasoning about a goal, exploring context, taking actions
through tools. Modularity comes from **agent skills**, not from splitting the agent.

## Why subagents hurt in commerce

| Problem | What happens |
|---|---|
| Tight coupling | Commerce conversations stay coupled across multiple intents and turns. |
| State loss | Each handoff drops conversational state, which degrades response quality. |
| Cost | Every handoff multiplies token cost. |
| Latency | Every handoff adds latency. |
| Boundaries | Commerce domains do not separate cleanly along agent lines. |

Measured outcome from the deployments behind this guidance: a single agent with skills has
consistently outperformed **both** the one-prompt-for-everything design **and** the subagent
design on quality — and often at lower cost and latency per task.

## When a subagent is still right

- The task is narrow and self-contained, and does not need the conversation's state. Deep
  research is the canonical example.
- The domain already operates its own dedicated agent, typically with its own compliance
  requirements, and calling it is an integration rather than a decomposition.

## The rule of thumb

If answering the user's next question could require what the other "agent" knows, it is a skill.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
