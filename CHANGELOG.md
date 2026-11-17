# Changelog

All notable changes to this repository are documented here.
Format: Keep a Changelog (https://keepachangelog.com/en/1.0.0/).

## [Unreleased]
### Added
- House Rules §9 (anti-bloat): roster frozen by default, one source
  of truth per fact, link-don't-copy, lean logs/memory, use-it-or-
  lose-it skills, bundle budget, process caps, no-repo-left-stale.
- `validate_repo.py` check 5: roster counts in current-state surfaces
  must match `office/staff/` and the bundle heading — stale counts
  now fail CI. Historical records are excluded on purpose.

### Fixed
- `office/PLAN.md`: "19 seats" -> "19 specialists" (19 + Mercer =
  20 roles), caught by the new count check's terminology pass.

## [2026-10-07] — Company-grade open source
### Added
- `ACTIVATE.md`: trigger-phrase activation contract — "I want to use
  Seller Protocol from nx9161's github public repo" boots the Mercer
  office in any agent session; the office stays active until "End
  Seller Protocol".
- `CODE_OF_CONDUCT.md` (Contributor Covenant 2.1), `SECURITY.md`,
  `CONTRIBUTING.md`, `.github/CODEOWNERS`, PR template, issue templates.
- CI: `.github/workflows/validate.yml` runs
  `office/scripts/validate_repo.py` (required files, reference checks,
  hygiene) on every push/PR.
- `CHANGELOG.md` (this file).

## [2026-10-07] — 15 seats
### Added
- Prompt Writer joins (Intelligence). Phase 0 is now two-step: Writer
  perfects the *ask*, Knowledge Wizard gathers the *knowledge*.

## [2026-10-07] — Office founded
### Added
- Virtual Commerce Office: 14 seats in 7 divisions led by Mercer (Chief
  Operator). Playbooks: intake, war-room, launch-product, fix-listing.
  House rules: money rule (no spend without owner approval), blocking
  seats (Trade Lawyer, Finance Counsel, Vendor Picker).

## [2026-10-15] — 20 roles: Growth & Brand division + first skill
- 5 new seats: Launch Strategist, SEO Specialist, Social Media
  Strategist (new Growth & Brand division); Product Visualizer, Art
  Director (Digital Storefront). Roster now 20 roles in 8 divisions.
- War Room Phase 4 extended with all five new seats.
- New skill `office/skills/fba-math/`: unit profit breakdown +
  restock planner, clean-room built (a hunted repo failed the
  popular/safe/licensed bar), with Finance Counsel ownership and a
  fee-freshness guardrail.
- Intake playbook: multi-modal intake + Prompt Writer closed-loop
  (from 2026-10-15 audit).
