**English** · [한국어](./firm-wide-ai-deployment.ko.md) · [Español](./firm-wide-ai-deployment.es.md) · [日本語](./firm-wide-ai-deployment.ja.md)

# Deploying AI across an entire firm

A guide to the shape of a firm-wide AI deployment, drawn from Bain & Company's rollout of
Claude to all 19,000 of its employees, announced when Bain joined the Claude Partner Network
as a Global Premier partner.

The announcement is a partnership announcement, but the deployment described inside it is
the useful part. It has four properties worth copying: a set of surfaces rather than a single
tool, a pilot that produced an adoption number before the broad launch, an enablement and
governance wrapper shipped with the launch rather than after it, and a client-facing target
chosen because of where the bottleneck actually sits.

## Deploy a surface set, not a tool

Claude reached employees through Claude.ai, Claude Cowork, Claude Code, Claude for Excel,
and Claude for Microsoft 365.

Read down that list and the logic is visible: a general chat surface, an agentic work
surface, an engineering surface, a spreadsheet surface, and the document-and-mail surface
that everyone already has open all day. Three of the five put the model inside a tool the
population was already using.

The single per-surface adoption number reported carries the lesson. More than two-thirds of
pilot participants took up Claude for Excel — the surface embedded in the tool a consulting
firm's analytical work actually happens in.

The implication for planning: map populations to surfaces before mapping them to licences.
A chat window handed to an entire organization gets adoption from the people who were
already going to adopt.

## Make the pilot produce a number

The reported figure is that more than 7,000 employees were actively using Claude within
weeks of the firm-wide deployment.

Two things about that number matter more than its size. It measures **active use**, not
accounts provisioned. And it is bounded by a short window, which makes it a statement about
uptake velocity rather than about eventual reach.

Design the pilot to produce exactly that: a cohort, a window, and a count of people actively
using each surface at the end of it. That number is what justifies the general-availability
decision and what every later cohort gets compared against.

## Ship enablement and governance with the launch

The implementation included onboarding materials, training sessions, webinars, expert
support, and governance structures, with user experience tracked through ongoing surveys and
feedback collection.

Treat those five as part of the launch, not as follow-up. A practical build order:

1. **Governance structures.** Data rules stated per surface, a position on what may be used
   in client-facing work, a named owner for new-surface decisions, and an escalation path.
   Governance written after launch is governance written in response to an incident.
2. **Onboarding materials.** One page per surface, with a role-specific first task rather
   than a feature tour, completable without booking time with anyone.
3. **Training sessions.** Live, role-segmented, hands-on, using the organization's own work
   as exercise material. Re-run for each cohort.
4. **Webinars.** Breadth and cadence. Record them; the recording becomes onboarding material.
5. **Expert support.** A staffed channel, routed by surface. Its second job is diagnostic —
   what arrives repeatedly is the gap in items 2 and 3.

And then keep the surveys running. A launch survey measures the launch; a recurring one tells
you whether adoption is holding and which surface is carrying it.

## Point it at work where context has been lost

The client-facing result reported is productivity gains of 30% to 50% across multiple
engagements involving complex legacy codebases — specifically ones lacking architectural
context.

That is a deliberate target, not a convenient one. The expensive part of such work is not
volume; it is that nobody holds the understanding any more and it has to be reconstructed
before anything can be changed. That reconstruction is what a model able to read an entire
codebase is unusually good at.

The transferable rule: choose the first serious workstream because its bottleneck is lost
context, not because it has a lot of repetitive work in it. Throughput problems yield modest,
linear gains. Context-recovery problems are where the large numbers come from.

## Budget for the deployment expertise

The partnership organizes client work around AI strategy, technology modernization, and
AI-enabled operations, staffed by more than 1,500 AI, data, analytics, architecture, and
engineering experts working alongside Bain's industry and capability practices.

Anthropic's Steve Corfield, Global Head of Business Development, read the speed and breadth
of Bain's adoption as a signal of what becomes possible when technology is paired with the
expertise to deploy it effectively. Bain's Philippe d'Arabian, EVP and Global Head of
Partnerships, described the partnership as combining frontier AI technology with strategic
and industry expertise to turn AI's potential into business results.

The planning consequence is unglamorous but real: model capability is not the scarce input.
Deployment capability is, and it has to be resourced — from inside the organization, from a
partner, or from both.

## Source

- https://claude.com/blog/bain-company-joins-the-claude-partner-network-as-a-global-premier-partner (August 25, 2026)
