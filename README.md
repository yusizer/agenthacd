# AgentHACD — PoW-anchored AI agent identity

> A HACD Stack Asset launch package for the HACD Labs Stack Token Incubator.
> Bitcoin proved PoW for money. HACD brings PoW to assets. AgentHACD brings PoW to agent identity.

## What this is

AgentHACD gives AI agents a credible on-chain identity by **forming** it on HACD's
Proof-of-Work container. One HACD lot forms one non-fungible agent identity plus
fungible attestation credits. Because identity formation costs real PoW + HAC,
creating fake agents is economically non-trivial — which is the entire anti-sybil
point, and something a zero-cost mint on a high-TPS chain cannot provide.

This repository is the complete launch package (8 documents + a machine-checkable
`launch_spec.json`) prepared with the [HACD Incubator AI Issuance Skill](https://github.com/Satyam-10124/hacd-incubator-ai-issuance-skill).

## Why HACD (PoW fit)

AI agent identity is an **economic** problem, not a cryptography problem. Free
identities are sybil-trivial: an attacker can mint thousands of fake agents for
~$0 to manipulate reputation, airdrops, attestations, or agent-to-agent trust.
PoW formation cost makes mass-fake-agent attacks cost real money at scale. HACD
also gives each identity a durable, independently-verifiable on-chain formation
history. This matches the Incubator's "Who Should Apply" line directly: *AI agent
builders exploring HACD as an identity container.*

## Package contents

| File | Purpose |
|------|---------|
| `launch_spec.json` | Machine-readable launch spec (validator-clean) |
| `issuer_intake_form.md` | Full 40-field issuer intake |
| `incubator_fit_review.md` | Fit review — verdict: Strong fit |
| `project_profile.md` | Project profile, problem, concept, why HACD |
| `stack_design.md` | Stack logic, supply math, formation rules, participant flow |
| `launchpad_copy.md` | Public Launchpad page copy |
| `issuer_faq.md` | FAQ |
| `x_announcement.md` | X announcement set (official, educational, founder, thread, 3 hooks) |
| `review_checklist.md` | Pre-submission review checklist |
| `validate.py` | Compact spec validator (mirrors the official `validate_launch_spec.py`) |
| `client/` | **Reference client** — register → attest → verify (7/7 tests pass, demo runs) |

## Supply math

```
total_supply           = total_hacd_lots × units_per_hacd_lot
                       = 256 × 65,536        = 16,777,216 attestation credits
agent_identities       = 256                 (1 NFT per lot)
formation_cost_hac     = 256 × 50            = 12,800 HAC
phase_lots             = 64 (allowlist) + 192 (public) = 256
```

Stack cost tier: 50 HAC/HACD (onboarding tier, 10–50) — real enough to deter sybil
spam, accessible to genuine agent builders. The 16,777,216 figure mirrors HACD's
16^6 possible names — one attestation-credit unit per possible HACD name.

## Validate

```bash
python validate.py launch_spec.json --strict
# OK: launch spec passed validation
# Formation cost reference: 12,800 HAC + network fees
```

Draft warnings (`issuer_confirmed` / `hacd_labs_reviewed` = false, empty
website/contact) are expected for a draft and are resolved before submission.

## Utility

**At launch (honest):** register an agent against a PoW-formed identity; verify any
identity's PoW formation on-chain; issue and receive attestation credits. The
open-source reference client in `client/` implements the full loop — **7/7 tests pass**
and the demo runs end-to-end (register two identities, attest, verify the reputation
signal). This is demonstrated utility, not a promise.

**Planned (roadmap, not launch):** GrowStreams/Vara streaming integration (PoW
identity as reputation collateral for streaming payments); Project NANDA / Internet
of AI Agents interop; a reputation oracle for agent marketplaces.

A PoW identity attests to formation provenance and sybil-resistance only. It does
**not** mean the agent is safe, correct, audited, or useful.

## Safety

No investment return, price floor, liquidity, or listing is guaranteed anywhere in
this package. Stack cost is described as a **formation cost reference**, never a
price floor. No banned promo language ("guarantee", "floor", "moon", "ROI", "yield",
"profit"). Not financial advice. Final Launchpad parameters must be verified by
HACD Labs before going live.

## License

Package contents: MIT (see the issuer's choice for the eventual on-chain asset).
