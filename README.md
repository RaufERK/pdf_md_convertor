# pdf_convertor

Локальный CLI: **PDF → Markdown**. Текст тот же, формат дешевле по токенам для Cursor.

## Папки

- `SOURCE/` — сюда кладёте PDF
- `OUTPUT/` — отсюда забираете `.md`

```bash
.venv/bin/python make_md.py
```

`SOURCE/GEOPR-879 - ….pdf` → `OUTPUT/GEOPR-879.md`

## Быстрый старт

```bash
cd /Users/rauf/Documents/WEB_PROJ/local/pdf_convertor
python3.12 -m venv .venv
.venv/bin/pip install -r requirements.txt
.venv/bin/python make_md.py
```

`--force` перезаписывает уже существующий `.md`. `--raw` — без чистки колонтитулов.
# pdf_md_convertor
