from __future__ import annotations

import sys

from showcase_validation import ROOT, markdown_files, run_base_checks


def main() -> int:
    errors, manifest = run_base_checks(ROOT)
    if errors:
        print("GymFlow showcase checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    assert manifest is not None
    gallery_total = manifest["gallery"]["total"]
    gallery_count = len(manifest["gallery"]["inventory"])
    approved_count = len(manifest["gallery"]["approved_sha256"])

    print("GymFlow showcase checks passed.")
    print(
        f"Gallery: {gallery_total} unique screenshots across "
        f"{gallery_count} galleries."
    )
    print(f"Screenshot integrity records: {approved_count} SHA-256 entries.")
    print(f"Markdown documents checked: {len(markdown_files(ROOT))}.")
    print("Repository hygiene, release record, links, and local tooling are consistent.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
