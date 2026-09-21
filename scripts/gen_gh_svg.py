"""Regenerates assets/github.svg from the GitHub API.

Run: python scripts/gen_gh_svg.py   (needs GITHUB_TOKEN)
Also run nightly by .github/workflows/stats.yml.

Replaces github-readme-stats and github-readme-activity-graph, which were
returning 503 and 402 respectively and rendering as broken images.

Uses REST, not GraphQL, on purpose: the workflow runs with the built-in
secrets.GITHUB_TOKEN, which is repo-scoped. GraphQL's
contributionsCollection needs a *user*-scoped token and quietly returns
"user": null for this one, so the card is built from REST endpoints that
a repo-scoped token can actually read.
"""
import json
import os
import pathlib
import urllib.error
import urllib.parse
import urllib.request

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "github.svg"
USER = "abhishekKokadwar"  # API login; the repo URL still uses the old name


def get(url, token):
    req = urllib.request.Request(url, headers={
        "Authorization": f"token {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "readme-stats/1.0",
    })
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.load(r), r.headers


def search_count(q, token):
    """Total hits for a search query; the count is all we need."""
    url = ("https://api.github.com/search/issues"
           "?per_page=1&advanced_search=true&q=" + urllib.parse.quote(q))
    data, _ = get(url, token)
    return data.get("total_count", 0)


def all_repos(token):
    repos, page = [], 1
    while page <= 4:  # 400 repos is well past what this account has
        batch, _ = get(
            f"https://api.github.com/users/{USER}/repos"
            f"?per_page=100&page={page}&type=owner&sort=pushed", token)
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1
    return [r for r in repos if not r["fork"]]


TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 176" width="900" height="176" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <rect width="900" height="176" rx="12" fill="#0d1117"/>
  <rect x="0.5" y="0.5" width="899" height="175" rx="12" fill="none" stroke="#1f2733"/>

  <text x="36" y="42" fill="#8b949e" font-size="13" font-weight="700" letter-spacing="2">GITHUB</text>
  <text x="864" y="42" fill="#6e7681" font-size="12" text-anchor="end">rebuilt nightly</text>
  <line x1="36" y1="58" x2="864" y2="58" stroke="#1f2733"/>

  <text x="36" y="100" fill="#58a6ff" font-size="30" font-weight="700">{merged}</text>
  <text x="36" y="120" fill="#6e7681" font-size="11">merged PRs</text>

  <text x="212" y="100" fill="#e6edf3" font-size="30" font-weight="700">{prs}</text>
  <text x="212" y="120" fill="#6e7681" font-size="11">PRs opened</text>

  <text x="388" y="100" fill="#e6edf3" font-size="30" font-weight="700">{issues}</text>
  <text x="388" y="120" fill="#6e7681" font-size="11">issues filed</text>

  <text x="564" y="100" fill="#e6edf3" font-size="30" font-weight="700">{repos}</text>
  <text x="564" y="120" fill="#6e7681" font-size="11">public repos</text>

  <text x="740" y="100" fill="#e6edf3" font-size="30" font-weight="700">{stars}</text>
  <text x="740" y="120" fill="#6e7681" font-size="11">stars earned</text>

  <line x1="36" y1="138" x2="864" y2="138" stroke="#1f2733"/>
{langs}
</svg>
"""

LANG_COLORS = {
    "Python": "#3572A5", "TypeScript": "#3178c6", "JavaScript": "#f1e05a",
    "C++": "#f34b7d", "Go": "#00ADD8", "Java": "#b07219", "C": "#555555",
    "HTML": "#e34c26", "CSS": "#563d7c", "Shell": "#89e051",
    "Jupyter Notebook": "#DA5B0B", "Dockerfile": "#384d54", "Svelte": "#ff3e00",
}


def lang_bar(repos):
    """One stacked bar of language share, by repo count."""
    counts = {}
    for r in repos:
        if r.get("language"):
            counts[r["language"]] = counts.get(r["language"], 0) + 1
    if not counts:
        return ""

    top = sorted(counts.items(), key=lambda kv: -kv[1])[:6]
    total = sum(c for _, c in top)
    out, x, width = [], 36.0, 828.0
    for name, count in top:
        w = width * count / total
        out.append(f'  <rect x="{x:.1f}" y="150" width="{max(w - 2, 2):.1f}" height="6" rx="3" '
                   f'fill="{LANG_COLORS.get(name, "#6e7681")}"/>')
        x += w
    legend = "   ".join(f"{n} {c}" for n, c in top)
    out.append(f'  <text x="36" y="172" fill="#6e7681" font-size="10">{legend}</text>')
    return "\n".join(out)


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; keeping existing github.svg")
        return 1

    try:
        repos = all_repos(token)
        merged = search_count(f"type:pr author:{USER} is:merged", token)
        prs = search_count(f"type:pr author:{USER}", token)
        issues = search_count(f"type:issue author:{USER}", token)
    except (urllib.error.URLError, KeyError, TypeError, ValueError) as e:
        # Keep the committed card rather than publishing zeroes.
        print(f"github fetch failed ({e}); keeping existing github.svg")
        return 1

    OUT.write_text(TEMPLATE.format(
        merged=merged, prs=prs, issues=issues,
        repos=len(repos),
        stars=sum(r["stargazers_count"] for r in repos),
        langs=lang_bar(repos),
    ), encoding="utf-8")
    print(f"github.svg: {merged} merged / {prs} PRs, {issues} issues, "
          f"{len(repos)} repos")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
