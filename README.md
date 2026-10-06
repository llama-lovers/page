# Llama Lovers — llama-lovers.org

English-only team website built with **MkDocs Material**, published on **GitHub Pages**.
It uses the Material layout and teal accents as FastFence, a white/light and
black/dark palette, and the supplied llama artwork as a theme-aware logo and background.
The theme selector remembers the visitor's choice. Light mode is the initial default.

## Local preview

```sh
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/mkdocs serve
```

Default address: http://127.0.0.1:8000.

```sh
.venv/bin/mkdocs build --strict
```

The pages use ordinary Markdown headings, paragraphs and links. There are no
project cards, promotional headlines or CTA buttons.

## Content

- `docs/team.md`: our team.
- `docs/projects/`: project catalog and FastFence / FastEcho details.
- `docs/hackathons.md`: hackathon projects, demos and slides.
- `docs/github.md`: repositories and contributing.
- `docs/presentations.md`: presentation materials.
- `docs/stylesheets/site.css`: theme-aware branding and llama background.

Public project URLs were checked on 6 October 2026. The current repositories are
`FastFence` and `FastEcho`. The presentation repository is now accessible and provides the FastFence,
Hackology II and Urban Kompas decks. Those files are served locally from
`docs/assets/presentations/`; deck text is the source for project descriptions. Private invitation links and team-only judging scores are excluded.

## Deployment

The workflow `.github/workflows/pages.yml` checks pull requests and deploys `main`
with the official GitHub Pages artifact. The repository is configured for
**Settings → Pages → Source → GitHub Actions**, with custom domain `llama-lovers.org`.

`site_url` and `docs/CNAME` specify the production domain. With Actions deployments,
the custom domain must also be set in the repository Pages settings; CNAME alone
does not configure it. DNS was already routed through Cloudflare during setup.

Official domain setup reference:
https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

## Search indexing

Each page has a unique description, an HTTPS canonical URL, Open Graph metadata
and Organization/WebSite/WebPage JSON-LD. `docs/robots.txt` permits crawling and
points to the MkDocs-generated sitemap. The 404 page is marked `noindex`.

Validate the build:

```sh
.venv/bin/mkdocs build --strict
.venv/bin/python scripts/check_seo.py
```

After deployment, submit `https://llama-lovers.org/sitemap.xml` in the verified
Google Search Console property and request indexing for the homepage through
URL Inspection. Verification must be completed by an account with access to the
domain or a Google-provided verification token. It is independent of GitHub Pages
deployment and does not guarantee immediate indexing.
