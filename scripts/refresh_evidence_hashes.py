from __future__ import annotations

import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = ROOT / "release" / "evidence-manifest.json"


def main() -> int:
    manifest = json.loads(MANIFEST_PATH.read_text(encoding="utf-8-sig"))
    inventory = manifest.get("gallery", {}).get("inventory", {})
    if not isinstance(inventory, dict):
        print("Invalid gallery inventory in release/evidence-manifest.json.")
        return 1

    approved: dict[str, str] = {}
    missing: list[str] = []

    for gallery, names in sorted(inventory.items()):
        if not isinstance(gallery, str) or not isinstance(names, list):
            print("Invalid gallery inventory entry.")
            return 1
        for name in names:
            relative = f"screenshots/{gallery}/{name}"
            path = ROOT / relative
            if not path.is_file():
                missing.append(relative)
                continue
            approved[relative] = hashlib.sha256(path.read_bytes()).hexdigest()

    if missing:
        print("Cannot refresh evidence hashes; files are missing:")
        for path in missing:
            print(f"- {path}")
        return 1

    if len(approved) != manifest.get("gallery", {}).get("total"):
        print(
            "Cannot refresh evidence hashes; inventory total does not match "
            f"the {len(approved)} files discovered."
        )
        return 1

    blocked = manifest.get("gallery", {}).get("blocked_sha256", {})
    blocked_hits = [
        path for path, digest in approved.items() if digest in blocked
    ]
    if blocked_hits:
        print("Cannot approve rejected evidence:")
        for path in blocked_hits:
            print(f"- {path}: {blocked[approved[path]]}")
        return 1

    manifest["gallery"]["approved_sha256"] = dict(sorted(approved.items()))
    MANIFEST_PATH.write_text(
        json.dumps(manifest, indent=2, ensure_ascii=False) + "\n",
        encoding="utf-8",
    )
    print(f"Recorded exact SHA-256 approval for {len(approved)} screenshots.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
