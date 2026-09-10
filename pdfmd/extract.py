from __future__ import annotations

from pathlib import Path

import pymupdf4llm


class ExtractError(RuntimeError):
    pass


def extract_pdf(pdf_path: Path) -> str:
    if not pdf_path.exists():
        raise ExtractError(f"PDF not found: {pdf_path}")
    try:
        markdown = pymupdf4llm.to_markdown(str(pdf_path), show_progress=False)
    except Exception as exc:
        raise ExtractError(f"Failed to extract {pdf_path.name}: {exc}") from exc
    text = (markdown or "").strip()
    if not text:
        raise ExtractError(f"No text extracted from {pdf_path.name}")
    return text + "\n"
