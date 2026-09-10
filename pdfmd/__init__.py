from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
DEFAULT_SOURCE_DIR = PROJECT_ROOT / "SOURCE"
DEFAULT_OUTPUT_DIR = PROJECT_ROOT / "OUTPUT"
TICKET_STEM_RE = r"^([A-Z][A-Z0-9]+-\d+)"


@dataclass(frozen=True)
class AppConfig:
    output_dir: Path
    force: bool = False
    raw: bool = False
