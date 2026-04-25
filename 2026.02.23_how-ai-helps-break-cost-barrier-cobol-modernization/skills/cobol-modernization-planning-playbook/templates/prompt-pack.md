# Prompt pack — COBOL modernization mapping and planning

These prompts are derived from the post’s described workflow (mapping → risk assessment → planning → tests → incremental execution).

## 1) Codebase mapping prompt
"Read this COBOL codebase and produce a structured map that includes: (1) program entry points, (2) execution paths across called subroutines, (3) data flows between modules, and (4) dependencies spanning hundreds of files. Go beyond a call graph: explicitly identify implicit dependencies created by shared data structures, file operations that create coupling, and initialization sequences that affect runtime behavior."

## 2) Risk and candidate identification prompt
"Using the codebase map, annotate the system with: (a) high-coupling modules that are risky to modernize early, (b) isolated components that are good early candidates, (c) duplicated logic that suggests refactoring opportunities, and (d) areas of accumulated technical debt that could create migration surprises."

## 3) Roadmap sequencing prompt
"Propose an initial component-by-component modernization sequence based on the risks, dependencies, and complexity you identified. For each step, explain why it should be early vs. late."

## 4) Testing and validation prompt
"Draft functional tests that verify the migrated implementation produces identical outputs to the legacy COBOL for the chosen component. List assumptions, required fixtures, and how to compare outputs. Also propose performance benchmarks to ensure the modernized component meets requirements."

## 5) Incremental execution prompt
"For the next component in the roadmap, propose an incremental migration plan: (1) translation approach, (2) API wrapper strategy for any legacy component that remains, (3) scaffolding to run old and new side-by-side during transition, and (4) validation gates for output equivalence and performance."

## Source
- https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization
