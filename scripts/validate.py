#!/usr/bin/env python3
"""Validate every blog-slug folder at the repo root against Claude Code official specs.

Checks:
- Per post folder: description.{en,ko,es,ja}.md + source.json present.
- Each description file has a language-switcher line at the top.
- source.json has url, title, published_date, blog_slug.
- At least one of skills/, agents/, guides/, hooks/, output-styles/, plugin/ exists.
- SKILL.md: frontmatter name (regex ^[a-z0-9-]+$, <=64, no claude/anthropic),
  description (<=1024 chars), body contains ## Instructions and ## Examples,
  total body <=500 lines.
- agents/*.md: frontmatter name same rules; description present; body non-empty;
  filename stem == frontmatter name.
- guides/: each logical guide has .en.md AND .ko.md AND .es.md AND .ja.md,
  each starting with the language switcher.
- hooks/*.json: valid JSON with top-level "hooks" key whose value is an object.
- hooks/*.md: matching .md exists for each .json (same stem).
- output-styles/*.md: frontmatter name + description; body non-empty.
- plugin/: .claude-plugin/plugin.json with name + description + version.

Exit code 0 on pass, 1 on any failure. Prints all failures.
"""
from __future__ import annotations

import json
import os
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]+$")
RESERVED = {"claude", "anthropic"}
LANG_SWITCHER_LABELS = ("English", "한국어", "Español", "日本語")
LANGS = ("en", "ko", "es", "ja")


def load_frontmatter(path: Path) -> tuple[dict, str]:
    text = path.read_text(encoding="utf-8")
    if not text.startswith("---"):
        return {}, text
    parts = text.split("---", 2)
    if len(parts) < 3:
        return {}, text
    fm_raw, body = parts[1], parts[2]
    fm: dict = {}
    current_key: str | None = None
    for raw_line in fm_raw.splitlines():
        if not raw_line.strip():
            current_key = None
            continue
        if raw_line.startswith(" ") and current_key is not None:
            fm[current_key] = (fm[current_key] + " " + raw_line.strip()).strip()
            continue
        if ":" in raw_line:
            key, _, value = raw_line.partition(":")
            key = key.strip()
            value = value.strip()
            fm[key] = value
            current_key = key if value == "" else None if "\n" not in value else key
        else:
            current_key = None
    return fm, body


def check_name(name: str, ctx: str, errs: list[str]) -> None:
    if not name:
        errs.append(f"{ctx}: missing name")
        return
    if len(name) > 64:
        errs.append(f"{ctx}: name '{name}' exceeds 64 chars")
    if not NAME_RE.match(name):
        errs.append(f"{ctx}: name '{name}' fails ^[a-z0-9-]+$")
    lower = name.lower()
    for r in RESERVED:
        if r in lower:
            errs.append(f"{ctx}: name '{name}' contains reserved word '{r}'")


def has_lang_switcher(path: Path) -> bool:
    """Accept either linked form `[Label](...)` or bolded current-language form
    `**Label**` for each of the four language labels."""
    try:
        head = path.read_text(encoding="utf-8").splitlines()[:3]
    except Exception:
        return False
    joined = " ".join(head)
    for label in LANG_SWITCHER_LABELS:
        if f"[{label}]" not in joined and f"**{label}**" not in joined:
            return False
    return True


COMPANION_DIRS = ("scripts", "templates", "references", "assets", "examples", "prompts", "data")
_EXECUTABLE_EXTS = {".sh", ".bash", ".zsh", ".fish", ".py"}
# Markdown link: [label](relative/path). Ignore absolute urls and in-page anchors.
_MD_LINK_RE = re.compile(r"\[[^\]]+\]\(([^)\s]+)\)")
# Bare companion-dir reference in prose or code, e.g. `scripts/foo.py`, `templates/bar.md`.
_BARE_REF_RE = re.compile(
    r"(?<![/\w])(?:" + "|".join(COMPANION_DIRS) + r")/[\w./-]+"
)


def _is_external(path: str) -> bool:
    return (
        path.startswith("http://")
        or path.startswith("https://")
        or path.startswith("#")
        or path.startswith("mailto:")
    )


def _check_companions(base_dir: Path, body: str, ctx: str, errs: list[str]) -> None:
    """Ensure every local file or companion-dir path mentioned in the body exists.

    - Markdown links `[label](path)` with non-external targets must resolve to a real file
      inside or next to `base_dir` (paths escaping the containing folder are skipped).
    - Bare references like `scripts/foo.py`, `templates/bar.md`, `references/baz.md`
      inside prose or code blocks must also resolve.
    - Shell/Python scripts in executable extensions must be `chmod +x`.
    """
    seen: set[str] = set()
    base_root = base_dir.resolve()

    def _record(rel: str) -> None:
        if not rel or _is_external(rel):
            return
        clean = rel.split("#", 1)[0].split("?", 1)[0].strip()
        if not clean or clean.startswith("/"):
            return
        # Ignore pure language-switcher siblings (./description.en.md etc.) that
        # validators for those files already cover; they always exist when valid.
        if clean in seen:
            return
        seen.add(clean)
        target = (base_dir / clean).resolve()
        try:
            target.relative_to(base_root)
        except ValueError:
            return
        if not target.exists():
            errs.append(f"{ctx}: referenced companion file missing: {clean}")
            return
        if target.is_file() and target.suffix in _EXECUTABLE_EXTS:
            if not os.access(target, os.X_OK):
                errs.append(f"{ctx}: companion script '{clean}' is not executable (chmod +x)")

    for m in _MD_LINK_RE.finditer(body):
        _record(m.group(1))
    for m in _BARE_REF_RE.finditer(body):
        _record(m.group(0))


def validate_post(post: Path, errs: list[str]) -> None:
    ctx = post.name

    # descriptions (4 languages)
    for lang in LANGS:
        desc = post / f"description.{lang}.md"
        if not desc.exists():
            errs.append(f"{ctx}: missing description.{lang}.md")
        elif not has_lang_switcher(desc):
            errs.append(f"{ctx}/description.{lang}.md: missing language switcher on top")

    # source.json
    src = post / "source.json"
    if not src.exists():
        errs.append(f"{ctx}: missing source.json")
    else:
        try:
            meta = json.loads(src.read_text(encoding="utf-8"))
            for key in ("url", "title", "published_date", "blog_slug"):
                if key not in meta:
                    errs.append(f"{ctx}/source.json: missing '{key}'")
        except json.JSONDecodeError as e:
            errs.append(f"{ctx}/source.json: invalid JSON ({e})")

    # At least one artifact folder
    artifact_dirs = ["skills", "agents", "guides", "hooks", "output-styles", "plugin"]
    if not any((post / d).exists() for d in artifact_dirs):
        errs.append(f"{ctx}: no artifact folders present")

    # SKILL.md
    skills_dir = post / "skills"
    if skills_dir.exists():
        for skill_folder in sorted(skills_dir.iterdir()):
            if not skill_folder.is_dir():
                continue
            sk = skill_folder / "SKILL.md"
            sctx = f"{ctx}/skills/{skill_folder.name}/SKILL.md"
            if not sk.exists():
                errs.append(f"{sctx}: missing SKILL.md")
                continue
            fm, body = load_frontmatter(sk)
            check_name(fm.get("name", ""), sctx, errs)
            desc = fm.get("description", "")
            if not desc:
                errs.append(f"{sctx}: missing description")
            elif len(desc) > 1024:
                errs.append(f"{sctx}: description exceeds 1024 chars ({len(desc)})")
            lines = body.splitlines()
            if len(lines) > 500:
                errs.append(f"{sctx}: body exceeds 500 lines ({len(lines)})")
            if "## Instructions" not in body:
                errs.append(f"{sctx}: missing '## Instructions' section")
            if "## Examples" not in body:
                errs.append(f"{sctx}: missing '## Examples' section")
            # Companion files: every relative path mentioned in SKILL.md must exist.
            # Covers markdown links [label](path), bare paths like scripts/foo.py,
            # templates/bar.md, references/baz.md, etc.
            _check_companions(skill_folder, body, sctx, errs)

    # agents/*.md
    agents_dir = post / "agents"
    if agents_dir.exists():
        for agent in sorted(agents_dir.glob("*.md")):
            actx = f"{ctx}/agents/{agent.name}"
            fm, body = load_frontmatter(agent)
            check_name(fm.get("name", ""), actx, errs)
            if fm.get("name", "") and fm["name"] != agent.stem:
                errs.append(f"{actx}: filename stem != frontmatter name ('{fm['name']}')")
            if not fm.get("description"):
                errs.append(f"{actx}: missing description")
            if not body.strip():
                errs.append(f"{actx}: empty body")
            # Agents can reference companion material (prompts/, references/, etc.)
            _check_companions(agents_dir, body, actx, errs)

    # guides/ pairs in 4 langs
    guides_dir = post / "guides"
    if guides_dir.exists():
        stems: dict[str, set[str]] = {}
        for g in sorted(guides_dir.glob("*.md")):
            # filename: <stem>.<lang>.md
            parts = g.name.rsplit(".", 2)
            if len(parts) != 3 or parts[1] not in LANGS:
                errs.append(f"{ctx}/guides/{g.name}: filename must be <stem>.{{en,ko,es,ja}}.md")
                continue
            stem, lang = parts[0], parts[1]
            stems.setdefault(stem, set()).add(lang)
            gctx = f"{ctx}/guides/{g.name}"
            if not has_lang_switcher(g):
                errs.append(f"{gctx}: missing language switcher")
            # Guides can bundle references/, assets/, etc.
            _check_companions(guides_dir, g.read_text(encoding="utf-8"), gctx, errs)
        for stem, langs_present in stems.items():
            missing = set(LANGS) - langs_present
            if missing:
                errs.append(
                    f"{ctx}/guides/{stem}: missing language versions: {sorted(missing)}"
                )

    # hooks/
    hooks_dir = post / "hooks"
    if hooks_dir.exists():
        for hk in sorted(hooks_dir.glob("*.json")):
            hctx = f"{ctx}/hooks/{hk.name}"
            try:
                data = json.loads(hk.read_text(encoding="utf-8"))
            except json.JSONDecodeError as e:
                errs.append(f"{hctx}: invalid JSON ({e})")
                continue
            if "hooks" not in data or not isinstance(data["hooks"], dict):
                errs.append(f"{hctx}: missing top-level 'hooks' object")
            md_counterpart = hooks_dir / (hk.stem + ".md")
            if not md_counterpart.exists():
                errs.append(f"{hctx}: missing companion {hk.stem}.md notes")
            else:
                _check_companions(
                    hooks_dir,
                    md_counterpart.read_text(encoding="utf-8"),
                    f"{ctx}/hooks/{md_counterpart.name}",
                    errs,
                )
            # Scripts referenced from command strings must exist in the same hooks/ folder
            # (they can live under .claude/hooks/<name> in deployment, but here we want the
            # source of truth present next to the JSON).
            for event_entries in data.get("hooks", {}).values():
                if not isinstance(event_entries, list):
                    continue
                for entry in event_entries:
                    for inner in entry.get("hooks", []) if isinstance(entry, dict) else []:
                        if not isinstance(inner, dict):
                            continue
                        cmd = inner.get("command", "")
                        if not isinstance(cmd, str):
                            continue
                        # Look for a /<name>.<ext> reference to a script we should ship.
                        for stem in (hk.stem,):
                            for ext in (".sh", ".bash", ".zsh", ".fish", ".ps1", ".py", ".js", ".ts"):
                                ref = f"{stem}{ext}"
                                if ref in cmd:
                                    script_path = hooks_dir / ref
                                    if not script_path.exists():
                                        errs.append(
                                            f"{hctx}: command references '{ref}' but no such file in hooks/"
                                        )
                                    elif ext in (".sh", ".bash", ".zsh", ".fish", ".py"):
                                        import os as _os
                                        if not _os.access(script_path, _os.X_OK):
                                            errs.append(
                                                f"{hctx}: companion script {ref} must be executable (chmod +x)"
                                            )

    # output-styles/
    ost_dir = post / "output-styles"
    if ost_dir.exists():
        for ost in sorted(ost_dir.glob("*.md")):
            octx = f"{ctx}/output-styles/{ost.name}"
            fm, body = load_frontmatter(ost)
            check_name(fm.get("name", ""), octx, errs)
            if fm.get("name", "") and fm["name"] != ost.stem:
                errs.append(f"{octx}: filename stem != frontmatter name")
            if not fm.get("description"):
                errs.append(f"{octx}: missing description")
            if not body.strip():
                errs.append(f"{octx}: empty body")
            _check_companions(ost_dir, body, octx, errs)

    # plugin/
    plugin_dir = post / "plugin"
    if plugin_dir.exists():
        manifest = plugin_dir / ".claude-plugin" / "plugin.json"
        if not manifest.exists():
            errs.append(f"{ctx}/plugin: missing .claude-plugin/plugin.json")
        else:
            try:
                data = json.loads(manifest.read_text(encoding="utf-8"))
                for key in ("name", "description", "version"):
                    if key not in data:
                        errs.append(f"{ctx}/plugin/.claude-plugin/plugin.json: missing '{key}'")
                if "name" in data:
                    check_name(str(data["name"]), f"{ctx}/plugin/plugin.json", errs)
            except json.JSONDecodeError as e:
                errs.append(f"{ctx}/plugin/.claude-plugin/plugin.json: invalid JSON ({e})")


def _load_known_slugs(repo: Path) -> set[str]:
    state = repo / "state" / "processed.json"
    if not state.exists():
        return set()
    try:
        data = json.loads(state.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return set()
    slugs: set[str] = set()
    for entry in (data.get("entries") or {}).values():
        slug = entry.get("blog_slug")
        if slug:
            slugs.add(slug)
    return slugs


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    known = _load_known_slugs(repo)

    errs: list[str] = []
    post_dirs: list[Path] = []
    for child in sorted(repo.iterdir()):
        if not child.is_dir():
            continue
        if child.name.startswith("."):
            continue
        if child.name in {"scripts", "state"}:
            continue
        # Only folders that look like post dirs (have description.en.md) count,
        # OR folders whose name is a known slug from state/processed.json.
        if (child / "description.en.md").exists() or child.name in known:
            post_dirs.append(child)

    if not post_dirs:
        print("No blog-slug folders found at repo root", file=sys.stderr)
        return 1

    for post in post_dirs:
        validate_post(post, errs)

    if errs:
        print("VALIDATION FAILED:")
        for e in errs:
            print(f"  - {e}")
        print(f"\n{len(errs)} issue(s) found.")
        return 1

    print("OK: all posts valid.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
