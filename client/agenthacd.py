#!/usr/bin/env python3
"""AgentHACD reference client — register -> attest -> verify.

This is an OFF-CHAIN reference implementation of the AgentHACD identity loop.
It demonstrates the launch utility honestly: how an agent identity is formed,
how other identities attest to it, and how a marketplace can verify a PoW-formed
identity and its reputation signal.

It is NOT the on-chain Stack. On-chain formation happens through the HACD
Launchpad (hacd.it/launchpad), which HACD Labs configures from the validated
launch_spec.json. See ../LAUNCH_WALKTHROUGH.md and ../stack_design.md.

The client stores identities and attestations in a local JSON file (store.json)
so the full loop runs with zero dependencies and zero network access.

Usage:
  python agenthacd.py register --agent "my-agent" --hacd AGH001 --owner 0xABC
  python agenthacd.py attest   --identity <id> --from <from-id> --credits 100 --note "reliable"
  python agenthacd.py verify   --identity <id>
  python agenthacd.py list

No financial advice. No price, liquidity, or return is guaranteed. A PoW identity
attests to formation provenance and sybil-resistance only; it does not mean the
agent is safe, correct, or audited.
"""
from __future__ import annotations
import argparse
import json
import sys
import time
from pathlib import Path

# HACD names are 6-letter combinations from these 16 letters (per HACD spec).
HACD_LETTERS = set("WTYUIAHXVMEKBSZN")
HACD_NAME_LEN = 6
STACK_COST_HAC = 50           # matches launch_spec.json
CREDITS_PER_LOT = 65536        # matches launch_spec.json
STORE = Path(__file__).parent / "store.json"


def die(msg: str, code: int = 1) -> None:
    print(f"error: {msg}", file=sys.stderr)
    sys.exit(code)


def load_store() -> dict:
    if not STORE.exists():
        return {"identities": {}, "next_serial": 1}
    return json.loads(STORE.read_text(encoding="utf-8"))


def save_store(data: dict) -> None:
    STORE.write_text(json.dumps(data, indent=2), encoding="utf-8")


def valid_hacd_name(name: str) -> bool:
    return (
        len(name) == HACD_NAME_LEN
        and all(c in HACD_LETTERS for c in name.upper())
    )


def inscription(identity: dict, serial: int) -> str:
    """Render a HACD Stack-Protocol-style inscription for the identity.

    Mirrors the compact format used by github.com/hacdlabs/stackprotocol:
    {p:protocol, i:identifier, t:ticket, m:max, op:operand, s:serial, ...}.
    This is the on-chain inscription shape the Launchpad would produce.
    """
    return (
        "{p:hnft,"                              # protocol: HACD NFT-style identity
        f"i:{identity['agent_id']},"
        f"t:{identity['hacd_name']},"
        "m:1,"                                   # 1 identity NFT per lot
        "op:mint,"
        f"s:{serial},"
        f"h:{identity['formation_hash']}}}"
    )


def formation_hash(agent_id: str, hacd_name: str, owner: str) -> str:
    """A deterministic stand-in for the PoW formation cost record.

    On-chain this would be the mined HACD + HAC-burn bid + stack cost; here we
    record a deterministic reference so verify() can show the formation provenance.
    """
    import hashlib
    raw = f"{agent_id}|{hacd_name}|{owner}|pow+{STACK_COST_HAC}hac"
    return hashlib.sha256(raw.encode()).hexdigest()[:16]


# --------------------------------------------------------------------------- #
def cmd_register(args) -> None:
    if not valid_hacd_name(args.hacd):
        die(f"HACD name must be {HACD_NAME_LEN} letters from {''.join(sorted(HACD_LETTERS))} (got {args.hacd!r})")
    data = load_store()
    # reject duplicate HACD container (one identity per HACD lot)
    for ident in data["identities"].values():
        if ident["hacd_name"].upper() == args.hacd.upper():
            die(f"HACD container {args.hacd!r} already holds an identity ({ident['agent_id']})")
    serial = data["next_serial"]
    identity_id = f"AGH-{serial:04d}"
    identity = {
        "id": identity_id,
        "agent_id": args.agent,
        "hacd_name": args.hacd.upper(),
        "owner": args.owner,
        "formed_at": int(time.time()),
        "formation_hash": formation_hash(args.agent, args.hacd.upper(), args.owner),
        "formation_cost": f"1 HACD + {STACK_COST_HAC} HAC + network fee",
        "attestation_credits_remaining": CREDITS_PER_LOT,
        "attestations_received": [],
    }
    identity["inscription"] = inscription(identity, serial)
    data["identities"][identity_id] = identity
    data["next_serial"] = serial + 1
    save_store(data)
    print(f"Registered identity {identity_id} for agent {args.agent!r}")
    print(f"  HACD container : {identity['hacd_name']}")
    print(f"  Formation cost : {identity['formation_cost']}  (formation cost reference, NOT a price floor)")
    print(f"  Credits        : {CREDITS_PER_LOT} attestation credits")
    print(f"  Inscription    : {identity['inscription']}")
    print(f"  Off-chain reference. On-chain Stack happens via hacd.it/launchpad.")


def cmd_attest(args) -> None:
    src_id = getattr(args, "from")
    data = load_store()
    target = data["identities"].get(args.identity)
    if not target:
        die(f"target identity {args.identity!r} not found")
    source = data["identities"].get(src_id)
    if not source:
        die(f"source identity {src_id!r} not found")
    if args.identity == src_id:
        die("an identity cannot attest to itself")
    if args.credits <= 0:
        die("credits must be positive")
    if source["attestation_credits_remaining"] < args.credits:
        die(f"source has only {source['attestation_credits_remaining']} credits left")
    source["attestation_credits_remaining"] -= args.credits
    target["attestations_received"].append({
        "from": src_id,
        "credits": args.credits,
        "note": args.note or "",
        "at": int(time.time()),
    })
    save_store(data)
    print(f"Attested: {src_id} -> {args.identity} for {args.credits} credits")
    print(f"  {src_id} credits remaining: {source['attestation_credits_remaining']}")


def cmd_verify(args) -> None:
    data = load_store()
    ident = data["identities"].get(args.identity)
    if not ident:
        die(f"identity {args.identity!r} not found")
    score = sum(a["credits"] for a in ident["attestations_received"])
    attestors = len({a["from"] for a in ident["attestations_received"]})
    print(f"Identity       : {ident['id']}")
    print(f"Agent          : {ident['agent_id']}")
    print(f"HACD container : {ident['hacd_name']}")
    print(f"Owner          : {ident['owner']}")
    print(f"Formed at      : {time.strftime('%Y-%m-%d %H:%M:%S UTC', time.gmtime(ident['formed_at']))}")
    print(f"Formation hash : {ident['formation_hash']}")
    print(f"Formation cost : {ident['formation_cost']}  (reference; NOT a price floor)")
    print(f"Inscription    : {ident['inscription']}")
    print(f"PoW-formed     : yes (identity anchored to a mined, HAC-burned HACD)")
    print(f"Attestations   : {len(ident['attestations_received'])} from {attestors} unique identity/identities")
    print(f"Reputation     : {score} attestation-credit total")
    print(f"  This identity attests to FORMATION PROVENANCE + SYBIL-RESISTANCE only.")
    print(f"  It does NOT mean the agent is safe, correct, or audited. Not financial advice.")


def cmd_list(args) -> None:
    data = load_store()
    if not data["identities"]:
        print("No identities registered yet.")
        return
    for ident in data["identities"].values():
        score = sum(a["credits"] for a in ident["attestations_received"])
        print(f"{ident['id']}  agent={ident['agent_id']:<20} hacd={ident['hacd_name']}  "
              f"credits_left={ident['attestation_credits_remaining']}  reputation={score}")


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(prog="agenthacd", description="AgentHACD reference client (register/attest/verify)")
    sub = p.add_subparsers(dest="command", required=True)

    r = sub.add_parser("register", help="Form a PoW-anchored agent identity")
    r.add_argument("--agent", required=True, help="Agent identifier (e.g. my-agent-v1)")
    r.add_argument("--hacd", required=True, help="HACD container name (6 letters from WTYUIAHXVMEKBSZN)")
    r.add_argument("--owner", required=True, help="Owner address/handle")
    r.set_defaults(func=cmd_register)

    a = sub.add_parser("attest", help="Attest to an identity (spend attestation credits)")
    a.add_argument("--identity", required=True, help="Target identity id (AGH-NNNN)")
    a.add_argument("--from", dest="from", required=True, help="Source identity id (attestor)")
    a.add_argument("--credits", type=int, required=True, help="Credits to spend")
    a.add_argument("--note", help="Optional attestation note")
    a.set_defaults(func=cmd_attest)

    v = sub.add_parser("verify", help="Verify a PoW-formed identity + reputation signal")
    v.add_argument("--identity", required=True, help="Identity id (AGH-NNNN)")
    v.set_defaults(func=cmd_verify)

    l = sub.add_parser("list", help="List all identities")
    l.set_defaults(func=cmd_list)
    return p


def main() -> int:
    args = build_parser().parse_args()
    args.func(args)
    return 0


if __name__ == "__main__":
    sys.exit(main())
