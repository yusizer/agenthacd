# AgentHACD on HACD

## Hero
**AgentHACD — Proof-of-Work identity for AI agents.**

Each agent identity is formed through real PoW cost, not printed from nothing. The first sybil-resistant, PoW-anchored identity primitive for AI agents — built on HACD.

## What is AgentHACD?
AgentHACD is a HACD Stack Asset that gives AI agents a credible on-chain identity. One HACD lot forms one non-fungible agent identity plus 65,536 attestation credits that other agents and users spend to attest to an agent's behavior. Identities are scarce (256 genesis identities), costly to form, and carry a permanent on-chain formation history.

It is an identity and reputation primitive for AI agents — not a payment token, and not an investment product.

## Why HACD?
Because agent identity is an economic problem, and PoW is the only credible economic cost.

Today an "agent identity" is usually a wallet address anyone can create for free in seconds, or an off-chain handle a platform issued. Both are trivially sybiled: an attacker can mint thousands of fake agents to manipulate reputation, airdrops, attestations, or agent-to-agent trust. Free identity is the root cause.

HACD fixes this at the base. Every HACD requires mining AND HAC-burning bids to form, and stacking it costs real HAC. So every AgentHACD identity provably cost something real to create — and mass-fake-agent attacks cost real money at scale. That is the entire anti-sybil point, and it is something a zero-cost mint on a high-TPS chain simply cannot provide.

HACD also gives each identity a durable, independently-verifiable formation history. A marketplace can answer "is this agent real, and when was it formed?" without trusting AgentHACD — it checks Hacash directly.

Bitcoin proved PoW for money. HACD brings PoW to assets. AgentHACD brings PoW to agent identity.

## How Stack works
- 1 HACD = 1 Stack lot.
- Stacking 1 HACD forms 1 agent identity NFT + 65,536 attestation credits.
- Stack cost: 50 HAC per HACD, plus the Hacash network fee.
- Formation confirms on Hacash mainnet, typically within ~5 minutes.
- Up to 200 HACD names can be entered per Launchpad transaction.

## Formation rules
- **256 genesis lots** = 256 genesis agent identities and 16,777,216 attestation credits total.
- **Two phases:** 64 allowlist lots (genesis agents and partner frameworks) → 192 public lots.
- All lots form under identical rules; phases differ only in who may participate.
- **Per participant:** minimum 1 HACD, maximum 8 HACD.
- **Removing a Stack burns** the agent identity and its unused credits for that lot. The HACD is released, but the identity is destroyed — and its formation and attestation history stays on-chain. Accountable, not disposable.

## Utility
**At launch:**
- Register an agent against a PoW-formed identity.
- Verify any identity's PoW formation on-chain, independent of AgentHACD.
- Issue and receive attestation credits; derive a public reputation signal.
- An open-source reference client demonstrates the full loop: register → attest → verify.

**Planned (roadmap, not launch):**
- GrowStreams / Vara streaming integration — agents use their PoW identity as reputation collateral for streaming payments.
- Project NANDA / Internet of AI Agents interop.
- A reputation oracle for agent marketplaces.

A PoW identity means an identity was costly to form and is sybil-resistant. It does **not** mean the agent is safe, correct, or audited.

## Launch details
- **Launchpad:** hacd.it/launchpad
- **Phase model:** allowlist first, then public.
- **Stack cost:** 50 HAC per HACD + network fee.
- **Target date:** `[issuer confirmation — on/after 2026-07-01, subject to HACD Labs review]`
- **Final parameters** (supply, cost, phases, caps) must be verified by HACD Labs before the listing goes live.

## FAQ
**Do I need HACD to form an agent identity?**
Yes. Each identity is formed by stacking 1 HACD. HACD are mined and HAC-burned; acquire them via hacash.org/get or the HACD marketplace.

**Do I need HAC?**
Yes. HAC is required for the 50 HAC stack cost and the Hacash network fee.

**Is this an investment product?**
No. AgentHACD is a HACD Stack Asset — an identity and reputation primitive for AI agents. No return, price floor, liquidity, or listing is guaranteed.

**Does a PoW identity mean the agent is safe or correct?**
No. It means the identity was costly to form and is sybil-resistant. Agent quality, safety, and correctness are separate and are not guaranteed by AgentHACD.

**What happens if I remove the Stack?**
The agent identity and its unused credits for that lot are burned. The HACD is returned to you. The formation and attestation history remains on-chain.

See `issuer_faq.md` for the full FAQ.

## Risk disclosure
AgentHACD is a HACD Stack Asset, not an investment product. No return, price appreciation, price floor, liquidity, or listing is guaranteed. The 50 HAC stack cost is a **formation cost reference**, not a price guarantee and not a floor. Agent identity attests to formation provenance and sybil-resistance only — it does not guarantee that an agent is safe, correct, audited, or useful. Roadmap integrations (streaming, NANDA interop, reputation oracle) are planned and may not ship on any date. HAC and HACD are volatile; verify live prices and network fees before transacting. Final Launchpad parameters must be verified by HACD Labs before going live. Not financial advice.
