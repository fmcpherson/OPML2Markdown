#!/usr/bin/env python3
"""
Convert an OPML file to Markdown in chronological order (oldest first).

Same formatting rules as opml_to_markdown.py:
  - outline[type="calendarMonth"]  -> ## Heading
  - outline[type="calendarDay"]    -> ### Heading
  - outline children of calendarDay -> bulleted list items (- text)
  - all other nodes are ignored

Differences from opml_to_markdown.py:
  - calendarMonth and calendarDay nodes are sorted oldest-first
    (e.g. January 1 at the top). Bullets within a day keep their
    original order.
  - HTML inside outline text is converted to its Markdown equivalent
    (links, bold, italic, code, strikethrough, images). Tags with no
    equivalent are dropped and the text inside them is kept.

Usage:
  python opml_to_markdown_chrono.py input.opml output.md
  python opml_to_markdown_chrono.py input.opml          # prints to stdout
"""

import sys
import xml.etree.ElementTree as ET
from datetime import datetime
from html.parser import HTMLParser

_INLINE_MARKERS = {
    "b": "**",
    "strong": "**",
    "i": "*",
    "em": "*",
    "code": "`",
    "s": "~~",
    "strike": "~~",
    "del": "~~",
}


def _markdown_url(url):
    """Angle-bracket URLs containing characters that would end a Markdown link."""
    return f"<{url}>" if any(c in url for c in " ()") else url


def _render_tag(tag, attrs, inner):
    """Render a closed tag as Markdown, keeping edge whitespace outside markers."""
    label = inner.strip()
    lead = inner[: len(inner) - len(inner.lstrip())]
    trail = inner[len(inner.rstrip()) :]

    if tag == "a":
        href = attrs.get("href")
        if not href:
            return inner
        return f"{lead}[{label or href}]({_markdown_url(href)}){trail}"

    if not label:
        return inner
    marker = _INLINE_MARKERS[tag]
    return f"{lead}{marker}{label}{marker}{trail}"


class _HTMLToMarkdown(HTMLParser):
    """Rewrites inline HTML as Markdown; unsupported tags are dropped, text kept."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        # Each frame is (tag, attrs, text parts); the first frame is the output.
        self.stack = [("", {}, [])]

    def _emit(self, text):
        self.stack[-1][2].append(text)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "br":
            self._emit(" ")
        elif tag == "img":
            if attrs.get("src"):
                self._emit(f"![{attrs.get('alt') or ''}]({_markdown_url(attrs['src'])})")
        elif tag == "a" or tag in _INLINE_MARKERS:
            self.stack.append((tag, attrs, []))

    def handle_endtag(self, tag):
        if not any(frame[0] == tag for frame in self.stack[1:]):
            return
        while True:
            open_tag, attrs, parts = self.stack.pop()
            inner = "".join(parts)
            if open_tag == tag:
                self._emit(_render_tag(tag, attrs, inner))
                return
            self._emit(inner)  # tag left unclosed inside this one

    def handle_data(self, data):
        self._emit(data)

    def result(self):
        while len(self.stack) > 1:
            self._emit_unclosed()
        return "".join(self.stack[0][2])

    def _emit_unclosed(self):
        _, _, parts = self.stack.pop()
        self._emit("".join(parts))


def html_to_markdown(text):
    """Convert HTML markup in an outline's text to Markdown."""
    parser = _HTMLToMarkdown()
    parser.feed(text)
    parser.close()
    return parser.result()


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
        text = html_to_markdown(node.get("text", "")).strip()

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
