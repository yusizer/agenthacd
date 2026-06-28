# Review Checklist — AgentHACD

## Formation logic
- [x] Supply matches HACD lots: 256 lots × 65,536 = 16,777,216 attestation credits (`launch_spec.json` `asset.total_supply` = 16,777,216; `stack.units_per_hacd_lot` = 65,536).
- [x] Phase-lot sum: 64 (first) + 192 (public) = 256 = `total_hacd_lots`.
- [x] Stack cost is clear: 50 HAC per HACD; total formation cost 12,800 HAC (stated in `stack_design.md`).
- [x] Participant flow is clear: prepare HACD → prepare HAC → enter names → confirm Stack → verify → use identity.
- [x] `removal_effect` = `burn` (identity + unused credits burned; HACD released; history stays on-chain).
- [x] `hacd_per_lot` = 1 (standard).
- [x] `decimals` = 0 (integer attestation credits).
- [x] Asset type = `HYBRID`, documented (NFT identity + FT credits) in `stack_design.md`.

## Copy safety (no banned language)
- [x] No "guarantee(d)" of return, price, floor, liquidity, or listing anywhere in public copy.
- [x] No "floor price" — stack cost described only as "formation cost reference".
- [x] No "risk-free", "moon", "ROI", "yield", "profit", "Nx returns", "backed value".
- [x] Identity ≠ endorsement: copy explicitly states PoW identity does not mean the agent is safe/correct/audited.
- [x] "Not financial advice" present in `launchpad_copy.md` risk disclosure and `issuer_faq.md`.
- [x] Risk disclosure present in `launch_spec.json` `copy.risk_disclosure` and `launchpad_copy.md`.
- [x] No requests for seed phrases, private keys, wallet passwords, keystore, or custody.
- [x] No legal compliance claims.

## Utility clarity (launch vs roadmap separation)
- [x] Launch utility stated honestly: register → attest → verify (reference client).
- [x] Roadmap items (GrowStreams streaming, NANDA interop, reputation oracle) labeled planned, not current, in `project_profile.md`, `stack_design.md`, `launchpad_copy.md`, `issuer_faq.md`.
- [x] "Nothing yet" not used because there is real launch utility — but it is scoped honestly.
- [x] No roadmap item presented as launch utility anywhere.

## Terminology
- [x] HACD described as PoW-native asset container / diamond identifier (not a HAC+Diamond composite; not a plain NFT).
- [x] HAC described as Hacash currency for stack cost and network fees.
- [x] Stack described as forming an asset state on HACD, not "just minting".
- [x] No claim that stack cost sets a price or that participants receive assured returns.

## Launch readiness
- [ ] Links verified (Launchpad URL `hacd.it/launchpad` is canonical; verify live before posting).
- [ ] Founder contact, project website, X handle filled in (`launch_spec.json` `project` — currently `Needs issuer confirmation`).
- [ ] Exact target launch date confirmed (currently `Needs issuer confirmation`).
- [ ] Final `max_hacd_per_participant` cap confirmed (drafted at 8).
- [ ] Open-source reference client (register → attest → verify) implemented and working — Utility-at-launch must be demonstrable, not claimed.
- [ ] `launch_spec.json` passes `validate_launch_spec.py --strict` with no ERRORs (run before submission; paste validator output `OK: launch spec passed basic validation`).
- [ ] `issuer_confirmed` and `hacd_labs_reviewed` flipped to `true` only after those reviews actually happen (left `false` for the draft — expected).
- [ ] HACD Labs reviews final parameters before Launchpad publication.

## Submission completeness (per CAMPAIGN.md)
- [x] `issuer_intake_form.md`
- [x] `incubator_fit_review.md`
- [x] `project_profile.md`
- [x] `stack_design.md`
- [x] `launch_spec.json`
- [x] `launchpad_copy.md`
- [x] `issuer_faq.md`
- [x] `x_announcement.md`
- [x] `review_checklist.md`
- [ ] Validator output screenshot/paste showing `OK: launch spec passed basic validation`
- [ ] Package submitted as ZIP or GitHub repo link before the deadline

## Open items before submission
1. Fill founder contact + website + X + target date (issuer).
2. Implement the reference client so launch utility is real.
3. Run the validator in `--strict`; fix any ERROR; capture the `OK` output.
4. Begin genuine community outreach to agent-framework teams (real traction signal).
5. Confirm with HACD Labs that the bounty/quest is still accepting submissions (Wizzhq listing shows 2026-07-01; the parallel hacd.it Cohort 2 closed 2026-06-27).
