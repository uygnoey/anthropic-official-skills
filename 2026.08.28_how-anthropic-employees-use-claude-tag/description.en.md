**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How Anthropic employees use Claude Tag

## What is this post?

Three accounts of teams at Anthropic putting Claude Tag — Claude inside chat tools like Slack — to
work. A product marketer turns a long thread into a review-ready one-pager; a product strategist
consolidates feature requests scattered across channels; a product counsel runs a review channel
that clears marketing assets before legal sees them. Each account includes the prompt shape, the
elapsed time, and what the human kept for themselves.

## When is it useful?

- A decision or a spec is buried in a thread and somebody now needs it as a document.
- The same request keeps surfacing in different channels and nobody has the consolidated list.
- A specialist review queue is the bottleneck and most items in it turn out to be fine.
- You are deciding what an in-chat agent should be allowed to do, and with what access.

## Key points

- **Tag Claude in a thread and it works from the conversation's context.** It follows the
  conversation, uses standing instructions, and decides when to participate.
- **Thread to document: 45 minutes.** A 15+ message thread became a review-ready one-pager. Claude
  drafted two pages in two minutes — feature description, business case, implementation details,
  appendix — and four verification rounds followed.
- **Verification is the human's job.** Claude separated claims it had verified from claims needing
  the product lead's sign-off; the marketer supplied official resources and Claude rewrote.
- **Consolidation: about 26 minutes.** Roughly 20 search variants across channels, deduplicated,
  yielding about 24 accounts with requester handles, teams, account names, and source links.
- **The weekly version: 50 minutes.** About 120 raw reports became 23 open and 14 resolved issues
  organized by product area — work estimated at a full week by hand.
- **Prompt structure for consolidation:** search targets, what counts as a match, and the output
  format with an example.
- **Review channel: a day down to 30 minutes per asset.** Claude spots unsubstantiated claims,
  verifies factual statements, flags issues with specific remediation, and works with requesters
  directly. On one newsletter it flagged three items and resolved one itself.
- **Instructions that improve themselves.** A correction became a standing instruction, and a
  Friday routine has Claude propose instruction updates from the week's feedback, for approval.
- **Access is deliberately scoped** to granted channels and documents, and users are notified when
  Claude lacks the access a task needs.
- **Availability:** Team and Enterprise plans through Anthropic's first-party service, set up at
  claude.ai/admin-settings/claude-tag. Currently in public beta.

## Bundled resources

- `skills/slack-thread-delegation/SKILL.md` — deciding what to delegate in chat, prompting for the
  shape of the work, and keeping the output trustworthy.
- `skills/slack-thread-delegation/references/prompt-patterns.md` — the synthesis, consolidation, and
  review prompt structures in full.
- `skills/slack-thread-delegation/examples/tag-workflows.md` — the three case studies with prompts,
  timings, and outputs.
- `skills/slack-thread-delegation/templates/review-channel-instructions.md` — a fill-in standing
  instruction set for a review channel.
- `guides/chat-tag-deployment.{en,ko,es,ja}.md` — deployment patterns, access and governance, and a
  rollout sequence.

## Source

<https://claude.com/blog/how-anthropic-employees-use-claude-tag> (2026-08-28)
