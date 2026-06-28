#!/usr/bin/env python3
"""Compact validator for an AgentHACD launch_spec.json.

Mirrors the checks of the official HACD Incubator skill validator
(validate_launch_spec.py): required fields, enums, supply equation, phase-lot
sum, decimals, banned promo terms (line- and negation-aware), cross-document
number consistency, and required safety disclosures.

Usage:
  python validate.py launch_spec.json
  python validate.py launch_spec.json --strict        # warnings = failure
  python validate.py launch_spec.json --no-docs       # JSON only

Exit 0 = clean (or warnings only without --strict); 1 = error / strict failure.
"""
from __future__ import annotations
import json, re, sys
from pathlib import Path

REQUIRED = ["schema_version", "project", "asset", "stack", "launch", "copy", "review"]
ASSET_TYPES = {"FT", "NFT", "SFT", "HYBRID"}
LAUNCH_STATUSES = {"draft", "review", "approved", "live", "completed"}
PHASE_MODELS = {"public", "allowlist", "designated_first", "custom"}
REMOVAL_EFFECTS = {"burn", "disable", "no_effect", "unknown"}

BANNED = [
    (r"\bguarantee(d|s)?\b", "implies a promise the issuer cannot make"),
    (r"\bprice floor\b", "stack cost is not a guaranteed floor"),
    (r"\bfloor price\b", "stack cost is not a guaranteed floor"),
    (r"\brisk[- ]free\b", "nothing here is risk-free"),
    (r"\bmoon(ing|shot)?\b", "price-hype language"),
    (r"\bto the moon\b", "price-hype language"),
    (r"\bROI\b", "investment-return framing"),
    (r"\byield\b", "investment-return framing"),
    (r"\bpassive income\b", "investment-return framing"),
    (r"\bprofit(s|able)?\b", "investment-return framing"),
    (r"\bget rich\b", "investment-return framing"),
    (r"\b\d+x\s+(return|gains?)\b", "price-appreciation promise"),
    (r"\bbacked value\b", "use 'formation cost reference', not 'backed value'"),
    (r"\bguaranteed (listing|return|profit|price)\b", "no guarantees permitted"),
]
TRAPS = [
    (r"HACD\s*=\s*HAC\s*\+\s*Diamond", "do not define HACD as 'HAC + Diamond'"),
    (r"\bStack is just minting\b", "Stack is formation, not minting"),
    (r"\bjust an NFT\b", "HACD is a PoW asset container, not 'just an NFT'"),
    (r"stack cost guarantees (the )?price", "stack cost guarantees nothing"),
]
NEG = re.compile(
    r"\b(no|not|never|without|cannot|can'?t|don'?t|doesn'?t|isn'?t|aren'?t|won'?t|"
    r"nor|neither|avoid|prohibit(ed)?|banned|n't|do not|does not|must not|"
    r"not a|no such|disclaim)\b", re.I)
PUBLIC = {"launchpad_copy.md", "issuer_faq.md", "x_announcement.md", "project_profile.md"}

errors: list[str] = []
warnings: list[str] = []


def nums(text: str) -> set[int]:
    out = set()
    for raw in re.findall(r"\d[\d,]*", text):
        d = raw.replace(",", "")
        if d.isdigit():
            out.add(int(d))
    return out


def safe_ctx(line: str, term: str) -> bool:
    if NEG.search(line):
        return True
    if re.search(r'["“‘]\s*' + re.escape(term) + r'\s*["”’]', line, re.I):
        return True
    return False


def main() -> int:
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    flags = {a for a in sys.argv[1:] if a.startswith("--")}
    strict = "--strict" in flags
    do_docs = "--no-docs" not in flags
    if len(args) != 1:
        print("Usage: python validate.py launch_spec.json [--strict] [--no-docs]")
        return 1
    path = Path(args[0])
    if not path.exists():
        print(f"ERROR: File not found: {path}")
        return 1
    try:
        spec = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        print(f"ERROR: Invalid JSON: {e}")
        return 1

    for k in REQUIRED:
        if k not in spec:
            errors.append(f"Missing root.{k}")

    project = spec.get("project", {})
    asset = spec.get("asset", {})
    stack = spec.get("stack", {})
    launch = spec.get("launch", {})
    review = spec.get("review", {})

    for k in ["name", "ticker", "category", "description"]:
        v = project.get(k)
        if v is not None and not v:
            warnings.append(f"project.{k} is empty")
    for k in ["website", "contact"]:
        if not project.get(k, ""):
            warnings.append(f"project.{k} is empty (fill before submission)")

    for v, allowed, field in [
        (asset.get("type"), ASSET_TYPES, "asset.type"),
        (launch.get("status"), LAUNCH_STATUSES, "launch.status"),
        (launch.get("phase_model"), PHASE_MODELS, "launch.phase_model"),
        (stack.get("removal_effect"), REMOVAL_EFFECTS, "stack.removal_effect"),
    ]:
        if v not in allowed:
            errors.append(f"{field} = {v!r} is not one of {sorted(allowed)}")

    ts = asset.get("total_supply")
    tl = stack.get("total_hacd_lots")
    up = stack.get("units_per_hacd_lot")
    hp = stack.get("hacd_per_lot")
    sc = stack.get("stack_cost_hac_per_hacd")
    dec = asset.get("decimals")

    def posint(v, f):
        if not isinstance(v, int) or isinstance(v, bool) or v <= 0:
            errors.append(f"{f} must be a positive integer (got {v!r})")
            return False
        return True

    ok_s = posint(ts, "asset.total_supply")
    ok_l = posint(tl, "stack.total_hacd_lots")
    ok_u = posint(up, "stack.units_per_hacd_lot")
    posint(hp, "stack.hacd_per_lot")
    if not isinstance(sc, (int, float)) or isinstance(sc, bool) or sc < 0:
        errors.append("stack.stack_cost_hac_per_hacd must be a non-negative number")
        sc = None
    if not isinstance(dec, int) or isinstance(dec, bool) or dec < 0:
        warnings.append("asset.decimals should be a non-negative integer")

    if ok_s and ok_l and ok_u and tl * up != ts:
        errors.append(f"Supply mismatch: {tl} x {up} = {tl*up:,} != total_supply {ts:,}")
    fp = stack.get("first_phase_hacd_lots")
    pp = stack.get("public_phase_hacd_lots")
    if isinstance(fp, int) and isinstance(pp, int) and ok_l and fp + pp != tl:
        errors.append(f"Phase-lot mismatch: {fp} + {pp} = {fp+pp} != total {tl}")

    if review.get("issuer_confirmed") is not True:
        warnings.append("review.issuer_confirmed is not true (expected for a draft)")
    if review.get("hacd_labs_reviewed") is not True:
        warnings.append("review.hacd_labs_reviewed is not true (expected for a draft)")

    facts = {"total_supply": ts, "total_hacd_lots": tl, "units_per_hacd_lot": up}

    if do_docs:
        docs = {}
        for md in sorted(path.parent.glob("*.md")):
            docs[md.name] = md.read_text(encoding="utf-8")
        for fn, text in docs.items():
            for pat, why in TRAPS:
                if re.search(pat, text, re.I):
                    errors.append(f"{fn}: terminology error — {why}")
            if fn not in PUBLIC:
                continue
            for line in text.splitlines():
                for pat, why in BANNED:
                    for m in re.finditer(pat, line, re.I):
                        term = m.group(0)
                        if not safe_ctx(line, term):
                            errors.append(f"{fn}: unsafe term '{term}' ({why}) -> {line.strip()[:80]}")
        for fn, keys in {"stack_design.md": ["total_supply", "total_hacd_lots", "units_per_hacd_lot"],
                         "launchpad_copy.md": ["total_supply", "total_hacd_lots"]}.items():
            if fn not in docs:
                warnings.append(f"{fn} not found — cannot cross-check numbers")
                continue
            present = nums(docs[fn])
            for k in keys:
                v = facts.get(k)
                if isinstance(v, int) and v not in present:
                    errors.append(f"{fn} does not mention {k} = {v:,} (cross-doc mismatch)")
        pub = " ".join(t.lower() for n, t in docs.items() if n in {"launchpad_copy.md", "issuer_faq.md"})
        if pub:
            for pat, why in [(r"not financial advice", "missing 'not financial advice' disclosure"),
                             (r"(risk disclosure|not an investment)", "missing risk / non-investment disclosure")]:
                if not re.search(pat, pub):
                    warnings.append(why)

    for e in errors:
        print(f"ERROR: {e}")
    for w in warnings:
        print(f"WARNING: {w}")
    if errors:
        print(f"\nFAILED: {len(errors)} error(s), {len(warnings)} warning(s)")
        return 1
    cost = tl * sc if (tl and sc is not None) else None
    print("OK: launch spec passed validation")
    if cost is not None:
        print(f"Formation cost reference: {cost:,} HAC + network fees")
    if warnings and strict:
        print(f"\nFAILED (--strict): {len(warnings)} warning(s) treated as errors")
        return 1
    if warnings:
        print(f"({len(warnings)} warning(s) — fine for a draft, resolve before final submission)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
