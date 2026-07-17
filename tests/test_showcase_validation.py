from __future__ import annotations

import json
import subprocess
import sys
import tempfile
import unittest
from copy import deepcopy
from pathlib import Path

SCRIPTS = Path(__file__).resolve().parents[1] / "scripts"
if str(SCRIPTS) not in sys.path:
    sys.path.insert(0, str(SCRIPTS))

import showcase_validation as validation
from check_release_candidate import check_release_state


def run_git(root: Path, *args: str) -> str:
    completed = subprocess.run(
        ["git", *args],
        cwd=root,
        check=True,
        capture_output=True,
        text=True,
    )
    return completed.stdout.strip()


class ShowcaseValidationTests(unittest.TestCase):
    def make_repo(self) -> Path:
        temp = tempfile.TemporaryDirectory()
        self.addCleanup(temp.cleanup)
        root = Path(temp.name)
        run_git(root, "init", "-q")
        run_git(root, "config", "user.email", "validation@gymflow-demo.test")
        run_git(root, "config", "user.name", "GymFlow Validation")
        return root

    def commit_all(self, root: Path, message: str = "fixture") -> str:
        run_git(root, "add", ".")
        run_git(root, "commit", "-qm", message)
        return run_git(root, "rev-parse", "HEAD")

    def test_tracked_file_discovery_ignores_untracked_bytecode(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text("# Fixture\n", encoding="utf-8")
        self.commit_all(root)

        cache = root / "scripts" / "__pycache__"
        cache.mkdir(parents=True)
        (cache / "validator.pyc").write_bytes(b"generated")

        tracked = {
            path.as_posix()
            for path in validation.tracked_relative_paths(root)
        }
        self.assertEqual(tracked, {"README.md"})

        errors: list[str] = []
        validation.check_tracked_file_safety(errors, root)
        self.assertEqual(errors, [])

    def test_obsolete_release_text_is_detected_in_public_docs(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text(
            "main is preparing `v1.0.1-showcase`\n",
            encoding="utf-8",
        )
        self.commit_all(root)

        errors: list[str] = []
        validation.check_text_safety(errors, root)
        self.assertTrue(
            any("obsolete release statement" in error for error in errors),
            errors,
        )

    def test_validator_source_can_contain_detection_literals(self) -> None:
        root = self.make_repo()
        scripts = root / "scripts"
        scripts.mkdir()
        (scripts / "fixture.py").write_text(
            'VALUE = "main is preparing `v1.0.1-showcase`"\n',
            encoding="utf-8",
        )
        self.commit_all(root)

        errors: list[str] = []
        validation.check_text_safety(errors, root)
        self.assertEqual(errors, [])

    def test_manifest_contract_accepts_current_release_record(self) -> None:
        manifest = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "release"
                / "evidence-manifest.json"
            ).read_text(encoding="utf-8")
        )
        errors: list[str] = []
        validation.check_manifest_contract(errors, manifest)
        self.assertEqual(errors, [])

    def test_manifest_contract_rejects_source_drift(self) -> None:
        manifest = json.loads(
            (
                Path(__file__).resolve().parents[1]
                / "release"
                / "evidence-manifest.json"
            ).read_text(encoding="utf-8")
        )
        changed = deepcopy(manifest)
        changed["source"]["frontend"]["commit"] = "0" * 40

        errors: list[str] = []
        validation.check_manifest_contract(errors, changed)
        self.assertIn("canonical frontend revision is incorrect", errors)

    def test_release_mode_requires_target_tag_on_clean_head(self) -> None:
        root = self.make_repo()
        (root / "README.md").write_text("# Fixture\n", encoding="utf-8")
        first = self.commit_all(root, "first")
        run_git(root, "tag", "v1.0.1-showcase", first)

        (root / "README.md").write_text("# Fixture\n\nSecond\n", encoding="utf-8")
        second = self.commit_all(root, "second")
        run_git(root, "tag", "v1.0.2-showcase", second)

        manifest = {
            "target_release": "v1.0.2-showcase",
            "latest_immutable_release": {
                "tag": "v1.0.1-showcase",
                "commit": first,
            },
        }
        errors: list[str] = []
        check_release_state(errors, manifest, True, root)
        self.assertEqual(errors, [])

        (root / "README.md").write_text("# Dirty\n", encoding="utf-8")
        errors = []
        check_release_state(errors, manifest, True, root)
        self.assertIn(
            "release validation requires a clean working tree",
            errors,
        )


if __name__ == "__main__":
    unittest.main()
