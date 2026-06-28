# Project Profile: AgentHACD

## One-liner
PoW-anchored AI agent identity — the first sybil-resistant, on-chain agent identity formed through real Proof-of-Work cost on HACD.

## Category
AI agent (identity primitive)

## Problem
AI agents are being deployed across Web3 at scale — in marketplaces, agent-to-agent protocols, payment flows, and autonomous services. But agent identity today is either (a) a wallet address anyone can create for free in seconds, or (b) an off-chain handle a platform issued. Both are trivially sybiled: an attacker can mint thousands of fake agents to manipulate reputation, airdrops, attestations, votes, or agent-to-agent trust. The result is that "which agent did this?" has no credible on-chain answer, and no protocol can economically prevent agent spam. Free identity is the root cause.

## Asset concept
AgentHACD forms agent identity through PoW. One HACD lot = one non-fungible agent identity, formed by stacking a mined, HAC-burned HACD plus 50 HAC stack cost. Each lot also carries 65,536 fungible attestation credits that other PoW-formed agents and users spend to attest to an agent's observed behavior, producing a transparent on-chain reputation signal. Identities are scarce (256 genesis identities), costly to form, and carry permanent formation history. Burning an identity leaves the history on-chain — accountable, not disposable. The asset is the identity and its reputation surface; it is not a payment token and not an investment.

## Why HACD
Because sybil resistance for identity is an economic problem, and PoW is the only credible economic cost. HACD is a PoW-native asset container: every HACD requires mining AND HAC-burning bids to form, and stacking it costs real HAC. That means every AgentHACD identity provably cost something real to create — so mass-fake-agent attacks cost real money at scale, which is the entire anti-sybit point. A zero-cost mint on a high-TPS chain cannot do this; the formation cost there is ~0, so the sybil resistance is ~0. HACD also gives each identity a durable, on-chain, independently-verifiable formation history — exactly what an agent marketplace needs to answer "is this agent real, and when was it formed?" HACD Stack Assets are *formed*, not merely deployed — and for identity, that distinction is the whole value.

## Target users
- **Agent framework teams** (CrewAI, LangGraph, AutoGen, MCP-based agents) that want to attribute actions to a verifiable, non-sybil identity.
- **Agent marketplaces and registries** that need a sybil-resistant reputation signal before listing or routing to an agent.
- **Agent-to-agent protocols** (including Internet-of-AI-Agents style networks) that need a credible "who called whom" layer.
- **Builders and researchers** working on agent identity, reputation, and trust.

## Launch readiness
- **Ready at launch:** identity registration (stack a HACD → form an agent identity NFT + credits), on-chain identity lookup/verification, and attestation credits with an open-source reference client demonstrating register → attest → verify. Supply math is consistent and validator-clean.
- **Not ready / planned (roadmap):** GrowStreams/Vara streaming integration (agents use PoW identity as reputation collateral for streaming payments), Project NANDA / Internet of AI Agents interop, and a reputation oracle for agent marketplaces. These are explicitly roadmap, not launch utility.
- **Needs issuer confirmation before submission:** founder contact, project website/X, exact Launchpad date, final per-participant cap. Final Launchpad parameters must be verified by HACD Labs before going live.
