from __future__ import annotations

import re
import sys
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
FORBIDDEN_PATH_PARTS = {".idea", ".vscode", "__pycache__"}

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
}

INTERNAL_AUTHORING_PHRASES = {
    "capture pending",
    "replacement procedure",
    "capture preparation",
    "video description template",
    "final review checklist",
    "full pre-recording checklist",
    "recommended product video order",
    "recommended engineering video order",
    "after recording",
    "publication sequence",
    "manual repository task",
    "manual repository setting",
    "<showcase repository url>",
    "<tag/commit>",
    "status in this release candidate",
    "engineering case-study candidate includes",
    "|merge",
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
APPROVED_SCREENSHOT_DIRS = {"desktop", "engineering", "localization", "mobile", "portal"}
APPROVED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
EXPECTED_SCREENSHOT_COUNTS = {
    "desktop": 22,
    "engineering": 10,
    "localization": 4,
    "mobile": 7,
    "portal": 10,
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
                errors.append(
                    f"internal authoring language remains in {name}: {phrase}"
                )


def check_screenshot_inventory(errors: list[str]) -> None:
    root = ROOT / "screenshots"
    counts = {name: 0 for name in APPROVED_SCREENSHOT_DIRS}

    for path in sorted(root.rglob("*")):
        if not path.is_file() or path == root / "README.md":
            continue
        rel = path.relative_to(root)
        if len(rel.parts) != 2:
            errors.append(
                f"screenshot must be one level below an approved gallery: {relative(path)}"
            )
            continue
        gallery = rel.parts[0]
        if gallery not in APPROVED_SCREENSHOT_DIRS:
            errors.append(f"unapproved screenshot gallery: {relative(path)}")
            continue
        if path.suffix.lower() not in APPROVED_IMAGE_SUFFIXES:
            errors.append(f"unsupported screenshot type: {relative(path)}")
            continue
        counts[gallery] += 1

    for gallery, expected in EXPECTED_SCREENSHOT_COUNTS.items():
        actual = counts[gallery]
        if actual != expected:
            errors.append(
                f"screenshot inventory mismatch for {gallery}: "
                f"expected {expected}, found {actual}"
            )

    total = sum(counts.values())
    if total != 53:
        errors.append(f"screenshot inventory mismatch: expected 53, found {total}")


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
        "2026-07-15",
        "| Release identifier | `v1.0.0-showcase` |",
        "`anes-dev-ml/GymFlow-Showcase` / `main`",
        "Screenshot gallery | Included",
        "53 tracked images",
        "Product walkthrough video | Not included",
        "No green hosted-CI claim is made for this release",
    }
    for value in sorted(required_values):
        if value not in manifest:
            errors.append(f"build manifest is missing release evidence: {value}")


def require_phrases(
    errors: list[str],
    path: str,
    phrases: set[str],
    label: str,
) -> None:
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
            "53-image visual gallery",
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
            "53 screenshots",
            "Selected product views",
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
            "Product review coverage",
        },
        "Demo document",
    )
    require_phrases(
        errors,
        "RELEASES.md",
        {
            "# GymFlow Release Integrity",
            "screenshot-bearing engineering case study",
            "does not claim green hosted CI",
            "Correction policy",
        },
        "Release document",
    )
    require_phrases(
        errors,
        "ROADMAP.md",
        {
            "Product evolution",
            "Production infrastructure",
            "Production claim boundary",
        },
        "Roadmap",
    )


def check_workflow_contract(errors: list[str]) -> None:
    workflow = (ROOT / ".github/workflows/showcase-quality.yml").read_text(
        encoding="utf-8-sig"
    )
    for value in {
        "permissions:\n  contents: read",
        "timeout-minutes: 5",
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
    print("Validated 53 screenshots across 5 approved galleries.")
    print(f"Validated {len(markdown_files())} Markdown documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
