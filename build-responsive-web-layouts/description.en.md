**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Build responsive web layouts

## What is this post?
This post explains how to use Claude (especially Claude Code) to generate and refactor responsive web layouts so they behave well across a wide range of viewport sizes.

## When is it useful?
- When fixed widths and rigid layout rules cause overflow or unreadable layouts on tablets and phones.
- When you want to move from manual breakpoint iteration to more systematic, test-backed responsive refactors.

## Key points
- Claude Code can scan existing stylesheets, identify rigid layout constraints, and replace them with flexible alternatives (e.g., max-width, flex-basis, auto-fit grid patterns).
- Add targeted media queries for breakpoints and validate behavior at small viewports (e.g., 320px, 512px) to prevent horizontal overflow.
- Generate Playwright tests to validate responsive behavior across common device sizes.

## Bundled resources
- Skill: `responsive-layout-refactor` (instructions, example prompts, example snippets)

## Source
- https://claude.com/blog/build-responsive-web-layouts
