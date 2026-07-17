from __future__ import annotations

import argparse
import hashlib
import re
import subprocess
import sys
from pathlib import Path

sys.dont_write_bytecode = True

import check_showcase

ROOT = Path(__file__).resolve().parents[1]
FRONTEND_SHA = "b73a623c3985e4bc458d04b4b484887ada593fa5"
BACKEND_SHA = "2234af20d1d9dd143bcac22edc699d3ee7fe515f"
TARGET_TAG = "v1.0.1-showcase"

CANONICAL_ROW = re.compile(
    r"^\|\s*(Frontend|Backend)\s*\|[^\n]*?\|\s*`([0-9a-f]{40})`\s*\|",
    re.MULTILINE,
)

# These exact assets have already completed manual review. Requiring their
# hashes prevents a later overwrite from silently weakening the release.
APPROVED_EXACT_HASHES = {
    "screenshots/mobile/04-check-in-pass.png": (
        "7bf6a105ba160fe87a35d46a97c62a6d4050d9a0dc20752f8025ea1e2fae61c7",
        "reviewed full-height pass with deliberately invalid static QR",
    ),
    "screenshots/mobile/06-dashboard.png": (
        "6d8570aaad3c305b9f495e340b274a4f10d6005a4834e90247f3719727f152cf",
        "approved compact mobile dashboard",
    ),
    "screenshots/portal/02-bookings.png": (
        "62a958d0f84fa37c8ed38dd1c65303f95ffea5444e6188b66c59a479e11fa5bd",
        "approved populated desktop portal bookings capture",
    ),
    "screenshots/engineering/15-frontend-commit-history.png": (
        "b04a3fcbf71aaf96254bf69e8d6639de522dd9675efc0b23208871be5438b347",
        "curated frontend history for the canonical regression-reconciled revision",
    ),
}

# Additional media found during the final source-alignment audit. These are
# intentionally separate from the base validator so the historical validator
# remains readable while the candidate gate becomes stricter.
REJECTED_FINAL_MEDIA = {
    "b40892477efe226ea39f10a83b2a3490752ec11dd83139b0c064c6cfd67caa32": (
        "staff messaging capture predates the final communication workspace"
    ),
    "86526846feed25d1343bc8be85fd8f40d7cdc15c3dff10142b3f16f6099ffaa5": (
        "frontend provenance image records the superseded frontend revision"
    ),
    "d6dd447e5c9e268cfc70a3810c39a59a680a408aef2207f8eaa2ef89bca7ff1f": (
        "mobile portal bookings capture shows an empty schedule"
    ),
}


def sha256(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def check_canonical_sources(errors: list[str]) -> None:
    manifest = (ROOT / "BUILD_MANIFEST.md").read_text(encoding="utf-8-sig")
    gallery = (ROOT / "screenshots/README.md").read_text(encoding="utf-8-sig")
    changelog = (ROOT / "CHANGELOG.md").read_text(encoding="utf-8-sig")

    canonical = {component: revision for component, revision in CANONICAL_ROW.findall(manifest)}
    expected = {"Frontend": FRONTEND_SHA, "Backend": BACKEND_SHA}

    for component, revision in expected.items():
        actual = canonical.get(component)
        if actual != revision:
            errors.append(
                f"canonical {component.lower()} revision mismatch: "
                f"expected {revision}, found {actual or 'missing'}"
            )

    for document, content in {
        "BUILD_MANIFEST.md": manifest,
        "screenshots/README.md": gallery,
        "CHANGELOG.md": changelog,
    }.items():
        if FRONTEND_SHA not in content:
            errors.append(f"{document} does not record final frontend revision {FRONTEND_SHA}")

    if BACKEND_SHA not in manifest or BACKEND_SHA not in gallery:
        errors.append(f"final backend revision {BACKEND_SHA} is not consistently recorded")


def check_final_media(errors: list[str]) -> None:
    for relative_path, (expected_hash, label) in APPROVED_EXACT_HASHES.items():
        path = ROOT / relative_path
        if not path.is_file():
            errors.append(f"missing approved release asset: {relative_path}")
            continue
        actual_hash = sha256(path)
        if actual_hash != expected_hash:
            errors.append(
                f"approved release asset changed: {relative_path} — expected {label} "
                f"(sha256 {expected_hash[:12]}…), found {actual_hash[:12]}…"
            )

    screenshots_root = ROOT / "screenshots"
    for path in screenshots_root.rglob("*"):
        if not path.is_file() or path.name == "README.md":
            continue
        digest = sha256(path)
        reason = REJECTED_FINAL_MEDIA.get(digest)
        if reason:
            errors.append(
                f"rejected final media remains: {path.relative_to(ROOT).as_posix()} — {reason}"
            )


def check_release_wording(errors: list[str]) -> None:
    video_status = re.sub(
        r"\s+",
        " ",
        (ROOT / "video/README.md").read_text(encoding="utf-8-sig").lower(),
    )
    manifest = re.sub(
        r"\s+",
        " ",
        (ROOT / "BUILD_MANIFEST.md").read_text(encoding="utf-8-sig").lower(),
    )

    for phrase in {
        "historical media",
        "not part of the current candidate",
        "provenance-bound tag",
    }:
        if phrase not in video_status:
            errors.append(f"video/README.md is missing release-boundary wording: {phrase}")

    if "product walkthrough video | not included" not in manifest:
        errors.append("BUILD_MANIFEST.md does not exclude video from the current candidate")


def git_output(*args: str) -> str | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return completed.stdout.strip()


def check_release_tag(errors: list[str]) -> None:
    head = git_output("rev-parse", "HEAD")
    tagged = git_output("rev-list", "-n", "1", TARGET_TAG)
    if head is None:
        errors.append("unable to resolve the current Git commit")
        return
    if tagged is None:
        errors.append(f"release tag {TARGET_TAG} does not exist")
        return
    if tagged != head:
        errors.append(
            f"release tag {TARGET_TAG} points to {tagged}, but reviewed HEAD is {head}"
        )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Run the complete GymFlow showcase release-candidate gate."
    )
    parser.add_argument(
        "--release",
        action="store_true",
        help=f"also require {TARGET_TAG} to point to the current reviewed commit",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()

    base_result = check_showcase.main()
    errors: list[str] = []
    check_canonical_sources(errors)
    check_final_media(errors)
    check_release_wording(errors)
    if args.release:
        check_release_tag(errors)

    if base_result != 0 or errors:
        if errors:
            print("GymFlow final candidate checks failed:")
            for error in errors:
                print(f"- {error}")
        return 1

    print("GymFlow final candidate checks passed.")
    print(f"Validated frontend provenance: {FRONTEND_SHA}.")
    print(f"Validated backend provenance: {BACKEND_SHA}.")
    if args.release:
        print(f"Validated release tag: {TARGET_TAG} points to reviewed HEAD.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
