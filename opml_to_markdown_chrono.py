#!/usr/bin/env python3
"""
Convert an OPML file to Markdown in chronological order (oldest first).

Same formatting rules as opml_to_markdown.py:
  - outline[type="calendarMonth"]  -> ## Heading
  - outline[type="calendarDay"]    -> ### Heading
  - outline children of calendarDay -> bulleted list items (- text)
  - all other nodes are ignored

The only difference: calendarMonth and calendarDay nodes are sorted
oldest-first (e.g. January 1 at the top). Bullets within a day keep
their original order.

Usage:
  python opml_to_markdown_chrono.py input.opml output.md
  python opml_to_markdown_chrono.py input.opml          # prints to stdout
"""

import sys
import xml.etree.ElementTree as ET
from datetime import datetime


def _month_key(node):
    """Sort key for a calendarMonth node, e.g. text="October 2026"."""
    try:
        return datetime.strptime(node.get("text", "").strip(), "%B %Y")
    except ValueError:
        return None


def _day_key(node, year):
    """Sort key for a calendarDay node, e.g. text="October 27"."""
    text = node.get("text", "").strip()
    try:
        return datetime.strptime(f"{text} {year}", "%B %d %Y")
    except ValueError:
        return None


def _chronological(nodes, key_func):
    """
    Return nodes sorted oldest-first. If any node's date can't be parsed,
    fall back to simply reversing the (reverse-chronological) source order.
    """
    keys = [key_func(n) for n in nodes]
    if all(k is not None for k in keys):
        return [n for _, n in sorted(zip(keys, nodes), key=lambda p: p[0])]
    return list(reversed(nodes))


def _ordered_children(node):
    """
    Return node's children with calendar siblings placed in chronological
    order. Non-calendar children keep their original positions; the slots
    occupied by calendar nodes are refilled in chronological order.
    """
    children = list(node)
    node_type = node.get("type", "")

    if node_type == "calendarMonth":
        month = _month_key(node)
        year = month.year if month else 2000
        kind = "calendarDay"
        key_func = lambda n: _day_key(n, year)
    else:
        kind = "calendarMonth"
        key_func = _month_key

    slots = [i for i, c in enumerate(children) if c.get("type", "") == kind]
    if len(slots) > 1:
        ordered = _chronological([children[i] for i in slots], key_func)
        for i, c in zip(slots, ordered):
            children[i] = c
    return children


def opml_to_markdown_chrono(opml_path: str) -> str:
    tree = ET.parse(opml_path)
    root = tree.getroot()

    body = root.find("body")
    if body is None:
        raise ValueError("No <body> element found in OPML file.")

    lines = []

    def process_node(node, inside_day=False):
        node_type = node.get("type", "")
        text = node.get("text", "").strip()

        if inside_day is not False:
            # Everything inside a calendarDay becomes an indented bullet
            # (original order preserved)
            indent = "  " * inside_day
            lines.append(f"{indent}- {text}")
            for child in node:
                process_node(child, inside_day=inside_day + 1)

        elif node_type == "calendarMonth":
            lines.append(f"\n## {text}")
            for child in _ordered_children(node):
                process_node(child, inside_day=False)

        elif node_type == "calendarDay":
            lines.append(f"\n### {text}")
            for child in node:
                process_node(child, inside_day=0)

        else:
            # Skip non-calendar nodes, but still recurse in case
            # calendarMonth/calendarDay nodes are nested inside them
            for child in _ordered_children(node):
                process_node(child, inside_day=False)

    for outline in _ordered_children(body):
        process_node(outline)

    return "\n".join(lines).strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python opml_to_markdown_chrono.py input.opml [output.md]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) >= 3 else None

    markdown = opml_to_markdown_chrono(input_path)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Markdown written to {output_path}")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
