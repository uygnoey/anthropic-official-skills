# Responsive refactor checklist

- Replace fixed widths with `max-width` and fluid sizing.
- Prefer mobile-first base styles; add breakpoints only for meaningful changes.
- Check for horizontal overflow at 320px and 512px.
- Use adaptive grid patterns (e.g., `auto-fit`/`minmax`) where appropriate.
- Generate Playwright coverage across representative device sizes.
