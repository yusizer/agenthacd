# AgentHACD reference client

A zero-dependency, off-chain reference implementation of the AgentHACD identity
loop: **register → attest → verify**. This is the launch utility described in
`../stack_design.md` and `../launchpad_copy.md`, made runnable so the utility is
demonstrated, not merely claimed.

> This is NOT the on-chain Stack. On-chain formation happens through the HACD
> Launchpad (hacd.it/launchpad), which HACD Labs configures from the validated
> `launch_spec.json`. This client mirrors that flow off-chain so the register →
> attest → verify loop can be run and tested with no HAC, no HACD, and no network.

## Run

```bash
# 1) Form a PoW-anchored agent identity (1 HACD lot = 1 identity + 65,536 credits)
python agenthacd.py register --agent "my-agent" --hacd WTYUIA --owner 0xABC

# 2) Have another identity attest to it (spends the attestor's credits)
python agenthacd.py register --agent "reviewer" --hacd AHXMBK --owner 0xREV
python agenthacd.py attest   --identity AGH-0001 --from AGH-0002 --credits 100 --note "reliable"

# 3) Verify the identity's PoW formation + reputation signal
python agenthacd.py verify   --identity AGH-0001

# 4) List all identities
python agenthacd.py list
```

## What each command does

- **register** — forms an agent identity anchored to a HACD container (6 letters
  from `WTYUIAHXVMEKBSZN`). Records the formation cost reference
  (`1 HACD + 50 HAC + network fee`), mints `65,536` attestation credits, and
  renders the HACD Stack-Protocol-style inscription (`{p:hnft,i:…,t:…,m:1,op:mint,…}`).
- **attest** — an identity spends some of its credits to attest to another
  identity's behavior. Rejects self-attest, duplicate HACD containers, and
  overdrafts.
- **verify** — prints the formation provenance (HACD container, formation hash,
  PoW-formed flag) and the reputation signal (attestation-credit total, unique
  attestors). Stresses that identity = provenance + sybil-resistance, NOT
  endorsement of agent safety/correctness.
- **list** — summary of all identities.

## Tests

```bash
python test_agenthacd.py
# 7 tests — register/attest/verify, invalid/duplicate/self-attest/overdraft, deterministic hash
```

## Honest scope

- Off-chain reference. No HAC/HACD required to run.
- `formation_hash` is a deterministic stand-in for the real PoW formation record
  (mined HACD + HAC-burn bid + stack cost). The on-chain record lives on Hacash
  mainnet and is verifiable via explorer.hacash.org.
- A PoW identity attests to **formation provenance and sybil-resistance only**.
  It does not mean the agent is safe, correct, or audited. Not financial advice.
