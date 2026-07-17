# Changelog

All notable changes to the GymFlow showcase are documented here. The private application repositories maintain their own histories; this changelog tracks the public case study, diagrams, screenshots, manifests, validation contracts, and release artifacts.

## [Unreleased] — v1.0.2-showcase

### Added

- Machine-readable release and evidence record at `release/evidence-manifest.json`.
- Traditional local release runners for PowerShell and POSIX shells.
- Validator regression tests covering tracked-file discovery, stale release wording, manifest drift, historical-tag integrity, target-tag alignment, and clean-worktree enforcement.
- Explicit evidence descriptions for all 53 gallery images.
- Professional release notes for `v1.0.2-showcase`.

### Changed

- Kept the canonical frontend revision at `b73a623c3985e4bc458d04b4b484887ada593fa5`.
- Kept the canonical backend revision at `2234af20d1d9dd143bcac22edc699d3ee7fe515f`.
- Reframed `v1.0.1-showcase` as the latest immutable historical release rather than an unfinished candidate.
- Reorganized the README around product evidence, engineering decisions, release status, and review boundaries.
- Centralized release constants so the validators no longer duplicate source, gallery, and artifact facts.
- Changed file safety validation to inspect tracked Git content instead of unrelated local cache files.
- Strengthened cross-document release-state and provenance checks.
- Replaced hosted Actions as release evidence with a documented local validation policy.
- Reduced duplicated documentation and clarified recruiter-facing evidence.

### Fixed

- Removed obsolete references to a superseded intermediate frontend revision.
- Removed statements claiming that `v1.0.1-showcase` had not yet been tagged.
- Removed completed screenshot replacements from “remaining gates.”
- Prevented validator self-detection of its own blocked strings.
- Prevented generated `__pycache__` directories from causing false release failures when they are untracked.
- Added Python cache rules to `.gitignore`.
- Removed the broken hosted workflow whose compile step created files forbidden by the following validation step.

## `v1.0.1-showcase` — 2026-07-16

### Added

- Provenance-bound final-candidate validator.
- Exact canonical frontend and backend revision checks.
- Approved hashes for high-risk QR, mobile dashboard, portal booking, and frontend-history evidence.
- Rejected hashes for stale, empty, cropped, duplicated, and credential-bearing media.
- Historical-media and no-video release boundaries.

### Changed

- Updated the canonical frontend provenance to `b73a623c3985e4bc458d04b4b484887ada593fa5`.
- Aligned the 53-image gallery with the final application snapshot.
- Replaced stale professional-messaging, mobile dashboard, portal-bookings, QR-pass, and frontend-history evidence.
- Clarified that deterministic validation is authoritative for exact seeded counts.
- Recorded the hosted-runner restriction without claiming successful hosted CI.

### Release record

- Showcase commit: `53aa79d5124902fc689c4f7b121c7d4b1fdccdc9`
- Frontend commit: `b73a623c3985e4bc458d04b4b484887ada593fa5`
- Backend commit: `2234af20d1d9dd143bcac22edc699d3ee7fe515f`
- Gallery: 53 unique screenshots across five galleries

## `v1.0.0-showcase` — 2026-07-15

### Added

- Product case study covering users, product surfaces, and connected workflows.
- Architecture case study with system context, trust boundaries, domain model, deployment, and sequence diagrams.
- Engineering, quality, operations, security-overview, and threat-model documentation.
- Guarded Northline Performance Club deterministic demo contract.
- Release policy, build manifest, roadmap, changelog, security policy, and protected-content license.
- Structured 53-file gallery covering desktop, portal, mobile, localization, and engineering evidence.

### Changed

- Rebuilt the README as a visual engineering landing page.
- Replaced stale demo credentials with password-at-rebuild guidance.
- Reframed production claims as production-oriented architecture plus deployment-specific operational verification.
- Added professional messaging, staff presence, portal settings, real-time behavior, and guarded demo infrastructure to the public system description.

### Removed

- Stale status tables and old demo account values.
- Repetitive feature inventories that did not explain decisions or evidence.
- Unsupported live-provider and production-operation claims.
- Editor-specific configuration and internal capture instructions.
- The obsolete 19-image gallery.

## `0.1.0` — 2026-07-05

### Added

- Initial public portfolio showcase structure.
