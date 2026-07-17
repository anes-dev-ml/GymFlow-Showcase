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

    gallery_total = manifest["gallery"]["total"] if manifest else "unknown"
    gallery_count = len(manifest["gallery"]["inventory"]) if manifest else "unknown"
    print("GymFlow showcase checks passed.")
    print(
        f"Validated {gallery_total} unique screenshots across "
        f"{gallery_count} approved galleries."
    )
    print(f"Validated {len(markdown_files(ROOT))} Markdown documents.")
    print("Validated tracked-file hygiene, release truth, and local tooling contracts.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
