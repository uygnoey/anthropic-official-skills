**English** · [한국어](./built-in-browser-rollout.ko.md) · [Español](./built-in-browser-rollout.es.md) · [日本語](./built-in-browser-rollout.ja.md)

# Rolling out the built-in browser in Cowork

## What shipped

Claude now has a browser built into Claude Cowork on the desktop app. When a task needs to use a
website, a browser opens in the side panel and Claude navigates webpages, reads them, clicks, and
types.

This is a browser of Claude's own — not your browser. It stays separate from your personal
browsing, and Claude never sees your tabs, bookmarks, or passwords.

## Who gets it, and when

- **Pro, Max, and Team:** rolling out through the week on macOS, Windows, and Linux (beta).
- **No setup required.** Give Claude a task that needs the web and the browser opens in the side
  panel.
- **Enterprise:** admins can enable it right away under **Organization settings → Cowork → Built-in
  browser**.

## Where the browser runs

The browser lives in the desktop app. Web and mobile can use it while the desktop app is open and
connected. Web-only users without the desktop app continue with Claude in Chrome.

Plan around that: a workflow that depends on the built-in browser needs a desktop app running
somewhere, even when the person driving it is on the web or on a phone.

## Choosing a default browser

Cowork now has two ways to act on the web, and the default switches based on whether you already
use Claude in Chrome. Set it explicitly under **Settings → Cowork → Preferred browser**.

Guidance from the announcement:

- **Built-in browser** — for web tasks that should run while you stay productive elsewhere:
  gathering research, collecting invoices from vendor portals.
- **Claude in Chrome** — for pages you already have open and are signed into: updating a CRM,
  working through an inbox, editing a document.

## Setting up logins

The built-in browser starts with no sessions. Logins are imported site by site:

- **macOS:** from Chrome, Edge, or Firefox.
- **Windows and Linux:** from Firefox.

Banking, email, and SSO sites are excluded by default unless explicitly included. Keeping that
default is the simplest way to bound what a browser task can reach.

## Safety posture

The built-in browser is exposed to prompt injection — hidden instructions in a page that try to
redirect Claude. It has the same safeguards as Claude in Chrome, including checks that actions
match the user's request. These meaningfully reduce the risk but can't eliminate it.

Start with websites you trust. Further guidance is in the safety documentation referenced by the
announcement.

## A rollout checklist

1. Confirm the platform: macOS, Windows, or Linux (beta), with the desktop app installed.
2. For an organization, enable it under Organization settings → Cowork → Built-in browser.
3. Set the preferred browser under Settings → Cowork → Preferred browser rather than accepting the
   inferred default.
4. Import only the logins the first tasks need; leave banking, email, and SSO excluded.
5. Start with trusted sites and low-consequence tasks — research gathering, invoice collection —
   before widening.

## Source

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
