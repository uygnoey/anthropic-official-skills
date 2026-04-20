#!/usr/bin/env python3
"""Validate all artifacts in posts/ against Claude Code official specs.

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
import re
import sys
from pathlib import Path

NAME_RE = re.compile(r"^[a-z0-9-]+$")
RESERVED = {"claude", "anthropic"}
LANG_SWITCHER_TOKENS = ("[English]", "[한국어]", "[Español]", "[日本語]")
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
    try:
        head = path.read_text(encoding="utf-8").splitlines()[:3]
    except Exception:
        return False
    joined = " ".join(head)
    return all(tok in joined for tok in LANG_SWITCHER_TOKENS)


def validate_post(post: Path, errs: list[str]) -> None:
    ctx = f"posts/{post.name}"

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
            if not has_lang_switcher(g):
                errs.append(f"{ctx}/guides/{g.name}: missing language switcher")
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


def main() -> int:
    repo = Path(__file__).resolve().parent.parent
    posts_dir = repo / "posts"
    if not posts_dir.exists():
        print(f"No posts/ directory at {posts_dir}", file=sys.stderr)
        return 1

    errs: list[str] = []
    for post in sorted(posts_dir.iterdir()):
        if post.is_dir():
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
