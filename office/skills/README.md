# Skill Registry

Skills the Knowledge Wizard hunted across the internet, vetted, and
installed. New skill = new directory `office/skills/<slug>/` with a
`SKILL.md` (frontmatter: name, description, version, source URL,
license, installed date) plus the original license file.

| Skill | Source | License | Installed | Tools wired |
|-------|--------|---------|-----------|-------------|
| `fba-math` | Concepts informed by shen169/amazon-fba-skills (MIT claimed; no LICENSE file found — inspiration only, original wording) | MIT (office-original) | 2026-10-15 | Unit profit breakdown (fees + landed cost + margin/ROI), restock planner (lead time + safety stock + order qty + reorder date). Freshness guardrail: Knowledge Wizard verifies Amazon's current fee schedule in Phase 0 — no hardcoded tables. |

## Format
Every skill directory follows the same shape the agent's own skill
system uses, so skills stay portable:

```
office/skills/<slug>/
├── SKILL.md        # frontmatter + how-to-use
├── LICENSE.*       # original license, kept verbatim
└── ...             # supporting files the skill needs
```
