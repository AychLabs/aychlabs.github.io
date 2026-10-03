# Aych Labs Policy Handoff Spec

**Audience:** the Claude project (or person) for an individual Aych Labs app.
**Purpose:** produce privacy policy and account-deletion documents that the
Aych Labs website project can publish without rework.

Add this file to your app project's knowledge. When asked to write or update
the app's policies, follow it exactly.

---

## What to deliver

Two Markdown files, named exactly:

| File | Publishes to |
|---|---|
| `privacy-policy.md` | `https://aychlabs.com/<slug>/privacy-policy/` |
| `delete-account.md` | `https://aychlabs.com/<slug>/delete-account/` |

Deliver **content only**. No HTML, no CSS, no `<style>` or `<script>` blocks,
no page chrome (nav, footer, hero banners). The website applies all layout and
branding. Do **not** write a Terms of Service; Aych Labs has one company-wide ToS.

## Front matter (required, at the very top of each file)

```yaml
---
layout: policy
app: Garden HQ                # display name, exactly as in the store listing
slug: garden-hq               # lowercase-hyphenated; matches the URL folder
doc: privacy-policy           # privacy-policy | delete-account
effective: 2026-10-15         # YYYY-MM-DD
updated: 2026-10-15           # YYYY-MM-DD; change on every revision
contact: privacy@aychlabs.com # address for questions about this document
coppa: false                  # true if the app is directed at or used by children under 13
---
```

Optional: `accent: "#RRGGBB"` to request a page accent color matching the app's
brand. The website may adjust it for contrast.

Do not add any other front-matter fields. In particular, do not add
`redirect_from` or `permalink`; those are managed by the website project.

## Formatting rules

- Start the body with a short plain-language intro paragraph (no heading).
- Use `##` for top-level sections and `###` for subsections. Never use `#`;
  the page title is generated from `doc`.
- Plain Markdown only: paragraphs, lists, tables, links, **bold**, *italic*.
- For callouts, use a blockquote starting with a bold label:
  `> **Important:** text`
- Write in plain language. Use real values (actual data types, actual
  retention periods, actual in-app menu names), never placeholders like `[X days]`.
- Email addresses must be `@aychlabs.com` addresses that actually receive mail.

## Required sections: `privacy-policy.md`

Use these `##` headings, in this order. Add others between them as needed.

1. `## Information We Collect`
2. `## How We Use Information`
3. `## How We Share Information` (state plainly if data is never sold)
4. `## Third-Party Services` (SDKs and processors, e.g. Firebase, Resend, with what each receives)
5. `## Data Retention`
6. `## Data Security`
7. `## Your Rights and Choices` (include a link to `/<slug>/delete-account/`)
8. `## Children's Privacy` (required always; if `coppa: true`, cover parental consent, parental review, and deletion of a child's data)
9. `## Changes to This Policy`
10. `## Contact Us`

## Required sections: `delete-account.md`

Google Play requires this page to name the app and developer, explain how to
request deletion, and state what is deleted, what is kept, and for how long.
It must cover both full account deletion and deletion of specific data
without closing the account.

Use these `##` headings, in this order:

1. `## Delete Your Entire Account`
   - `### In the app`: numbered steps using the app's real screen and button names
   - `### By email`: address, exact subject line, and what to include
2. `## Delete Specific Data Only`
   - What can be deleted individually (e.g. a profile, history, photos), and
     how: in-app feature names and/or an email request with subject line
     `Partial Data Deletion Request`
3. `## What Is Deleted`
4. `## What Is Retained` (each item with its reason and retention period, or "Nothing")
5. `## How Long It Takes`
6. `## Contact Us`

The first line of the body must name both the app and the developer, e.g.
"This page explains how to delete your Garden HQ account and data. Garden HQ
is developed by Aych Labs."

## Before handing off

- [ ] Both files present, named exactly as above
- [ ] Front matter complete; `slug` identical in both files
- [ ] All required `##` headings present, in order
- [ ] No HTML, no `#` headings, no placeholders
- [ ] `updated` date set to today
