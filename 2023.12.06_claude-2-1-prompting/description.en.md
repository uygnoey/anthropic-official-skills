**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

## What is this post?
This post describes a simple long-context prompting tweak for Claude 2.1 that improves retrieval accuracy in “needle-in-a-haystack” style tasks.

## When is it useful?
Use it when you provide a long document (up to ~200K tokens) and need the model to answer based on a specific sentence that may be out of place or injected.

## Key points
- Claude 2.1 has a 200K-token context window and strong long-document retrieval.
- The model can be reluctant to answer based on a single out-of-place sentence.
- Adding a short instruction to begin the response with “Here is the most relevant sentence in the context:” significantly improves accuracy.

## Bundled resources
- Skill: long-context-needle-finding
- Prompt template: response-leading sentence for needle finding

## Source
- https://claude.com/blog/claude-2-1-prompting
