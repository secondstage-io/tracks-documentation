"""MkDocs hook: stamp sitemap <lastmod> with each page's last commit date.

MkDocs defaults `page.update_date` to the build date, so every deploy tells
search engines that all 54 indexed pages changed — a signal that carries no
information. This hook replaces it with the date of the commit that last
touched the page's source file.

It runs on `on_env`, which fires after every page has been read but before
MkDocs renders sitemap.xml. `on_page_context` would be too late: theme
templates are written before individual pages are built.

Any file git doesn't know about keeps the build date, which covers shallow
clones with too little history and uncommitted local edits. The build never
fails on account of git being unavailable.
"""

from __future__ import annotations

import os
import subprocess

from mkdocs.plugins import log


def _run(args: list[str]) -> str | None:
    try:
        return subprocess.run(
            args, capture_output=True, text=True, timeout=30, check=True
        ).stdout
    except (OSError, subprocess.SubprocessError):
        return None


def _commit_dates(docs_dir: str) -> tuple[str, dict[str, str]]:
    """Return (repo root, {repo-relative path: YYYY-MM-DD of last commit})."""
    root = _run(["git", "rev-parse", "--show-toplevel"])
    if root is None:
        log.info("git_dates: not a git checkout; lastmod falls back to the build date")
        return "", {}

    out = _run(
        ["git", "log", "--pretty=format:@%cs", "--name-only", "--no-renames", "--", docs_dir]
    )
    if out is None:
        return "", {}

    dates: dict[str, str] = {}
    date = ""
    for line in out.splitlines():
        if line.startswith("@"):
            date = line[1:]
        elif line and date:
            dates.setdefault(line, date)
    return root.strip(), dates


def on_env(env, config, files):  # noqa: ARG001 - MkDocs signature
    root, dates = _commit_dates(config.docs_dir)
    if not dates:
        return env

    stamped = 0
    for file in files.documentation_pages():
        if file.page is None:
            continue
        key = os.path.relpath(file.abs_src_path, root) if root else file.abs_src_path
        date = dates.get(key)
        if date:
            file.page.update_date = date
            stamped += 1

    missing = len(files.documentation_pages()) - stamped
    log.info(
        "git_dates: %d page(s) stamped from git%s",
        stamped,
        f", {missing} kept the build date" if missing else "",
    )
    return env
