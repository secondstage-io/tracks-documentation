# TRACKS Documentation

Public documentation site for [TRACKS](https://tracks.secondstage.io/) — Second Stage's attribution and marketing-intelligence platform for PC and console games. The built site is published at [documentation.secondstage.io](https://documentation.secondstage.io).

Built with [MkDocs](https://www.mkdocs.org/) and the [Material for MkDocs](https://squidfunk.github.io/mkdocs-material/) theme.

## Hosting

- **Production**: Vercel, deployed from `main` on every push.
- **Previews**: Vercel preview deployments on every pull request, linked in the PR's Checks panel.
- **CI**: a GitHub Actions workflow (`.github/workflows/ci.yml`) runs `mkdocs build --strict` on every PR to catch broken internal links, missing images, invalid YAML, and plugin misconfiguration before merge.

## Local development

Requires Python 3.11+ (tested on 3.13).

```bash
# One-time setup
python3 -m venv .venv
.venv/bin/pip install -r requirements.txt

# Run the live-reload dev server
make dev
```

Open `http://127.0.0.1:8000/` in a browser. Edits under `docs/` auto-reload. Changes to `mkdocs.yml`, `overrides/`, or `hooks/` require restarting the server (`Ctrl+C` then `make dev` again).

### Other Make targets

| Command | What it does |
|---|---|
| `make dev` | Live-reload dev server on `127.0.0.1:8000` |
| `make build` | Strict build — same check CI runs on every PR |
| `make clean` | Remove the `site/` output directory |

Always use `make dev` rather than `mkdocs serve` directly — there is a flag-parsing quirk in MkDocs 1.6.1 that silently disables the file watcher unless `--livereload` is passed explicitly, which the Makefile handles.

## Repo layout

```
docs/                 Markdown sources + static assets
  assets/             Images, screenshots, diagrams, logos
  javascripts/        Site JS (Helpscout Beacon, feedback widget)
  stylesheets/        Custom CSS
  robots.txt          Crawler policy — training denied, citation allowed
overrides/            Material theme overrides
  partials/           Custom header, footer, feedback widget
  main.html           Page identity meta tags (title, OG/Twitter cards, noindex)
hooks/                MkDocs build hooks
  recent_updates.py   Parses changelog.md and injects recent entries on the landing page
mkdocs.yml            Site config, navigation, plugins, redirects
requirements.txt      Pinned Python dependencies (mkdocs, material, glightbox, redirects)
vercel.json           Vercel build config
.github/workflows/    CI (build-strict check)
Makefile              Dev shortcuts
```

## Configuring navigation

The left sidebar and top-level sections are defined in the `nav:` block at the bottom of `mkdocs.yml`. Adding a new page means:

1. Create the Markdown file under `docs/…`.
2. Add an entry to `nav:` so it appears in the sidebar.
3. Run `make build` locally to verify the strict build still passes.

When a page moves or is renamed, add an entry to `plugins.redirects.redirect_maps` in `mkdocs.yml` so existing external links (bookmarks, emails, search results) keep working.

## Deploying

Merging a pull request into `main` triggers a Vercel production deployment automatically. No manual deploy step.

## License / ownership

&copy; Second Stage GmbH. Content is proprietary; see the site footer for legal notices and imprint.
