---
name: cobol-modernization-planning-playbook
description: A structured workflow for using AI assistance (e.g., Claude Code) to map, plan, test, and execute incremental COBOL modernization with human review and stepwise validation.
---

# COBOL Modernization Planning Playbook

## Instructions
Use this skill to turn a large, poorly documented COBOL codebase into an actionable modernization plan, then execute migration incrementally with up-front validation.

### 1) Map the codebase (build a shared understanding)
1. Ask the AI to read the whole codebase and produce:
   - Program entry points
   - Execution paths across called subroutines
   - Data flows between modules
   - Dependencies spanning hundreds of files
2. Require the mapping to include **implicit dependencies** that often hide in:
   - Shared data structures
   - File operations that create coupling
   - Initialization sequences that affect runtime behavior

### 2) Assess modernization risk and candidates
Ask the AI to annotate the map with:
- High-coupling modules that are risky to change early
- Isolated components that are good early candidates
- Duplicated logic (refactoring opportunities)
- Areas of accumulated technical debt (migration risk)

### 3) Plan a roadmap with human decision-making
1. Have the AI propose an initial sequence of components to modernize based on risk, dependencies, and complexity.
2. Your team reviews and finalizes priorities based on:
   - Business value
   - Technical risk
   - Organizational constraints
3. Define at this stage (with human ownership):
   - Target architecture
   - Code standards
   - Integration requirements

### 4) Define testing and validation before changes
1. Ask the AI to draft functional tests that confirm migrated code produces identical outputs to the legacy COBOL.
2. Decide with subject-matter experts:
   - Which business scenarios require manual validation
   - Performance benchmarks the modernized components must meet

### 5) Execute incrementally with side-by-side validation
For each component:
- Translate COBOL logic into the target language
- Create API wrappers around legacy components that remain in place
- Build scaffolding to run old and new code side by side during transition
- Validate at each step before proceeding

### 6) Start small
Start with a single component/workflow with clear boundaries and moderate complexity.

## Examples
- See: [COBOL modernization workflow checklist](./templates/modernization-workflow-checklist.md)
- See: [Prompt pack for mapping and planning](./templates/prompt-pack.md)
- See: [Example: component-by-component execution plan](./examples/component-execution-plan-example.md)

## Source
- https://claude.com/blog/how-ai-helps-break-cost-barrier-cobol-modernization
