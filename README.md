# Llama Lovers — llama-lovers.org

Strona zespołu zbudowana w **MkDocs**, publikowana przez **GitHub Pages**.
Własny motyw HTML/CSS, polskie treści i lokalne materiały graficzne.

## Uruchomienie

```sh
uv venv .venv
uv pip install --python .venv/bin/python -r requirements.txt
.venv/bin/mkdocs serve
```

Podgląd: http://127.0.0.1:8000. Kontrola produkcyjna:

```sh
.venv/bin/mkdocs build --strict
```

## Treści

- `docs/team.md`: nasz zespół.
- `docs/projects/`: katalog projektów i szczegóły FastFence / FastEcho.
- `docs/hackathons.md`: projekty na hackathonach z demo i slajdami.
- `docs/github.md`: repozytoria i współpraca.
- `docs/presentations.md`: dodatkowe materiały prezentacyjne.
- `theme/`: własny motyw MkDocs.
- `docs/stylesheets/site.css`: układ responsywny i oprawa graficzna.

Linki projektów sprawdzono 6 października 2026. Publiczne repozytoria to
`FastFence` i `FastEcho`. `llama-lovers/presentations` zwracało 404;
wykorzystano publiczne materiały `FastFence/presentation` i podane filmy.
Prywatne zaproszenia oraz oceny widoczne tylko dla zespołu nie są publikowane.

## GitHub Pages

Workflow `.github/workflows/pages.yml` sprawdza pull requesty i publikuje
`main` przez oficjalny artefakt Pages. Repozytorium korzysta z **Settings → Pages → Source → GitHub Actions**.

Domena produkcyjna: `llama-lovers.org` (`site_url` i `docs/CNAME`).
W **Settings → Pages → Custom domain** ustaw `llama-lovers.org`, a po
zakończeniu weryfikacji DNS i wystawieniu certyfikatu włącz **Enforce HTTPS**.

DNS u operatora domeny:

| Typ | Nazwa | Wartość |
| --- | --- | --- |
| A | @ | 185.199.108.153 |
| A | @ | 185.199.109.153 |
| A | @ | 185.199.110.153 |
| A | @ | 185.199.111.153 |
| CNAME | www | llama-lovers.github.io |

Nie dodawaj nowych rekordów A obok starych, konfliktujących rekordów.
Oficjalne instrukcje: https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site

Domena była już przypisana do Pages przez Cloudflare podczas wdrożenia.
Publikowanie wymaga konfiguracji Pages w ustawieniach repozytorium;
plik CNAME w artefakcie sam nie zmienia ustawień dla wdrożeń GitHub Actions.
