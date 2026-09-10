from __future__ import annotations

import re


_GIS_ONLY = re.compile(r"^gis$", re.IGNORECASE)
_EXPORTED = re.compile(r"^Exported on\b", re.IGNORECASE)
_RUNNING_HEADER = re.compile(r"^gis\s+[–-]\s+", re.IGNORECASE)
_PAGE_ONLY = re.compile(r"^–\s*\d+\s*$")
_PAGE_FOOTER = re.compile(r"^.+\s+–\s+\d+\s*$")
_PAGE_OF = re.compile(r"^--\s*\d+\s+of\s+\d+\s*--$")
_SUP = re.compile(r"<sup>\d+</sup>")
_URL_WRAP = re.compile(r"(https?://[^\s]+/)\s+(\d)")


def clean_markdown(text: str) -> str:
    """Drop PDF chrome only. Do not rewrite, summarize, or reorder content."""
    text = text.replace("pageid=", "page-id=")
    text = _URL_WRAP.sub(r"\1\2", text)
    lines = [_clean_line(line) for line in text.splitlines()]
    kept = [line for line in lines if not _is_chrome(line)]
    return _collapse_blank_lines(kept).strip() + "\n"


def _clean_line(line: str) -> str:
    return _SUP.sub("", line).rstrip()


def _is_chrome(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False
    if _GIS_ONLY.match(stripped):
        return True
    if _EXPORTED.match(stripped):
        return True
    if _RUNNING_HEADER.match(stripped):
        return True
    if _PAGE_ONLY.match(stripped) or _PAGE_OF.match(stripped):
        return True
    if _PAGE_FOOTER.match(stripped):
        return True
    return False


def _collapse_blank_lines(lines: list[str]) -> str:
    out: list[str] = []
    blank = False
    for line in lines:
        if line.strip():
            out.append(line)
            blank = False
            continue
        if not blank and out:
            out.append("")
            blank = True
    return "\n".join(out)
