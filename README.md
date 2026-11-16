# Portfolio

Source for https://intehad-lasker.github.io/Portfolio/

- `docs/` is the published site. Its contents are pushed to the `gh-pages` branch, which GitHub Pages serves.
- `drafts/terminal/` is the design source the site is built from.
- `scripts/build_site.py` rebuilds `docs/` from the design source.
- `scripts/publish.sh` pushes `docs/` to the `gh-pages` branch.

## Changing the site

Edit `drafts/terminal/index.html`, then rebuild:

```bash
python3 scripts/build_site.py
```

Commit the result, then publish it:

```bash
scripts/publish.sh
```

## How publishing works

GitHub Pages serves the `gh-pages` branch, which holds only the contents of `docs/`. `scripts/publish.sh` rebuilds `docs/` and pushes it to that branch.
