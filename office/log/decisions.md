# Decisions Log

## 2026-10-07 — Office founded
- **Context:** Owner requested a second virtual office for Amazon FBA /
  e-commerce, mirroring the IT office operating model.
- **Decision:** Founded the Virtual Commerce Office: 14 seats in 7
  divisions, led by Mercer (Chief Operator). Blocking authorities:
  Trade Lawyer (compliance), Finance Counsel (tax/financial
  compliance), Vendor Picker (QC). Money rule: no spend without
  explicit owner approval.
- **Owner:** Naman

## 2026-10-07 — Wizard becomes mandatory War Room Phase 0
- **Context:** Owner ordered that everything goes through the Knowledge
  Wizard first: every word of a prompt is searched, every related
  document is read in full, knowledge is injected into the discussion,
  and only then do the seats talk.
- **Decision:** Added Phase 0 (Wizard Briefing) as a mandatory gate in
  the war-room playbook; no seat speaks before the Wizard's dossier
  lands. Updated `office/staff/knowledge-wizard.md` (7-step briefing
  procedure) and `office/AGENTS.md` (protocol + roster table).
- **Owner:** Naman

## 2026-10-07 — Prompt Writer joins as 15th seat; Phase 0 becomes two-step
- **Context:** Owner ordered both offices to have a Prompt Writer and a
  Knowledge Wizard as subagents. Commerce office had the Wizard; added
  the Writer.
- **Decision:** New seat `prompt-writer` (Intelligence). Clean split:
  Prompt Writer perfects the *ask*, Knowledge Wizard gathers the
  *knowledge*. Phase 0 is now two-step: Writer forges the perfected
  prompt → Wizard parses every word, searches, reads all related docs
  in full, injects the per-seat dossier → no seat speaks before the
  dossier lands. Intake playbook updated: Writer perfects before the
  Wizard briefs.
- **Owner:** Naman

## 2026-10-07 — Activation contract: trigger phrase boots the office
- **Context:** Owner wants the phrase "I want to use Seller Protocol
  from nx9161's github public repo" to activate the Mercer office in any
  agent session.
- **Decision:** Added `ACTIVATE.md` (agent-agnostic activation contract:
  fetch repo → read office/AGENTS.md → adopt Mercer → load memory →
  confirm with the exact activation line) and an "Activate this office"
  section in the README with the copy-paste trigger phrase.
- **Owner:** Naman
