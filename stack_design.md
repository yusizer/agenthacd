# Stack Design: AgentHACD

## Asset type
**HYBRID.** Each HACD lot forms two linked components:
- **1 non-fungible agent identity** (the agent's PoW-anchored on-chain identity), and
- **65,536 fungible attestation credits** (unit name: `credit`) used to attest to agent behavior and derive a reputation signal.

The NFT is the identity; the credits are its reputation surface. They are formed together from one Stack action on one HACD lot and are not separable at formation.

## Supply
- **Total supply (attestation credits, FT):** 16,777,216
- **HACD lots:** 256
- **HACD per lot:** 1
- **Units per HACD lot:** 65,536 credits + 1 agent identity NFT
- **Agent identity NFTs (total):** 256

Arithmetic:
```
total_supply = total_hacd_lots × units_per_hacd_lot
            = 256 × 65,536
            = 16,777,216  ✓

agent_identities = total_hacd_lots × 1 = 256  ✓
```

The 16,777,216 figure mirrors the total possible HACD names (16^6) — one attestation-credit unit per possible HACD name — a deliberate symbolic tie between the identity layer and HACD's own scarcity.

## Stack cost
- **Cost per HACD (stack cost, in HAC):** 50 HAC
- **Estimated total formation cost:** 12,800 HAC
  ```
  formation_cost_hac = total_hacd_lots × stack_cost_hac_per_hacd
                     = 256 × 50
                     = 12,800 HAC  ✓
  ```
- **Network fee:** required (Hacash network fee per Stack transaction; `[VERIFY LIVE]` before launch).
- **Minimum backing reference per identity:** 1 HACD + 50 HAC + network fee. This is a **formation cost reference**, not a price floor and not a guaranteed value.

Cost tier rationale: 50 HAC/HACD sits in the 10–50 "maximize onboarding" tier, chosen so that forming an agent identity is real enough to deter sybil spam yet accessible to genuine agent builders. It is meaningfully below the Carat benchmark (100 HAC/HACD) because agent builders are the target audience and the goal is adoption of the identity primitive, not exclusivity.

## Formation rules
- 1 HACD = 1 Stack lot = 1 agent identity NFT + 65,536 attestation credits.
- All lots form under identical rules; the two phases differ only in *who* may participate, not in formation terms.
- Up to 200 HACD names can be entered per Launchpad transaction (per HACD Stack Protocol).
- Formation confirms on Hacash mainnet, typically within ~5 minutes.
- `removal_effect = burn`: removing a Stack burns the agent identity and its unused credits for that lot. The formation history remains on-chain permanently — a burned identity is gone, but the record that it existed and was attested to is not erased. This is the accountability property.

## Phases
- **First phase (allowlist):** 64 lots — reserved for genesis agents: partner agent-framework teams, early builders, and contributors. Allowlist managed via the Launchpad `allowlist` phase model.
- **Public phase:** 192 lots — open to any participant on the Launchpad.
- Phase-lot sum check:
  ```
  first_phase_hacd_lots + public_phase_hacd_lots = total_hacd_lots
  64 + 192 = 256  ✓
  ```
- **Per-participant bounds:** minimum 1 HACD, maximum 8 HACD (final cap subject to HACD Labs review). The cap limits single-operator identity concentration to preserve the anti-sybil property.

## Participant flow
1. **Prepare HACD** — obtain or already hold the HACD name(s) you intend to stack (HACD are mined and HAC-burned; acquire via hacash.org/get or the marketplace).
2. **Prepare HAC** — hold enough HAC for the 50 HAC stack cost per HACD plus the network fee.
3. **Enter HACD name(s)** on the AgentHACD Launchpad page (up to 200 per transaction).
4. **Confirm the Stack transaction** — the protocol forms the agent identity NFT + 65,536 credits per stacked HACD.
5. **Verify the formed asset** — check the identity and credits on hacd.it/launchpad and explorer.hacash.org.
6. **Use the identity** — register your agent against the identity in the reference client; receive and issue attestation credits.

## Removal / burn logic
Removing the Stack on a lot **burns** the agent identity NFT and the unused attestation credits for that lot. The HACD is released back to the holder, but the identity is destroyed and cannot be re-formed on that lot. The on-chain formation and attestation history for that identity remains visible — accountability, not erasure. This makes abandoning a misbehaving agent identity costly and visible rather than free and silent.

## Utility at launch (honest)
- Register an agent against a PoW-formed identity.
- Verify any agent identity's PoW formation on-chain (independent of AgentHACD).
- Issue and receive attestation credits; derive a public reputation signal.
- Open-source reference client: register → attest → verify.

## Utility that is planned, not launch (roadmap)
- GrowStreams/Vara streaming integration (PoW identity as reputation collateral for streaming payments).
- Project NANDA / Internet of AI Agents interop.
- Reputation oracle for agent marketplaces.
