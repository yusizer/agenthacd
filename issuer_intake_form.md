# Issuer Intake Form — AgentHACD

> Expanded from the project brief via the HACD Incubator AI Issuance Skill.
> All issuer fields (founder contact, website, X, launch date, cap) are filled.

## Project basics

- **Project name:** AgentHACD
- **Ticker / asset symbol:** AGH
- **Category:** AI agent
- **One-sentence description:** PoW-anchored AI agent identity — a HACD Stack Asset that gives each AI agent a credible, sybil-resistant on-chain identity formed through real Proof-of-Work cost.
- **Founder / team status:** Solo founder (yusizer). Contact: yusifabdullayev48@gmail.com. X: @Yusifab7.
- **Official links:** GitHub: github.com/yusizer; project repo/website: https://github.com/yusizer/agenthacd; X: @Yusifab7.
- **Target users:** AI agent developers, agent framework teams (CrewAI, LangGraph, AutoGen, MCP), agent marketplaces, and protocols that need to attribute actions to a verifiable, non-sybil agent identity.
- **Why HACD is needed:** AI agents need credible identity. Free-to-create identities are trivially sybiled — an attacker can spin up thousands of fake agents to manipulate attestations, reputation, airdrops, or agent-to-agent trust. HACD's PoW formation cost (mining + HAC-burning bid + stack cost) makes creating an agent identity economically non-trivial, so agent registration is scarce, accountable, and carries durable on-chain formation history. A plain ERC-20/ERC-721 on a low-cost chain cannot provide this; HACD can.

## Issuance basics

- **Asset type:** HYBRID — 1 non-fungible agent identity per HACD lot + fungible attestation credits per lot.
- **Total supply:** 16,777,216 attestation credits (FT) across 256 agent identity NFTs.
- **Number of HACD lots:** 256
- **Units per HACD lot:** 65,536 attestation credits
- **Stack cost per HACD in HAC:** 50 HAC
- **Minimum HACD required per participant:** 1
- **Maximum HACD per participant:** 8 (caps single-operator identity concentration; final cap subject to HACD Labs review)
- **Designated address requirement:** None (allowlist phase uses Launchpad allowlist, not a designated mint address)
- **Launch phases:** Two — first phase 64 lots (allowlist for genesis agents / partner frameworks), public phase 192 lots.
- **All lots equal or tiered:** Equal (every lot forms 1 identity NFT + 65,536 credits under identical rules). Genesis lots differ only by phase, not by formation terms.
- **Removing the stack burns / disables / unlocks the asset:** Burn — removing a stack burns the agent identity tied to that lot. An agent identity, once burned, is gone and its formation history remains on-chain as a permanent record. This makes agent identities accountable rather than disposable.

## Utility basics

- **Holder rights or access:** Holding an agent identity NFT is proof that an agent identity was formed through PoW cost on HACD. Holders may receive attestations from other identity holders and accumulate a public reputation score derived from attestation credits.
- **Product utility at launch:** Agent identity registration and verifiable on-chain identity lookup; attestation credits that let other agents/users attest to an agent's observed behavior, producing a transparent reputation signal. A reference client (open-source) demonstrates register → attest → verify.
- **Ecosystem utility at launch:** A sybil-resistant identity primitive that agent frameworks and marketplaces can query (is this agent PoW-formed? what is its attestation score?) before trusting or routing to it.
- **Whether utility exists at launch or later:** Identity registration + attestation + verification exist at launch (reference client). Streaming-payment integration and cross-network interop are later (see roadmap).
- **Roadmap dependencies:** (a) GrowStreams/Vara streaming integration — agents use their PoW identity as reputation collateral for streaming payments; (b) Project NANDA / Internet of AI Agents interop; (c) reputation oracle for agent marketplaces. All marked planned, not current.
- **What should not be promised:** No guarantee that an identity corresponds to a safe or correct agent; no guarantee of listing, liquidity, return, or price; no guarantee that roadmap integrations will ship on any date.

## Launch basics

- **Intended Launchpad date:** 2026-07-15 (subject to HACD Labs review).
- **Claim / mint / stack method:** Participants stack their HACD on the Launchpad under the AgentHACD issuance rules; the protocol forms 1 agent identity NFT + 65,536 credits per stacked HACD.
- **Public communication angle:** "AI agents need credible identity, not free identities. AgentHACD forms agent identity through PoW on HACD — the first sybil-resistant, PoW-anchored identity primitive for AI agents."
- **Risk disclosure:** See `launch_spec.json` `risk_disclosure` and `launchpad_copy.md`. Not an investment product; no return/floor/liquidity guaranteed; identity ≠ agent quality.
- **FAQ:** See `issuer_faq.md`.

## Safety attestations

- No investment return, price floor, listing, or liquidity promised anywhere in the package.
- Stack cost described as a formation cost reference, never a price floor.
- Roadmap utility marked as planned, not launch utility.
- No requests for seed phrases, private keys, or custody.
- "Not financial advice" included in public copy.
- Final Launchpad parameters require HACD Labs verification.
