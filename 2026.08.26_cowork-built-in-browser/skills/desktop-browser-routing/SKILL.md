---
name: desktop-browser-routing
description: Choose between the browser built into Cowork on the desktop app and Claude in Chrome for a given web task, and work safely in either one. Use when a web task should run on its own while you keep working elsewhere, when the work belongs on pages you already have open and signed into, when deciding which logins to import into the built-in browser, or when weighing the prompt-injection risk of letting an agent act on a website.
---

# Desktop browser routing

Cowork on the desktop app has a browser of its own. When a task needs a website, a browser opens in
the side panel and Claude navigates webpages, reads them, clicks, and types. That browser is
separate from your personal browsing — Claude never sees your tabs, bookmarks, or passwords.

Claude in Chrome remains the other option: it works inside the browser you are already using, with
the pages and sessions you already have open.

Routing a task to the wrong one wastes the strength of both. This skill covers the choice, the
login setup that makes the built-in browser usable, and the safety posture that applies either way.

## Instructions

### 1. Route by where the work lives

Ask one question first: does this task need the pages you already have open, or can it start from a
blank browser?

- **Starts from nothing, runs on its own → built-in browser.** Web work that should proceed while
  you stay productive elsewhere: gathering research, collecting invoices from vendor portals. It
  opens in the side panel, so the task is visible without taking over your screen.
- **Depends on pages you are already in → Claude in Chrome.** Work on pages you have open and are
  signed into: updating a CRM, working through an inbox, editing a document.

See [references/browser-choice.md](references/browser-choice.md) for the two side by side.

### 2. Set the preferred browser deliberately

The default switches based on whether you already use Claude in Chrome. Don't leave that to
inference if your work has a clear centre of gravity — choose it under
**Settings → Cowork → Preferred browser**.

### 3. Import only the logins the task needs

The built-in browser starts with no sessions. Logins are imported site by site, from Chrome, Edge,
or Firefox on macOS, and from Firefox on Windows and Linux.

Banking, email, and SSO sites are excluded by default. Treat that default as the policy rather than
a speed bump: include such a site only when the task genuinely cannot proceed without it, and
prefer running that task in Claude in Chrome under your own eyes instead.

### 4. Assume page content may be hostile

The risk in any browser task is prompt injection — hidden instructions in a page trying to redirect
Claude. The built-in browser carries the same safeguards as Claude in Chrome, including checking
actions against what you actually asked for. These meaningfully reduce the risk but can't eliminate
it.

Practical consequences:

- Start with websites you trust, and widen from there.
- Scope the task narrowly enough that an off-request action is obvious when you glance at the side
  panel.
- Keep the highest-consequence sites out of the imported set, per step 3.

Details in [references/logins-and-safety.md](references/logins-and-safety.md).

### 5. Know where the browser actually runs

The browser lives in the desktop app. Web and mobile can use it while the desktop app is open and
connected. Without the desktop app, web-only users stay with Claude in Chrome — so a task planned
around the built-in browser needs the desktop app running somewhere.

## Examples

**Collecting invoices from vendor portals.** Nothing is open, the work is repetitive, and you want
to keep writing in another window. Built-in browser, with only the vendor portal logins imported.

**Research sweep across public pages.** No sign-in required at all, so no import is needed. Built-in
browser; start with sources you already trust.

**Updating records in a CRM you have open.** The session, the filters, and the current view are all
already in your Chrome window. Claude in Chrome.

**Working through an inbox.** Email is excluded from login import by default, and the pages are ones
you are already signed into. Claude in Chrome.

**Editing a document in a web editor.** The document is open and mid-edit. Claude in Chrome.

**Enabling the feature for a team.** An admin turns it on under Organization settings → Cowork →
x

## Source

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
