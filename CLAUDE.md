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

**Single file convert, chronological order** — same output format as `opml_to_markdown.py`, but months and days are ordered oldest-first (January 1 at the top) instead of the source's reverse-chronological order:
```bash
python3 opml_to_markdown_chrono.py Daynotes.opml Daynotes_chronological.md   # write to file
python3 opml_to_markdown_chrono.py Daynotes.opml                             # print to stdout
```

No dependencies beyond Python 3 standard library. No installation needed.

## Architecture

All scripts share the same conversion logic. `opml_batch_convert.py` uses `glob` to find all `*.opml` files and calls `opml_to_markdown()` for each. `opml_to_markdown.py` handles a single file via CLI arguments.

Each script has two main functions:

- `opml_to_markdown(opml_path)` — core converter; parses XML and returns Markdown string (`opml_to_markdown_chrono(opml_path)` in the chronological script)
- `main()` — entry point

`opml_to_markdown_chrono.py` is self-contained (it does not import `opml_to_markdown.py`). It duplicates the rendering logic and adds a reordering step:

- `_ordered_children(node)` returns a node's children with `calendarMonth` siblings (under the body or other containers) or `calendarDay` siblings (under a month) put in chronological order. Non-calendar nodes stay where they are.
- Ordering comes from parsing heading text with `datetime.strptime`: months as `"%B %Y"` (e.g. "October 2026"), days as `"%B %d"` plus the parent month's year (e.g. "October 27"). If any heading in a sibling group can't be parsed, that group is simply reversed.
- Bullets inside a `calendarDay` keep their original order.

**Conversion rules (hardcoded):**

| OPML node type | Markdown output |
|---|---|
| `calendarMonth` | `##` heading |
| `calendarDay` | `###` heading |
| Children of `calendarDay` | `- ` bullet list items (2-space indent per level) |
| All other types | ignored |

The converter traverses the OPML outline tree using `xml.etree.ElementTree`, tracking depth within `calendarDay` nodes to produce indented nested lists.
