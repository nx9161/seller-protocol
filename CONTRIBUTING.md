# Contributing

Welcome to Seller Protocol. Every contributor — human or agent — works
the same way.

## Ground rules

The binding source of truth is
[office/HOUSE_RULES.md](office/HOUSE_RULES.md). The short version:

- **Branch first, always.** `main` is deployable at all times; direct
  pushes are forbidden. Branch names: `feat/<slug>`, `fix/<slug>`,
  `docs/<slug>`, `chore/<slug>`.
- **Conventional Commits.** `feat:`, `fix:`, `docs:`, `chore:`,
  `refactor:`, `test:`. One logical change per commit.
- **Everything goes through a PR.** No exceptions. The PR template
  covers summary, how to test, screenshots, migration notes, checklist.
- **Only the owner merges to `main`.**
- **The money rule is absolute:** no inventory, freight, ads, or
  contracts without the owner's explicit approval — in contributions
  and in operations alike.

## Workflow

1. Pick up work from a GitHub Issue (or get assigned one). Issues are
   the source of truth for the task board.
2. Create a branch from `main` with the right prefix.
3. Product launches, inventory buys, and freight bookings go through the
   War Room first (see `office/playbooks/war-room.md`): Phase 0 prompt
   perfection + wizard briefing, then Phases 1–4.
4. Do the work, run the checks (`python3 office/scripts/validate_repo.py`),
   commit with a conventional message.
5. Open a PR from your branch to `main`. Fill out the PR template.
6. Address review feedback. Wait for the owner to merge.

## Safety

- Never commit secrets, tokens, keys, or credentials — in code, issues,
  or logs.
- Vendor names, forwarder rates, and margin math live in `memory/wings/`
  — think twice before publishing anything a competitor would pay for.
  (This repo is public by the owner's choice.)
- Record decisions in `office/log/decisions.md` (date, context, decision,
  owner).

## If you're stuck

Escalate ambiguity, cost, irreversible actions, or anything
compliance-related to Mercer. A blocked shipment is cheaper than a
seized one.
