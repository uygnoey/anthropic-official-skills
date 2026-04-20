#!/usr/bin/env python3
"""Normalize the language-switcher line so that the link matching the file's
own language becomes bold plain text (not a link). Applies to:
  - README.{md,ko.md,es.md,ja.md}
  - <blog-slug>/description.{en,ko,es,ja}.md
  - <blog-slug>/guides/*.{en,ko,es,ja}.md

README.md is treated as English.
"""
from __future__ import annotations
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

LANGS = [
    ("en", "English"),
    ("ko", "한국어"),
    ("es", "Español"),
    ("ja", "日本語"),
]
LABEL_BY_LANG = dict(LANGS)

SWITCHER_LINE_RE = re.compile(
    r"^\[English\]\([^)]+\)\s*·\s*\[한국어\]\([^)]+\)\s*·\s*\[Español\]\([^)]+\)\s*·\s*\[日本語\]\([^)]+\)\s*$"
)

def detect_lang(path: Path) -> str | None:
    name = path.name
    if name == "README.md":
        return "en"
    m = re.match(r"^README\.(ko|es|ja)\.md$", name)
    if m:
        return m.group(1)
    m = re.match(r"^description\.(en|ko|es|ja)\.md$", name)
    if m:
        return m.group(1)
    # guides/<stem>.<lang>.md
    m = re.match(r"^.+\.(en|ko|es|ja)\.md$", name)
    if m:
        return m.group(1)
    return None

def build_line(current_lang: str, link_targets: dict[str, str]) -> str:
    parts = []
    for code, label in LANGS:
        if code == current_lang:
            parts.append(f"**{label}**")
        else:
            parts.append(f"[{label}]({link_targets[code]})")
    return " · ".join(parts)

def existing_link_targets(line: str) -> dict[str, str]:
    """Extract href for each language label from a switcher line (link-form).
    Returns a dict with keys en/ko/es/ja mapped to their href. If a label is
    already bold (not a link), that language's href is inferred from the others.
    """
    out: dict[str, str] = {}
    for code, label in LANGS:
        m = re.search(rf"\[{re.escape(label)}\]\(([^)]+)\)", line)
        if m:
            out[code] = m.group(1)
    return out

def infer_target_for_lang(path: Path, lang: str) -> str:
    # README family
    if path.name.startswith("README"):
        return "./README.md" if lang == "en" else f"./README.{lang}.md"
    # description
    if path.name.startswith("description."):
        return f"./description.{lang}.md"
    # guides/<stem>.<lang>.md
    m = re.match(r"^(.+)\.(en|ko|es|ja)\.md$", path.name)
    if m:
        stem = m.group(1)
        return f"./{stem}.{lang}.md"
    return ""

def normalize_file(path: Path) -> bool:
    text = path.read_text(encoding="utf-8")
    lines = text.splitlines()
    if not lines:
        return False
    first = lines[0]
    # Look within the first 3 lines for an existing switcher. Accept any line
    # that mentions all four language labels (as link or bold).
    switcher_idx = None
    for i in range(min(3, len(lines))):
        s = lines[i].strip()
        ok = True
        for label in ("English", "한국어", "Español", "日本語"):
            if f"[{label}]" not in s and f"**{label}**" not in s:
                ok = False
                break
        if ok and s:
            switcher_idx = i
            break
    if switcher_idx is None:
        return False

    lang = detect_lang(path)
    if lang is None:
        return False

    existing = lines[switcher_idx]
    # Always derive targets from the current filename so a renamed stem fixes
    # stale references automatically.
    targets: dict[str, str] = {code: infer_target_for_lang(path, code) for code, _ in LANGS}
    # Fallback: if inference yields nothing (unknown pattern), fall back to any
    # link present in the existing switcher line.
    for code, _ in LANGS:
        if not targets[code]:
            existing_targets = existing_link_targets(existing)
            if code in existing_targets:
                targets[code] = existing_targets[code]

    new_line = build_line(lang, targets)
    if existing.strip() == new_line.strip():
        return False
    lines[switcher_idx] = new_line
    new_text = "\n".join(lines)
    if text.endswith("\n"):
        new_text += "\n"
    path.write_text(new_text, encoding="utf-8")
    return True

def main():
    candidates: list[Path] = []
    for name in ["README.md", "README.ko.md", "README.es.md", "README.ja.md"]:
        p = ROOT / name
        if p.exists():
            candidates.append(p)
    # Every top-level blog-slug folder is a post root.
    for child in ROOT.iterdir():
        if not child.is_dir() or child.name.startswith(".") \
                or child.name in {"scripts", "state"}:
            continue
        if not (child / "description.en.md").exists():
            continue
        for p in child.glob("description.*.md"):
            candidates.append(p)
        guides = child / "guides"
        if guides.exists():
            for p in guides.glob("*.md"):
                if re.match(r".+\.(en|ko|es|ja)\.md$", p.name):
                    candidates.append(p)

    changed = 0
    for p in candidates:
        if normalize_file(p):
            changed += 1
            print(f"updated {p.relative_to(ROOT)}")
    print(f"done. {changed} file(s) updated of {len(candidates)} scanned.")

if __name__ == "__main__":
    main()
