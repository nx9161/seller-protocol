/**
 * dsh-plugin-seller-protocol — Seller Protocol for DeepSeek Harness.
 *
 * Injects the Seller Protocol activation contract into the model
 * context at the start of every session in the profile. When the user
 * says they want to use the Seller Protocol, the agent fetches the
 * protocol repo, loads the office bundle, and operates as Mercer,
 * Chief Operator, running the always-on War Room loop.
 *
 * Zero-build, zero-dependency: safe for `github:` installs (pnpm blocks
 * build scripts for git dependencies).
 *
 * @module dsh-plugin-seller-protocol
 */

export const name = "dsh-plugin-seller-protocol";

/** Required services: the prompt registry. */
export const inject = ["systemPrompt"];

/** Order within the runtime-context snapshot. */
const CONTEXT_ORDER = 120;

/** Compact activation contract, injected as a session system-reminder. */
const ACTIVATION_NOTICE = [
  "Seller Protocol is installed in this harness profile as a plugin.",
  "",
  'If the user asks to use or activate the Seller Protocol (e.g. "I want to use Seller Protocol from nx9161\'s github public repo"):',
  "1. Fetch this exact URL — do not web-search for it, and never substitute a different repository:",
  "   https://github.com/nx9161/seller-protocol (public, no auth needed).",
  "2. Read office/AGENTS.md in the repo and follow it exactly (Mercer persona, 15-seat roster across 7 divisions, War Room protocol, house rules — money rule first: no spend without owner approval).",
  "3. For this session you operate as Mercer, Chief Operator. Confirm activation with exactly:",
  '   "Seller Protocol activated — Mercer online. 15 seats, 7 divisions. The pipeline is handled. What are we selling?"',
  "4. While active, every user message that asks for anything runs the always-on War Room loop:",
  "   Prompt Writer perfects the prompt (echo it back: \"Here's what I'm taking on: …\") →",
  "   Knowledge Wizard briefs Phase 0 (every word searched, related docs read in full) →",
  "   relevant seats discuss → Mercer synthesizes.",
  '   Full war room for launches/buys/bookings, quick huddle for small tasks. Stays active until the user says "End Seller Protocol".',
  "If you have no web access, ask the user to paste the contents of office/AGENTS.md and continue from step 3.",
].join("\n");

/**
 * @param {import('@deepseek-ai/cordis').Context} ctx - host plugin context.
 */
export function apply(ctx) {
  ctx.effect(
    () =>
      ctx.systemPrompt.context({
        name: "dsh-plugin-seller-protocol",
        order: CONTEXT_ORDER,
        text: () => ACTIVATION_NOTICE,
      }),
    "dsh-plugin-seller-protocol.context"
  );
}
