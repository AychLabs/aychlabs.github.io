#!/usr/bin/env python3
"""Validate policy Markdown files against POLICY_SPEC.md.

Usage:
    python3 tools/check_policy.py path/to/privacy-policy.md [more files...]
    python3 tools/check_policy.py --all      # every policy under <slug>/ folders

Standard library only. Exits 1 if any file fails.
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent

REQUIRED_FIELDS = ["layout", "app", "slug", "doc", "effective", "updated", "contact", "coppa"]
ALLOWED_FIELDS = set(REQUIRED_FIELDS) | {"accent", "redirect_from"}  # redirect_from: site-maintainer only

REQUIRED_H2 = {
    "privacy-policy": [
        "Information We Collect", "How We Use Information", "How We Share Information",
        "Third-Party Services", "Data Retention", "Data Security", "Your Rights and Choices",
        "Children's Privacy", "Changes to This Policy", "Contact Us",
    ],
    "delete-account": [
        "Delete Your Entire Account", "Delete Specific Data Only", "What Is Deleted",
        "What Is Retained", "How Long It Takes", "Contact Us",
    ],
}
REQUIRED_H3 = {"delete-account": ["In the app", "By email"]}

DATE = re.compile(r"^\d{4}-\d{2}-\d{2}$")
SLUG = re.compile(r"^[a-z0-9]+(-[a-z0-9]+)*$")
HEX = re.compile(r'^"?#[0-9A-Fa-f]{6}"?$')
PLACEHOLDER = re.compile(r"\[(?:X|TBD|TODO|INSERT)[^\]]*\]|YYYY-MM-DD|APP NAME", re.I)


def parse(text):
    if not text.startswith("---\n"):
        return None, text
    end = text.find("\n---", 4)
    if end == -1:
        return None, text
    fm = {}
    for line in text[4:end].splitlines():
        line = line.split(" #", 1)[0].rstrip()
        if not line or line.startswith("#") or line.startswith(" ") or line.startswith("-"):
            continue
        key, _, val = line.partition(":")
        fm[key.strip()] = val.strip()
    return fm, text[end + 4:]


def check(path):
    errs = []
    fm, body = parse(path.read_text(encoding="utf-8"))
    if fm is None:
        return ["missing front matter block"]

    for f in REQUIRED_FIELDS:
        if not fm.get(f):
            errs.append(f"front matter: missing '{f}'")
    for f in fm:
        if f not in ALLOWED_FIELDS:
            errs.append(f"front matter: unexpected field '{f}'")

    doc = fm.get("doc", "")
    if fm.get("layout") and fm["layout"] != "policy":
        errs.append("front matter: layout must be 'policy'")
    if doc not in REQUIRED_H2:
        errs.append(f"front matter: doc must be one of {sorted(REQUIRED_H2)}")
    elif path.stem != doc:
        errs.append(f"file name '{path.name}' does not match doc '{doc}'")
    if fm.get("slug") and not SLUG.match(fm["slug"]):
        errs.append("front matter: slug must be lowercase-hyphenated")
    if fm.get("slug") and path.parent.name != fm["slug"] and path.parent != ROOT / "_templates":
        errs.append(f"slug '{fm['slug']}' does not match folder '{path.parent.name}/'")
    for f in ("effective", "updated"):
        if fm.get(f) and not DATE.match(fm[f]):
            errs.append(f"front matter: {f} must be YYYY-MM-DD")
    if fm.get("coppa") and fm["coppa"] not in ("true", "false"):
        errs.append("front matter: coppa must be true or false")
    if fm.get("accent") and not HEX.match(fm["accent"]):
        errs.append('front matter: accent must look like "#RRGGBB"')
    if fm.get("contact") and not fm["contact"].endswith("@aychlabs.com"):
        errs.append("front matter: contact must be an @aychlabs.com address")

    if re.search(r"^# ", body, re.M):
        errs.append("body uses a '#' heading; use '##' and below")
    if re.search(r"<(style|script|div|span|section)\b", body, re.I):
        errs.append("body contains raw HTML")
    if PLACEHOLDER.search(body) or PLACEHOLDER.search(" ".join(fm.values())):
        errs.append("placeholder text found")

    h2 = re.findall(r"^## (.+?)\s*$", body, re.M)
    h3 = re.findall(r"^### (.+?)\s*$", body, re.M)
    if doc in REQUIRED_H2:
        need = REQUIRED_H2[doc]
        missing = [h for h in need if h not in h2]
        if missing:
            errs.append("missing sections: " + ", ".join(missing))
        else:
            order = [h2.index(h) for h in need]
            if order != sorted(order):
                errs.append("required sections are out of order")
        for h in REQUIRED_H3.get(doc, []):
            if h not in h3:
                errs.append(f"missing subsection: ### {h}")
    return errs


def main(argv):
    if argv == ["--all"]:
        files = sorted(p for p in ROOT.glob("*/*.md")
                       if p.stem in REQUIRED_H2 and not p.parent.name.startswith("_"))
    else:
        files = [Path(a).resolve() for a in argv]
    if not files:
        print(__doc__)
        return 1
    failed = 0
    for f in files:
        errs = check(f)
        rel = f.relative_to(ROOT) if f.is_relative_to(ROOT) else f
        if errs:
            failed += 1
            print(f"FAIL  {rel}")
            for e in errs:
                print(f"      - {e}")
        else:
            print(f"OK    {rel}")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
