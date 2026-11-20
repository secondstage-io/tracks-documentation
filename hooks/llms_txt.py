"""MkDocs hook: generate /llms.txt from the navigation.

llms.txt (llmstxt.org) is a plain-text index an assistant can read in one
request instead of crawling 55 pages: section headings from the nav, and one
line per page carrying its title, URL and description.

It is generated from the same front matter that feeds <meta name="description">,
so adding a page to the nav adds it here — nothing to maintain by hand.

Pages marked `noindex: true` are left out, matching the sitemap.
"""

from __future__ import annotations

import os

from mkdocs.plugins import log

# Terms live canonically on secondstage.io; the docs copy is reader-facing only.
EXTERNAL_LINKS = [
    (
        "Glossary",
        "https://secondstage.io/glossary",
        "Definitions for every marketing, attribution and player-lifecycle term "
        "TRACKS uses — one page per term.",
    ),
]

SUMMARY = (
    "TRACKS is Second Stage's marketing intelligence platform for PC and console "
    "games, joining ad-platform spend, store data and in-game events into one "
    "attribution and reporting model. This documentation covers the integration "
    "end to end: cloud setup, ad-platform access, the Measurement API, conversion "
    "postbacks, and how every reported metric is calculated."
)

_descriptions: dict[str, str] = {}
_nav = None


def on_nav(nav, config, files):  # noqa: ARG001 - MkDocs signature
    global _nav
    _nav = nav
    return nav


def on_page_context(context, page, config, nav):  # noqa: ARG001 - MkDocs signature
    meta = page.meta or {}
    if not meta.get("noindex"):
        _descriptions[page.file.src_uri] = str(meta.get("description", "")).strip()
    return context


def _render(items, config, depth: int = 0) -> list[str]:
    lines: list[str] = []
    for item in items:
        if item.is_section:
            lines.append("")
            lines.append(f"## {item.title}")
            lines.append("")
            lines.extend(_render(item.children, config, depth + 1))
        elif item.is_page:
            src = item.file.src_uri
            if src not in _descriptions:
                continue
            # The homepage's file.url is "." or "./" — everything else is a path.
            path = item.file.url
            path = "" if path in (".", "./") else path.lstrip("/")
            url = config.site_url.rstrip("/") + "/" + path
            desc = _descriptions[src]
            lines.append(f"- [{item.title}]({url}){': ' + desc if desc else ''}")
    return lines


def on_post_build(config):  # noqa: ARG001 - MkDocs signature
    if _nav is None or not config.site_url:
        log.warning("llms_txt: no nav or site_url; skipping llms.txt")
        return

    body = _render(_nav.items, config)

    # Pages reachable from the nav root sit above the first section heading.
    lines = [f"# {config.site_name}", "", f"> {SUMMARY}", ""]
    lines.extend(line for line in body if line is not None)

    if EXTERNAL_LINKS:
        lines.append("")
        lines.append("## Elsewhere")
        lines.append("")
        for title, url, desc in EXTERNAL_LINKS:
            lines.append(f"- [{title}]({url}): {desc}")

    text = "\n".join(lines).strip() + "\n"
    # Collapse the blank line a section heading adds when it opens the document.
    text = text.replace("\n\n\n", "\n\n")

    path = os.path.join(config.site_dir, "llms.txt")
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)

    pages = sum(1 for line in text.splitlines() if line.startswith("- ["))
    log.info("llms_txt: wrote llms.txt (%d entries)", pages)
