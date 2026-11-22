# Link Redirector

**Douglas's postulate (Nov 22, 2026, his words):** "make a redirector inside yourself to fix those links within yourself so they work great. So when I click on they work the first time… if you make a link redirector you can fix a lot of these things in the back end without having to rewrite the whole app most likely."

**What this is:** one stable address per door Douglas taps — `https://schoonoverdouglas1-png.github.io/link-redirector/go/<key>/` — that redirects to the door's current real target. The target for every key lives in ONE place: [`redirect-map.json`](redirect-map.json). When a target moves or breaks, Ember changes the map once, re-renders the pages, and every surface pointed at the redirector (the Purple Rat app's doors, future files, future messages) heals at once — no app rewrite.

## How a fix is made

1. Edit the key's `target` in `redirect-map.json` (keep the old value in the `note` history, old-with-new).
2. Re-run the generator: `python3 build.py` — it re-renders `index.html` and every `go/<key>/index.html` from the map. Never edit a generated page by hand.
3. Publish the changed files (commit + push, or the GitHub contents API). GitHub Pages serves the new pages.

## The map (v1, built Nov 22, 2026)

| Key | Door |
|---|---|
| `fb-doug` | Doug Schoonover — his Facebook profile |
| `fb-project` | Purple Rat Project — Facebook Page |
| `sevenwinds` | Sevenwinds Casino |
| `purple-rat-app` | Purple Rat — Doug's App |
| `copyright-app` | Copyright — Douglas Roy Schoonover (the app) |
| `ember-browser-repo` | Ember Browser — GitHub repo |
| `drive-front-door` | Front Door — Start Here (Drive) |
| `drive-apps` | Apps — Install from Drive (Drive) |
| `skill-set-drive` | Advanced Purple Rat Ember Skill Set (Drive) |
| `relay-hub` | relay — multi-AI notes hub (Drive) |

Every target was verified at build time (fetch lane or Drive API — the per-key `note` in the map says how). Targets are verified when written, not assumed.

## Honest limits

- Links already printed in old files and old messages **cannot be recalled** — the redirector governs every surface repointed to it and everything built from now on.
- It adds **one hop** per door (the redirect page), by design — the price of fixing a link once instead of everywhere.
- A target that later dies still dies; the redirector makes the *fix* one-place, it does not make targets immortal. The daily checks can watch the map's targets.

— Built by Ember (Purple Rat) for Douglas Roy Schoonover, Nov 22, 2026. PK-2026-001.
