import json
import pathlib
import re
import subprocess
import sys
import tempfile
import unittest

from scripts.retrieval_benchmark import (
    BENCH_DIR, CASES, POST_HOC, REFERENCE_UIUX02, REFERENCE_UIUX03, REFERENCE_V02, ROOT, TOOLS, Implementation, catalog_identity,
    catalog_index, compare, load_json, parse_output, reproduction_differences, run_command,
    score_case, sha256_file,
)

BASELINE = BENCH_DIR / "baseline-v0.2-481bb18.json"
EXPERIMENT_DIR = BENCH_DIR / "experiments" / "specialist-uiux-02"
EXPERIMENT_JUDGMENTS = EXPERIMENT_DIR / "judgments.json"
EXPERIMENT_RESULT = EXPERIMENT_DIR / "candidate-results.json"
EXPERIMENT_FREEZE = EXPERIMENT_DIR / "candidate-freeze.json"
REFINEMENT_DIR = BENCH_DIR / "experiments" / "specialist-uiux-03"
REFINEMENT_JUDGMENTS = REFINEMENT_DIR / "judgments.json"
REFINEMENT_RESULT = REFINEMENT_DIR / "candidate-results.json"
REFINEMENT_FREEZE = REFINEMENT_DIR / "candidate-freeze.json"
RELEASE_RESULT = BENCH_DIR / "experiments" / "specialist-uiux-04" / "candidate-results.json"
FROZEN_CASES_SHA256 = "6b6dda63eac336f2ee6078550f82f3175d0a1e440fd8a666a8de324b0d6038d2"
FROZEN_POST_HOC_SHA256 = "573f4da10fe2dd72c0abb6fd2f4508b179f3db76ea4586f0090d1a4d73684f1d"


def raw(stdout="", exit_code=0, stderr=""):
    return {"argv": ["python3"], "exit_code": exit_code, "stdout": stdout, "stderr": stderr}


class RetrievalBenchmarkFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.fixture = json.loads(CASES.read_text(encoding="utf-8"))
        cls.cases = {c["id"]: c for c in cls.fixture["cases"]}
        cls.post_hoc = json.loads(POST_HOC.read_text(encoding="utf-8"))
        cls.baseline = json.loads(BASELINE.read_text(encoding="utf-8"))
        cls.index = catalog_index()

    def test_case_ids_unique_and_synthetic_cases_labelled(self):
        ids = [c["id"] for c in self.fixture["cases"]]
        self.assertEqual(len(ids), len(set(ids)))
        synthetic = [c for c in self.fixture["cases"] if c["origin"] == "synthetic"]
        self.assertTrue(8 <= len(synthetic) <= 12)
        self.assertTrue(all(c["id"].startswith("SYN-") for c in synthetic))
        self.assertTrue(all(c["origin"] == "historical" for c in self.fixture["cases"] if c["id"].startswith("HIST-")))

    def test_held_out_subset_is_synthetic_and_present(self):
        held = [c for c in self.fixture["cases"] if c["split"] == "held_out"]
        self.assertTrue(held)
        self.assertTrue(all(c["origin"] == "synthetic" for c in held))

    def test_every_judged_and_rule_id_exists_in_catalog(self):
        for case in self.fixture["cases"]:
            for ids in case["judgments"].values():
                for cid in ids:
                    self.assertIn(cid, self.index, f"{case['id']} {cid}")
            for name in case["conflict_rules"]:
                self.assertIn(name, self.fixture["conflict_rules"])
        for rule in self.fixture["conflict_rules"].values():
            for cid in rule.get("ids", []):
                self.assertIn(cid, self.index)
            for key in ("name_regex", "text_regex"):
                if key in rule:
                    re.compile(rule[key])
        for case_id, grades in self.post_hoc["judgments"].items():
            self.assertEqual(self.cases[case_id]["origin"], "synthetic")
            for cid, item in grades.items():
                self.assertIn(cid, self.index)
                self.assertIn(item["grade"], (0, 1, 2, 3))
                self.assertFalse(any(cid in ids for ids in self.cases[case_id]["judgments"].values()))

    def test_frozen_expectations_unchanged(self):
        self.assertEqual(sha256_file(CASES), FROZEN_CASES_SHA256)
        self.assertEqual(self.baseline["cases_sha256"], FROZEN_CASES_SHA256)
        self.assertEqual(self.post_hoc["judged_after"]["cases_sha256"], FROZEN_CASES_SHA256)
        self.assertEqual(sha256_file(POST_HOC), FROZEN_POST_HOC_SHA256)

    def test_experiment_judgments_are_separate_and_labelled(self):
        data = load_json(EXPERIMENT_JUDGMENTS)
        self.assertEqual(data["label"], "post_hoc_uiux02")
        self.assertEqual(data["judged_after"]["cases_sha256"], FROZEN_CASES_SHA256)
        for case_id, grades in data["judgments"].items():
            case = self.cases[case_id]
            earlier = self.post_hoc["judgments"].get(case_id, {})
            for cid, item in grades.items():
                self.assertIn(cid, self.index)
                self.assertIn(item["grade"], (0, 1, 2, 3))
                self.assertIn(item["phase"], ("development", "reserved_evaluation"))
                self.assertTrue(item["rationale"])
                self.assertNotIn(cid, earlier)
                self.assertFalse(any(cid in ids for ids in case["judgments"].values()))
                if case["split"] == "held_out":
                    self.assertEqual(item["phase"], "reserved_evaluation")

    def test_refinement_judgments_are_separate_and_labelled(self):
        data = load_json(REFINEMENT_JUDGMENTS)
        earlier_experiment = load_json(EXPERIMENT_JUDGMENTS)["judgments"]
        self.assertEqual(data["label"], "post_hoc_uiux03")
        self.assertEqual(data["judged_after"]["cases_sha256"], FROZEN_CASES_SHA256)
        self.assertEqual(data["judged_after"]["uiux02_judgments_sha256"], sha256_file(EXPERIMENT_JUDGMENTS))
        for case_id, grades in data["judgments"].items():
            case = self.cases[case_id]
            for cid, item in grades.items():
                self.assertIn(cid, self.index)
                self.assertIn(item["grade"], (0, 1, 2, 3))
                self.assertEqual(item["phase"], "development")
                self.assertTrue(item["rationale"])
                self.assertNotIn(cid, self.post_hoc["judgments"].get(case_id, {}))
                self.assertNotIn(cid, earlier_experiment.get(case_id, {}))
                self.assertFalse(any(cid in ids for ids in case["judgments"].values()))

    def test_pinned_uiux02_scripts_match_their_freeze(self):
        freeze = load_json(EXPERIMENT_FREEZE)["retrieval_scripts_sha256"]
        for name, (path, _) in TOOLS.items():
            self.assertEqual(sha256_file(REFERENCE_UIUX02 / pathlib.Path(path).name), freeze[name])

    def test_pinned_uiux03_scripts_match_their_freeze(self):
        freeze = load_json(REFINEMENT_FREEZE)["retrieval_scripts_sha256"]
        for name, (path, _) in TOOLS.items():
            self.assertEqual(sha256_file(REFERENCE_UIUX03 / pathlib.Path(path).name), freeze[name])

    def test_historical_cases_reproduce_retained_output_with_v02(self):
        with Implementation("v0.2") as impl:
            for case in self.fixture["cases"]:
                if case["origin"] != "historical":
                    continue
                result = run_command(case, impl.workdir)
                self.assertEqual(result["exit_code"], 0, case["id"])
                self.assertEqual(result["stderr"], "", case["id"])
                self.assertEqual(result["stdout"], (BENCH_DIR / case["retained_output"]).read_text(encoding="utf-8"), case["id"])

    def test_catalog_and_pinned_v02_scripts_match_baseline(self):
        env = self.baseline["environment"]
        self.assertEqual(catalog_identity(), env["catalog"])
        for name, (path, _) in TOOLS.items():
            self.assertEqual(sha256_file(REFERENCE_V02 / pathlib.Path(path).name), env["retrieval_scripts_sha256"][name])


class RetrievalBenchmarkScoringTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        fixture = json.loads(CASES.read_text(encoding="utf-8"))
        cls.rules = fixture["conflict_rules"]
        cls.cases = {c["id"]: c for c in fixture["cases"]}
        cls.index = catalog_index()

    def score(self, case_id, output):
        return score_case(self.cases[case_id], output, self.rules, self.index, {})

    def retained(self, case_id):
        return raw((BENCH_DIR / self.cases[case_id]["retained_output"]).read_text(encoding="utf-8"))

    def test_conflicting_result_is_flagged(self):
        scored = self.score("HIST-02", self.retained("HIST-02"))
        top = scored["results"][0]
        self.assertEqual(top["catalog_id"], "uupm:ux-guidelines:64")
        self.assertIn("mobile_first_direction", top["conflicts"])
        self.assertEqual(scored["conflict_count"], 1)
        self.assertFalse(scored["useful"])

    def test_useful_result_receives_credit(self):
        scored = self.score("HIST-03", self.retained("HIST-03"))
        self.assertEqual(scored["status"], "ok")
        self.assertEqual(scored["first_actionable_rank"], 1)
        self.assertEqual(scored["relevant_in_top3"], 1)
        self.assertEqual(scored["results"][0]["grade"], 3)
        self.assertEqual(scored["conflict_count"], 0)
        self.assertTrue(scored["useful"])

    def test_relevance_and_conflict_are_independent(self):
        scored = self.score("HIST-01", self.retained("HIST-01"))
        midnight = next(r for r in scored["results"] if r["catalog_id"] == "hallmark:theme:midnight")
        self.assertEqual(midnight["grade"], 1)
        self.assertEqual(midnight["conflicts"], ["replacement_identity"])
        self.assertEqual(midnight["redistribution_status"], "metadata_only")

    def test_empty_result_distinguished_from_command_failure(self):
        empty = self.score("SYN-09", raw(json.dumps({"references": []})))
        self.assertEqual(empty["status"], "empty")
        self.assertEqual(empty["abstention"], "correct")
        failed = self.score("SYN-09", raw("", exit_code=2, stderr="error"))
        self.assertEqual(failed["status"], "command_failed")
        self.assertEqual(failed["abstention"], "not_assessable")
        self.assertEqual(self.retained("HIST-04")["stdout"].strip()[:1], "{")
        historical_empty = self.score("HIST-04", self.retained("HIST-04"))
        self.assertEqual(historical_empty["status"], "empty")
        self.assertEqual(historical_empty["abstention"], "unacceptable_empty")

    def test_malformed_output_is_not_success(self):
        good = {"catalog_id": "uupm:ux-guidelines:41", "relevance_score": 1.0}
        variants = [
            "not json",
            "",
            json.dumps([good]),
            json.dumps({"results": [good]}),
            json.dumps({"references": {"0": good}}),
            json.dumps({"references": ["uupm:ux-guidelines:41"]}),
            json.dumps({"references": [{"relevance_score": 1.0}]}),
            json.dumps({"references": [{"catalog_id": "", "relevance_score": 1.0}]}),
            json.dumps({"references": [{"catalog_id": "uupm:ux-guidelines:41"}]}),
            json.dumps({"references": [{"catalog_id": "uupm:ux-guidelines:41", "relevance_score": "9"}]}),
            json.dumps({"references": [{"catalog_id": "uupm:ux-guidelines:41", "relevance_score": True}]}),
            '{"references": [{"catalog_id": "uupm:ux-guidelines:41", "relevance_score": NaN}]}',
        ]
        for stdout in variants:
            with self.subTest(stdout=stdout):
                status, items, problems = parse_output("recommend", raw(stdout))
                self.assertEqual(status, "malformed")
                self.assertEqual(items, [])
                self.assertTrue(problems)
                scored = self.score("SYN-09", raw(stdout))
                self.assertEqual(scored["abstention"], "not_assessable")
                self.assertFalse(scored["useful"])

    def test_unknown_catalog_id_is_reported_not_credited(self):
        scored = self.score("HIST-03", raw(json.dumps({"references": [
            {"catalog_id": "missing:record", "relevance_score": 3.0}]})))
        self.assertEqual(scored["results"][0]["in_catalog"], False)
        self.assertIsNone(scored["results"][0]["grade"])
        self.assertFalse(scored["useful"])


class RetrievalBenchmarkBaselineTests(unittest.TestCase):
    def run_cli(self, *args):
        with tempfile.TemporaryDirectory() as tmp:
            out = pathlib.Path(tmp) / "run.json"
            proc = subprocess.run(
                [sys.executable, "scripts/retrieval_benchmark.py", "--raw", "--output", str(out), *args],
                cwd=ROOT, capture_output=True, text=True, timeout=300,
            )
            self.assertEqual(proc.returncode, 0, proc.stderr)
            return out.read_bytes()

    def test_v02_run_reproduces_frozen_baseline(self):
        first = self.run_cli("--implementation", "v0.2", "--check-historical")
        self.assertEqual(reproduction_differences(load_json(BASELINE), json.loads(first)), [])
        self.assertEqual(first, self.run_cli("--implementation", "v0.2", "--check-historical"))

    def test_pinned_uiux02_reproduces_its_frozen_results(self):
        run = json.loads(self.run_cli("--implementation", "specialist-uiux-02",
                                      "--judgments", str(EXPERIMENT_JUDGMENTS)))
        expected = load_json(EXPERIMENT_RESULT)
        # Frozen while those scripts were the working tree.
        self.assertEqual(expected["environment"]["implementation"], "working-tree")
        expected["environment"]["implementation"] = "specialist-uiux-02"
        self.assertEqual(reproduction_differences(expected, run), [])

    def test_pinned_uiux03_reproduces_its_frozen_results(self):
        run = json.loads(self.run_cli("--implementation", "specialist-uiux-03",
                                      "--judgments", str(EXPERIMENT_JUDGMENTS),
                                      "--judgments", str(REFINEMENT_JUDGMENTS)))
        expected = load_json(REFINEMENT_RESULT)
        self.assertEqual(expected["environment"]["implementation"], "working-tree")
        expected["environment"]["implementation"] = "specialist-uiux-03"
        self.assertEqual(reproduction_differences(expected, run), [])

    def test_working_tree_reproduces_release_results(self):
        run = json.loads(self.run_cli("--judgments", str(EXPERIMENT_JUDGMENTS),
                                      "--judgments", str(REFINEMENT_JUDGMENTS)))
        expected = load_json(RELEASE_RESULT)
        # QUALITY-01 intentionally changes the recommender source, not this frozen
        # benchmark's outputs. Pin the reviewed replacement identity explicitly;
        # retain every original behavioral comparison, including raw stdout.
        self.assertEqual(expected["environment"]["retrieval_scripts_sha256"]["recommend"],
                         "c054c1adf6fa24be6723c8f344942ef0157df00fe42d86a3daef736bc288ab53")
        expected["environment"]["retrieval_scripts_sha256"]["recommend"] = (
            "0e7301d41d98556b4a54e564a8e1389352eba7a3b43c09fe6c8521d87a7706b3")
        self.assertEqual(reproduction_differences(expected, run), [])

    def test_reproduction_check_detects_changed_results(self):
        baseline = load_json(BASELINE)
        changed = json.loads(json.dumps(baseline))
        changed["cases"][0]["results"][0]["catalog_id"] = "other"
        changed["environment"]["repository"]["head"] = "different"
        self.assertEqual(reproduction_differences(baseline, changed), [("cases", 0, "results", 0, "catalog_id")])

    def test_comparison_reports_gains_and_regressions(self):
        base = load_json(BASELINE)
        cand = json.loads(json.dumps(base))
        hist = next(c for c in cand["cases"] if c["id"] == "HIST-02")
        hist.update(useful=True, conflict_count=0, first_actionable_rank=1)
        hist["results"] = [dict(hist["results"][0], catalog_id="uupm:ux-guidelines:36", grade=3, conflicts=[])]
        key = next(c for c in cand["cases"] if c["id"] == "HIST-03")
        key.update(useful=False, first_actionable_rank=None)
        report = compare(base, cand)
        self.assertEqual(report["newly_useful"], ["HIST-02"])
        self.assertEqual(report["regressed"], ["HIST-03"])
        self.assertTrue(report["same_catalog"])


if __name__ == "__main__":
    unittest.main()
