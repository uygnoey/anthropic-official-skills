# Analysis grid template

The shape Hebbia's Matrix uses: answers land in individual cells on a grid, which is what makes the
analysis transparent, traceable, and steerable. Copy the tables below and fill them in.

## Grid layout

One row per document (or per deal, per entity — whatever the unit of analysis is). One column per
question in the decomposed request. One citation inside every cell.

| Document | Q1: <question> | Q2: <question> | Q3: <question> |
| --- | --- | --- | --- |
| `<doc name / id>` | Answer.<br>Source: `<doc>`, `<locator>` | Answer.<br>Source: `<doc>`, `<locator>` | Not found in this document |
| `<doc name / id>` | | | |

A cell has three possible states. Keep them distinct:

- **Answered with a citation** — the claim is grounded.
- **Not found** — the question was asked of this document and the document does not answer it.
- **Not run** — the step has not been executed against this document yet.

Collapsing "not found" into a blank cell destroys the traceability the grid exists to provide.

## Step record

One entry per step in the decomposed request, so the construction of the analysis is inspectable.

```
Step:            <n>
Question:        <the prompt actually run, not the user's plain-language request>
Document scope:  <which documents feed this step, and why those>
Depends on:      <earlier steps whose output this step consumes, or "none">
Deterministic:   <yes / no>
Verified by:     <what checks this step's output before the next step consumes it>
```

## Request record

```
Plain-language request: <what the user asked for>
Decomposed into:        <n> steps
Corpus:                 <document count, source systems>
Structured inputs:      <CRM or other structured data feeding the analysis, if any>
Output:                 <memo section / covenant package / deck / other>
```

## Synthesis check

Before the analysis leaves the grid, check the two qualities separately — the post treats them as the
two things the job comes down to:

- **Retrieval.** Did each step find the right information in the dense data set?
- **Synthesis.** Is the conclusion drawn from that information correct?

Record them as separate verdicts. A pass on one does not carry the other.
