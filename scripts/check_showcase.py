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
        f"Validated {gallery_total} unique screenshots across "
        f"{gallery_count} approved galleries."
    )
    print(f"Validated {approved_count} exact screenshot SHA-256 approvals.")
    print(f"Validated {len(markdown_files(ROOT))} Markdown documents.")
    print("Validated tracked-file hygiene, release truth, and local tooling contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
