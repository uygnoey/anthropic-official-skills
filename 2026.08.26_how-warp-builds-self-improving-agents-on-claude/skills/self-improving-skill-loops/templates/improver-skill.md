---
name: improve-<base-skill-name>
description: Observer skill that runs on a schedule, reads accumulated human feedback on <base-skill-name>'s output, and proposes the smallest edit to that skill which captures the feedback. Opens a pull request for human review; never edits the running system directly.
---

# Improve `<base-skill-name>`

Scaffold for the outer skill in a self-improvement loop. Replace every `<...>` placeholder.
This skill runs **on a schedule**, not per task.

## Instructions

### 1. Authenticate

Authenticate to `<system holding the feedback — e.g. GitHub>` using
`<the credential mechanism your scheduler provides>`. Stop and report if authentication fails;
do not proceed with a partial view of the feedback.

### 2. Collect recent feedback

Run the bundled collector to pull the recent `<issues | pull requests | reviews>` that carry
human feedback on `<base-skill-name>`'s output, and write the result as JSON:

```
scripts/collect_feedback.py --since <N>d --out feedback.json
```

### 3. Summarize into concrete signals

For each item, record:

- what the agent suggested,
- how the human responded,
- the stated rationale, if any,
- whether the response is an affirmation, a correction, or noise.

Discard items with no rationale and no clear correction. Weight detailed, domain-specific
feedback from `<who counts as a domain expert here>` above cursory reactions.

### 4. Sanity-check before accepting

Assume some feedback is wrong. For each candidate signal, check it against the existing base
skill and the surrounding `<codebase | product | policy>` context. If a signal contradicts an
existing principle, surface the conflict in the PR description rather than silently choosing one.

### 5. Propose the smallest edit

Edit `<path/to/base/SKILL.md>` — or the resource file it points to — with the narrowest change
that captures the signal. Prefer:

- adding or sharpening a **principle with its rationale** over adding a rule,
- editing an existing section over adding a new one,
- moving detail into a companion file when the base skill grows.

### 6. Open a pull request

The PR body must state, for each change: the signal that prompted it, where that signal came
from, and what behavior should change on the next run. A human reviews, approves, and merges.
Only then does the change become inherited knowledge for the next run of the base skill.

## Examples

### A missing label

Feedback: a maintainer explained that an item should have received `<label>` because
`<rationale>`. Proposed edit: one sentence in the base skill's labeling section stating the
condition and the reason. No other change.

### Conflicting feedback

Two reviewers disagree about `<behavior>`. The improver does not pick a winner; it opens a PR
describing both positions and asks the reviewers to settle it in the base skill.
