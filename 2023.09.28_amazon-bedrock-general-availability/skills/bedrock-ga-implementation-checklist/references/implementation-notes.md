# Implementation notes (Bedrock GA announcement)

Decision points to record as you adopt Claude via Amazon Bedrock.

## Access and operations
- Which teams/projects will use Bedrock for Claude access?
- Which environments (dev/staging/prod) need model access?

## Agentic orchestration
- If using agentic workflows, define actions as callable functions (for example, AWS Lambda functions).
- Specify permissions boundaries and auditing for action execution.

## Customization
- Determine whether customization or fine-tuning is needed.
- Establish evaluation criteria for output quality and safety.

## Source
- https://claude.com/blog/amazon-bedrock-general-availability
