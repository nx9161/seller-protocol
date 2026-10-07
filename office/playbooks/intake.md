# Playbook: Intake

Turn a raw owner request into dispatched, tracked work.

## Procedure (one subagent per step)

1. **Triage (Mercer).** Read the request. Classify: product research,
   sourcing, logistics, listing/launch, storefront, legal/finance, or
   general question. If it's a general question, route to the Knowledge
   Wizard first.
2. **Clarify.** If the request is missing anything that changes the
   work (product, quantity, budget, deadline, market), ask the owner —
   one round, specific questions.
3. **Brief (Knowledge Wizard).** For anything non-trivial, the Wizard
   researches current facts and writes a perfected brief: objective,
   constraints, acceptance criteria, done-definition.
4. **Dispatch.** Mercer assigns the briefed work to the right
   specialists as subagents, with dependencies ordered (e.g., landed
   cost before supplier outreach; QC plan before bulk order).
5. **Track.** Open/update a GitHub Issue; journal the run in
   `office/log/runs/`.

## Rules
- No step starts without the brief when the Wizard was engaged.
- Anything involving money, suppliers-as-the-business, or compliance
  gets flagged for owner approval before execution.
