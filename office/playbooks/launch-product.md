# Playbook: Launch Product

End-to-end pipeline for taking a product from idea to selling.
Run as one subagent per step; Mercer orchestrates.

1. **War Room.** Full four phases. Verdict must be GO (conditions
   cleared) before proceeding.
2. **Sample.** Sourcing Expert orders samples; Vendor Picker verifies
   against spec.
3. **Contract.** Terms sheet → Trade Lawyer review → owner approval →
   sign.
4. **Bulk + QC.** Place order (owner-approved funds); Vendor Picker
   runs the inspection plan. Failed QC = blocked shipment.
5. **Freight.** Shipping Expert books the vetted forwarder, all-in
   quote, customs docs checked.
6. **Warehouse.** Warehouse Expert receives, preps (FBA compliance),
   places inventory.
7. **List.** Amazon Services Expert builds the listing; FBA Specialist
   files the shipment plan; UI Designer signs off creatives.
8. **Launch.** PPC live within the owner-approved budget; Shopify
   product page live; test orders pass.
9. **Review (30 days).** Finance Counsel posts per-SKU P&L; Product
   Suggester flags restock or kill.

## Gates
Steps 3, 4, 5, and 8 each require explicit owner approval (money moves).
Any blocking seat can halt the pipeline at its gate.
