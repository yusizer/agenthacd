"""Tests for the AgentHACD reference client — register / attest / verify loop.

Run:  python test_agenthacd.py
No external deps (stdlib unittest). Uses a temp store so it never touches a
real store.json.
"""
import argparse
import os
import sys
import tempfile
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import agenthacd  # noqa: E402


class TestAgentHACD(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.NamedTemporaryFile(suffix=".json", delete=False)
        self.tmp.close()
        agenthacd.STORE = Path(self.tmp.name)
        agenthacd.save_store({"identities": {}, "next_serial": 1})

    def tearDown(self):
        os.unlink(self.tmp.name)

    def ns(self, **kw):
        return argparse.Namespace(**kw)

    def test_register_creates_identity(self):
        agenthacd.cmd_register(self.ns(agent="agent1", hacd="AAAAAA", owner="0xABC"))
        data = agenthacd.load_store()
        self.assertEqual(len(data["identities"]), 1)
        ident = next(iter(data["identities"].values()))
        self.assertEqual(ident["agent_id"], "agent1")
        self.assertEqual(ident["hacd_name"], "AAAAAA")
        self.assertEqual(ident["attestation_credits_remaining"], agenthacd.CREDITS_PER_LOT)
        self.assertIn("inscription", ident)
        self.assertIn("p:hnft", ident["inscription"])
        self.assertIn("op:mint", ident["inscription"])

    def test_register_rejects_invalid_hacd_name(self):
        with self.assertRaises(SystemExit):
            agenthacd.cmd_register(self.ns(agent="a", hacd="BADNAME", owner="0x"))
        with self.assertRaises(SystemExit):
            agenthacd.cmd_register(self.ns(agent="a", hacd="AGH01", owner="0x"))  # 5 letters

    def test_register_rejects_duplicate_container(self):
        agenthacd.cmd_register(self.ns(agent="a1", hacd="AAAAAA", owner="0x1"))
        with self.assertRaises(SystemExit):
            agenthacd.cmd_register(self.ns(agent="a2", hacd="AAAAAA", owner="0x2"))

    def test_attest_flow_and_verify(self):
        agenthacd.cmd_register(self.ns(agent="target", hacd="AAAAAA", owner="0xT"))
        agenthacd.cmd_register(self.ns(agent="attestor", hacd="BBBBBB", owner="0xA"))
        data = agenthacd.load_store()
        ids = list(data["identities"].keys())
        target, source = ids[0], ids[1]
        agenthacd.cmd_attest(self.ns(identity=target, **{"from": source}, credits=100, note="reliable"))
        # verify reputation
        import io, contextlib
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            agenthacd.cmd_verify(self.ns(identity=target))
        out = buf.getvalue()
        self.assertIn("Reputation", out)
        self.assertIn("100 attestation-credit", out)
        # source credits decremented
        data = agenthacd.load_store()
        self.assertEqual(data["identities"][source]["attestation_credits_remaining"], agenthacd.CREDITS_PER_LOT - 100)

    def test_attest_rejects_self(self):
        agenthacd.cmd_register(self.ns(agent="a", hacd="AAAAAA", owner="0x"))
        ident = next(iter(agenthacd.load_store()["identities"].keys()))
        with self.assertRaises(SystemExit):
            agenthacd.cmd_attest(self.ns(identity=ident, **{"from": ident}, credits=10, note=""))

    def test_attest_rejects_insufficient_credits(self):
        agenthacd.cmd_register(self.ns(agent="a", hacd="AAAAAA", owner="0x"))
        agenthacd.cmd_register(self.ns(agent="b", hacd="BBBBBB", owner="0x"))
        ids = list(agenthacd.load_store()["identities"].keys())
        with self.assertRaises(SystemExit):
            agenthacd.cmd_attest(self.ns(identity=ids[0], **{"from": ids[1]}, credits=agenthacd.CREDITS_PER_LOT + 1, note=""))

    def test_formation_hash_deterministic(self):
        h1 = agenthacd.formation_hash("a", "AAAAAA", "0x1")
        h2 = agenthacd.formation_hash("a", "AAAAAA", "0x1")
        h3 = agenthacd.formation_hash("a", "BBBBBB", "0x1")
        self.assertEqual(h1, h2)
        self.assertNotEqual(h1, h3)


if __name__ == "__main__":
    unittest.main(verbosity=2)
