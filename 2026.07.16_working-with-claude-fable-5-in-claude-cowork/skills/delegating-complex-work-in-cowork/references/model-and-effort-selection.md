# Choosing a model and an effort level in Claude Cowork

## The model choice

Claude Fable 5 is not the default in Claude Cowork — you have to select it. As of the post's
publication (July 16, 2026) the default is Claude Sonnet 5.

| Model | Fits | Signals |
| --- | --- | --- |
| **Claude Sonnet 5** (default) | Everyday tasks | Work you would handle yourself in a quick pass |
| **Claude Opus** | Deep work with a clear shape | You already know what the end result looks like |
| **Claude Fable 5** | The most complex or ambiguous projects | Multiple tools, a series of judgment calls, may have been out of reach for prior models |

Fable 5 spends more time thinking and more of your usage limits. That trade is worth it on work that
is time-consuming or costly to get wrong. The post's recommendation: reserve it for your most
important work, especially jobs that use multiple tools and require a series of judgment calls.

## The effort setting

Effort tunes the choice further, independent of which model you picked.

**Higher effort** — Claude plans more before it kicks off a job and checks in more throughout the run.
Keep effort high for complex or multi-step projects you expect Claude to complete from beginning to
end.

**Lower effort** — a faster response that still takes advantage of frontier intelligence. Consider it
for tasks that need frontier judgment but not deep exploration:

- agentic runs made of many easy steps
- work where the result is easy for Claude to check

In Anthropic's testing, Claude Fable 5 at lower effort often matched or exceeded the performance of
earlier models at their highest effort levels.

The post points to a companion explanation of how model choice and effort interact in Claude Code for
a more detailed look under the hood.

## Safety classifiers and the Opus 4.8 fallback

Claude Fable 5 ships with a new set of classifiers: separate AI systems that detect potential misuse
in requests related to cybersecurity or to biology and chemistry.

What happens when one triggers:

1. The response is automatically handled by **Claude Opus 4.8** instead.
2. You are informed whenever this occurs.
3. The chat **stays on Opus from there** — start a new conversation to get back to Fable 5.

Opus 4.8 is a highly capable model in its own right. The safeguards were tuned conservatively so a
Mythos-class model could be released for general use both safely and quickly, which means they will
sometimes catch harmless requests — including phrases in Claude Cowork that only touch on related
topics. Anthropic says it is working to reduce these false positives as the safeguards are refined.

## Usage notes

- Claude reads the whole conversation again with every new message, so a long conversation may use
  more of your usage. Start new tasks in a fresh conversation.
- Scheduled tasks count toward your limit too. Check yours occasionally and turn off any you no longer
  need.

## Source

[Working with Claude Fable 5 in Claude Cowork](https://claude.com/blog/working-with-claude-fable-5-in-claude-cowork)
— Josefina Albert, July 16, 2026.
