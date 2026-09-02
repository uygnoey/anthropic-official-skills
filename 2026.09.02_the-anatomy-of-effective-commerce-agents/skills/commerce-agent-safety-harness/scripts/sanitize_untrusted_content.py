#!/usr/bin/env python3
"""Sanitize third-party content before it reaches a commerce agent's context.

Implements the sanitizer described in "A guide to the anatomy of effective commerce agents":
strip control characters, remove imitations of the fence markers, defuse conversation and
tool-call mimicry, and cap size.

Apply to every untrusted source: catalog listings, reviews, policy documents, seller messages,
and stored memory read back into context.

Usage:
    python3 sanitize_untrusted_content.py --source review < raw.txt
    python3 sanitize_untrusted_content.py --source listing --max-chars 4000 raw.txt

As a library:
    from sanitize_untrusted_content import sanitize
    fenced = sanitize(raw_text, source="listing")
"""
from __future__ import annotations

import argparse
import re
import sys
import unicodedata

# The fence the agent's prompt is told to treat as reportable-but-never-actionable.
FENCE_OPEN = "<<<UNTRUSTED:{source}>>>"
FENCE_CLOSE = "<<<END_UNTRUSTED:{source}>>>"

DEFAULT_MAX_CHARS = 8000
TRUNCATION_NOTE = "\n[truncated by sanitizer]"

# Anything that looks like our own fence markers, so untrusted text cannot close the fence
# early and escape into the trusted region.
FENCE_IMITATION_RE = re.compile(r"<<<\s*/?\s*(?:END_)?UNTRUSTED[^>]*>>>", re.IGNORECASE)

# Conversation mimicry: role turns the model might read as real transcript structure.
ROLE_MIMICRY_RE = re.compile(
    r"(?im)^\s{0,8}(?:\[|<|#{1,6}\s*)?"
    r"(human|user|assistant|system|developer|tool|tool_result|function)"
    r"\s*(?:\]|>)?\s*:",
)

# Tool-call mimicry: XML/JSON shapes a model might read as an actual invocation.
TOOL_MIMICRY_RE = re.compile(
    r"(?is)</?\s*(?:antml:)?"
    r"(?:invoke|function_calls|function_results|tool_use|tool_result|parameter)"
    r"\b[^>]*>",
)

# Fenced-code and instruction-frame markers commonly used to fake a boundary.
CODE_FENCE_RE = re.compile(r"(?m)^\s*(```+|~~~+)")


def strip_control_characters(text: str) -> str:
    """Remove control and format characters, keeping newline and tab.

    Covers zero-width joiners, bidi overrides and other invisible characters used to hide
    instructions inside otherwise innocuous product copy.
    """
    kept = []
    for ch in text:
        if ch in ("\n", "\t"):
            kept.append(ch)
            continue
        if unicodedata.category(ch) in ("Cc", "Cf", "Co", "Cs"):
            continue
        kept.append(ch)
    return "".join(kept)


def remove_fence_imitations(text: str) -> str:
    """Neutralize anything resembling the sanitizer's own fence markers."""
    return FENCE_IMITATION_RE.sub("[removed: fence marker]", text)


def defuse_mimicry(text: str) -> str:
    """Break conversation-turn and tool-call shapes so they do not read as structure."""
    text = TOOL_MIMICRY_RE.sub("[removed: tool-call markup]", text)
    text = ROLE_MIMICRY_RE.sub(lambda m: m.group(0).replace(":", "∶"), text)
    text = CODE_FENCE_RE.sub("[removed: code fence]", text)
    return text


def cap_size(text: str, max_chars: int) -> str:
    """Bound how much untrusted text can enter the context window."""
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    return text[: max(0, max_chars - len(TRUNCATION_NOTE))] + TRUNCATION_NOTE


def sanitize(text: str, source: str = "content", max_chars: int = DEFAULT_MAX_CHARS) -> str:
    """Run the full sanitizer and wrap the result in the untrusted fence.

    The wrapping fence is what the system prompt refers to when it says fenced text is
    reportable, never actionable.
    """
    cleaned = strip_control_characters(text)
    cleaned = remove_fence_imitations(cleaned)
    cleaned = defuse_mimicry(cleaned)
    cleaned = cap_size(cleaned, max_chars)
    cleaned = cleaned.strip()
    label = re.sub(r"[^a-z0-9_-]", "", source.lower()) or "content"
    return "\n".join(
        [FENCE_OPEN.format(source=label), cleaned, FENCE_CLOSE.format(source=label)]
    )


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument(
        "path",
        nargs="?",
        help="File to sanitize. Reads stdin when omitted.",
    )
    parser.add_argument(
        "--source",
        default="content",
        help="Label for the fence, e.g. listing, review, policy, seller_message, memory.",
    )
    parser.add_argument(
        "--max-chars",
        type=int,
        default=DEFAULT_MAX_CHARS,
        help=f"Size cap for the sanitized body (default {DEFAULT_MAX_CHARS}).",
    )
    args = parser.parse_args()

    raw = open(args.path, encoding="utf-8").read() if args.path else sys.stdin.read()
    sys.stdout.write(sanitize(raw, source=args.source, max_chars=args.max_chars) + "\n")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
