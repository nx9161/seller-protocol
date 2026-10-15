---
name: fba-math
description: Unit profit and restock math for Amazon FBA — referral + fulfillment fee breakdown, landed-cost assembly, margin/ROI, and reorder planning. Assists Finance Counsel; never replaces the signed-off landed-cost model.
version: 1.0.0
source: Concepts informed by shen169/amazon-fba-skills (MIT claimed in frontmatter; no LICENSE file found — inspiration only, nothing vendored). All wording and structure are original to this office.
license: MIT
installed: 2026-10-15
---

# FBA Math — unit profit & restock calculator

Do the arithmetic behind every buy decision. Two tools, one rule:
**the numbers here assist Finance Counsel's landed-cost model — they
never replace it.** No inventory purchase happens without Finance
Counsel's signed-off model and the owner's explicit approval (money
rule).

## Freshness guardrail (binding)
Amazon's fee schedules change. **Never hardcode fee tables into a
decision.** Before any calculation that matters, the Knowledge Wizard
verifies the current referral and FBA fulfillment fees against Amazon's
official fee schedule in Phase 0. A calculation built on last year's
fees is a wrong calculation.

## Tool 1 — Unit profit breakdown

Inputs: selling price, marketplace, product cost (CNY), dimensions
(cm), weight (kg), inbound freight mode, ad spend per unit (optional).

1. **Dimensional weight:** `vol_weight_kg = (L × W × H) / 5000`.
   Chargeable weight = max(actual, dimensional).
2. **Inbound freight:** chargeable weight × current per-kg rate for
   the chosen mode (sea/air/express — Shipping Expert's live quotes
   beat any table).
3. **Amazon fees:** referral fee (price × category rate — verify
   current) + FBA fulfillment fee (size tier + weight — verify
   current).
4. **Landed cost per unit:** product cost + inbound freight + prep +
   any per-unit overhead, in the marketplace currency.
5. **Outputs:** net profit per unit, net margin %, ROI on cash
   invested. Show the full trace — every line item visible, nothing
   hidden in a black box.

Kill rule: if net margin % is below the owner's floor after honest
inputs, the answer is NO — say it plainly with the numbers.

## Tool 2 — Restock planner

Inputs: average daily sales, domestic prep days, shipping days,
safety days, restock frequency.

1. **Total lead time** = prep days + shipping days + safety days.
2. **Safety stock** = daily sales × safety days × stability factor
   (stable 1.0 / fluctuating 1.3 / unstable 1.6 — set from actual
   sales variance, not optimism).
3. **Order quantity** = daily sales × restock frequency + safety
   stock − current inbound/inventory.
4. **Reorder date** = today + (days of cover remaining − total lead
   time). If that's in the past, flag it loud: you're already late.

## Who uses this
- **Finance Counsel:** runs it, signs the model.
- **Product Suggester / Amazon FBA Specialist:** quick margin sanity
  checks during research — flagged clearly as estimates, not models.
- **Warehouse Expert:** restock timing inputs (3PL receiving times).
