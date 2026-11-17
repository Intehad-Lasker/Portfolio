#!/usr/bin/env python3
"""Build the GitHub Pages site in docs/ from the design source in drafts/terminal/.

The source file is a page fragment (title, styles, markup, script). This wraps it
in a full HTML document with the metadata a public site needs.

Usage: python3 scripts/build_site.py
"""
from pathlib import Path
import re
import shutil

ROOT = Path(__file__).resolve().parent.parent
SRC = ROOT / "drafts" / "terminal"
OUT = ROOT / "docs"

URL = "https://intehad-lasker.github.io/Portfolio/"
TITLE = "Intehad Lasker, Full-Stack Developer"
DESC = (
    "Full-stack developer and Management Engineering student at the University of "
    "Waterloo. Web apps built end to end, data pipelines, and ML tooling."
)
ICON = (
    "data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 32 32'%3E"
    "%3Crect width='32' height='32' fill='%2306080a'/%3E"
    "%3Crect x='11' y='6' width='10' height='20' fill='%23e8282d'/%3E%3C/svg%3E"
)

HEAD = f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1, viewport-fit=cover">
<title>{TITLE}</title>
<meta name="description" content="{DESC}">
<meta name="theme-color" content="#06080a">
<link rel="canonical" href="{URL}">
<link rel="icon" href="{ICON}">
<meta property="og:type" content="website">
<meta property="og:url" content="{URL}">
<meta property="og:title" content="{TITLE}">
<meta property="og:description" content="{DESC}">
<meta property="og:image" content="{URL}og.png">
<meta name="twitter:card" content="summary_large_image">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
"""

RESET = "body{margin:0}img{max-width:100%}[hidden]{display:none!important}\n"


def main() -> None:
    page = (SRC / "index.html").read_text(encoding="utf-8")
    page = re.sub(r"<title>.*?</title>\n", "", page, count=1)
    page = re.sub(r'<meta name="claude:[^>]*>\n', "", page)
    head_part, body_part = page.split("</style>", 1)
    head_part = head_part.replace("<style>\n", "<style>\n" + RESET, 1)

    OUT.mkdir(exist_ok=True)
    html = f"{HEAD}{head_part}</style>\n</head>\n<body>{body_part.rstrip()}\n</body>\n</html>\n"
    (OUT / "index.html").write_text(html, encoding="utf-8")
    (OUT / ".nojekyll").write_text("", encoding="utf-8")
    shutil.copytree(SRC / "shots", OUT / "shots", dirs_exist_ok=True)
    print(f"Built {OUT / 'index.html'} ({len(html):,} bytes)")


if __name__ == "__main__":
    main()
