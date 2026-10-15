# Playbook: Intake

Turn a raw owner request into dispatched, tracked work — in any
modality. Mercer runs this on every incoming request.

## Pipeline

```
[ Raw prompt ] → [ Prompt Writer: perfect ] → [ Intake parse ] →
[ War Room or launch-product ] → [ Execute ]
```

Every agent downstream works from the perfected prompt, never the raw
one. The Prompt Writer also owns the closed loop: it verifies each
deliverable against the acceptance criteria and retries (max 3, each
retry changing something) before escalating to Mercer.

## 1. Text (chat messages, GitHub issues)
- Parse intent: product research, sourcing, logistics, listing/launch,
  storefront, legal/finance, or general question.
- Well-defined + small → direct dispatch to the relevant seat(s).
- Significant (launches, inventory buys, freight bookings) →
  `war-room` procedure.
- Ambiguous → ask the owner one sharp clarifying question, then route.

## 2. Images (product photos, QC defect shots, listing mockups, competitor listings)
- Attach the image to a GitHub issue for the record.
- Spawn the relevant seat(s) to interpret: Product Suggester or Vendor
  Picker for product/QC photos (defects, craftsmanship, packaging);
  Amazon Services Expert + UI Designer for listing mockups and
  competitor screenshots (layout, claims, creative gaps).
- Continue as text intake with the interpretation attached.

## 3. Audio (voice notes)
- Transcribe with the office's available transcription tooling.
- Treat the transcript as text intake. Keep the original audio linked
  in the issue.
- If transcription is unavailable, ask the owner for a text summary
  rather than guessing.

## 4. Perfect (Prompt Writer)
For anything non-trivial, the Prompt Writer forges the raw request
into the perfected prompt — objective, constraints, acceptance
criteria, done-definition. No agent works from the raw version.

## 5. Brief (Knowledge Wizard)
The Wizard takes the perfected prompt, researches every word, reads
all related documentation in full, and writes the per-seat dossier.
No step starts without the brief when the Wizard was engaged.

## 6. Dispatch (Mercer)
Assign the briefed work to the right specialists as subagents, with
dependencies ordered (e.g., landed cost before supplier outreach;
QC plan before bulk order).

## 7. Track
Open/update a GitHub Issue; journal the run in `office/log/runs/`.

## Rules
- Anything involving money, suppliers-as-the-business, or compliance
  gets flagged for owner approval before execution.
- The Prompt Writer verifies every deliverable against the perfected
  prompt's acceptance criteria before the intake closes.
