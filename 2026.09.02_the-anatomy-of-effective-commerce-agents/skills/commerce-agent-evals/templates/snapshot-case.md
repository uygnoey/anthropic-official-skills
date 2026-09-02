# Snapshot eval case: <short name>

Fill one file (or one row) per case. A snapshot case constructs state directly rather than
simulating a conversation.

## Metadata

- **Area:** core | context-dependent | safety-and-brand | interface | multi-capability
- **Flow:** <which user flow this belongs to>
- **Owner:** <team that owns the skill or tool under test>
- **Origin:** <production transcript / SME-authored / converted from simulated-user run>
- **CI tier:** core-high-traffic | safety-always | change-scoped

## Constructed state

**System prompt:** <version or identifier>

**Tools available:** <list>

**Messages array (verbatim):**

```json
[
  {"role": "user", "content": "..."},
  {"role": "assistant", "content": [{"type": "tool_use", "name": "...", "input": {}}]},
  {"role": "user", "content": [{"type": "tool_result", "content": "..."}]}
]
```

> Prefer histories that are long, messy or internally contradictory. Clean-state cases are
> already over-represented in most suites.

## Test message

```
<the user message appended to the state above>
```

## Grading

### Final state

- [ ] <expected write, or explicitly: no write occurs>
- [ ] <cap or limit that must hold>

### Response

- [ ] <claim that must be traceable to returned data>
- [ ] <what the model must say when data is missing>
- [ ] <language that must appear byte-for-byte, if regulated>
- [ ] <what must NOT appear — internal IDs, unretrieved prices>

### Multi-capability cases only

- [ ] Half A graded independently: <...>
- [ ] Half B graded independently: <...>

## Notes

<Why this case exists. Link the production incident or SME rule it encodes.>
