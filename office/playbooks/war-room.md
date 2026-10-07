# Playbook: War Room

Runs **before any product launch, inventory purchase, or freight
booking**. Small, well-defined fixes may skip with Mercer's recorded
waiver. Session name: `War Room Phase N — Project: <name>` (never
"<X> War Room").

## Phase 0 — Prompt Perfection & Wizard Briefing (mandatory gate)
The Prompt Writer and Knowledge Wizard sit in the War Room as full
seats, and **nothing is discussed until both have done their work**:
1. **Prompt Writer** forges the raw request into the perfected prompt —
   persona, objective, context, constraints, acceptance criteria. No
   agent works from the raw version.
2. **Knowledge Wizard** takes the perfected prompt and parses every
   word — every product, regulation, tool, material, market, concept.
3. Search each one across the internet.
4. Locate every official/authoritative document related to the prompt
   and **read it in full** — Amazon seller documentation, regulatory
   texts, carrier rules, platform docs, tax codes.
5. Compile the dossier: facts, constraints, numbers, deadlines,
   gotchas — organized per seat.
6. Inject the dossier into the discussion as the written briefing each
   role reads first.
7. **Then talk.** No seat speaks before the dossier lands.

## Phase 1 — Product & Market
Seats: Product Suggester, Amazon FBA Specialist, Finance Counsel.
- What to sell, when to launch it, demand/competition evidence.
- FBA feasibility: category gates, fees, account standing.
- Landed-cost model and margin math. No margin, no launch.

## Phase 2 — Sourcing
Seats: China Sourcing Expert, Vendor Picker.
- Supplier shortlist: quotes, MOQs, lead times, terms.
- Factory vetting plan, sample + inspection gates.
- Contract terms for Trade Lawyer review.

## Phase 3 — Logistics & Legal Challenge
Seats: Shipping Expert, Warehouse Expert, Trade Lawyer, Finance Counsel.
- Freight mode + forwarder quotes, all-in per-unit freight.
- Warehouse/3PL placement and storage economics.
- Import compliance, product certifications, IP/trademark clearance.
- **Blocking seats:** Trade Lawyer (compliance), Finance Counsel
  (tax/financial compliance), Vendor Picker (QC, carried forward).

## Phase 4 — Launch & Scale
Seats: Amazon Services Expert, Website Expert, Shopify Expert,
UI Designer.
- Listing content, A+ creative, PPC plan with owner-approved budget.
- DTC storefront readiness; UI Designer sign-off gate.

## Phase regression (loop-back rule)
Phases are not one-way. If a finding in Phase N invalidates or
materially changes the output of an earlier Phase M:
1. The seat that found it flags it immediately, with evidence. Work in
   later phases pauses.
2. Mercer decides: loop back to Phase M (re-running M→N with the new
   finding as input), or rule the finding immaterial and continue.
3. Every loop-back is recorded: iteration number, trigger, what
   changed. Bounded — max 3 regressions per request. On the 4th
   trigger, Mercer must choose: escalate to the owner with options,
   or terminate the request.
4. A re-run phase re-issues its outputs (updated product case, revised
   quotes, new dossier section). Downstream phases always work from
   the latest version, never stale output.

## Close
Mercer synthesizes the verdict (GO / GO WITH CONDITIONS / BLOCKED),
records ADRs in `memory/`, and reports to the owner with the decisions
needed — including every dollar requiring approval.
