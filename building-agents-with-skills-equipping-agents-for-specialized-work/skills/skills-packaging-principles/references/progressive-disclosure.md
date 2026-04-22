# Progressive disclosure (from the post)

The post describes a three-tier loading approach:

- Metadata (YAML `name` + `description`) is shown first and is small enough to keep many skills discoverable.
- If needed, the full `SKILL.md` is read.
- For deeper detail, reference files (e.g., in `references/`) can be loaded on demand.

It also gives rough token sizing examples: metadata ~50 tokens, SKILL.md ~500 tokens, and reference files 2,000+ tokens.
