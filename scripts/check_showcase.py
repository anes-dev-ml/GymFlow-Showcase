from __future__ import annotations

import hashlib
import re
import struct
import sys
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]

REQUIRED_FILES = {
    "README.md",
    "ARCHITECTURE.md",
    "SECURITY.md",
    "DEMO.md",
    "RELEASES.md",
    "ROADMAP.md",
    "CHANGELOG.md",
    "BUILD_MANIFEST.md",
    "LICENSE",
    ".gitignore",
    ".gitattributes",
    ".github/workflows/showcase-quality.yml",
    "docs/PRODUCT.md",
    "docs/ENGINEERING.md",
    "docs/SECURITY_OVERVIEW.md",
    "docs/THREAT_MODEL.md",
    "docs/QUALITY.md",
    "docs/OPERATIONS.md",
    "docs/ENGINEERING_JOURNEY.md",
    "screenshots/README.md",
    "video/README.md",
}

PUBLIC_PRESENTATION_FILES = {
    "README.md",
    "BUILD_MANIFEST.md",
    "CHANGELOG.md",
    "DEMO.md",
    "RELEASES.md",
    "ROADMAP.md",
    "screenshots/README.md",
    "video/README.md",
}

FORBIDDEN_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "id_rsa",
    "id_ed25519",
    "criptscheck_showcase.pyExit",
}
FORBIDDEN_SUFFIXES = {".pem", ".p12", ".pfx", ".sqlite", ".sqlite3", ".db", ".dump"}
FORBIDDEN_PATH_PARTS = {".idea", ".vscode", "__pycache__", ".pytest_cache", ".dart_tool"}

STALE_VALUES = {
    "owner@" + "gymflow.demo",
    "staff@" + "gymflow.demo",
    "Demo" + "Owner123!",
    "Demo" + "Staff123!",
    "85fb121968bf862945de" + "bf349ce8c28df72c0fdd",
    "7bef6bfdf7ba1fbd3db" + "9669b59aafa6ce6f2b9ac",
    "client-dashboard-" + "redesign",
}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "Stripe live secret": re.compile(r"\bsk_live_[A-Za-z0-9]{12,}"),
    "Stripe test secret": re.compile(r"\bsk_test_[A-Za-z0-9]{12,}"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9]{20,}"),
    "Google API key": re.compile(r"\bAIza[0-9A-Za-z_-]{30,}"),
    "JWT-like credential": re.compile(
        r"\beyJ[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\.[A-Za-z0-9_-]{8,}\b"
    ),
}

INTERNAL_AUTHORING_PHRASES = {
    "capture pending",
    "replacement procedure",
    "capture preparation",
    "video description template",
    "full pre-recording checklist",
    "recommended product video order",
    "recommended engineering video order",
    "after recording",
    "publication sequence",
    "manual repository task",
    "manual repository setting",
    "<showcase repository url>",
    "<tag/commit>",
    "|merge",
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
APPROVED_SCREENSHOT_DIRS = {"desktop", "engineering", "localization", "mobile", "portal"}
APPROVED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}

EXPECTED_SCREENSHOTS = {
    "desktop": {
        "01-public-home.png",
        "02-owner-dashboard.png",
        "03-client-command-center.png",
        "04-staff-presence.png",
        "05-bookings.png",
        "06-reports.png",
        "07-professional-messaging.png",
        "08-public-features.png",
        "09-public-pricing.png",
        "10-public-security.png",
        "11-auth.png",
        "12-clients.png",
        "13-plans.png",
        "14-services.png",
        "15-trainer-availability.png",
        "16-invitations.png",
        "17-check-ins.png",
        "18-payments.png",
        "19-notifications.png",
        "20-activity-logs.png",
        "21-settings.png",
        "22-billing.png",
    },
    "engineering": {
        "07-frontend-project-structure.png",
        "08-backend-project-structure.png",
        "09-postgresql-schema.png",
        "10-openapi.png",
        "11-docker-runtime.png",
        "12-demo-clients-data.png",
        "13-demo-messages-data.png",
        "14-demo-payments-data.png",
        "15-frontend-commit-history.png",
        "16-backend-commit-history.png",
    },
    "localization": {
        "01-arabic-rtl.png",
        "02-french-dashboard.png",
        "03-arabic-portal-mobile.png",
        "04-arabic-portal-desktop.png",
    },
    "mobile": {
        "01-portal-home.png",
        "02-portal-bookings.png",
        "03-portal-payments.png",
        "04-check-in-pass.png",
        "05-public-home.png",
        "06-dashboard.png",
        "07-client-detail.png",
    },
    "portal": {
        "00-access.png",
        "01-portal-home.png",
        "02-bookings.png",
        "03-membership.png",
        "04-payments.png",
        "05-receipt.png",
        "06-progress.png",
        "07-check-in-pass.png",
        "08-messages.png",
        "09-profile-settings.png",
    },
}

# Known media that failed a release review. Keeping their hashes here prevents a
# filename-only replacement or accidental reintroduction. The last three entries
# intentionally keep the candidate red until fresh application captures replace
# those exact files.
BLOCKED_IMAGE_SHA256 = {
    "d074a81c15e600540ff5bfdc1c61ff737639e7deae727bbb88e50ed5d85045ee": "published QR contained a generated credential",
    "09c0a175c226c94908873b9092174704f8b50c2496cad66ab28d3d52020f9e5d": "browser zoom overlay remained visible",
    "9bbf368029eae06475ab9eba2fd55512923f85f404097bbf9e6674ac8460b8f8": "mobile check-in pass is cropped before the QR evidence",
    "8f5deb25a640bd748b183e68017ecd12d49c26b63c47aa603e84251f6f6e5788": "mobile dashboard repeats the same summary cards",
    "a937ef59a984ee6f33caa89a049a2a528e2566415e522d8a7ab91bfc95ce8f16": "portal bookings capture shows no available services or upcoming bookings",
}


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def text_files() -> list[Path]:
    allowed = {".md", ".txt", ".yml", ".yaml", ".py", ""}
    ignored_parts = {".git", "downloads", "exports"}
    return [
        path
        for path in ROOT.rglob("*")
        if path.is_file()
        and not any(part in ignored_parts for part in path.parts)
        and (path.suffix.lower() in allowed or path.name == "LICENSE")
    ]


def markdown_files() -> list[Path]:
    return [
        path
        for path in ROOT.rglob("*.md")
        if path.is_file() and ".git" not in path.parts
    ]


def screenshot_files() -> list[Path]:
    root = ROOT / "screenshots"
    return [
        path
        for path in sorted(root.rglob("*"))
        if path.is_file() and path != root / "README.md"
    ]


def check_required_files(errors: list[str]) -> None:
    for item in sorted(REQUIRED_FILES):
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")


def check_unsafe_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if any(part in FORBIDDEN_PATH_PARTS for part in path.parts):
            errors.append(f"forbidden editor/generated path: {relative(path)}")
        if path.name in FORBIDDEN_FILE_NAMES:
            errors.append(f"forbidden sensitive or accidental file name: {relative(path)}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden sensitive artifact type: {relative(path)}")


def normalize_link(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    return value.split()[0] if value else ""


def check_markdown_links(errors: list[str]) -> None:
    for document in markdown_files():
        content = document.read_text(encoding="utf-8-sig")
        for match in MARKDOWN_LINK.finditer(content):
            target = normalize_link(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            candidate = (
                ROOT / path_part.lstrip("/")
                if path_part.startswith("/")
                else document.parent / path_part
            )
            if not candidate.resolve().exists():
                errors.append(f"broken local link in {relative(document)}: {target}")


def check_text_safety(errors: list[str]) -> None:
    for path in text_files():
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue
        for stale in STALE_VALUES:
            if stale in content:
                errors.append(f"stale demo credential/value in {relative(path)}: {stale}")
        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possible {name} in {relative(path)}")


def check_public_tone(errors: list[str]) -> None:
    for name in sorted(PUBLIC_PRESENTATION_FILES):
        path = ROOT / name
        content = path.read_text(encoding="utf-8-sig").lower()
        for phrase in sorted(INTERNAL_AUTHORING_PHRASES):
            if phrase in content:
                errors.append(f"internal authoring language remains in {name}: {phrase}")


def read_png_size(path: Path) -> tuple[int, int]:
    with path.open("rb") as handle:
        signature = handle.read(24)
    if len(signature) < 24 or signature[:8] != b"\x89PNG\r\n\x1a\n":
        raise ValueError("invalid PNG signature")
    return struct.unpack(">II", signature[16:24])


def read_jpeg_size(path: Path) -> tuple[int, int]:
    data = path.read_bytes()
    if not data.startswith(b"\xff\xd8"):
        raise ValueError("invalid JPEG signature")
    index = 2
    while index + 9 < len(data):
        if data[index] != 0xFF:
            index += 1
            continue
        marker = data[index + 1]
        index += 2
        if marker in {0xD8, 0xD9}:
            continue
        if index + 2 > len(data):
            break
        length = int.from_bytes(data[index:index + 2], "big")
        if length < 2 or index + length > len(data):
            break
        if marker in {0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7, 0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF}:
            height = int.from_bytes(data[index + 3:index + 5], "big")
            width = int.from_bytes(data[index + 5:index + 7], "big")
            return width, height
        index += length
    raise ValueError("JPEG dimensions not found")


def image_size(path: Path) -> tuple[int, int]:
    suffix = path.suffix.lower()
    if suffix == ".png":
        return read_png_size(path)
    if suffix in {".jpg", ".jpeg"}:
        return read_jpeg_size(path)
    raise ValueError("unsupported image type")


def check_dimensions(path: Path, gallery: str, errors: list[str]) -> None:
    try:
        width, height = image_size(path)
    except ValueError as exc:
        errors.append(f"invalid image in {relative(path)}: {exc}")
        return

    if width < 600 or height < 650:
        errors.append(f"image is too small for review: {relative(path)} is {width}x{height}")

    name = path.name
    mobile_layout = gallery == "mobile" or (
        gallery == "localization" and name == "03-arabic-portal-mobile.png"
    )
    if mobile_layout:
        if height <= width or width < 650 or height < 1200:
            errors.append(f"mobile image must be a readable portrait capture: {relative(path)} is {width}x{height}")
    elif gallery in {"desktop", "portal"} or gallery == "localization":
        if width <= height or width < 1400:
            errors.append(f"desktop image must be a readable landscape capture: {relative(path)} is {width}x{height}")


def check_screenshot_inventory(errors: list[str]) -> None:
    root = ROOT / "screenshots"
    actual: dict[str, set[str]] = {name: set() for name in APPROVED_SCREENSHOT_DIRS}
    hashes: dict[str, list[str]] = defaultdict(list)

    for path in screenshot_files():
        rel = path.relative_to(root)
        if len(rel.parts) != 2:
            errors.append(f"screenshot must be one level below an approved gallery: {relative(path)}")
            continue
        gallery = rel.parts[0]
        if gallery not in APPROVED_SCREENSHOT_DIRS:
            errors.append(f"unapproved screenshot gallery: {relative(path)}")
            continue
        if path.suffix.lower() not in APPROVED_IMAGE_SUFFIXES:
            errors.append(f"unsupported screenshot type: {relative(path)}")
            continue

        actual[gallery].add(path.name)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes[digest].append(relative(path))
        if digest in BLOCKED_IMAGE_SHA256:
            errors.append(
                f"rejected screenshot remains: {relative(path)} — {BLOCKED_IMAGE_SHA256[digest]}"
            )
        check_dimensions(path, gallery, errors)

    for gallery, expected_names in EXPECTED_SCREENSHOTS.items():
        missing = sorted(expected_names - actual[gallery])
        extra = sorted(actual[gallery] - expected_names)
        for name in missing:
            errors.append(f"missing screenshot: screenshots/{gallery}/{name}")
        for name in extra:
            errors.append(f"unexpected screenshot: screenshots/{gallery}/{name}")

    total = sum(len(names) for names in actual.values())
    if total != 53:
        errors.append(f"screenshot inventory mismatch: expected 53, found {total}")

    for digest, paths in sorted(hashes.items()):
        if len(paths) > 1:
            errors.append(
                "duplicate screenshot content: " + ", ".join(paths) + f" (sha256 {digest[:12]}…)"
            )

    if len(hashes) != 53:
        errors.append(f"screenshot uniqueness mismatch: expected 53 unique hashes, found {len(hashes)}")


def check_video_inventory(errors: list[str]) -> None:
    root = ROOT / "video"
    allowed = {root / "README.md"}
    for path in sorted(root.rglob("*")):
        if path.is_file() and path not in allowed:
            errors.append(f"undeclared video asset remains: {relative(path)}")


def check_release_contract(errors: list[str]) -> None:
    manifest = (ROOT / "BUILD_MANIFEST.md").read_text(encoding="utf-8-sig")
    required_values = {
        "489a82e03059465755c74b1be39ae7c05f98fb9b",
        "2234af20d1d9dd143bcac22edc699d3ee7fe515f",
        "9e4f6a8c2d1b",
        "2026-07-16",
        "| Target release identifier | `v1.0.1-showcase` |",
        "`anes-dev-ml/GymFlow-Showcase` / `main`",
        "53 tracked files",
        "Product walkthrough video | Not included",
        "No green hosted-CI claim is made for this release candidate",
        "all 53 image files have unique content hashes",
    }
    for value in sorted(required_values):
        if value not in manifest:
            errors.append(f"build manifest is missing release evidence: {value}")


def require_phrases(errors: list[str], path: str, phrases: set[str], label: str) -> None:
    content = (ROOT / path).read_text(encoding="utf-8-sig").lower()
    for phrase in sorted(phrases):
        if phrase.lower() not in content:
            errors.append(f"{label} is missing required public content: {phrase}")


def check_document_contracts(errors: list[str]) -> None:
    require_phrases(
        errors,
        "README.md",
        {
            "multi-tenant",
            "client portal",
            "staff presence",
            "deterministic professional demo",
            "GymFlow Visual Gallery",
            "does not claim green hosted CI",
            "Project ownership",
        },
        "README",
    )
    require_phrases(
        errors,
        "screenshots/README.md",
        {
            "# GymFlow Visual Gallery",
            "53 stable screenshot paths",
            "53 unique image hashes",
            "Capture and privacy standard",
            "Deterministic data and visual state",
            "Provenance and integrity",
        },
        "Screenshot gallery",
    )
    require_phrases(
        errors,
        "video/README.md",
        {
            "# GymFlow Walkthrough Status",
            "does not include a public walkthrough video",
            "Intended walkthrough narrative",
            "Future media releases",
        },
        "Walkthrough status",
    )
    require_phrases(
        errors,
        "DEMO.md",
        {
            "# GymFlow Demo Environment",
            "Safety contract",
            "Visual-capture semantics",
            "No screenshot may publish a real generated token or QR credential",
        },
        "Demo document",
    )
    require_phrases(
        errors,
        "RELEASES.md",
        {
            "# GymFlow Release Integrity",
            "v1.0.1-showcase",
            "Historical release",
            "does not claim green hosted CI",
            "Correction policy",
        },
        "Release document",
    )
    require_phrases(
        errors,
        "SECURITY.md",
        {
            "Report a vulnerability",
            "Security",
            "Advisories",
            "Do not post exploit details",
        },
        "Security policy",
    )
    require_phrases(
        errors,
        "ROADMAP.md",
        {"Product evolution", "Production infrastructure", "Production claim boundary"},
        "Roadmap",
    )


def check_workflow_contract(errors: list[str]) -> None:
    workflow = (ROOT / ".github/workflows/showcase-quality.yml").read_text(encoding="utf-8-sig")
    for value in {
        "workflow_dispatch:",
        "permissions:\n  contents: read",
        "timeout-minutes: 5",
        "PYTHONUTF8: '1'",
        "python -m compileall -q scripts",
        "python scripts/check_showcase.py",
    }:
        if value not in workflow:
            errors.append(f"showcase workflow is missing safety contract: {value}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_unsafe_files(errors)
    check_markdown_links(errors)
    check_text_safety(errors)
    check_public_tone(errors)
    check_screenshot_inventory(errors)
    check_video_inventory(errors)
    check_release_contract(errors)
    check_document_contracts(errors)
    check_workflow_contract(errors)

    if errors:
        print("GymFlow showcase checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GymFlow showcase checks passed.")
    print("Validated 53 unique screenshots across 5 approved galleries.")
    print(f"Validated {len(markdown_files())} Markdown documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())