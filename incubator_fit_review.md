# Incubator Fit Review: AgentHACD

## Verdict
**Strong fit.**

## Why it fits HACD
AgentHACD is one of the clearest possible HACD Stack use cases because it needs exactly what PoW provides and exactly what cheap-issuance chains cannot provide:

- **Credible asset origin.** An agent identity is only useful as a trust signal if it is non-trivial to create. HACD identities are formed through mining + HAC-burning bids + stack cost, so every agent identity carries a real, verifiable formation cost and a durable on-chain origin. A free-to-mint identity on a low-cost chain carries none of this and is sybil-trivial.
- **PoW-backed formation cost.** Sybil resistance for agent identity is an economic problem, not a cryptography problem. PoW formation cost makes mass-fake-agent attacks economically infeasible in a way that a zero-cost mint cannot. This is the core HACD thesis ("PoW brings credible formation cost to assets") applied to identity.
- **Scarce HACD containers.** 256 genesis lots = 256 genesis agent identities. Scarcity is not a marketing choice here; it is the anti-spam property. The cap directly serves the utility.
- **Visible on-chain formation progress.** Agent identity formation is observable on Hacash mainnet (formation confirms in ~5 minutes), so an agent's "I am PoW-formed" claim is independently checkable by any framework or marketplace.
- **Durable identity / state history.** Each agent identity carries a permanent formation history. Burning an identity leaves the history on-chain — accountable, not erasable. This is exactly the "durable formation history" HACD Stack is built to provide.
- **Community formation around Stack lots.** Allowlist → public phasing lets partner agent frameworks and early builders claim genesis identities, creating real community formation around the issuance rather than a speculative mint.

This matches the Cohort 2 "Who Should Apply" line directly: *AI agent builders exploring HACD as an identity container.*

## What HACD adds
- **PoW container:** each agent identity is anchored to a unique, mined, HAC-burned HACD — not a contract address anyone can clone.
- **Formation cost:** 50 HAC + 1 HACD + network fee per identity. Forming 1,000 fake agents costs ~1,000× that, which is the entire anti-sybil point.
- **Asset history:** formation + attestation history is permanent and on-chain; burned identities leave a trace.
- **Community formation:** 64 genesis (allowlist) + 192 public lots create a real issuance community, not a silent deploy.

## Main concerns
- **Utility-at-launch must be demonstrable, not promised.** The reference client (register → attest → verify) must actually work for the submission to score on Utility clarity. A slide is not enough.
- **Identity ≠ endorsement.** Copy must never imply that a PoW identity means an agent is safe, correct, or audited. It means the identity was costly to form and is sybil-resistant — nothing more. This is a Copy-safety risk to police.
- **Founder credibility / contact.** Currently `Needs issuer confirmation`. Team credibility is a judged dimension; the founder must be identifiable and reachable before submission.
- **Roadmap vs launch separation.** GrowStreams streaming integration, NANDA interop, and the reputation oracle are roadmap. They must be labeled planned everywhere; any hint of "launches with streaming" is a Utility-clarity deduction.

## Required issuer confirmations
- Founder real name + contact (email/X/Telegram) for `project.contact` and Team credibility.
- Project website + official X handle (currently empty).
- Final target Launchpad date (on/after 2026-07-01, subject to HACD Labs review).
- Final `max_hacd_per_participant` cap (drafted at 8).
- Confirmation that the reference client (register/attest/verify) is the launch utility and works.

## Recommended next step
1. Founder fills the `Needs issuer confirmation` fields above.
2. Generate `stack_design.md` + `launchpad_copy.md` + `launch_spec.json` from this review (done in this package).
3. Build the open-source reference client (register → attest → verify) so Utility-at-launch is real, not claimed.
4. Run `validate_launch_spec.py --strict` on `launch_spec.json`; fix any ERROR.
5. Write the X announcement set and begin genuine community outreach to agent-framework teams (real traction is a judged signal).
6. Submit the complete package (ZIP or GitHub repo) per CAMPAIGN.md before the deadline, after HACD Labs reviews final parameters.
