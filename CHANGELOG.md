# Changelog

All notable changes to the GymFlow showcase are documented here. The private application repositories maintain their own histories; this file tracks the public case study, gallery, manifests, validation contracts, and release artifacts.

## Unreleased — public narrative refresh

### Changed

- Refined the README around the product, connected workflows, architecture, and engineering story before release mechanics.
- Reframed the visual gallery as a product tour while preserving its complete release-integrity record.
- Reworked roadmap language around product evolution and the path from showcase to commercial operation.
- Simplified private-source and source-review wording without changing access or licensing boundaries.
- Reduced defensive “proof / no claim / evidence boundary” phrasing across public-facing documentation.
- Kept technical provenance, hashes, validation, security, and release mechanics in the dedicated documents where they remain useful.

## v1.0.3-showcase — 2026-07-17

### Added

- Schema version 2 for `release/evidence-manifest.json`, with explicit current and previous release identities.
- Exact SHA-256 approval for all 53 screenshots.
- `scripts/refresh_evidence_hashes.py` for deterministic evidence-hash maintenance.
- Neutral `scripts/check_release.py` validation for record and release modes.
- Regression coverage for malformed manifests, complete hash coverage, historical wording, tag alignment, and the complete repository gate.
- Final public-release notes for `v1.0.3-showcase`.

### Changed

- Preserved frontend revision `b73a623c3985e4bc458d04b4b484887ada593fa5`.
- Preserved backend revision `2234af20d1d9dd143bcac22edc699d3ee7fe515f`.
- Recorded `v1.0.2-showcase` at `4e6f10276a5d17a51f7ddad12d9f909fd6f0fd7f` as the previous immutable release.
- Replaced dynamic “latest immutable release” wording with stable current and previous release semantics.
- Strengthened local-link containment and nested manifest validation.
- Updated active release documentation and tooling to `v1.0.3-showcase`.

### Removed

- Obsolete `scripts/check_release_candidate.py` naming and candidate-oriented output.
- Pre-tag instructions that remained visible after `v1.0.2-showcase` existed.
- The rule that incorrectly required `v1.0.1-showcase` to remain the latest immutable release.

## `v1.0.2-showcase` — 2026-07-17

### Added

- Machine-readable release evidence at `release/evidence-manifest.json`.
- Traditional PowerShell and POSIX release runners.
- Initial validator regression tests.
- Evidence descriptions for all 53 gallery images.

### Changed

- Reorganized the README around product evidence, engineering decisions, release status, and review boundaries.
- Changed file-safety validation to inspect tracked Git content.
- Replaced unavailable hosted execution with a documented local validation policy.

### Release record

- Showcase commit: `4e6f10276a5d17a51f7ddad12d9f909fd6f0fd7f`
- Frontend commit: `b73a623c3985e4bc458d04b4b484887ada593fa5`
- Backend commit: `2234af20d1d9dd143bcac22edc699d3ee7fe515f`
- Gallery: 53 unique screenshots across five galleries

## `v1.0.1-showcase` — 2026-07-16

### Added

- Provenance-bound release validation.
- Exact canonical frontend and backend revision checks.
- Approved hashes for high-risk evidence and permanently blocked rejected media.
- Historical-media and no-video boundaries.

### Release record

- Showcase commit: `53aa79d5124902fc689c4f7b121c7d4b1fdccdc9`
- Frontend commit: `b73a623c3985e4bc458d04b4b484887ada593fa5`
- Backend commit: `2234af20d1d9dd143bcac22edc699d3ee7fe515f`
- Gallery: 53 unique screenshots across five galleries

## `v1.0.0-showcase` — 2026-07-15

### Added

- Product, architecture, engineering, quality, operations, security, and threat-model case studies.
- Guarded Northline Performance Club deterministic demo contract.
- Release policy, build manifest, roadmap, changelog, security policy, protected-content license, and structured gallery.

## `0.1.0` — 2026-07-05

### Added

- Initial public portfolio showcase structure.
