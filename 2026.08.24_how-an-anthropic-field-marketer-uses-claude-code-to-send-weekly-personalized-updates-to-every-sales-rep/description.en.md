**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# How an Anthropic field marketer uses Claude Code to send weekly personalized updates to every sales rep

## What is this post?

Adam Ward, a field marketer at Anthropic, describes how he replaced a manual Sunday-evening slide deck with an automated system that generates a personalized Monday-morning digest for every sales representative he supports. The system was first built in about an hour during a marketing hackathon, then hardened over several weeks of pilot feedback.

Ward's central claim is that marketers do not need coding skills to build this — they need to explain their business problem clearly. He opened with a prompt that framed him as a product manager rather than a technician, recorded voice explanations to give Claude business context, and supplied template examples showing the output format he wanted.

## When is it useful?

- You send a recurring update (weekly, monthly) that is time-consuming to personalize by hand.
- You support several teams and the same briefing has to be recut per audience.
- You have CRM, event, and content data spread across systems and need it matched to individual owners.
- You want a rollout path that starts as a self-review loop and only later becomes an autonomous send.

## Key points

- **Lead with the business problem.** Brief Claude the way you would brief a new colleague. Ward positioned himself as a product manager, not a technician, and recorded voice explanations of the problem to convey business context.
- **Show the format you want.** Template examples of the desired output — structured as the "top three things for the week," prioritizing actionable items — did more than abstract instructions.
- **Connect the real data.** Claude was connected to BigQuery through MCP, the marketing data source that pulls from HubSpot, Clay, and Salesforce. Personalization comes from the rep's CRM territory, relevant account updates from Slack, and matching against marketing initiatives.
- **Turn every correction into an explicit rule.** After the first week the prompt held nine explicit content rules, each traceable to specific feedback: never invent a URL and only render links from exact source data; verify contact titles against the event audience; gate by industry so retail accounts do not get finance-focused events; write a custom welcome note for new sellers who have no accounts yet.
- **Make the prompt survive schema drift.** The field events sheet rearranged its columns three times in six weeks. The fix was to have Claude read the header row and verify column mapping first, using semantic instructions like "look at the column with the event URL" instead of hard-coded column references.
- **Pilot with a committed group.** One sales team of ten reps who agreed to give feedback surfaced the data-quality and relevance failures before a wider rollout.
- **Scaling is a copy plus one field.** When BDRs asked for their own version, Ward duplicated the prompt and changed the single field describing how BDRs map to accounts in the CRM; it launched in two days. Customer success, alliances, and cross-functional partners followed.
- **Measurable impact.** Registrations for an executive dinner doubled within a week of the digest rolling out. Each Monday send is archived for audit, managers get consolidated roll-ups, and the system ran on its own while Ward was on holiday.

## Bundled resources

- `skills/personalized-weekly-digests/SKILL.md` — build and operate a recurring personalized digest with Claude Code.
- `skills/personalized-weekly-digests/templates/kickoff-prompt.md` — the opening brief that frames the business problem.
- `skills/personalized-weekly-digests/templates/digest-message-template.md` — the "top three things" message shape.
- `skills/personalized-weekly-digests/references/content-rules.md` — the rule catalog derived from pilot feedback.
- `skills/personalized-weekly-digests/references/data-sources.md` — data wiring and schema-drift handling.
- `skills/personalized-weekly-digests/examples/feedback-to-rule.md` — worked feedback-to-rule conversions.
- `guides/automating-a-recurring-personalized-briefing.{en,ko,es,ja}.md` — the rollout methodology in four languages.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep (published 2026-08-24, by Adam Ward)
