# UI components as tools

## The pattern

Rather than defining custom markup the model has to emit correctly, expose each UI component as
a tool. `present_products`, `present_itinerary`, and so on. The model calls the tool; the client
renders the component from the arguments.

## What it buys you

- **History that survives.** Components are stored in their native format in the messages array,
  so they remain part of the conversation history the model reads on the next turn.
- **Type safety and validation.** The component's contract is the tool schema.
- **Referenceable layout.** Because the ordered list is in the transcript, the user can say "the
  first hotel" or "third one down" and the model resolves it.
- **Progressive streaming.** The component can be streamed to the client as it is produced.

## The trade-off, and the mitigation

Presentation tool arguments buffer on the server before they reach the client, which shows up as
perceived latency on component-heavy turns.

Setting `eager_input_streaming: true` streams tool input at the token level instead of buffering
it. The cost is reduced schema guarantees — the client may start rendering from a partial,
not-yet-validated argument object. In practice schema violations are very rare on Claude
Sonnet-class models and up, which makes this a reasonable default for presentation tools.

## Safety constraint

Presentation tools render only server-supplied records. A component must never render a product,
price or order that the model produced from its own text rather than from a tool result. See the
`commerce-agent-safety-harness` skill for the server-issued ID rule that enforces this.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
