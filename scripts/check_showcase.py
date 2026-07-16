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

FORBIDDEN_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "id_rsa",
    "id_ed25519",
    "criptscheck_showcase.pyExit",
}

FORBIDDEN_SUFFIXES = {
    ".pem",
    ".p12",
    ".pfx",
    ".sqlite",
    ".sqlite3",
    ".db",
    ".dump",
}

FORBIDDEN_PATH_PARTS = {
    ".idea",
    ".vscode",
    "__pycache__",
}

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

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")


def relative(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def text_files() -> list[Path]:
    allowed = {".md", ".txt", ".yml", ".yaml", ".py", ""}
    ignored_parts = {".git", "downloads", "exports"}
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in allowed or path.name == "LICENSE":
            result.append(path)
    return result


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
            errors.append(
                f"forbidden sensitive or accidental file name: {relative(path)}"
            )
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


def check_release_contract(errors: list[str]) -> None:
    manifest = (ROOT / "BUILD_MANIFEST.md").read_text(encoding="utf-8-sig")
    required_values = {
        "489a82e03059465755c74b1be39ae7c05f98fb9b",
        "2234af20d1d9dd143bcac22edc699d3ee7fe515f",
        "9e4f6a8c2d1b",
        "2026-07-15",
        "| Release tag | `v1.0.0-showcase` |",
        "`anes-dev-ml/GymFlow-Showcase` / `main`",
        "Current application screenshots | Not included",
        "Product walkthrough video | Not included",
        "No green hosted-CI claim is made for this release",
        "- [x] Create `v1.0.0-showcase` on the finalized showcase commit.",
    }
    for value in sorted(required_values):
        if value not in manifest:
            errors.append(f"build manifest is missing release evidence: {value}")

    allowed_unchecked = {
        "- [ ] Configure the GitHub social preview from an approved release design."
    }
    for line in manifest.splitlines():
        stripped = line.strip()
        if stripped.startswith("- [ ]") and stripped not in allowed_unchecked:
            errors.append(f"unexpected unfinished manifest checklist item: {stripped}")

    forbidden_phrases = {
        "capture pending",
        "will be captured later",
        "will be captured from",
        "after screenshots and video are finalized",
        "checks are green",
        "all three prs are merged",
        "|merge",
        "status in this release candidate",
        "engineering case-study candidate includes",
    }
    for document in markdown_files():
        content = document.read_text(encoding="utf-8-sig").lower()
        for phrase in sorted(forbidden_phrases):
            if phrase in content:
                errors.append(
                    f"unfinished or contradictory release wording in "
                    f"{relative(document)}: {phrase}"
                )

    screenshot_root = ROOT / "screenshots"
    for path in sorted(screenshot_root.rglob("*")):
        if path.is_file() and path != screenshot_root / "README.md":
            errors.append(f"undeclared screenshot asset remains: {relative(path)}")

    video_root = ROOT / "video"
    for path in sorted(video_root.rglob("*")):
        if path.is_file() and path != video_root / "README.md":
            errors.append(f"undeclared video asset remains: {relative(path)}")


def check_document_contracts(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    required_readme_phrases = {
        "multi-tenant",
        "client portal",
        "staff presence",
        "messaging",
        "deterministic professional demo",
        "environment readiness",
        "project ownership",
        "does not claim a current screenshot set",
        "does not claim green hosted ci",
    }
    lowered = readme.lower()
    for phrase in sorted(required_readme_phrases):
        if phrase not in lowered:
            errors.append(f"README is missing required positioning: {phrase}")

    roadmap = (ROOT / "ROADMAP.md").read_text(encoding="utf-8-sig")
    required_roadmap_phrases = {
        "| Git tag | Complete | `v1.0.0-showcase` |",
        "Deferred to media release",
        "No downloadable media or binaries are included",
    }
    for phrase in sorted(required_roadmap_phrases):
        if phrase not in roadmap:
            errors.append(f"ROADMAP is missing final release state: {phrase}")

    releases = (ROOT / "RELEASES.md").read_text(encoding="utf-8-sig")
    required_release_phrases = {
        "The `v1.0.0-showcase` tag is a documentation-only engineering case study.",
        "must not claim green hosted CI",
        "A code failure, test failure, configuration failure inside a running job",
    }
    for phrase in sorted(required_release_phrases):
        if phrase not in releases:
            errors.append(f"RELEASES is missing evidence policy: {phrase}")


def check_workflow_contract(errors: list[str]) -> None:
    workflow = (ROOT / ".github/workflows/showcase-quality.yml").read_text(
        encoding="utf-8-sig"
    )
    required_values = {
        "permissions:\n  contents: read",
        "timeout-minutes: 5",
        "python -m compileall -q scripts",
        "python scripts/check_showcase.py",
    }
    for value in sorted(required_values):
        if value not in workflow:
            errors.append(f"showcase workflow is missing safety contract: {value}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_unsafe_files(errors)
    check_markdown_links(errors)
    check_text_safety(errors)
    check_release_contract(errors)
    check_document_contracts(errors)
    check_workflow_contract(errors)

    if errors:
        print("GymFlow showcase checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GymFlow showcase checks passed.")
    print(f"Validated {len(markdown_files())} Markdown documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
