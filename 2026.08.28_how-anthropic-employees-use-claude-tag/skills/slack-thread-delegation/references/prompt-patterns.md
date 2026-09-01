# Prompt patterns for in-chat delegation

Three shapes of work, three prompt structures. All are drawn from the workflows described in the
source post.

## 1. Synthesis — thread to document

The thread is the specification, so the prompt can be short. Name the source, the artifact, and who
it is for.

> go through this Slack thread and come up with a one pager that [the requester] is asking for

What made it work:

- Tagged **inside the thread**, so the whole conversation is the context — no pasting, no summary.
- Names the **artifact type** ("one pager"), which sets length and register.
- Names the **requester**, which sets the audience and the level of detail.

The draft that came back was structured on its own: feature description, business case,
implementation details, appendix. Let Claude propose the structure from the thread before you
impose one — the thread usually already implies it.

### Follow-up prompts for the verification loop

1. *Check the factual accuracy of this draft.* — Claude separates what it can verify from what
   needs sign-off by the owner.
2. *Here are the official resources for [X].* — supply sources for the unverified claims.
3. *Rewrite those sections against these sources.* — repeat until nothing is left unattributed.

Four versions was the realistic count for a one-pager before it was ready to send to the product
lead.

## 2. Consolidation — scattered mentions to one list

State three things explicitly:

1. **Search targets** — which channels, which time range, which kinds of message.
2. **Match definition** — what counts as an instance of the thing you are looking for. This is what
   lets Claude dedupe rather than return every near-miss.
3. **Output format, with an example row** — the columns you want and one filled-in example.

Sketch:

> Search [channels] since [date] for [thing]. Count it as a match when [criteria]; the same
> request mentioned in two places is one entry. Return a table with columns [A, B, C, source link],
> like this: | ... | ... | ... | ... |

Reported behavior on a real run: roughly 20 search variants across channels, deduplication across
sources, and about 24 entries carrying requester handle, team, account name, and a link back to the
source thread.

### Scaling the same pattern to a recurring digest

The weekly version asked for every product problem reported by enterprise customers. Same three
elements, wider target, plus one grouping instruction:

- Organize by **product area**.
- Split **open** from **resolved**.
- Give each entry a **summary** and a **link to the source thread**.

About 120 raw reports became 23 open and 14 resolved issues in 50 minutes.

## 3. Review — standing instructions instead of per-item prompts

Do not prompt per asset. Create a dedicated channel, write the rules once, and let requesters post
into it. The per-asset prompt then collapses to posting the asset. A starting structure is in the
sibling `templates/review-channel-instructions.md`.

The instruction set should cover:

- **What to check** — for marketing assets: unsubstantiated claims, factual statements that need a
  source.
- **What access to use** — company chat, an internal knowledge index, the public web.
- **What to do with a finding** — flag it with specific remediation instructions, and work with the
  requester directly to resolve it.
- **When to resolve it alone** — if the supporting information exists in internal documents, verify
  the claim in real time rather than flagging it back.

## Turning feedback into standing instructions

When a correction applies beyond the item at hand, say so:

> From now on, when you flag a claim, first try to verify it in real time. Add that as a standing
> instruction.

And schedule the meta-review:

> Every Friday, review the feedback I gave on this week's reviews and propose updates to your
> standing instructions for my approval.

Approval stays with the human. The instruction set becomes the accumulated judgment of the reviews
it has already been through.
