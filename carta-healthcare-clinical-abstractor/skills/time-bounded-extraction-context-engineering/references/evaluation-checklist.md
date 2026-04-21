# Evaluation checklist (prompt vs context vs retrieval)

Use this checklist to debug failures in time-bounded extraction.

## 1) Prompt wording
- Is the target field definition unambiguous?
- Is the time boundary stated as a concrete timestamp?
- Did you explicitly instruct the model to exclude post-boundary values?
- Did you require evidence quotes and timestamps in the output?

## 2) Context assembly
- Did you include the most time-adjacent documentation around the boundary?
- Did you include the right document types (notes vs vitals vs labs)?
- Is the context ordered so relevant evidence appears early?
- Did you exclude distracting post-event notes that could confuse selection?

## 3) Retrieval gaps
- Is the needed evidence missing from the retrieved snippets?
- Are timestamps normalized correctly (timezones, formats, missing date)?
- Are there multiple systems/locations where the value could be documented?

## 4) Human feedback loop
- Can expert reviewers describe why the correct value is elsewhere?
- Did you capture that explanation and encode it as a rule for context selection?

## 5) Transparency
- Can a reviewer validate the answer from the shown evidence alone?

## Source
Derived from engineering lessons in: https://claude.com/blog/carta-healthcare-clinical-abstractor
