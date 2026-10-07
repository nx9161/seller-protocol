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

## 2026-10-07 — Skill Hunt: Wizard finds/vets/installs skills from the whole internet
- **Context:** Owner ordered that the Knowledge Wizard find every
  existing skill (GitHub public repos, Hugging Face, registries, open
  web), install it, wire up all required tools, and go down the rabbit
  hole until the task is executable.
- **Decision:** New `skill-hunt` playbook (define → hunt → vet →
  install → wire tools recursively → test → record); skills live in
  `office/skills/<slug>/SKILL.md` with a registry; Wizard owns it, any
  seat can request a hunt. Guardrails: provenance recorded, no blind
  installs, no exfiltration/phone-home without owner approval,
  secrets/keys/accounts stop the hunt and escalate. House rules §8.
- **Owner:** Naman

## 2026-10-07 — Always-on War Room loop
- **Context:** Owner wants every message after activation to go through
  the War Room — agents/subagents discuss each input, on any platform
  (including chats without subagent support like Gemini/DeepSeek).
- **Decision:** Added the always-on loop to ACTIVATE.md: every
  request/question/command runs Prompt Writer → Knowledge Wizard
  (Phase 0) → seat discussion → Chief synthesis, until the end phrase.
  Two depths (Full war room / Huddle), announced by the Chief.
  Tabletop mode for platforms without subagents: labeled seats in phase
  order inside one response. Chief staff files updated with loop duty.
- **Owner:** Naman

## 2026-10-07 — Phase regression + Chief monitor authority
- **Context:** Owner wants every request to flow through phases, with
  loop-back when a later phase's finding invalidates earlier output,
  and the Chief holding full decision power.
- **Decision:** Added phase regression rule to the war-room playbook:
  phases are not one-way; new findings loop back (max 3 regressions
  per request, then escalate or terminate); re-run phases re-issue
  outputs. Chief (Sloane/Mercer) monitors every phase gate with full
  operational authority: advance, loop back, re-scope, pause, escalate,
  terminate. Hard boundaries preserved: money, production deploys, and
  external commitments still need the owner's explicit approval.
- **Owner:** Naman

## 2026-10-07 — Live discussion: seats debate each other
- **Context:** Owner wants subagents to discuss live with each other,
  on every platform including chats without subagent support.
- **Decision:** Added live-discussion procedure to the war-room
  playbook: Chief keeps all seat subagents alive, opens with the
  motion, runs positions → open floor (rebut/support/concede via
  relayed transcript), max 3 rounds per question, then gavels and
  synthesizes. Discussion rules: evidence or concede, no repeats,
  concessions are room wins, blocks need evidence. Tabletop mode for
  no-subagent platforms: the agent writes the debate as live dialogue,
  seats answering by name. Chief staff files gained facilitator duty.
- **Owner:** Naman

## 2026-10-07 — Re-discussion ("discuss again")
- **Context:** Owner wants a "discuss again" command that re-debates
  everything — the original request plus all already-discussed topics.
- **Decision:** Added re-discussion procedure to the war-room playbook:
  Chief pulls the prior record (no re-arguing from scratch), Prompt
  Writer restates the motion with prior conclusions as context,
  Knowledge Wizard re-runs Phase 0 and briefs deltas ("what's new since
  last time"), seats hold/update/concede positions live, Chief
  synthesizes a new verdict referencing the prior ADR/decision.
  Honesty rule: repeated invocations with no new information get a
  recommendation, not theater.
- **Owner:** Naman
