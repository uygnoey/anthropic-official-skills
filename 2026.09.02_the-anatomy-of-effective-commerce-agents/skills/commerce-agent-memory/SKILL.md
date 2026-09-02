---
name: commerce-agent-memory
description: Give a commerce agent long-term memory that survives the session, without paying latency for it. Covers storing facts as typed records in a production database rather than in model context, writing memory asynchronously from a separate extraction pass instead of through an agent tool, the three read layers (always in context, pre-fetched per turn, lookup tool), and the data-handling requirements for retention, correction and deletion. Use when users have to repeat constraints across sessions, or when designing memory extraction and retrieval for a shopping or merchant agent.
---

# Commerce agent memory

A returning customer should not have to restate that they are allergic to shellfish, that they
wear a size 11, or which store they collect from. Long-term memory is what makes the second
session better than the first.

## Instructions

### 1. Store memory in your database, not in model context

Memory belongs in a production database. Structure each fact as a **typed record**:

| Field | Meaning |
|---|---|
| `key` | The fact's identity — `shoe_size`, `default_store`. |
| `value` | The remembered value. |
| `category` | The class of fact, used for retention and retrieval policy. |
| `source_session` | Where the fact came from, for audit and correction. |

A ready-to-fill record shape is in
[templates/memory-fact-record.json](templates/memory-fact-record.json).

### 2. Write memory asynchronously, outside the agent

Do **not** give the agent a `remember_this` tool. Instead, run extraction in the harness: at the
end of each turn, or every few turns, a separate thread or process reads the conversation and
creates, updates, or deletes facts.

Why this wins:

- No latency added to the user-facing turn.
- Measured **13% higher fact recall** in internal evals than tool-based writing.
- The agent no longer has to decide what is worth remembering while it is also trying to answer.

**The extraction prompt must read only user and assistant text — never tool results.** Otherwise
product descriptions from the catalog turn into "facts about the user".

### 3. Read memory in three layers

1. **Always in context.** The small set of fixed facts nearly every request needs — default
   store, fulfillment preference.
2. **Pre-fetched per turn.** Facts made relevant by signals in the current request.
3. **Lookup tool.** Everything else, behind an explicit retrieval call.

The layering is what keeps memory from eating the context window and the cache prefix.

### 4. Meet the data-handling requirements

- Decide which **types** of memory you retain, and enforce that at the write path with a
  validator — not with a prompt instruction.
- Give users an interface to **view, correct and delete** stored facts.
- Set **retention periods**; preferences age out.
- Make memory a **per-deployment toggle** so jurisdictions with different rules can run the same
  agent.

Full requirements are in [references/memory-data-handling.md](references/memory-data-handling.md).

## Examples

### A fact that should be extracted

> User: "no shellfish for me, I'm allergic"

Extraction writes `{key: "dietary_restriction", value: "no shellfish", category: "safety",
source_session: "..."}`. Because the category is `safety`, this fact goes in layer 1 — always in
context — for a grocery or restaurant agent.

### A fact that should not be extracted

A catalog tool result describes a jacket as "waterproof to 10,000mm". Because the extractor reads
only user and assistant text, this never becomes `{key: "waterproof_rating"}` on the user's
record. This is exactly the failure the tool-result exclusion prevents.

### A layer-3 fact

> User, six months ago: "the dining table I bought was for the lake house"

Not needed on most turns. It lives behind the lookup tool and surfaces when the user asks about
furniture again.

### An update, not an append

> User: "actually I moved — use the Oakland store now"

Extraction updates `default_store` in place rather than adding a second record. Extraction
creates, updates **and deletes**.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents (published 2026-09-02)
