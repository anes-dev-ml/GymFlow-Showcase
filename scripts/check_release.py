from __future__ import annotations

import argparse
import sys
from pathlib import Path

from showcase_validation import ROOT, git_text, run_base_checks


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the GymFlow showcase release gate."
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help="require the current release tag to point to the clean reviewed HEAD",
    )
    return parser.parse_args()


def resolve_tag(root: Path, tag: str) -> str | None:
    return git_text(root, "rev-list", "-n", "1", tag)


def check_tag(
    errors: list[str],
    tag: str,
    expected_commit: str,
    root: Path = ROOT,
) -> None:
    actual = resolve_tag(root, tag)
    if actual is None:
        errors.append(f"unable to resolve Git tag {tag}")
    elif actual != expected_commit:
        errors.append(f"tag {tag} points to {actual}, expected {expected_commit}")


def check_release_state(
    errors: list[str],
    manifest: dict,
    release_mode: bool,
    root: Path = ROOT,
) -> None:
    previous = manifest.get("previous_release", {})
    release = manifest.get("release", {})
    previous_tag = previous.get("tag")
    previous_commit = previous.get("commit")
    current_tag = release.get("tag")

    if isinstance(previous_tag, str) and isinstance(previous_commit, str):
        check_tag(errors, previous_tag, previous_commit, root)

    head = git_text(root, "rev-parse", "HEAD")
    if head is None:
        errors.append("unable to resolve the current Git commit")
        return

    if not isinstance(current_tag, str):
        errors.append("release record does not define a current tag")
        return

    current_target = resolve_tag(root, current_tag)
    if release_mode:
        if current_target is None:
            errors.append(f"unable to resolve Git tag {current_tag}")
        elif current_target != head:
            errors.append(
                f"tag {current_tag} points to {current_target}, expected reviewed HEAD {head}"
            )

        status = git_text(root, "status", "--porcelain")
        if status is None:
            errors.append("unable to inspect Git working-tree state")
        elif status:
            errors.append("release validation requires a clean working tree")
    elif current_target is not None and current_target != head:
        errors.append(
            f"existing tag {current_tag} points to {current_target}, not current HEAD {head}"
        )


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
    release_tag = manifest["release"]["tag"]
    frontend = manifest["source"]["frontend"]["commit"]
    backend = manifest["source"]["backend"]["commit"]

    print("GymFlow release checks passed.")
    print(f"Release record: {release_tag}.")
    print(f"Frontend revision: {frontend}.")
    print(f"Backend revision: {backend}.")
    print("Local showcase integrity and provenance are consistent.")
    if args.release:
        print(f"Release tag {release_tag} points to the reviewed HEAD.")
    else:
        current_target = resolve_tag(ROOT, release_tag)
        if current_target is None:
            print("Release record is ready for tag creation.")
        else:
            print(f"Existing tag alignment is valid for {release_tag}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
