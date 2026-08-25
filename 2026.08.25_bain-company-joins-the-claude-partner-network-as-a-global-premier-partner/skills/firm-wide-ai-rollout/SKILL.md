---
name: firm-wide-ai-rollout
description: Plan and run a firm-wide AI assistant rollout the way a professional-services firm does it — pick the surface set rather than a single tool, pilot before going broad, wrap the launch in enablement and governance, and measure adoption by active use within weeks instead of seats provisioned. Use when deploying an AI assistant across an entire workforce, when a pilot needs to be turned into a general availability plan, when adoption has stalled after licences were handed out, or when a delivery organization wants its internal deployment to become the basis for client-facing work.
---

# Firm-wide AI rollout

A rollout method drawn from Bain & Company's deployment of Claude to all 19,000 of its
employees, announced alongside its joining the Claude Partner Network as a Global Premier
partner. The deployment is interesting less for its size than for its shape: a suite of
surfaces rather than one tool, a pilot that produced a real adoption number before the
firm-wide launch, and an enablement-and-governance wrapper treated as part of the product
rather than as follow-up.

The reported result of the pilot phase — more than 7,000 employees actively using Claude
within weeks — is the metric worth copying. It is a statement about active use over a short
window, not about provisioned accounts.

## Instructions

### 1. Choose a surface set, not a tool

The deployment covered Claude.ai, Claude Cowork, Claude Code, Claude for Excel, and Claude
for Microsoft 365. Each of those meets a different population where it already works: the
chat surface for general knowledge work, Cowork for agentic delivery work, Code for
engineering, Excel for the modelling work that consultants live in, and Microsoft 365 for
the document and mail surface everyone already has open.

Map your own populations to surfaces before you map them to licences. A single chat surface
handed to an entire firm gets adoption from the people who were already going to adopt.

The one adoption number reported by function is that more than two-thirds of pilot
participants took up Claude for Excel. Treat that as the general lesson: the surface that
sits inside the tool a role already lives in is the one that converts.

### 2. Pilot to produce a number, then go broad

Run the pilot as a measurement exercise with a deadline, not as an open-ended trial. The
question it answers is how many people are *actively* using the tool after a few weeks —
that number is what justifies the firm-wide launch and what you compare later cohorts
against.

### 3. Ship enablement as part of the launch

The reported enablement wrapper had five parts: onboarding materials, training sessions,
webinars, expert support, and governance structures. Build all five before general
availability, not after the first quiet month. See
[references/enablement-and-governance.md](references/enablement-and-governance.md) for what
each one covers and the order to build them in.

### 4. Instrument the feedback loop

User experience was tracked through ongoing surveys and feedback collection. "Ongoing" is
the operative word: a launch survey tells you about the launch, while a recurring one tells
you where adoption is decaying and which surface is carrying the weight.

### 5. Point the capability at the work that resists

The client-facing outcome reported is productivity gains of 30% to 50% across multiple
engagements involving complex legacy codebases — specifically codebases lacking
architectural context. That is a deliberate choice of target: the work where the bottleneck
is reconstructing lost understanding, which is exactly what a model that can read the whole
codebase is good at.

Pick the equivalent inside your own organization: work that is expensive because the context
has been lost, not work that is expensive because there is a lot of it.

### 6. Pair technology with delivery capability

The partnership itself is organized around three areas — AI strategy, technology
modernization, and AI-enabled operations — and is staffed by more than 1,500 AI, data,
analytics, architecture, and engineering experts working alongside industry and capability
practices.

The structural point for anyone planning a rollout: capability alone does not produce
outcomes. Anthropic's Steve Corfield framed the speed and breadth of Bain's adoption as a
signal of what happens when technology is paired with the expertise to deploy it
effectively. Budget for the deployment expertise, whether it comes from inside or from a
partner.

Use [templates/rollout-plan.md](templates/rollout-plan.md) to record the plan and its
checkpoints.

## Examples

A worked walkthrough of the Bain rollout as reported —
surface set, pilot numbers, enablement wrapper, and client outcome — is in
[examples/bain-rollout.md](examples/bain-rollout.md).

**Turning a stalled pilot into a firm-wide launch.** Licences went out six months ago and
usage is flat. Applying step 2: the pilot never produced an active-use number, so there is
nothing to defend a broader launch with. Re-run it as a bounded cohort with a defined
window, and report active users rather than provisioned seats. Applying step 1: check
whether the cohort was given a chat surface only, and whether the role-specific surface —
the spreadsheet, the IDE, the mail client — was ever deployed.

**Choosing the first client-facing engagement.** Two candidate workstreams: a large volume
of routine ticket triage, and a modernization of a legacy system nobody currently
understands. Step 5 points at the second. The reported 30–50% gains came from codebases
lacking architectural context, where the model's contribution is reconstructing the
understanding rather than adding throughput.

**Sequencing the enablement build.** A launch date is set for six weeks out and only
onboarding docs exist. The reference file orders the five components by what blocks a
launch: governance structures and onboarding materials are prerequisites, training and
webinars scale the launch, and expert support catches what the first two miss.

## Source

- https://claude.com/blog/bain-company-joins-the-claude-partner-network-as-a-global-premier-partner (August 25, 2026)
