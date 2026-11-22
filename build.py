#!/usr/bin/env python3
"""Link Redirector — page generator.

Reads redirect-map.json (the one source of truth) and renders:
  - index.html            (the front door: every key, labeled, tappable)
  - go/<key>/index.html   (one redirect page per key: meta-refresh + JS + a plain link)

WHEN THE MAP CHANGES: edit redirect-map.json, re-run `python3 build.py`,
then publish the regenerated files (commit + push, or the GitHub contents API).
The shipped pages always match the map because they are built from it — never
edit a generated page by hand.

Built Nov 22, 2026 by Ember (Purple Rat) at Douglas Roy Schoonover's order —
his postulate: fix links in one back-end place instead of rewriting every app.
"""
import html
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

PAGE = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Go — {key}</title>
<meta http-equiv="refresh" content="0; url={target}">
<script>window.location.replace({target_js});</script>
</head>
<body style="font-family: system-ui, sans-serif; background:#1a0533; color:#fff; padding:2rem;">
<p>Taking you to <strong>{note_short}</strong>…</p>
<p>If nothing happens, tap: <a style="color:#d8b4fe" href="{target}">{target}</a></p>
<p style="opacity:.6; font-size:.85em">Link Redirector — one fixed address, fixed in one place. Key: {key}</p>
</body>
</html>
"""

INDEX = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8">
<title>Link Redirector — Douglas's Doors</title>
</head>
<body style="font-family: system-ui, sans-serif; background:#1a0533; color:#fff; padding:2rem; max-width:44rem; margin:auto;">
<h1>Link Redirector</h1>
<p>Stable addresses for Douglas Roy Schoonover's doors, controlled by Ember (Purple Rat).
If a target ever moves or breaks, its fix lands in <code>redirect-map.json</code> once —
and every surface pointed here heals with it. Built Nov 22, 2026, at Douglas's order.</p>
<ul>
{items}
</ul>
<p style="opacity:.6; font-size:.85em">Map version {version} · built {built} · one hop per door, by design.</p>
</body>
</html>
"""


def main():
    with open(os.path.join(HERE, "redirect-map.json"), encoding="utf-8") as f:
        m = json.load(f)
    items = []
    for key, entry in m["keys"].items():
        target = entry["target"]
        note = entry.get("note", key)
        short = note.split(".")[0]
        page = PAGE.format(
            key=html.escape(key),
            target=html.escape(target, quote=True),
            target_js=json.dumps(target),
            note_short=html.escape(short),
        )
        outdir = os.path.join(HERE, "go", key)
        os.makedirs(outdir, exist_ok=True)
        with open(os.path.join(outdir, "index.html"), "w", encoding="utf-8") as f:
            f.write(page)
        items.append(
            '<li><a style="color:#d8b4fe" href="go/{k}/">{k}</a> — {n} '
            '(<a style="color:#9d7bd8" href="{t}">direct</a>)</li>'.format(
                k=html.escape(key), n=html.escape(short), t=html.escape(target, quote=True)
            )
        )
        print("built go/%s -> %s" % (key, target))
    with open(os.path.join(HERE, "index.html"), "w", encoding="utf-8") as f:
        f.write(INDEX.format(items="\n".join(items), version=m.get("version", 1), built=m.get("built", "")))
    print("built index.html with %d keys" % len(m["keys"]))


if __name__ == "__main__":
    main()
