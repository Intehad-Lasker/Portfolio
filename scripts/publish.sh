#!/usr/bin/env bash
# Rebuild docs/ and publish it to the gh-pages branch that GitHub Pages serves.
# Run from anywhere inside the repo, after committing your changes.
set -euo pipefail
cd "$(git rev-parse --show-toplevel)"
python3 scripts/build_site.py
if ! git diff --quiet -- docs || [ -n "$(git status --porcelain -- docs)" ]; then
  echo "docs/ changed after the build. Commit it, then run this again." >&2
  exit 1
fi
git push origin "$(git subtree split --prefix docs HEAD)":refs/heads/gh-pages
echo "Published. https://intehad-lasker.github.io/Portfolio/ updates in about a minute."
