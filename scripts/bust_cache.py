"""Stamps each generated card's URL in README.md with a hash of its content.

Run: python scripts/bust_cache.py   (after the gen_*_svg.py scripts)

The cards are served through jsDelivr and GitHub's image proxy, both of
which cache by URL for days. A ?v=<hash> that changes only when the file
does makes a refreshed card show up at once, and leaves the README alone
when nothing changed.
"""
import hashlib
import pathlib
import re

ROOT = pathlib.Path(__file__).resolve().parent.parent
CARDS = ["dsa.svg", "github.svg", "oss.svg"]


def main():
    readme = ROOT / "README.md"
    text = readme.read_text(encoding="utf-8")
    for name in CARDS:
        digest = hashlib.sha1((ROOT / "assets" / name).read_bytes()).hexdigest()[:8]
        text = re.sub(rf'(assets/{re.escape(name)})(\?v=[0-9a-f]+)?"', rf'\1?v={digest}"', text)
    readme.write_text(text, encoding="utf-8", newline="\n")


if __name__ == "__main__":
    main()
