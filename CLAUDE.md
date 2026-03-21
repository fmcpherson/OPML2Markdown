# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What This Project Does

Converts OPML (Outline Processor Markup Language) files to Markdown. Specifically designed around calendar-structured OPML files (e.g., daily notes with `calendarMonth` and `calendarDay` node types).

## Scripts

**Batch convert** — converts all `.opml` files in the current directory to `.md` files:
```bash
python3 opml_batch_convert.py
```

**Single file convert** — converts one OPML file:
```bash
python3 opml_to_markdown.py input.opml output.md   # write to file
python3 opml_to_markdown.py input.opml             # print to stdout
```

No dependencies beyond Python 3 standard library. No installation needed.

## Architecture

Both scripts share the same conversion logic. `opml_batch_convert.py` uses `glob` to find all `*.opml` files and calls `opml_to_markdown()` for each. `opml_to_markdown.py` handles a single file via CLI arguments.

Each script has two functions:

- `opml_to_markdown(opml_path)` — core converter; parses XML and returns Markdown string
- `main()` — entry point

**Conversion rules (hardcoded):**

| OPML node type | Markdown output |
|---|---|
| `calendarMonth` | `##` heading |
| `calendarDay` | `###` heading |
| Children of `calendarDay` | `- ` bullet list items (2-space indent per level) |
| All other types | ignored |

The converter traverses the OPML outline tree using `xml.etree.ElementTree`, tracking depth within `calendarDay` nodes to produce indented nested lists.
