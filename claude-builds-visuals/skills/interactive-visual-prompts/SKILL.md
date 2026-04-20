---
name: interactive-visual-prompts
description: Helps the user prompt Claude to generate and iteratively refine temporary, inline interactive visuals (charts, diagrams, and visualizations) during a conversation. Trigger when the user asks to draw a diagram, visualize a trend over time, or wants an explanation supported by interactive visuals.
---

# Prompting Claude for Inline Interactive Visuals

Claude can create temporary, inline interactive charts, diagrams, and visualizations as part of a conversation to support understanding.

## Instructions
1. State the concept or dataset you want explained.
2. Ask explicitly for a visual when needed (for example: “draw this as a diagram” or “visualize how this might change over time”).
3. After the visual appears, request specific adjustments (labels, axes, layout, additional variables) or ask to explore the topic more deeply.
4. Continue iterating, treating the visual as part of the conversational flow.

## Examples
- “Explain compound interest, and visualize the growth curve so I can explore it.”
- “Show me the periodic table as an interactive visualization where I can click an element to see details.”
- “Draw this as a diagram: A → B → C, where B depends on A, and C depends on both.”
- “Visualize how this might change over time, then adjust it to include a second scenario.”

## Tips
- If the first visual is not what you intended, describe the specific change you want (e.g., “make the x-axis monthly” or “turn this into a flowchart”).
- Expect visuals to be temporary and to evolve as the conversation continues.

## Human-readable descriptions
This skill is summarized for humans in [../../description.en.md](../../description.en.md) and [../../description.ko.md](../../description.ko.md).

## Source
Distilled from [Claude builds interactive visuals right in your conversation](https://claude.com/blog/claude-builds-visuals) (published 2026-03-12).
