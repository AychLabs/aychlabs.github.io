# CLAUDE.md — Aych Labs website (aychlabs.com)

Company site for Aych Labs and the hosting home for every Aych Labs app's
legal pages. Read this before changing anything.

## What this site is for

1. Landing page for Aych Labs at `aychlabs.com`.
2. Per-app privacy policy and account-deletion pages (required by Google Play).
3. One company-wide Terms of Service covering all apps.

## Apps

| App | Slug | Status |
|---|---|---|
| Family Rewards (name may change before release) | `family-rewards` | Live on Google Play |
| Garden HQ | `garden-hq` | In development |
| Aych IQ | `aych-iq` | In development |

The registry lives in `_data/apps.yml`. Nav and footer read from it, so add or
update an app there, not by hand-editing templates.

## Stack

- **Jekyll**, built automatically by **GitHub Pages** on push to `main`. No local build step is required to deploy.
- Custom domain via `CNAME` (`aychlabs.com`). DNS is managed in Squarespace; the
  `www` CNAME points to `aychlabs.github.io` and four A records point to GitHub Pages.
- `permalink: pretty` gives clean trailing-slash URLs: `garden-hq/privacy-policy.md` publishes at `/garden-hq/privacy-policy/`.
- Plugin: `jekyll-redirect-from` (supported natively by GitHub Pages).
- The repo must **not** contain a `.nojekyll` file, or GitHub skips the build.
- Local working copy lives on the dev mini PC, cloned from the GitHub repo.
  Do work on a branch; the Pages branch (Settings → Pages) is live.
  **Never force-push to the Pages branch.**

## Structure

```
_config.yml          site config, permalinks, plugins, excludes
_data/apps.yml       app registry (name, slug, status, accent, Play URL)
_layouts/default.html   base page: head, nav, main, footer
_layouts/policy.html    policy pages; sets --accent from front matter or registry
_includes/           head.html, nav.html, footer.html
assets/css/site.css  all site styles (currently a placeholder)
_templates/          blank starter policy files (not published)
<slug>/              one folder per app: privacy-policy.md, delete-account.md
legal/               company-wide pages: terms-of-service.md
tools/check_policy.py   validates policy files against POLICY_SPEC.md
POLICY_SPEC.md       the handoff spec given to each app project
```

## URL rules

- Pattern: `/<slug>/privacy-policy/`, `/<slug>/delete-account/`, `/legal/terms-of-service/`.
- Every URL submitted to Google Play is permanent. **Never move or delete one
  without adding a `redirect_from` entry on the page that replaces it.**
- Renaming an app does not require renaming its slug. If a slug ever must
  change, keep the old path alive with `redirect_from`.
- Redirects on GitHub Pages are client-side (meta refresh), not HTTP 301s. After
  moving a URL, also update it in the Play Console; treat redirects as a safety net.

## Live URLs (submitted to Google Play — must keep working)

| Old URL | Now served at | Status |
|---|---|---|
| `/privacy-policy` | `/family-rewards/privacy-policy/` | redirect pending (step 3) |
| `/delete-account` | `/family-rewards/delete-account/` | redirect pending (step 3) |
| `/terms-of-service` | `/legal/terms-of-service/` | redirect pending (step 3) |

Update this table whenever a URL is added, moved, or entered in the Play Console.

## Policy handoff process

App-specific policies are written by each app's own Claude project, because it
knows the app. This project publishes them.

1. The app project has `POLICY_SPEC.md` in its knowledge and delivers
   `privacy-policy.md` and `delete-account.md` as content-only Markdown.
2. Place both files in `<slug>/`.
3. Run `python3 tools/check_policy.py <slug>/*.md` and fix or send back any failures.
4. If the app is new, add it to `_data/apps.yml`.
5. Commit and push. Verify the live URLs, then record any Play Console
   submissions in the Live URLs table above.

Do not rewrite an app's policy content here. Formatting fixes are fine;
substantive changes go back to the app project so its source stays the source
of truth. When `POLICY_SPEC.md` changes, re-share it with every app project.

## Design

- The site shell is **neutral Aych Labs branding**, shared by every page.
  The design is pending (step 2); `assets/css/site.css` is a placeholder.
- Each app expresses its own identity only through its `accent` color
  (`_data/apps.yml`, or `accent:` in a page's front matter). Garden HQ and
  Family Rewards have their own looks; the dark "Hyperion" style belongs to Aych IQ, not the shell.
- Policy pages are long legal text: prioritize readability (line length under
  ~75 characters, high contrast, accessible accent usage) over decoration.
- Hal's preferences: clean, sharp, uncluttered.

## Email addresses used on the site

Mail is hosted on Zoho Mail. Addresses used on the site:

| Address | Type | Delivers to |
|---|---|---|
| `support@aychlabs.com` | Mailbox | support |
| `privacy@aychlabs.com` | Alias | support |
| `legal@aychlabs.com` | Alias | support |

Never publish an address that isn't in this table. If a new one is needed,
create it in Zoho first (an alias on `support` is usually enough), then add it here.
Other Zoho mailboxes (`dev@`, `admin@`, `qa01@`, `reviewer@`) are internal and
should not appear on the site.

## Local preview (optional)

```
bundle install
bundle exec jekyll serve      # http://localhost:4000
```

## Conventions

- Markdown for content, HTML only in `_layouts/` and `_includes/`.
- No inline `<style>` blocks in pages; all CSS lives in `assets/css/site.css`.
- No new front-matter fields on policy pages without updating `POLICY_SPEC.md` and `tools/check_policy.py`.
- Commit messages: imperative, scoped, e.g. `garden-hq: add privacy policy`.

## Roadmap

1. ~~Scaffold repo~~ (done)
2. Design the neutral Aych Labs shell
3. Migrate Family Rewards pages and ToS to Markdown; add redirects; update Play Console URLs
4. Publish Garden HQ and Aych IQ policies as their projects hand them off
