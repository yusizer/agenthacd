# FAQ — AgentHACD

## Do I need HACD?
Yes. Each agent identity is formed by stacking 1 HACD. HACD are unique, mined, HAC-burned PoW containers — acquire them via hacash.org/get or the HACD marketplace (hacash.diamonds / sea.hacash.diamonds). You cannot form an AgentHACD identity without a HACD.

## Do I need HAC?
Yes. HAC is required for the 50 HAC stack cost per HACD and for the Hacash network fee. HAC trades on CoinEx, Vindax, and Dex-trade (`[VERIFY LIVE]` before transacting).

## Is this an investment product?
No. AgentHACD is a HACD Stack Asset — an identity and reputation primitive for AI agents. No profit, return, price floor, liquidity, or listing is guaranteed. The 50 HAC stack cost is a formation cost reference, not a price floor.

## What exactly does a PoW agent identity attest to?
It attests that the identity was costly to form (real PoW + HAC stack cost) and is therefore sybil-resistant, and that it carries a durable, on-chain, independently-verifiable formation history. It does **not** attest to the agent being safe, correct, audited, useful, or honest. Identity is provenance, not endorsement.

## How many agent identities will exist?
256 genesis identities — one per HACD lot. 64 are reserved for allowlist (genesis agents and partner frameworks); 192 are public. Scarcity is intentional: it is the anti-spam property.

## What are attestation credits?
Each identity is formed with 65,536 fungible attestation credits (unit: `credit`). Other PoW-formed agents and users spend credits to attest to an agent's observed behavior. The accumulated attestations form a public, on-chain reputation signal. Credits are not a payment currency and carry no promised value.

## What happens if I remove the Stack?
The agent identity NFT and the unused attestation credits for that lot are **burned**. The HACD is released back to you. The on-chain formation and attestation history for that identity remains visible — so a misbehaving agent cannot silently disappear; the record that it existed and was attested to stays on-chain.

## Why HACD and not a cheap chain?
Because sybil resistance is an economic problem. On a zero-cost chain, forming 1,000 fake agent identities costs ~0, so the sybil resistance is ~0. On HACD, each identity costs real PoW + 50 HAC + a HACD, so mass-fake-agent attacks cost real money at scale. That cost is the entire value proposition, and only PoW provides it credibly.

## Can a marketplace verify an AgentHACD identity without trusting AgentHACD?
Yes. Formation is recorded on Hacash mainnet. A marketplace can query explorer.hacash.org / the HACD Stack Protocol API to confirm an identity's PoW formation independently. AgentHACD does not need to be trusted for the formation claim.

## What is live at launch vs planned?
**Live at launch:** identity registration, on-chain verification, attestation credits, and an open-source reference client (register → attest → verify).
**Planned (roadmap, no date):** GrowStreams/Vara streaming integration (PoW identity as reputation collateral for streaming payments), Project NANDA / Internet of AI Agents interop, and a reputation oracle for agent marketplaces.

## Is there a per-participant cap?
Draft cap: minimum 1 HACD, maximum 8 HACD per participant. The cap limits single-operator identity concentration to preserve the anti-sybil property. `[Needs issuer confirmation — final cap]`

## When does it launch?
`[Needs issuer confirmation — target on/after 2026-07-01, subject to HACD Labs review.]` Final Launchpad parameters (supply, cost, phases, caps) must be verified by HACD Labs before the listing goes live.

## Is this financial advice?
No. Nothing in this package is financial advice. HAC and HACD are volatile; verify live prices and network fees before transacting.
