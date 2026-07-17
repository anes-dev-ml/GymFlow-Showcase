from __future__ import annotations

import hashlib
import json
import re
import struct
import subprocess
from collections import defaultdict
from pathlib import Path
from urllib.parse import unquote

ROOT = Path(__file__).resolve().parents[1]
MANIFEST_PATH = Path("release/evidence-manifest.json")

REQUIRED_FILES = {
    "README.md",
    "ARCHITECTURE.md",
    "BUILD_MANIFEST.md",
    "CHANGELOG.md",
    "DEMO.md",
    "LICENSE",
    "RELEASES.md",
    "ROADMAP.md",
    "SECURITY.md",
    "docs/ENGINEERING.md",
    "docs/OPERATIONS.md",
    "docs/PRODUCT.md",
    "docs/QUALITY.md",
    "docs/SECURITY_OVERVIEW.md",
    "docs/THREAT_MODEL.md",
    "release/evidence-manifest.json",
    "release/v1.0.2-release-notes.md",
    "screenshots/README.md",
    "scripts/check_release_candidate.py",
    "scripts/check_showcase.py",
    "scripts/showcase_validation.py",
    "scripts/validate_release.ps1",
    "scripts/validate_release.sh",
    "tests/test_showcase_validation.py",
    "video/README.md",
}

PUBLIC_PRESENTATION_FILES = {
    "README.md",
    "ARCHITECTURE.md",
    "BUILD_MANIFEST.md",
    "CHANGELOG.md",
    "DEMO.md",
    "LICENSE",
    "RELEASES.md",
    "ROADMAP.md",
    "SECURITY.md",
    "docs/ENGINEERING.md",
    "docs/OPERATIONS.md",
    "docs/PRODUCT.md",
    "docs/QUALITY.md",
    "docs/SECURITY_OVERVIEW.md",
    "docs/THREAT_MODEL.md",
    "release/v1.0.2-release-notes.md",
    "screenshots/README.md",
    "video/README.md",
}

INTERNAL_AUTHORING_PHRASES = {
    "how to capture",
    "capture this image",
    "replace this image",
    "for the owner",
    "tell the owner",
    "instructions for the owner",
    "todo for owner",
    "screenshot instructions",
}

FORBIDDEN_PATH_PARTS = {
    ".idea",
    ".vscode",
    "__pycache__",
    ".pytest_cache",
    ".mypy_cache",
    ".dart_tool",
    "build",
}

FORBIDDEN_FILE_NAMES = {
    ".env",
    ".env.local",
    ".env.production",
    "key.properties",
    "google-services.json",
    "GoogleService-Info.plist",
}

FORBIDDEN_SUFFIXES = {
    ".pem",
    ".p12",
    ".pfx",
    ".jks",
    ".keystore",
    ".sqlite",
    ".db",
    ".log",
}

OBSOLETE_RELEASE_TEXT = {
    "8242f24fb05f0918393e439b5e0f1cc2e5f3086d",
    "main is preparing `v1.0.1-showcase`",
    "unreleased — `v1.0.1-showcase` candidate",
    "before the candidate tag is created",
    "tag only after every final gate passes",
}

SECRET_PATTERNS = {
    "private key": re.compile(r"-----BEGIN (?:RSA |EC |OPENSSH )?PRIVATE KEY-----"),
    "GitHub token": re.compile(r"\bgh[pousr]_[A-Za-z0-9_]{20,}\b"),
    "Stripe live secret": re.compile(r"\bsk_live_[A-Za-z0-9]{16,}\b"),
    "Stripe live restricted key": re.compile(r"\brk_live_[A-Za-z0-9]{16,}\b"),
    "JWT-like token": re.compile(
        r"\beyJ[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\.[A-Za-z0-9_-]{12,}\b"
    ),
}

MARKDOWN_LINK = re.compile(r"!?\[[^\]]*\]\(([^)]+)\)")
APPROVED_IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg"}
APPROVED_SCREENSHOT_DIRS = {
    "desktop",
    "portal",
    "mobile",
    "localization",
    "engineering",
}


def git_bytes(root: Path, *args: str) -> bytes | None:
    try:
        completed = subprocess.run(
            ["git", *args],
            cwd=root,
            check=True,
            capture_output=True,
        )
    except (FileNotFoundError, subprocess.CalledProcessError):
        return None
    return completed.stdout


def git_text(root: Path, *args: str) -> str | None:
    value = git_bytes(root, *args)
    if value is None:
        return None
    return value.decode("utf-8", errors="replace").strip()


def tracked_relative_paths(root: Path = ROOT) -> list[Path]:
    output = git_bytes(root, "ls-files", "-z")
    if output is None:
        ignored = {".git", "downloads", "exports", "__pycache__"}
        return sorted(
            path.relative_to(root)
            for path in root.rglob("*")
            if path.is_file() and not any(part in ignored for part in path.parts)
        )
    return sorted(
        Path(item.decode("utf-8"))
        for item in output.split(b"\0")
        if item
    )


def tracked_files(root: Path = ROOT) -> list[Path]:
    return [root / path for path in tracked_relative_paths(root)]


def relative(path: Path, root: Path = ROOT) -> str:
    return path.relative_to(root).as_posix()


def load_manifest(root: Path = ROOT) -> dict:
    path = root / MANIFEST_PATH
    try:
        data = json.loads(path.read_text(encoding="utf-8-sig"))
    except (FileNotFoundError, json.JSONDecodeError) as exc:
        raise ValueError(f"invalid evidence manifest: {exc}") from exc
    if not isinstance(data, dict):
        raise ValueError("invalid evidence manifest: root must be an object")
    return data


def expected_screenshots(manifest: dict) -> dict[str, set[str]]:
    inventory = manifest.get("gallery", {}).get("inventory", {})
    if not isinstance(inventory, dict):
        return {}
    return {
        gallery: set(names)
        for gallery, names in inventory.items()
        if isinstance(gallery, str) and isinstance(names, list)
    }


def text_files(root: Path = ROOT) -> list[Path]:
    allowed = {".md", ".txt", ".yml", ".yaml", ".py", ".ps1", ".sh", ".json", ""}
    return [
        path
        for path in tracked_files(root)
        if path.suffix.lower() in allowed or path.name == "LICENSE"
    ]


def markdown_files(root: Path = ROOT) -> list[Path]:
    return [path for path in tracked_files(root) if path.suffix.lower() == ".md"]


def screenshot_files(root: Path = ROOT) -> list[Path]:
    screenshot_root = root / "screenshots"
    return [
        path
        for path in tracked_files(root)
        if screenshot_root in path.parents and path != screenshot_root / "README.md"
    ]


def check_required_files(errors: list[str], root: Path = ROOT) -> None:
    tracked = {path.as_posix() for path in tracked_relative_paths(root)}
    for item in sorted(REQUIRED_FILES):
        if item not in tracked:
            errors.append(f"missing required tracked file: {item}")


def check_tracked_file_safety(errors: list[str], root: Path = ROOT) -> None:
    for path in tracked_files(root):
        rel = path.relative_to(root)
        if any(part in FORBIDDEN_PATH_PARTS for part in rel.parts):
            errors.append(f"forbidden tracked editor/generated path: {rel.as_posix()}")
        if path.name in FORBIDDEN_FILE_NAMES:
            errors.append(f"forbidden tracked sensitive file name: {rel.as_posix()}")
        if path.suffix.lower() in FORBIDDEN_SUFFIXES:
            errors.append(f"forbidden tracked sensitive artifact type: {rel.as_posix()}")


def normalize_link(raw: str) -> str:
    value = raw.strip()
    if value.startswith("<") and value.endswith(">"):
        value = value[1:-1]
    return value.split()[0] if value else ""


def check_markdown_links(errors: list[str], root: Path = ROOT) -> None:
    for document in markdown_files(root):
        content = document.read_text(encoding="utf-8-sig")
        for match in MARKDOWN_LINK.finditer(content):
            target = normalize_link(match.group(1))
            if not target or target.startswith(("http://", "https://", "mailto:", "#")):
                continue
            path_part = unquote(target.split("#", 1)[0].split("?", 1)[0])
            if not path_part:
                continue
            candidate = (
                root / path_part.lstrip("/")
                if path_part.startswith("/")
                else document.parent / path_part
            )
            if not candidate.resolve().exists():
                errors.append(
                    f"broken local link in {relative(document, root)}: {target}"
                )


def check_text_safety(errors: list[str], root: Path = ROOT) -> None:
    for path in text_files(root):
        try:
            content = path.read_text(encoding="utf-8-sig")
        except UnicodeDecodeError:
            continue

        rel = relative(path, root)
        if not rel.startswith(("scripts/", "tests/")):
            lowered = content.lower()
            for stale in OBSOLETE_RELEASE_TEXT:
                if stale.lower() in lowered:
                    errors.append(f"obsolete release statement in {rel}: {stale}")

        for name, pattern in SECRET_PATTERNS.items():
            if pattern.search(content):
                errors.append(f"possible {name} in {rel}")


def check_public_tone(errors: list[str], root: Path = ROOT) -> None:
    tracked = {path.as_posix() for path in tracked_relative_paths(root)}
    for name in sorted(PUBLIC_PRESENTATION_FILES):
        if name not in tracked:
            continue
        content = (root / name).read_text(encoding="utf-8-sig").lower()
        for phrase in sorted(INTERNAL_AUTHORING_PHRASES):
            if phrase in content:
                errors.append(
                    f"internal authoring language remains in {name}: {phrase}"
                )


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
        if marker in {
            0xC0, 0xC1, 0xC2, 0xC3, 0xC5, 0xC6, 0xC7,
            0xC9, 0xCA, 0xCB, 0xCD, 0xCE, 0xCF,
        }:
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


def check_dimensions(
    path: Path,
    gallery: str,
    errors: list[str],
    root: Path = ROOT,
) -> None:
    try:
        width, height = image_size(path)
    except ValueError as exc:
        errors.append(f"invalid image in {relative(path, root)}: {exc}")
        return

    if width < 600 or height < 650:
        errors.append(
            f"image is too small for review: {relative(path, root)} is {width}x{height}"
        )

    mobile_layout = gallery == "mobile" or (
        gallery == "localization"
        and path.name == "03-arabic-portal-mobile.png"
    )
    if mobile_layout:
        if height <= width or width < 650 or height < 1200:
            errors.append(
                "mobile image must be a readable portrait capture: "
                f"{relative(path, root)} is {width}x{height}"
            )
    elif gallery in {"desktop", "portal", "localization"}:
        if width <= height or width < 1400:
            errors.append(
                "desktop image must be a readable landscape capture: "
                f"{relative(path, root)} is {width}x{height}"
            )


def check_manifest_contract(
    errors: list[str],
    manifest: dict,
) -> None:
    expected_top = {
        "schema_version",
        "target_release",
        "latest_immutable_release",
        "state",
        "evidence_date",
        "source",
        "validation",
        "gallery",
        "artifacts",
        "boundaries",
    }
    missing = expected_top - set(manifest)
    for key in sorted(missing):
        errors.append(f"evidence manifest is missing top-level field: {key}")

    if manifest.get("schema_version") != 1:
        errors.append("evidence manifest schema_version must be 1")
    if manifest.get("target_release") != "v1.0.2-showcase":
        errors.append("evidence manifest target_release must be v1.0.2-showcase")
    if manifest.get("state") != "tag-bound-release-record":
        errors.append("evidence manifest state must be tag-bound-release-record")

    latest = manifest.get("latest_immutable_release", {})
    if latest.get("tag") != "v1.0.1-showcase":
        errors.append("latest immutable showcase tag must be v1.0.1-showcase")
    if latest.get("commit") != "53aa79d5124902fc689c4f7b121c7d4b1fdccdc9":
        errors.append("v1.0.1-showcase commit record is incorrect")

    source = manifest.get("source", {})
    frontend = source.get("frontend", {})
    backend = source.get("backend", {})
    if frontend.get("commit") != "b73a623c3985e4bc458d04b4b484887ada593fa5":
        errors.append("canonical frontend revision is incorrect")
    if backend.get("commit") != "2234af20d1d9dd143bcac22edc699d3ee7fe515f":
        errors.append("canonical backend revision is incorrect")
    if backend.get("alembic_head") != "9e4f6a8c2d1b":
        errors.append("canonical Alembic head is incorrect")

    validation = manifest.get("validation", {})
    if validation.get("mode") != "local":
        errors.append("showcase validation mode must be local")
    if validation.get("hosted_ci_claim") is not False:
        errors.append("evidence manifest must not claim hosted CI")

    gallery = manifest.get("gallery", {})
    inventory = expected_screenshots(manifest)
    if set(inventory) != APPROVED_SCREENSHOT_DIRS:
        errors.append("evidence manifest gallery names do not match the approved set")
    total = sum(len(names) for names in inventory.values())
    if gallery.get("total") != 53 or total != 53:
        errors.append(
            f"evidence manifest screenshot total must be 53, found {gallery.get('total')} / {total}"
        )
    counts = gallery.get("counts", {})
    for gallery_name, names in inventory.items():
        if counts.get(gallery_name) != len(names):
            errors.append(
                f"evidence manifest count mismatch for {gallery_name}: "
                f"expected {len(names)}, found {counts.get(gallery_name)}"
            )


def check_screenshot_inventory(
    errors: list[str],
    manifest: dict,
    root: Path = ROOT,
) -> None:
    screenshot_root = root / "screenshots"
    expected = expected_screenshots(manifest)
    actual: dict[str, set[str]] = {
        name: set() for name in APPROVED_SCREENSHOT_DIRS
    }
    hashes: dict[str, list[str]] = defaultdict(list)
    blocked = manifest.get("gallery", {}).get("blocked_sha256", {})

    for path in screenshot_files(root):
        rel = path.relative_to(screenshot_root)
        if len(rel.parts) != 2:
            errors.append(
                "screenshot must be one level below an approved gallery: "
                f"{relative(path, root)}"
            )
            continue
        gallery = rel.parts[0]
        if gallery not in APPROVED_SCREENSHOT_DIRS:
            errors.append(f"unapproved screenshot gallery: {relative(path, root)}")
            continue
        if path.suffix.lower() not in APPROVED_IMAGE_SUFFIXES:
            errors.append(f"unsupported screenshot type: {relative(path, root)}")
            continue

        actual[gallery].add(path.name)
        digest = hashlib.sha256(path.read_bytes()).hexdigest()
        hashes[digest].append(relative(path, root))
        reason = blocked.get(digest)
        if reason:
            errors.append(
                f"rejected screenshot remains: {relative(path, root)} — {reason}"
            )
        check_dimensions(path, gallery, errors, root)

    for gallery, expected_names in expected.items():
        for name in sorted(expected_names - actual[gallery]):
            errors.append(f"missing screenshot: screenshots/{gallery}/{name}")
        for name in sorted(actual[gallery] - expected_names):
            errors.append(f"unexpected screenshot: screenshots/{gallery}/{name}")

    total = sum(len(names) for names in actual.values())
    if total != 53:
        errors.append(f"screenshot inventory mismatch: expected 53, found {total}")

    for digest, paths in sorted(hashes.items()):
        if len(paths) > 1:
            errors.append(
                "duplicate screenshot content: "
                + ", ".join(paths)
                + f" (sha256 {digest[:12]}…)"
            )
    if len(hashes) != 53:
        errors.append(
            f"screenshot uniqueness mismatch: expected 53 unique hashes, found {len(hashes)}"
        )


def check_approved_media(
    errors: list[str],
    manifest: dict,
    root: Path = ROOT,
) -> None:
    approved = manifest.get("gallery", {}).get("approved_exact_sha256", {})
    for relative_path, expected_hash in sorted(approved.items()):
        path = root / relative_path
        if not path.is_file():
            errors.append(f"missing approved release asset: {relative_path}")
            continue
        actual_hash = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual_hash != expected_hash:
            errors.append(
                f"approved release asset changed: {relative_path} — "
                f"expected {expected_hash[:12]}…, found {actual_hash[:12]}…"
            )


def check_video_inventory(errors: list[str], root: Path = ROOT) -> None:
    allowed = {"video/README.md"}
    for path in tracked_relative_paths(root):
        if path.parts and path.parts[0] == "video" and path.as_posix() not in allowed:
            errors.append(f"undeclared video asset remains: {path.as_posix()}")


def normalize_document_text(content: str) -> str:
    return " ".join(content.lower().split())


def require_phrases(
    errors: list[str],
    path: str,
    phrases: set[str],
    label: str,
    root: Path = ROOT,
) -> None:
    document = root / path
    if not document.is_file():
        errors.append(f"{label} is missing required file: {path}")
        return
    content = normalize_document_text(
        document.read_text(encoding="utf-8-sig")
    )
    for phrase in sorted(phrases):
        normalized_phrase = normalize_document_text(phrase)
        if normalized_phrase not in content:
            errors.append(f"{label} is missing required public content: {phrase}")


def check_document_contracts(
    errors: list[str],
    manifest: dict,
    root: Path = ROOT,
) -> None:
    frontend = manifest["source"]["frontend"]["commit"]
    backend = manifest["source"]["backend"]["commit"]
    target = manifest["target_release"]
    latest = manifest["latest_immutable_release"]["tag"]

    require_phrases(
        errors,
        "README.md",
        {
            "multi-tenant",
            "client portal",
            "deterministic professional demo",
            "local release validation",
            target,
            latest,
            frontend,
            backend,
            "Project ownership",
        },
        "README",
        root,
    )
    require_phrases(
        errors,
        "BUILD_MANIFEST.md",
        {
            target,
            latest,
            frontend,
            backend,
            "tag-bound release record",
            "local validation",
            "53 unique screenshots",
            "No green hosted-CI claim",
        },
        "Build manifest",
        root,
    )
    require_phrases(
        errors,
        "RELEASES.md",
        {
            target,
            latest,
            frontend,
            backend,
            "Local validation policy",
            "Correction policy",
        },
        "Release policy",
        root,
    )
    require_phrases(
        errors,
        "CHANGELOG.md",
        {
            f"{target} — evidence date 2026-07-17",
            latest,
            frontend,
            backend,
        },
        "Changelog",
        root,
    )
    require_phrases(
        errors,
        "screenshots/README.md",
        {
            "# GymFlow Visual Gallery",
            "53 stable screenshot paths",
            "53 unique image hashes",
            target,
            frontend,
            backend,
            "Evidence index",
        },
        "Screenshot gallery",
        root,
    )
    require_phrases(
        errors,
        "video/README.md",
        {
            "# GymFlow Walkthrough Status",
            target,
            "not included",
            "historical media",
            "provenance-bound release",
        },
        "Walkthrough status",
        root,
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
        root,
    )
    require_phrases(
        errors,
        "SECURITY.md",
        {
            "Report a vulnerability",
            "Advisories",
            "Do not post exploit details",
        },
        "Security policy",
        root,
    )
    require_phrases(
        errors,
        "ROADMAP.md",
        {
            target,
            latest,
            "Product evolution",
            "Production infrastructure",
            "Production claim boundary",
        },
        "Roadmap",
        root,
    )


def check_local_validation_contract(
    errors: list[str],
    root: Path = ROOT,
) -> None:
    tracked = {path.as_posix() for path in tracked_relative_paths(root)}
    if ".github/workflows/showcase-quality.yml" in tracked:
        errors.append(
            "obsolete hosted Actions workflow remains; this release line uses local validation"
        )

    powershell_path = root / "scripts/validate_release.ps1"
    shell_path = root / "scripts/validate_release.sh"
    gitignore_path = root / ".gitignore"
    if not powershell_path.is_file() or not shell_path.is_file() or not gitignore_path.is_file():
        return

    powershell = powershell_path.read_text(encoding="utf-8-sig")
    shell = shell_path.read_text(encoding="utf-8-sig")
    required_commands = {
        "python -m unittest discover",
        "python scripts/check_showcase.py",
        "python scripts/check_release_candidate.py",
    }
    for command in sorted(required_commands):
        if command not in powershell:
            errors.append(f"PowerShell validator is missing command: {command}")
        if command not in shell:
            errors.append(f"shell validator is missing command: {command}")

    gitignore = gitignore_path.read_text(encoding="utf-8-sig")
    for value in {"__pycache__/", "*.py[cod]", ".pytest_cache/"}:
        if value not in gitignore:
            errors.append(f".gitignore is missing Python hygiene rule: {value}")


def run_base_checks(root: Path = ROOT) -> tuple[list[str], dict | None]:
    errors: list[str] = []
    try:
        manifest = load_manifest(root)
    except ValueError as exc:
        errors.append(str(exc))
        manifest = None

    check_required_files(errors, root)
    check_tracked_file_safety(errors, root)
    check_markdown_links(errors, root)
    check_text_safety(errors, root)
    check_public_tone(errors, root)
    check_video_inventory(errors, root)
    check_local_validation_contract(errors, root)

    if manifest is not None:
        check_manifest_contract(errors, manifest)
        check_screenshot_inventory(errors, manifest, root)
        check_approved_media(errors, manifest, root)
        check_document_contracts(errors, manifest, root)

    return errors, manifest
