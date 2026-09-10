from __future__ import annotations

from pathlib import Path

from . import AppConfig
from .clean import clean_markdown
from .extract import ExtractError, extract_pdf
from .paths import output_path, output_stem


def process_pdf(pdf_path: Path, config: AppConfig) -> str:
    stem = output_stem(pdf_path)
    dest = output_path(config.output_dir, stem)
    if dest.exists() and not config.force:
        return f"Skip (output exists): {dest}"

    markdown = extract_pdf(pdf_path)
    if not config.raw:
        markdown = clean_markdown(markdown)
    dest.parent.mkdir(parents=True, exist_ok=True)
    dest.write_text(markdown, encoding="utf-8")
    return f"Wrote {dest}"


__all__ = ["ExtractError", "process_pdf"]
