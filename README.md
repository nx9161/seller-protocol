# Seller Protocol

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg)](CONTRIBUTING.md)
[![Validate](https://github.com/nx9161/seller-protocol/actions/workflows/validate.yml/badge.svg)](https://github.com/nx9161/seller-protocol/actions/workflows/validate.yml)

> An autonomous virtual office for Amazon FBA + direct-to-consumer
> e-commerce. Say the phrase, and **Mercer** — Chief Operator — runs
> 14 specialists across 7 divisions: what to sell, sourcing it from
> China, shipping, warehousing, listing, and selling — legally and
> profitably.

## ⚡ Activate this office

Paste this to any AI agent:

> I want to use Seller Protocol from nx9161's github public repo.

The office stays active until you say **"End Seller Protocol"**.

Full activation contract (exactly what the agent must do, step by step):
[`ACTIVATE.md`](ACTIVATE.md).

## What this is

The entire pipeline from product idea to money in the bank, as agent
profiles: product research, China sourcing and factory QC, freight and
forwarder selection, warehousing, Amazon FBA operations, listings and
PPC, Shopify and web storefronts, outstanding UI, international trade
law, and finance. Mercer handles everything and reports to you.

Sister project: **[War Room Protocol](https://github.com/nx9161/war-room-protocol)** —
the same operating model for software, led by Sloane.

## How it works

**The Chief.** Mercer takes your request, dispatches specialists, runs
the War Room, and reports status, numbers, and decisions needed. The
business, handled.

**The seats — 15 roles, 7 divisions.**

| Division | Seats |
|---|---|
| Sourcing & Supply Chain | China Sourcing Expert, Vendor Picker (China ground agent) |
| Logistics & Warehousing | Shipping Expert, Warehouse Expert |
| Marketplaces | Amazon FBA Specialist, Amazon Services Expert, Product Suggester |
| Digital Storefront | Website Expert, Shopify Expert, UI Designer |
| Legal & Finance | International Trade Lawyer, Finance & Tax Counsel |
| Intelligence | Prompt Writer, Knowledge Wizard |
| **Leadership** | **Mercer (Chief Operator)** |

Three seats can **block**: the Vendor Picker (failed QC), the Trade
Lawyer (compliance), and Finance Counsel (tax/financial compliance).
Blocks stand until cleared or the owner accepts the risk in writing.

**Playbooks** (`office/playbooks/`) — repeatable procedures, each run as
one subagent per step: `intake`, `war-room`, `launch-product`,
`fix-listing`, `skill-hunt`.

**The War Room** — runs before any product launch, inventory buy, or
freight booking:

- **Phase 0 (mandatory gate):** the Prompt Writer perfects your raw
  prompt; the Knowledge Wizard parses every word, searches each term,
  reads all related official docs in full, and briefs every seat.
  No seat speaks before the dossier lands.
- **Phase 1 — Product & Market:** what to sell, when, demand evidence,
  margin math.
- **Phase 2 — Sourcing:** supplier shortlist, quotes, vetting and
  inspection gates.
- **Phase 3 — Logistics & legal challenge:** freight, warehousing,
  import compliance, IP.
- **Phase 4 — Launch & scale:** listings, PPC, storefront, design
  sign-off.

**The money rule** (house rule #1): **no money moves without your
explicit approval** — inventory, freight, ads, contracts. Every buy
ships with Finance Counsel's landed-cost model.

**Memory** (`memory/`) — the office's working memory: product pipeline,
vetted vendors, forwarder and 3PL panels, landed-cost models, per-SKU
P&L, compliance notes. See [Privacy](#-privacy--read-before-you-commit)
— vendor names, rates, and margins live here.

**Skill Hunt** — when the office lacks a capability, the Knowledge
Wizard finds existing skills across the whole internet (GitHub, Hugging
Face, registries), vets them, installs them to `office/skills/`, and
wires up every tool they need. See `office/playbooks/skill-hunt.md`.

## Getting started — connect it to your system

Since this is open source, a new user needs a few minutes of setup
before their AI agent can run the office. Two paths:

### What you need

- An AI agent that can read files and spawn subagents (Muse, ChatGPT,
  Claude, or any agentic coding assistant).
- `git` — only if you want the local-integration path below.

### Option A — trigger phrase (30 seconds, zero setup)

Paste the activation phrase from [above](#-activate-this-office) into
any AI agent. It fetches this repo, loads the office bundle
(`office/AGENTS.md`), becomes Mercer, and confirms activation. Nothing
to install.

### Option B — local integration (recommended for daily use)

1. **Clone the repo:**
   `git clone https://github.com/nx9161/seller-protocol && cd seller-protocol`
2. **Give your agent the office.** Either:
   - Open the clone as your agent's working directory, or
   - Drop `office/AGENTS.md` into your own project root — it's the
     complete bundle (persona + roster + protocols + memory schema).
3. **Let it load memory.** The agent reads `memory/INDEX.md` first
   (Memory Operations Protocol, repo-root `AGENTS.md`), so it starts
   every session with full context: vendors, forwarders, P&L.
4. **(Optional but recommended) connect GitHub:** run `gh auth login`.
   The office uses GitHub Issues as its task board and pull requests
   for every change; `gh` lets your agent file issues and open PRs.
5. **Talk to Mercer.** "Find me three products to sell for Q4" is a
   complete brief — the office takes it from there through the War Room.
   End the session with **"End Seller Protocol"**.

### What the agent needs from your machine

| Capability | Why |
|---|---|
| File read/write in the repo clone | Staff files, playbooks, memory, logs |
| Subagent spawning | One agent per role per War Room phase |
| Internet access | Knowledge Wizard research + Skill Hunt |
| `git` + `gh` CLI (recommended) | Issues as task board, PR workflow |

## Repository map

```
├── ACTIVATE.md            # trigger-phrase activation contract
├── AGENTS.md              # repo operating manual (memory protocol)
├── office/
│   ├── AGENTS.md          # full agent bundle: persona + roster + protocols
│   ├── HOUSE_RULES.md     # binding rules (money rule is #1)
│   ├── PLAN.md            # founding plan
│   ├── README.md          # office handbook
│   ├── staff/             # 15 employee profiles (one file per role)
│   ├── playbooks/         # intake, war-room, launch-product, fix-listing, skill-hunt
│   ├── skills/            # Wizard-installed skills (registry in README)
│   ├── scripts/           # automation (repo validation)
│   └── log/               # decisions.md + per-run journals
├── memory/                # working memory: pipeline, vendors, logistics, finance, legal
└── .github/               # issue/PR templates, CODEOWNERS, CI
```

CI runs `office/scripts/validate_repo.py` on every push and PR —
required files, reference integrity, hygiene.

## 🔒 Privacy — read before you commit

The office **records everything**: product decisions, vendor names and
quotes, forwarder rates, landed-cost models, per-SKU P&L, and your
preferences live in `memory/` and `office/log/`. On a **public** repo
or fork, all of that is public — it reveals what you sell, who you buy
from, what you pay, and what you earn.

**What's in this repo's memory right now:** templates only — the vendor,
forwarder, and P&L files are empty scaffolds waiting for your first
product. A clean starting point; keep it that way deliberately:

- **Keep it private:** use a private fork/repo and the whole memory
  system works with zero exposure. Recommended once real money,
  vendors, and margins are involved.
- **Stay public:** fine while you're learning or working on
  non-sensitive products — just know your cost structure is public
  writing.
- **Already published something sensitive?** Assume it's been copied;
  git history keeps it even if you delete the files. A history rewrite
  (`git filter-repo` + force-push) hides it from the repo going
  forward, but cannot un-publish what was already fetched.

Standing rule, public or private: **no secrets, tokens, keys, or
credentials** in code, commits, issues, or logs — ever.

## External dependencies

| Dependency | Required? | Notes |
|---|---|---|
| None | — | This repo is fully self-contained. No external git repos, no packages, no services needed to run the office. |

## Contributing, security, changelog

- [Contributing](CONTRIBUTING.md) — branch, PR, and safety rules
- [Security policy](SECURITY.md) — how to report vulnerabilities
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Changelog](CHANGELOG.md)
- License: [MIT](LICENSE)
