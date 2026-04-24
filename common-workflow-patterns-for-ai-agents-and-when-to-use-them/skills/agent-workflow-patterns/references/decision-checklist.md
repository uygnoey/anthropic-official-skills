# Workflow pattern decision checklist

Use this checklist to decide whether you need a workflow at all, and if so which pattern.

## 1) Do you need a workflow?
- Can a single agent handle this task effectively?
  - If yes, do not add orchestration.
  - If no, identify what fails: dependency, latency, or quality.

## 2) If the task has dependencies
Choose **Sequential**.
- Does step B require step A’s output?
- Are you building a multi-stage pipeline (extract → validate → load, draft → review → polish)?

## 3) If the task is decomposable into independent subtasks
Choose **Parallel**.
- Can subtasks run without sharing intermediate context?
- Is wall-clock latency the bottleneck?
- What is your aggregation strategy (vote, merge, best-of, specialized arbiter)?

## 4) If the task needs higher quality than a single pass
Choose **Evaluator–optimizer**.
- Can you write explicit evaluation criteria?
- What are your stopping conditions (max iterations, quality threshold)?
- Is the quality gain worth the extra tokens and latency?

## Source
- https://claude.com/blog/common-workflow-patterns-for-ai-agents-and-when-to-use-them
