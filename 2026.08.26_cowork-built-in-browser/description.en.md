**English** · [한국어](./description.ko.md) · [Español](./description.es.md) · [日本語](./description.ja.md)

# Claude gets its own browser in Cowork

## What is this post?

A product announcement: Claude Cowork on the desktop app now has a browser of its own. When a task
needs a website, a browser opens in the side panel and Claude navigates pages, reads them, clicks,
and types. The post explains how this browser differs from Claude in Chrome, which one to reach for
in which situation, how logins can be imported site by site, what protects the session against
prompt injection, and how the rollout works for paid plans and enterprise admins.

## When is it useful?

- A web task should run on its own while you keep working in another window.
- You are deciding between the built-in browser and Claude in Chrome for a given piece of work.
- You want an agent to reach a site without exposing your personal tabs, bookmarks, or passwords.
- You are an enterprise admin who needs to turn the built-in browser on for an organization.

## Key points

- **A browser inside the desktop app.** When a task needs a website, a browser opens in the side
  panel and Claude navigates webpages, reads them, clicks, and types.
- **Separate from your personal browsing.** Claude never sees your tabs, bookmarks, or passwords.
- **Logins are imported site by site**, from Chrome, Edge, or Firefox on macOS, and from Firefox on
  Windows and Linux. Banking, email, and SSO sites are excluded by default unless you explicitly
  include them.
- **Use the built-in browser** for web work that should run while you stay productive elsewhere —
  gathering research, collecting invoices from vendor portals.
- **Use Claude in Chrome** for pages you already have open and are signed into — updating a CRM,
  working through an inbox, editing a document.
- **The default depends on your history.** It switches based on whether you already use Claude in
  Chrome, and you can choose manually in Settings → Cowork → Preferred browser.
- **Prompt injection is the risk.** Hidden instructions in a page try to redirect Claude. The
  built-in browser carries the same safeguards as Claude in Chrome, including checking actions
  against what you asked for. These meaningfully reduce the risk but can't eliminate it — start
  with websites you trust.
- **Rollout.** Through the week for Pro, Max, and Team on macOS, Windows, and Linux (beta); no
  setup needed beyond giving Claude a web task. Enterprise admins can enable it right away under
  Organization settings → Cowork → Built-in browser.
- **The browser lives on the desktop.** Web and mobile can use it while the desktop app is open and
  connected; without the desktop app, web-only users stay with Claude in Chrome.

## Bundled resources

- `skills/desktop-browser-routing/SKILL.md` — choosing between the built-in browser and Claude in
  Chrome, and working safely in either.
- `skills/desktop-browser-routing/references/browser-choice.md` — the two browsers side by side.
- `skills/desktop-browser-routing/references/logins-and-safety.md` — login import scope and the
  prompt-injection posture.
- `guides/built-in-browser-rollout.{en,ko,es,ja}.md` — rollout, admin enablement, and setup.

## Source

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
