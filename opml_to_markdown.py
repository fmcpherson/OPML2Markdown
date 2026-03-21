#!/usr/bin/env python3
"""
Convert an OPML file to Markdown.

Rules:
  - outline[type="calendarMonth"]  -> ## Heading
  - outline[type="calendarDay"]    -> ### Heading
  - outline children of calendarDay -> bulleted list items (- text)
  - all other nodes are ignored

Usage:
  python opml_to_markdown.py input.opml output.md
  python opml_to_markdown.py input.opml          # prints to stdout
"""

import sys
import xml.etree.ElementTree as ET


def opml_to_markdown(opml_path: str) -> str:
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
            indent = "  " * inside_day
            lines.append(f"{indent}- {text}")
            for child in node:
                process_node(child, inside_day=inside_day + 1)

        elif node_type == "calendarMonth":
            lines.append(f"\n## {text}")
            for child in node:
                process_node(child, inside_day=False)

        elif node_type == "calendarDay":
            lines.append(f"\n### {text}")
            for child in node:
                process_node(child, inside_day=0)

        else:
            # Skip non-calendar nodes, but still recurse in case
            # calendarMonth/calendarDay nodes are nested inside them
            for child in node:
                process_node(child, inside_day=False)

    for outline in body:
        process_node(outline)

    return "\n".join(lines).strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python opml_to_markdown.py input.opml [output.md]")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2] if len(sys.argv) >= 3 else None

    markdown = opml_to_markdown(input_path)

    if output_path:
        with open(output_path, "w", encoding="utf-8") as f:
            f.write(markdown)
        print(f"Markdown written to {output_path}")
    else:
        print(markdown)


if __name__ == "__main__":
    main()
