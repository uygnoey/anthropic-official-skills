#!/usr/bin/env python3
"""Sync the Index table rows (blog post | published | artifacts) from README.md
into README.ko.md, README.es.md, README.ja.md. Only the post rows are replaced.
The header rows and everything else remain untouched per file."""
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

HEADER_MARKERS = [
    ("Blog post", "Published", "Artifacts"),   # en
    ("블로그 글", "게시일", "아티팩트"),            # ko
    ("Post", "Publicado", "Artefactos"),        # es
    ("ブログ記事", "公開日", "成果物"),           # ja
]

def _is_index_header(line: str) -> bool:
    s = line.strip()
    if not s.startswith("|"):
        return False
    for a, b, c in HEADER_MARKERS:
        if a in s and b in s and c in s:
            return True
    return False

def extract_post_rows(md_text: str) -> list[str]:
    lines = md_text.splitlines()
    rows = []
    in_index = False
    for line in lines:
        if _is_index_header(line):
            in_index = True
            continue
        if in_index:
            if line.strip().startswith("|---"):
                continue
            if line.strip().startswith("| ["):
                rows.append(line)
            else:
                break
    return rows

def replace_post_rows(md_text: str, new_rows: list[str]) -> str:
    lines = md_text.splitlines()
    out = []
    i = 0
    n = len(lines)
    replaced = False
    while i < n:
        line = lines[i]
        out.append(line)
        if not replaced and _is_index_header(line):
            # keep divider line next
            if i + 1 < n and lines[i+1].strip().startswith("|---"):
                out.append(lines[i+1])
                i += 2
            else:
                i += 1
            # skip existing post rows
            while i < n and lines[i].strip().startswith("| ["):
                i += 1
            # insert new rows
            out.extend(new_rows)
            replaced = True
            continue
        i += 1
    return "\n".join(out) + ("\n" if md_text.endswith("\n") else "")

def main():
    src = (ROOT / "README.md").read_text(encoding="utf-8")
    rows = extract_post_rows(src)
    if len(rows) < 10:
        raise SystemExit(f"Unexpected row count from README.md: {len(rows)}")
    for name in ["README.ko.md", "README.es.md", "README.ja.md"]:
        path = ROOT / name
        text = path.read_text(encoding="utf-8")
        new_text = replace_post_rows(text, rows)
        path.write_text(new_text, encoding="utf-8")
        print(f"synced {name}: {len(rows)} rows")

if __name__ == "__main__":
    main()
