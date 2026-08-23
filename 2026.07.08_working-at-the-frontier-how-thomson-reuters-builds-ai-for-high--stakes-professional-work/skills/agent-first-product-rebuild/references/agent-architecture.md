# The agent-first architecture

What the post states about Thomson Reuters' rebuild, and where it stops.

## The change

**From:** products built as chatbots; CoCounsel Legal running separate skills sequentially.

**To:** products rebuilt as agent-based systems. A single agent accesses hundreds of company tools
simultaneously. CoCounsel Legal rebuilt on the Claude Agent SDK, planning and orchestrating across
tools in real time.

The post is explicit that the alternative path was rejected: instead of creating smarter chatbots,
Thomson Reuters rebuilt products as agent-based systems.

## What the architecture demands of the model

Because one agent plans across a large tool surface, the abilities that matter are the ones planning
and tool use depend on:

| Ability | Why the architecture needs it |
| --- | --- |
| Making plans | No pre-wired flow decides the sequence; the agent constructs it |
| Using tools effectively | Hundreds of tools are available simultaneously |
| Context management | Thread continuity has to hold across extended tool-use chains |

Hron's framing: "Our big test for Claude is to assess how good it is at making plans and using tools
effectively."

## Constraints that are part of the design

- **Customer data remains protected** and is not used for third-party model training.
- **The human professional stays accountable** for the end work product, and the model is expected to
  bring them into developing it rather than delivering a finished artifact for sign-off.
- **Citations are validated before findings reach human review.**

## What is next, per the post

Hron's team prioritizes:

- longer-horizon work,
- better context management,
- dependable tool-calling across agent task chains.

## What the post does not specify

- Which tools the agent has access to, or how they are grouped.
- How the agent is evaluated on plan quality, beyond the statement that it is the big test.
- How the migration from sequential skills to a single agent was staged.
- What "hundreds of company tools" covers.

## Source

[Working at the Frontier: How Thomson Reuters Builds AI for High-Stakes Professional Work](https://claude.com/blog/working-at-the-frontier-how-thomson-reuters-builds-ai-for-high--stakes-professional-work) — Claude blog, July 8, 2026.
