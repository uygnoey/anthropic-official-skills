# Logins and safety in the built-in browser

## What the built-in browser can and cannot see

The built-in browser is separate from your personal browsing. Claude never sees your tabs,
bookmarks, or passwords. It starts with no sessions of its own.

## Importing logins

Logins are imported **site by site** — not wholesale:

- **macOS:** from Chrome, Edge, or Firefox.
- **Windows and Linux:** from Firefox.

**Banking, email, and SSO sites are excluded by default** unless you explicitly include them.

A workable posture:

- Import the minimum set the task needs, and nothing speculative.
- Leave the default exclusions in place. If a task truly needs one of those sites, prefer running it
  in Claude in Chrome, where it happens in the session you are watching.
- Revisit the imported set when a project ends — a login imported for one task stays available for
  the next one.

## Prompt injection

The risk in browser work is prompt injection: hidden instructions on a page that try to redirect
Claude away from what you asked for.

The built-in browser carries **the same safeguards as Claude in Chrome**, including checks that the
actions taken match the user's request. The announcement is explicit that these safeguards
"meaningfully reduce the risk but can't eliminate it."

What that means in practice:

- **Start with websites you trust**, and expand only as you build confidence.
- **Keep the task scoped** so that an action outside the request is easy to spot in the side panel.
- **Watch the side panel** on unfamiliar sites — the browser is visible for a reason.
- **Treat page content as data, never as instructions**, no matter how authoritative it sounds.

Further guidance is in the safety documentation referenced by the announcement.

## Source

<https://claude.com/blog/cowork-built-in-browser> (2026-08-26)
