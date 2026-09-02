# Memory data handling

Long-term memory turns a commerce agent into a system that holds personal data about a person
across sessions. Four requirements follow.

## 1. Decide what types you retain — and enforce it in code

Choose the categories of fact the deployment is allowed to keep. Enforce the decision **at the
write path with a validator**. A prompt instruction telling the extractor what not to save is not
enforcement; a validator that rejects an out-of-policy category is.

## 2. Give users control of their own facts

Provide a user-facing interface to:

- **view** what is stored,
- **correct** a wrong fact,
- **delete** a fact.

## 3. Set retention periods

Preferences age out. Attach a retention period per category and expire records on it, rather than
keeping everything forever by default.

## 4. Make memory a per-deployment toggle

Jurisdictions differ. The same agent should be able to run with memory fully off, so compliance
is a deployment setting rather than a code fork.

## The extraction boundary

The extraction prompt reads **only user and assistant text**. Tool results are excluded, so
catalog copy, review text and seller messages cannot become facts about the user. This is both a
quality rule and a safety rule — untrusted third-party content reaching the memory writer is an
injection path.

Stored memory itself counts as untrusted input on the way back in, and passes through the
sanitizer with everything else. See the `commerce-agent-safety-harness` skill.

## Source

- https://claude.com/blog/the-anatomy-of-effective-commerce-agents
