---
name: long-context-needle-finding
description: Improve long-context retrieval by requiring the model to first quote the most relevant sentence from the provided context before answering.
---

## Instructions
Use this when the user provides a long document and asks a question that should be answered from a specific sentence.

1. Before answering, locate the single most relevant sentence in the provided context.
2. Start your response with exactly:
   - "Here is the most relevant sentence in the context:"
3. Quote the sentence verbatim.
4. Then answer the question, explicitly grounded in that sentence.

If you cannot find a relevant sentence in the provided context, say so and ask for clarification or more context.

See the prompt template and examples in the companion files.

## Examples
- Prompt template: [templates/response-prefix.md](./templates/response-prefix.md)
- Example usage: [examples/example.md](./examples/example.md)
- Notes on failure modes: [references/notes.md](./references/notes.md)
