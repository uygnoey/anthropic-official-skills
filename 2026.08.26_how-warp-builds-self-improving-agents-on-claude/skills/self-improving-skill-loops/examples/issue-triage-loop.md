# The loop in action: Warp's issue triage agent

A walkthrough of one full turn of the self-improvement loop, as described in the post. The agent
is public: https://github.com/warpdotdev/warp-agents-demo-github-issue-triage

## 1. The base skill runs

Someone files a GitHub issue. A GitHub Action triggers the triage agent, which:

- analyzes complexity and feasibility,
- assigns labels,
- suggests a direction for the fix.

## 2. A human notices a gap

On a sample issue the inner skill performed well but missed the **`ready to spec`** label — the
label that signals contributors can build product and technical specs from the issue.

## 3. Feedback is left where the work happened

A maintainer left feedback directly on the issue, explaining both the expectation and the
rationale. No separate form, no feedback tool — a comment on the thing being discussed.

## 4. The improver skill runs on its schedule

Running in Warp's internal agent orchestration platform (Oz) as a scheduled "update triage"
agent, the outer skill:

1. authenticated to GitHub,
2. ran a bundled Python script to pull recent issues with feedback,
3. summarized the findings into JSON,
4. identified the concrete signals in them.

## 5. The smallest edit is proposed

It proposed the smallest edit that captured the feedback: apply **`ready to spec`** when an issue
describes a real problem despite undefined UI/UX details.

## 6. A human approves the merge

The update moved through the standard code-review workflow. The PR arrived with explanations of
which signals prompted which changes. After human review and approval, the merged change became
inherited knowledge for the next run of the triage skill — keeping humans in control of actual
system changes.

## 7. Repeat across agents

Warp now runs this pattern across its open-source repo, with separate spec-writing, review, and
triage agents, each carrying its own self-improvement loop.

## Source

- https://claude.com/blog/how-warp-builds-self-improving-agents-on-claude (published 2026-08-26)
