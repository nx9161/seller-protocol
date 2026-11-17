#!/usr/bin/env python3
"""Company-grade repo hygiene checks. Exits non-zero on any violation.

Checks:
  1. Required standard files exist (LICENSE, README, ACTIVATE, ...).
  2. Every office/staff/*.md and office/playbooks/*.md is referenced in
     the canonical docs (office/README.md, office/AGENTS.md, AGENTS.md).
  3. ACTIVATE.md carries the trigger phrase.
  4. No trailing whitespace in tracked markdown files.
  5. Roster counts in current-state surfaces match the source of truth:
     office/staff/*.md (roles; specialists = roles - 1) and the bundle
     roster heading (divisions). Historical records (CHANGELOG, the
     decision log, dated memory entries) are excluded on purpose —
     their numbers were true when written. (House Rules §9.)
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
errors = []

REQUIRED = [
    "LICENSE",
    "README.md",
    "ACTIVATE.md",
    "CONTRIBUTING.md",
    "CODE_OF_CONDUCT.md",
    "SECURITY.md",
    "CHANGELOG.md",
    ".github/CODEOWNERS",
    ".github/PULL_REQUEST_TEMPLATE.md",
    "office/HOUSE_RULES.md",
    "office/README.md",
    "office/AGENTS.md",
    "memory/INDEX.md",
]
for f in REQUIRED:
    if not (ROOT / f).exists():
        errors.append(f"missing required file: {f}")

canon = ""
for f in ["office/README.md", "office/AGENTS.md", "AGENTS.md", "README.md"]:
    p = ROOT / f
    if p.exists():
        canon += "\n" + p.read_text(encoding="utf-8")
canon_n = canon.lower().replace("-", "").replace("_", "")


def referenced(stem: str) -> bool:
    return stem.lower().replace("-", "").replace("_", "") in canon_n


for d in ["office/staff", "office/playbooks"]:
    for md in sorted((ROOT / d).glob("*.md")):
        if not referenced(md.stem):
            errors.append(f"unreferenced file: {md.relative_to(ROOT)}")

act = (ROOT / "ACTIVATE.md").read_text(encoding="utf-8")
if "github public repo" not in act.lower():
    errors.append("ACTIVATE.md missing the trigger phrase")

for md in sorted(ROOT.rglob("*.md")):
    if ".git/" in str(md):
        continue
    for i, line in enumerate(
        md.read_text(encoding="utf-8").splitlines(), 1
    ):
        if line != line.rstrip():
            errors.append(
                f"trailing whitespace: {md.relative_to(ROOT)}:{i}"
            )
            break

roles = len(list((ROOT / "office/staff").glob("*.md")))
bundle = (ROOT / "office/AGENTS.md").read_text(encoding="utf-8")
heading = re.search(r"(\d+) Roles, (\d+) Divisions", bundle)
divisions = None
if not heading:
    errors.append(
        "office/AGENTS.md roster heading missing 'N Roles, N Divisions'"
    )
else:
    if int(heading.group(1)) != roles:
        errors.append(
            f"office/AGENTS.md heading says {heading.group(1)} roles, "
            f"office/staff/ has {roles}"
        )
    divisions = int(heading.group(2))

expected = {
    "role": roles,
    "roles": roles,
    "seat": roles,
    "seats": roles,
    "specialist": roles - 1,
    "specialists": roles - 1,
}
if divisions is not None:
    expected["division"] = divisions
    expected["divisions"] = divisions

SURFACES = [
    "README.md",
    "ACTIVATE.md",
    "office/AGENTS.md",
    "office/README.md",
    "AGENTS.md",
    "office/PLAN.md",
    "lib/dsh-plugin.js",
    "package.json",
]
claim = re.compile(r"(\d+)[\s-]+(roles?|seats?|specialists|divisions)\b", re.I)
for f in SURFACES:
    p = ROOT / f
    if not p.exists():
        continue
    for i, line in enumerate(p.read_text(encoding="utf-8").splitlines(), 1):
        for num, unit in claim.findall(line):
            want = expected[unit.lower()]
            if int(num) != want:
                errors.append(
                    f"stale count: {f}:{i} says {num} {unit}, expected {want}"
                )

if errors:
    print("validate_repo.py FAILED:")
    for e in errors:
        print(" -", e)
    sys.exit(1)
print("validate_repo.py OK")
