from __future__ import annotations

import argparse
import sys
from pathlib import Path

from showcase_validation import ROOT, git_text, run_base_checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the provenance-bound GymFlow showcase release gate."
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="require the target showcase tag to point to the current clean HEAD",
    )
    return parser.parse_args()


def check_tag(
    errors: list[str],
    tag: str,
    expected_commit: str | None,
    root: Path = ROOT,
) -> None:
    actual = git_text(root, "rev-list", "-n", "1", tag)
    if actual is None:
        errors.append(f"unable to resolve Git tag {tag}")
        return
    if expected_commit is not None and actual != expected_commit:
        errors.append(
            f"tag {tag} points to {actual}, expected {expected_commit}"
        )


def check_release_state(
    errors: list[str],
    manifest: dict,
    release_mode: bool,
    root: Path = ROOT,
) -> None:
    latest = manifest["latest_immutable_release"]
    check_tag(errors, latest["tag"], latest["commit"], root)

    head = git_text(root, "rev-parse", "HEAD")
    if head is None:
        errors.append("unable to resolve the current Git commit")
        return

    if release_mode:
        target = manifest["target_release"]
        check_tag(errors, target, head, root)
        status = git_text(root, "status", "--porcelain")
        if status is None:
            errors.append("unable to inspect Git working-tree state")
        elif status:
            errors.append("release validation requires a clean working tree")


def main() -> int:
    args = parse_args()
    errors, manifest = run_base_checks(ROOT)

    if manifest is not None:
        check_release_state(errors, manifest, args.release, ROOT)

    if errors:
        print("GymFlow release checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    assert manifest is not None
    frontend = manifest["source"]["frontend"]["commit"]
    backend = manifest["source"]["backend"]["commit"]
    target = manifest["target_release"]

    print("GymFlow release checks passed.")
    print(f"Validated frontend provenance: {frontend}.")
    print(f"Validated backend provenance: {backend}.")
    print("Validated local-only release evidence without a hosted-CI claim.")
    if args.release:
        print(f"Validated release tag: {target} points to reviewed HEAD.")
    else:
        print(f"Release record is ready for final review before tagging {target}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
