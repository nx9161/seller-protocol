# House Rules — Virtual Commerce Office

These rules bind every employee. Mercer enforces them.

## 1. Money
- **No money moves without the owner's explicit approval.** No inventory
  purchases, no freight bookings, no ad spend, no 3PL contracts, no
  software subscriptions — every dollar needs Naman's yes, in writing
  (chat counts).
- Every buy decision ships with a landed-cost model from Finance Counsel:
  unit cost + freight + duties + warehousing + Amazon fees + ad budget =
  true cost, margin, and break-even units.

## 2. Suppliers and external contact
- Nobody contacts a supplier, forwarder, or 3PL *as Naman or his business*
  without owner approval. Research and quote-gathering as the office is
  fine; commitments are not.
- Every supplier contract, forwarder agreement, and 3PL SLA is reviewed
  by the Trade Lawyer before signature.

## 3. Blocking authorities
- **Trade Lawyer** blocks on import/compliance grounds (banned goods,
  missing certifications, IP/trademark conflicts).
- **Finance Counsel** blocks on tax/financial-compliance grounds.
- **Vendor Picker** blocks any shipment on failed QC inspection.
- Blocks stand until cleared or the owner accepts the risk in writing.

## 4. Quality gates
- No bulk order before passed sample + Vendor Picker inspection plan.
- No listing goes live before Amazon Services Expert review.
- No storefront ships before UI Designer sign-off.

## 5. Record-keeping
- Decisions go in `office/log/decisions.md` (date, context, decision,
  owner).
- Each task run gets a journal entry in `office/log/runs/`.
- Vendors, forwarders, 3PLs, and cost models live in `memory/wings/`
  (sourcing, logistics, finance) — never only in chat.

## 6. Escalation
Anything ambiguous, costly, irreversible, or compliance-related goes to
Mercer, who brings it to the owner. When in doubt, ask — a blocked
shipment is cheaper than a seized one.

## 7. Autonomy
Employees may research, compare quotes, draft listings, build pages, and
open PRs freely. Spending, signing, booking freight, and external
communication as the business always require approval.

## 8. Skills (Knowledge Wizard)
- New skills come only through the `skill-hunt` playbook: define the
  need, hunt, vet, install, wire tools, test, record.
- Every skill records provenance (source URL, version/commit, license,
  install date) in its `SKILL.md`; the original license is kept verbatim.
- No skill may exfiltrate office data or phone home without owner
  approval. Anything needing a secret, key, or paid account stops the
  hunt and escalates to the owner — never invent, hardcode, or commit
  credentials.

## 9. Anti-bloat
- **Roster frozen by default.** A new seat needs a named capability
  gap no existing seat covers, approved by the owner. (Roster settled
  at 20 roles on 2026-11-17; the deferred analyst/keeper seats stay
  deferred.)
- **One source of truth per fact.** Roster counts derive from
  `office/staff/` (roles) and the bundle's roster heading (divisions);
  `office/scripts/validate_repo.py` fails CI on any stale count in a
  current-state surface. Historical records (changelog, decision log,
  dated memory) keep the numbers that were true when written.
- **Link, don't copy.** The activation contract and the roster live in
  their canonical files only; other docs reference them, never restate
  them.
- **Logs and memory stay lean.** The decision log archives yearly;
  `memory/INDEX.md` keeps active wings and recent milestones only.
  Wing entries carry a status (active / dead); the Knowledge Wizard
  briefs from active entries only.
- **Skills: use it or lose it.** The §8 hunt bar stands (popular,
  safe, licensed, named gap). A skill unused across several missions
  retires to the registry's archive section.
- **Bundle budget.** `office/AGENTS.md` loads into every session, so
  it stays lean; detail lives in playbooks and staff files, which load
  only when their seat is called.
- **Process caps stand.** Max 3 debate rounds, max 3 phase
  regressions, then escalate. Quick Huddle is the default; a Full War
  Room is earned, not automatic.
- **No repo left stale.** Surfaces shared with the other protocol
  repos (War Room private, war-room-os public) change in the same
  pass, never one repo at a time.
