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

STALE_VALUES = {
    "owner@" + "gymflow.demo",
    "staff@" + "gymflow.demo",
    "Demo" + "Owner123!",
    "Demo" + "Staff123!",
    "85fb121968bf862945debf349ce8c28df72c0fdd",
    "7bef6bfdf7ba1fbd3db9669b59aafa6ce6f2b9ac",
    "client-dashboard-redesign",
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
    ignored_parts = {".git", "downloads"}
    result: list[Path] = []
    for path in ROOT.rglob("*"):
        if not path.is_file() or any(part in ignored_parts for part in path.parts):
            continue
        if path.suffix.lower() in allowed or path.name == "LICENSE":
            result.append(path)
    return result


def check_required_files(errors: list[str]) -> None:
    for item in sorted(REQUIRED_FILES):
        if not (ROOT / item).is_file():
            errors.append(f"missing required file: {item}")


def check_unsafe_files(errors: list[str]) -> None:
    for path in ROOT.rglob("*"):
        if not path.is_file() or ".git" in path.parts:
            continue
        if path.name in FORBIDDEN_FILE_NAMES:
            errors.append(f"forbidden sensitive file name: {relative(path)}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden sensitive artifact type: {relative(path)}")


def normalize_link(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    return value.split()[0] if value else ""


def check_markdown_links(errors: list[str]) -> None:
    for document in ROOT.rglob("*.md"):
        if ".git" in document.parts:
            continue
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
        "6866feb84288bd1624b8ca6d4cc8a4407da5dd80",
        "10b7af743c73e3f7eca686080e1e74dc7ee67bde",
        "9e4f6a8c2d1b",
        "2026-07-15",
        "Current application screenshots | Not included",
        "Product walkthrough video | Not included",
    }
    for value in sorted(required_values):
        if value not in manifest:
            errors.append(f"build manifest is missing release evidence: {value}")

    forbidden_phrases = {
        "capture pending",
        "will be captured later",
        "will be captured from",
        "after screenshots and video are finalized",
    }
    for document_name in ("README.md", "BUILD_MANIFEST.md", "CHANGELOG.md"):
        content = (ROOT / document_name).read_text(encoding="utf-8-sig").lower()
        for phrase in sorted(forbidden_phrases):
            if phrase in content:
                errors.append(f"unfinished release wording in {document_name}: {phrase}")

    legacy = sorted(
        path for path in (ROOT / "screenshots").glob("*.*") if path.name != "README.md"
    )
    for path in legacy:
        errors.append(f"legacy root screenshot remains: {relative(path)}")


def check_readme_contract(errors: list[str]) -> None:
    readme = (ROOT / "README.md").read_text(encoding="utf-8-sig")
    required_phrases = {
        "multi-tenant",
        "client portal",
        "staff presence",
        "messaging",
        "deterministic professional demo",
        "environment readiness",
        "project ownership",
    }
    lowered = readme.lower()
    for phrase in sorted(required_phrases):
        if phrase not in lowered:
            errors.append(f"README is missing required positioning: {phrase}")


def main() -> int:
    errors: list[str] = []
    check_required_files(errors)
    check_unsafe_files(errors)
    check_markdown_links(errors)
    check_text_safety(errors)
    check_release_contract(errors)
    check_readme_contract(errors)

    if errors:
        print("GymFlow showcase checks failed:")
        for error in errors:
            print(f"- {error}")
        return 1

    print("GymFlow showcase checks passed.")
    print(f"Validated {len(list(ROOT.rglob('*.md')))} Markdown documents.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
