---
name: responsive-layout-refactor
description: Identify rigid CSS layout constraints and refactor them into responsive patterns with breakpoint checks and device-coverage tests.
---

# Responsive Layout Refactor

## Instructions
Use this skill when a UI breaks across viewport sizes (overflow, collisions, unreadable grids, or navigation that doesn’t collapse).

1) **Audit for rigid constraints**
- Search for fixed widths/heights that don’t scale (e.g., `width: 1200px`, large fixed paddings, fixed column counts).
- Note layout systems in use (Flexbox, Grid, utility framework classes).

2) **Refactor to flexible patterns**
- Prefer `max-width` and fluid containers over fixed widths.
- For grids, prefer adaptive column definitions (e.g., `auto-fit` + `minmax`).
- For flex layouts, consider `flex-wrap` and fluid `flex-basis`.

3) **Add targeted breakpoint rules**
- Add media queries for tablet/desktop breakpoints where layout meaningfully changes.
- Keep base styles mobile-friendly by default.

4) **Validate at small viewports**
- Check at least 320px and 512px for horizontal overflow and readability.

5) **Add automated coverage tests**
- Generate a Playwright test plan covering representative device sizes (e.g., iPhone SE, iPhone 12, iPad, iPad Pro, Desktop).

## Examples
- See prompts: [templates/prompts.md](./templates/prompts.md)
- See snippet examples: [examples/snippets.md](./examples/snippets.md)
- See responsive checklist: [references/checklist.md](./references/checklist.md)

## Source
- https://claude.com/blog/build-responsive-web-layouts
