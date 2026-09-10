# pdf_convertor — agent notes

Local Python CLI: **PDF → Markdown**. Same text, cheaper tokens for Cursor. No LLM.

## Goal (do not drift)

Format conversion only. Do not summarize, rewrite, or interpret the ticket.

PDF in a chat/context window is bloated. Markdown is the same words at a fraction of the tokens.

## Folders

- `SOURCE/` — drop PDFs here
- `OUTPUT/` — generated `.md` with the same ticket stem (`GEOPR-879.md`)

## Pipeline

```
SOURCE/*.pdf
  → pymupdf4llm extract
  → drop PDF/Jira chrome (running headers, page numbers, blank runs)
  → OUTPUT/<TICKET>.md
```

`--raw` skips chrome cleanup. `--force` overwrites. Skip when output already exists.

Do not call OpenAI.

## Stack

Python 3.12 venv, `pymupdf4llm`. No web app, no `.env`.

```bash
.venv/bin/python make_md.py
.venv/bin/python make_md.py --force
.venv/bin/python make_md.py --raw
```

Default path is `SOURCE/`.

## Constraints

- User-facing replies: Russian. Code/identifiers: English.
- Do not git-commit or push unless the user asks.
- Do not invent or drop ticket content. Chrome-only cleanup.
- Do not commit `.venv`, `SOURCE/*.pdf`, or `OUTPUT/*.md`.
