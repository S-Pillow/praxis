"""Additive DevOps mechanisms and navigation; not semantic agent qualification."""
import json
from pathlib import Path
import re
import tempfile
import unittest
from unittest.mock import patch
from scripts import praxis_context as ctx

ROOT = Path(__file__).resolve().parents[1]
DEV = ROOT / "skills/devops-reliability"
RQ = ROOT / "knowledge/repository-quality"
CAP = ROOT / "knowledge/capabilities"
SKILL = "skills/devops-reliability/SKILL.md"
MODES = ("plan", "diagnose", "review")
FAMILIES = {
    "source-repository.md", "build-ci.md", "delivery-release.md",
    "infrastructure-config.md", "runtime-platform.md", "networking-dns-tls.md",
    "observability.md", "reliability-incidents.md", "data-recovery.md",
    "devsecops.md", "cost-resource.md", "operational-documentation.md",
}
PRIOR_CAPS = {
    "CAP-H01", "CAP-H02", "CAP-H03", "CAP-D01", "CAP-D02", "CAP-D03", "CAP-D04",
    "CAP-D05", "CAP-O01", "CAP-I01", "CAP-C01", "CAP-C02", "CAP-Q01", "CAP-M01",
    "CAP-N01", "CAP-V01", "CAP-V02", "CAP-V03", "CAP-B01", "CAP-B02", "CAP-B03",
    "CAP-B04", "CAP-B05", "CAP-B06", "CAP-B07", "CAP-B08", "CAP-S01", "CAP-S02",
    "CAP-S03", "CAP-S04",
}


def read(path):
    return path.read_text(encoding="utf-8")


def slug(heading):
    return re.sub(r"[^\w -]", "", heading.lower()).replace(" ", "-")


class DevOpsIntegration(unittest.TestCase):
    def test_exact_prior_registry_and_new_contract(self):
        prior = json.loads(read(ROOT / "tests/fixtures/devops_prior_registry.json"))
        registry = json.loads(read(ROOT / "skills/specialists.json"))
        self.assertEqual(prior["schema_version"], registry["schema_version"])
        self.assertEqual(registry["specialists"][:-1], prior["specialists"])
        self.assertEqual(len(registry["specialists"]), 5)
        new = registry["specialists"][-1]
        self.assertEqual(new["id"], "aipf-devops-reliability")
        self.assertEqual(new["version"], "0.1")
        self.assertEqual(new["tasks"], {"devops-" + m: m for m in MODES})
        self.assertEqual(new["chapters_any"], list(range(11, 22)))
        self.assertEqual(new["tools"], [])
        self.assertNotIn("retrieval_script", new)
        for path in [new["skill"], *new["knowledge_sources"]]:
            self.assertTrue((ROOT / path).is_file(), path)
        tasks = [t for s in registry["specialists"] for t in s["tasks"]]
        self.assertEqual(len(tasks), len(set(tasks)))
        self.assertFalse(any("repository-quality" in s["id"] for s in registry["specialists"]))

    def test_modes_framework_and_no_lookup(self):
        self.assertEqual(ctx.verify_framework(ROOT), "8.10.1")
        with patch.object(ctx.subprocess, "run") as run:
            for mode in MODES:
                for chapter in range(11, 22):
                    with self.subTest(mode=mode, chapter=chapter):
                        result = ctx.resolve("devops-" + mode, [chapter], ROOT)
                        self.assertEqual(result["status"], "consult")
                        self.assertEqual(result["authority"], "advisory_only")
                        self.assertEqual(result["specialists"], [{
                            "id": "aipf-devops-reliability", "version": "0.1",
                            "skill": SKILL, "mode": mode, "status": "available",
                        }])
                        self.assertEqual(ctx.retrieve(result, "material operation", root=ROOT)
                                         ["specialists"][0]["lookup_status"], "not_applicable")
            run.assert_not_called()

    def test_missing_skill_path_and_unknown_are_not_success(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            (root / "skills").mkdir()
            (root / "skills/specialists.json").write_text(
                read(ROOT / "skills/specialists.json"), encoding="utf-8")
            with patch.object(ctx, "verify_framework", return_value="8.10.1"):
                for mode in MODES:
                    task = "devops-" + mode
                    missing = ctx.resolve(task, [12], root)
                    self.assertEqual(missing["status"], "specialist_unavailable")
                    self.assertEqual(missing["specialists"][0]["status"], "unavailable")
                    for chapters in ([], [10], [22]):
                        self.assertEqual(ctx.resolve(task, chapters, root)["status"],
                                         "recheck_framework_path")
                for task in ("non-ui", "minor-ui"):
                    self.assertEqual(ctx.resolve(task, [12], root)["status"], "not_needed")
                for task in ("devops", "devops-verify", "repository-quality", ""):
                    with self.assertRaises(ValueError):
                        ctx.resolve(task, [12], root)

    def test_entry_shared_access_and_roles(self):
        entry = read(ROOT / "skills/praxis/SKILL.md")
        skill = read(DEV / "SKILL.md")
        for value in (SKILL, "knowledge/repository-quality/INDEX.md",
                      "whether or not DevOps is activated", "not a sixth registered specialist"):
            self.assertIn(value, entry)
        self.assertIn("Distinct Builder needs no Praxis, AIPF, PRD or specialist access", skill)
        self.assertIn("no self-handoff", skill)
        self.assertIn("Available access is not authority", skill)


class DevOpsKnowledge(unittest.TestCase):
    def test_twelve_families_and_indexed_cards(self):
        guides = list((DEV / "references").glob("*.md"))
        self.assertEqual({p.name for p in guides}, FAMILIES)
        index = read(DEV / "INDEX.md")
        found = []
        for guide in guides:
            body = read(guide)
            cards = re.split(r"(?m)^## (?=DO-D\d{2} —)", body)[1:]
            self.assertTrue(cards, guide)
            for card in cards:
                heading = card.splitlines()[0]
                found.append(heading.split()[0])
                for field in ("Applicability / context", "Decision and alternatives",
                              "Counterexample", "Observable verification", "Sources and limits"):
                    self.assertIn("**" + field + ":**", card)
                self.assertIn("DO-S", card)
                self.assertIn(f"(references/{guide.name}#{slug(heading)})", index)
        self.assertEqual(len(found), len(set(found)))
        self.assertCountEqual(found, re.findall(r"\[(DO-D\d{2}) —", index))

    def test_shared_profiles_and_cards(self):
        index = read(RQ / "INDEX.md")
        found = []
        for filename in ("profiles.md", "verification.md", "repository-health.md"):
            body = read(RQ / filename)
            cards = re.split(r"(?m)^## (?=RQ-D\d{2} —)", body)[1:]
            self.assertTrue(cards)
            for card in cards:
                heading = card.splitlines()[0]
                found.append(heading.split()[0])
                for field in ("Applicability / decision and alternatives", "Counterexample",
                              "Observable verification and sources"):
                    self.assertIn("**" + field + ":**", card)
                self.assertIn(f"({filename}#{slug(heading)})", index)
        self.assertEqual(len(found), len(set(found)))
        self.assertCountEqual(found, re.findall(r"\[(RQ-D\d{2}) —", index))
        self.assertIn("synthetic", read(RQ / "examples/CLI.md"))
        self.assertIn("synthetic", read(RQ / "examples/SERVICE.md"))

    def test_sources_and_retained_research(self):
        register = ROOT / "research/devops-reliability/DEVOPS-SOURCE-REGISTER-01.md"
        ids = set(re.findall(r"(?m)^\| (DO-S\d{2}) \|", read(register)))
        self.assertEqual(ids, {f"DO-S{i:02d}" for i in range(1, 56)})
        for source in list((DEV / "references").glob("*.md")) + [
            RQ / "profiles.md", RQ / "verification.md", RQ / "repository-health.md",
            CAP / "operations.md",
        ]:
            cited = set(re.findall(r"\bDO-S\d{2}\b", read(source)))
            self.assertTrue(cited, source)
            self.assertTrue(cited <= ids, (source, cited - ids))
        cross = ROOT / "research/CROSS-SPECIALIST-RESEARCH-REGISTER.md"
        self.assertEqual(set(re.findall(r"(?m)^\| (XR-\d{2}) \|", read(cross))),
                         {f"XR-{i:02d}" for i in range(1, 15)})

    def test_internal_links_and_anchors(self):
        for source in list(DEV.rglob("*.md")) + list(RQ.rglob("*.md")) + [CAP / "operations.md"]:
            for dest in re.findall(r"\]\(([^)]+)\)", read(source)):
                if "://" in dest:
                    continue
                path, _, frag = dest.partition("#")
                target = (source.parent / path).resolve() if path else source
                self.assertTrue(target.is_file(), (source, dest))
                if frag:
                    heads = re.findall(r"(?m)^#+\s+(.+)$", read(target))
                    self.assertIn(frag, [slug(h) for h in heads], (source, dest))

    def test_capability_extension_exact(self):
        index = read(CAP / "INDEX.md")
        ids = re.findall(r"\[(CAP-[A-Z]\d{2}) —", index)
        self.assertEqual(len(ids), len(set(ids)))
        added = {f"CAP-R{i:02d}" for i in range(1, 10)}
        self.assertEqual(set(ids), PRIOR_CAPS | added)
        self.assertEqual(set(re.findall(r"(?m)^## (CAP-[A-Z]\d{2})$", read(CAP / "operations.md"))), added)


if __name__ == "__main__":
    unittest.main()
