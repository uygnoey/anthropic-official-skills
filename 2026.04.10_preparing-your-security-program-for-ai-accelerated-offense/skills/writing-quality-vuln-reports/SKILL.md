---
name: writing-quality-vuln-reports
description: Writes upstream-quality vulnerability reports when a model has assisted in finding the bug. Use when preparing to send a finding to an open-source maintainer, vendor, or internal security team, especially if AI was involved in discovery or drafting.
---

# Writing quality vulnerability reports

Open-source maintainers are already receiving large volumes of low-quality automated reports, and many ignore anything that looks AI-generated. This skill enforces the report-quality bar from the post: a report is sent only when a human has verified it and is willing to put their name on it.

## Instructions

Follow each item in order. Skip none. If any item cannot be completed honestly, do not send the report.

1. **State the bug and its impact in plain language.** A maintainer should understand what is wrong and why it matters from the first paragraph, without running anything.
2. **Walk through the code path.** Show where the input enters, where it is mishandled, and where the consequence occurs. This is the part that distinguishes a real finding from a pattern match.
3. **Provide a working reproduction.** A proof-of-concept the maintainer can run, or a test case that fails, is more credible than any amount of explanation.
4. **Include a proposed patch you would accept if you were the maintainer.** A patch demonstrates the reporter understands the codebase well enough to fix the problem in a way that fits the project's conventions.
5. **Disclose AI involvement upfront.** If a model found the bug or drafted the report, say so in the first line. Concealing it costs more credibility than disclosing it.
6. **Defer to the maintainer's judgment.** If they decline the report, make peace with that. The goodwill of being easy to work with is worth more than winning an argument over one bug.

## Self-check before sending

Close the editor and explain the bug from memory. **If you cannot describe what goes wrong without referring back to the model output, you do not understand it well enough to report it.** Do not send.

## Examples

**Good opening paragraph**

> This report describes a TOCTOU race in `acquire_lock()` that lets a second caller bypass the ownership check under load. The model ran a directed scan and I verified the race with the attached reproduction (runs in < 1 s). A fix is included. AI was used for discovery and draft; I have reviewed and verified.

**Bad opening paragraph (do not send)**

> An AI scan detected a possible race condition in acquire_lock. This may be exploitable. Please investigate.

The bad version violates items 1–4 and fails the memory self-check.

## Anti-patterns

- Submitting a finding you cannot reproduce yourself.
- Patches "in the style of the project" that no human has read end to end.
- Hiding that a model was involved.
- Arguing with a maintainer who has already declined.

## Source

Distilled from [Preparing your security program for AI-accelerated offense](https://claude.com/blog/preparing-your-security-program-for-ai-accelerated-offense) (published 2026-04-10).
