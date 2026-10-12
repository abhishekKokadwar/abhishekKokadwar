"""Regenerates assets/oss.svg, the open-source card, from the GitHub API.

Run: python scripts/gen_oss_svg.py   (needs GITHUB_TOKEN)
Also run on a schedule by .github/workflows/stats.yml, so a newly merged PR
shows up on the profile without anyone editing the README.

Everything on the card is derived from search results, and nothing on it is
a timestamp of the run itself: the card only changes when the data does, so
the workflow only commits when something actually merged.
"""
import datetime
import html
import os
import pathlib
import urllib.error
import urllib.parse

from gen_gh_svg import UPSTREAM_EXCLUDE, USER, get, search_count

OUT = pathlib.Path(__file__).resolve().parent.parent / "assets" / "oss.svg"

LATEST = 4          # most recent merges listed by title
CHAR_W = 7.3        # advance of one 12px monospace glyph, near enough
CHIPS = 5           # repos shown as chips before the rest collapse to "+n"


def merged_prs(token):
    """Every merged upstream PR, newest merge first."""
    q = f"type:pr author:{USER} is:merged is:public {UPSTREAM_EXCLUDE}"
    url = ("https://api.github.com/search/issues?per_page=100&sort=updated"
           "&advanced_search=true&q=" + urllib.parse.quote(q))
    data, _ = get(url, token)
    prs = [{
        "repo": i["repository_url"].split("/repos/")[1],
        "number": i["number"],
        "title": i["title"],
        "merged": (i.get("pull_request") or {}).get("merged_at") or i["closed_at"],
    } for i in data["items"]]
    return sorted(prs, key=lambda p: p["merged"], reverse=True), data["total_count"]


def short(repo):
    """kubeflow/mcp-server -> mcp-server; the org is on the card already."""
    return repo.split("/")[1]


def day(iso):
    d = datetime.date.fromisoformat(iso[:10])
    return f"{d.day} {d:%b %Y}"


def clip(text, n):
    return text if len(text) <= n else text[:n - 1].rstrip() + "…"


def bar(y, part, whole, cls):
    """A track with a fill that grows in from the left on load."""
    w = 828 * part / whole if whole else 0
    return (f'  <rect x="36" y="{y}" width="828" height="6" rx="3" fill="#161d27"/>\n'
            f'  <rect class="grow {cls}" x="36" y="{y}" width="{w:.1f}" height="6" rx="3" fill="#58a6ff"/>')


def chips(by_repo, y):
    out, x = [], 36
    top = sorted(by_repo.items(), key=lambda kv: (-kv[1], kv[0]))
    shown = top[:CHIPS]
    if len(top) > CHIPS:
        shown.append((f"+{len(top) - CHIPS} more", ""))
    for name, count in shown:
        label = f"{name} {count}".strip()
        w = len(label) * CHAR_W + 24
        out.append(f'  <rect x="{x:.0f}" y="{y}" width="{w:.0f}" height="24" rx="12" fill="#0f151d" stroke="#26303c"/>')
        out.append(f'  <text x="{x + 12:.0f}" y="{y + 16}" fill="#8b949e" font-size="12">{html.escape(name)}'
                   f' <tspan fill="#58a6ff" font-weight="700">{count}</tspan></text>')
        x += w + 8
    return "\n".join(out)


def latest(prs, y):
    out = []
    for n, p in enumerate(prs[:LATEST]):
        ref = f"{short(p['repo'])} #{p['number']}"
        tx = 92 + len(ref) * CHAR_W + 12
        out.append(
            f'  <g class="row r{n}">'
            f'<text x="80" y="{y + n * 22}" fill="#6e7681" font-size="12" text-anchor="end">{day(p["merged"])[:-5]}</text>'
            f'<text x="92" y="{y + n * 22}" fill="#58a6ff" font-size="12">{html.escape(ref)}</text>'
            f'<text x="{tx:.0f}" y="{y + n * 22}" fill="#c9d1d9" font-size="12">'
            f'{html.escape(clip(p["title"], int((864 - tx) / CHAR_W)))}</text></g>')
    return "\n".join(out)


TEMPLATE = """<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 900 {height}" width="900" height="{height}" font-family="ui-monospace, SFMono-Regular, Menlo, Consolas, monospace">
  <style>
    .grow {{ transform-box: fill-box; transform-origin: left center; animation: grow 1.4s cubic-bezier(.2,.8,.2,1) both }}
    .b1 {{ animation-delay: .25s }}
    @keyframes grow {{ from {{ transform: scaleX(0) }} to {{ transform: scaleX(1) }} }}
    .row {{ animation: rise .6s cubic-bezier(.2,.8,.2,1) both }}
    .r0 {{ animation-delay: .7s }} .r1 {{ animation-delay: .85s }} .r2 {{ animation-delay: 1s }} .r3 {{ animation-delay: 1.15s }}
    @keyframes rise {{ from {{ opacity: 0; transform: translateY(6px) }} to {{ opacity: 1; transform: translateY(0) }} }}
    .live {{ animation: pulse 2s ease-in-out infinite }}
    @keyframes pulse {{ 0%, 100% {{ opacity: .35 }} 50% {{ opacity: 1 }} }}
    @media (prefers-reduced-motion: reduce) {{ .grow, .row, .live {{ animation: none }} }}
  </style>
  <rect width="900" height="{height}" rx="12" fill="#0d1117"/>
  <rect x="0.5" y="0.5" width="899" height="{height_inner}" rx="12" fill="none" stroke="#1f2733"/>

  <text x="36" y="42" fill="#8b949e" font-size="13" font-weight="700" letter-spacing="2">OPEN SOURCE</text>
  <text x="864" y="42" fill="#58a6ff" font-size="12" text-anchor="end">{merged} merged PRs, all upstream</text>
  <line x1="36" y1="58" x2="864" y2="58" stroke="#1f2733"/>

  <text x="36" y="84" fill="#6e7681" font-size="11" letter-spacing="1.5">MERGED UPSTREAM</text>
  <text x="864" y="84" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="end">{merged} merged / {opened} opened</text>
{bar_prs}

  <text x="36" y="128" fill="#6e7681" font-size="11" letter-spacing="1.5">ISSUES CLOSED</text>
  <text x="864" y="128" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="end">{closed} closed / {filed} filed</text>
{bar_issues}

  <text x="36" y="172" fill="#6e7681" font-size="11" letter-spacing="1.5">REPOS LANDED IN</text>
  <text x="864" y="172" fill="#e6edf3" font-size="12" font-weight="700" text-anchor="end">{repo_count} upstream repos</text>
{chips}

  <line x1="36" y1="224" x2="864" y2="224" stroke="#1f2733"/>
  <circle class="live" cx="40" cy="244" r="3.5" fill="#3fb950"/>
  <text x="54" y="248" fill="#6e7681" font-size="11" letter-spacing="1.5">LATEST MERGED</text>
  <text x="864" y="248" fill="#6e7681" font-size="11" text-anchor="end">last merge {last}</text>
{latest}
</svg>
"""


def main():
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("GITHUB_TOKEN not set; keeping existing oss.svg")
        return 1

    try:
        prs, merged = merged_prs(token)
        opened = search_count(f"type:pr author:{USER} is:public {UPSTREAM_EXCLUDE}", token)
        issues = f"type:issue author:{USER} is:public {UPSTREAM_EXCLUDE}"
        filed = search_count(issues, token)
        closed = search_count(issues + " is:closed", token)
    except (urllib.error.URLError, KeyError, TypeError, ValueError) as e:
        # Keep the committed card rather than publishing zeroes.
        print(f"github fetch failed ({e}); keeping existing oss.svg")
        return 1
    if not prs:
        print("no merged PRs returned; keeping existing oss.svg")
        return 1

    by_repo = {}
    for p in prs:
        by_repo[p["repo"]] = by_repo.get(p["repo"], 0) + 1

    height = 270 + min(len(prs), LATEST) * 22
    OUT.write_text(TEMPLATE.format(
        height=height, height_inner=height - 1,
        merged=merged, opened=opened, closed=closed, filed=filed,
        bar_prs=bar(94, merged, opened, "b0"),
        bar_issues=bar(138, closed, filed, "b1"),
        repo_count=len(by_repo), chips=chips(by_repo, 184),
        last=day(prs[0]["merged"]), latest=latest(prs, 274),
    ), encoding="utf-8", newline="\n")
    print(f"oss.svg: {merged} merged / {opened} opened, {closed}/{filed} issues, "
          f"{len(by_repo)} repos, latest {short(prs[0]['repo'])} #{prs[0]['number']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
