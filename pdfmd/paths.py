from __future__ import annotations

import re
from pathlib import Path

from . import TICKET_STEM_RE


def collect_pdf_paths(path: Path) -> list[Path]:
    if path.is_file():
        if path.suffix.lower() != ".pdf":
            raise SystemExit(f"Not a PDF file: {path}")
        return [path]
    if not path.exists():
        raise SystemExit(f"Path not found: {path}")
    return sorted(item for item in path.rglob("*.pdf") if item.is_file())


def output_stem(pdf_path: Path) -> str:
    match = re.match(TICKET_STEM_RE, pdf_path.stem)
    if match:
        return match.group(1)
    return pdf_path.stem


def output_path(output_dir: Path, stem: str) -> Path:
    return output_dir / f"{stem}.md"
