# Data sources and wiring

Personalization is a join between the recipient and the data. This file records what was
connected in the source case and how to keep those connections stable.

## The warehouse, over MCP

Claude was connected to **BigQuery via MCP** — the marketing data source that itself pulls from:

- **HubSpot**
- **Clay**
- **Salesforce**

Connect the warehouse rather than each upstream tool where you can; the warehouse is where the
records have already been reconciled.

## The personalization join

For each recipient, the system:

1. Pulls the rep's **territory** from the CRM.
2. Retrieves relevant **account updates from Slack**.
3. Matches those against the current **marketing initiatives**.

The single field that determines this join is *how this audience maps to accounts in the CRM*.
It differs between audiences — BDRs map to accounts differently from account executives — and it
is the one field you change when duplicating the prompt for a new team.

## Content sources added over time

The briefing started narrow and grew to include:

- Blog articles
- eBooks
- Customer stories
- Webinars (including the list of registrants from the rep's own accounts)
- Partner ecosystem events
- Field events (from a spreadsheet)

## Handling schema drift in spreadsheets

The field events sheet rearranged its columns three times in six weeks. Hard-coded column
references break silently and produce confidently wrong output.

Instruct Claude to:

1. Read the **header row** before anything else.
2. Map each required field by **header name**.
3. Use **semantic instructions** — "look at the column with the event URL" — rather than column
   positions or letters.
4. **Verify the mapping** before processing rows, and stop and report a missing required header
   instead of guessing.

## Archiving

Archive each send for audit and accountability. The archive is what lets you trace a complaint
back to the exact message a recipient received, and it is what makes a rule addition verifiable.

## Source

- https://claude.com/blog/how-an-anthropic-field-marketer-uses-claude-code-to-send-weekly-personalized-updates-to-every-sales-rep
