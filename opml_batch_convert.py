#!/usr/bin/env python3
"""
Convert all OPML files in the current directory to Markdown.

Rules:
  - outline[type="calendarMonth"]  -> ## Heading (optional; skipped if absent)
  - outline[type="calendarDay"]    -> ### Heading
  - outline children of calendarDay -> bulleted list items (- text)
  - all other nodes are ignored

Usage:
  python opml_batch_convert.py
"""

import glob
import os
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
    opml_files = glob.glob("*.opml")
    if not opml_files:
        print("No .opml files found in the current directory.")
        return

    for opml_path in sorted(opml_files):
        base = os.path.splitext(opml_path)[0]
        output_path = base + ".md"
        try:
            markdown = opml_to_markdown(opml_path)
            with open(output_path, "w", encoding="utf-8") as f:
                f.write(markdown)
            print(f"{opml_path} -> {output_path}")
        except Exception as e:
            print(f"Error processing {opml_path}: {e}")


if __name__ == "__main__":
    main()
