# Portfolio

Source for https://intehad-lasker.github.io/Portfolio/

- `docs/` is the published site. GitHub Pages serves this folder.
- `drafts/terminal/` is the design source the site is built from.
- `scripts/build_site.py` rebuilds `docs/` from the design source.

## Changing the site

Edit `drafts/terminal/index.html`, then run:

```bash
python3 scripts/build_site.py
```

Commit and push. GitHub Pages republishes on every push to the branch it is set to serve.

## Publishing

In the repository settings, open Pages, choose "Deploy from a branch", then pick the branch and the `/docs` folder.
