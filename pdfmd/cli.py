from __future__ import annotations

import argparse
import sys
from pathlib import Path

from . import DEFAULT_OUTPUT_DIR, DEFAULT_SOURCE_DIR, PROJECT_ROOT, AppConfig
from .extract import ExtractError
from .paths import collect_pdf_paths
from .pipeline import process_pdf


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    targets = collect_pdf_paths(args.path)
    if not targets:
        print(f"No .pdf files found in {args.path}", file=sys.stderr)
        return 1

    config = AppConfig(output_dir=args.output, force=args.force, raw=args.raw)
    failures = 0
    for index, pdf_path in enumerate(targets, start=1):
        print(f"\n=== [{index}/{len(targets)}] {pdf_path.name} ===")
        try:
            print(process_pdf(pdf_path, config))
        except KeyboardInterrupt:
            print("\nInterrupted.", file=sys.stderr)
            return 130
        except (ExtractError, OSError) as exc:
            failures += 1
            print(f"ERROR: {exc}", file=sys.stderr)
            continue

    if failures:
        print(f"\nFinished with {failures} error(s) out of {len(targets)} file(s).")
        return 1
    print(f"\nFinished {len(targets)} file(s).")
    return 0


def parse_args(argv: list[str] | None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Convert PDF files to Markdown. Keeps the text, drops PDF chrome.",
    )
    parser.add_argument(
        "path",
        nargs="?",
        default=str(DEFAULT_SOURCE_DIR),
        help="PDF file or folder (default: SOURCE/)",
    )
    parser.add_argument("--force", action="store_true", help="Overwrite existing .md")
    parser.add_argument("--raw", action="store_true", help="Write pymupdf dump without chrome cleanup")
    parser.add_argument(
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT_DIR,
        help="Directory for .md files (default: OUTPUT/)",
    )
    args = parser.parse_args(argv)
    args.path = Path(args.path).expanduser().resolve()
    args.output = args.output.expanduser()
    if not args.output.is_absolute():
        args.output = PROJECT_ROOT / args.output
    return args
