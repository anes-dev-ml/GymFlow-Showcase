# Changelog

All notable changes to the GymFlow showcase are documented here. The application
source repositories maintain their own histories; this changelog tracks the case
study, diagrams, screenshots, manifests, validation contracts, and release
artifacts.

## Unreleased — `v1.0.1-showcase` candidate

### Changed

- Updated the evidence date to 2026-07-16 and separated the historical
  `v1.0.0-showcase` tag from the current release candidate.
- Defined distinct replacement evidence for the duplicate client, messaging, and
  payment engineering images.
- Prepared curated replacements for raw IDE, Docker, and source-history captures.
- Added a safe static-QR requirement that rejects the previously published
  token-bearing check-in image.
- Strengthened the screenshot validator to enforce exact filenames, unique image
  hashes, valid dimensions, rejected-media hashes, and release-candidate values.
- Clarified that deterministic validator output is authoritative for exact counts;
  screenshots provide representative fictional product evidence.
- Added a concrete GitHub private-vulnerability-reporting path to the security policy.

### Remaining release gate

The prepared replacement package covers the rejected desktop, engineering,
portal-QR, and portal-messaging evidence. Three fresh application captures remain
before the candidate can be tagged:

- `screenshots/mobile/04-check-in-pass.png` — show the complete mobile pass with a
  deliberately invalid static QR, no raw token, no clipped action, and no
  navigation overlap;
- `screenshots/mobile/06-dashboard.png` — show one non-duplicated metric summary
  followed by a different useful dashboard section;
- `screenshots/portal/02-bookings.png` — show at least one upcoming booking and
  at least one available fictional service.

The final tag remains blocked until all prepared and manually recaptured images
are committed and the complete validator passes on the same commit.

## 1.0.0-showcase — 2026-07-15

### Added

- Product case study covering users, product surfaces, and connected workflows.
- Architecture case study with system context, trust boundaries, domain model,
  deployment, and sequence diagrams.
- Engineering document covering frontend, backend, database, security,
  reliability, messaging, presence, testing, and environment decisions.
- Root vulnerability disclosure policy, security overview, and threat model.
- Quality strategy with risk-to-evidence mapping.
- Operations runbook for Docker, deployment, migrations, observability,
  incidents, backups, and scaling.
- Engineering journey, product roadmap, build manifest, and release policy.
- Showcase validation workflow and protected-content license.
- A structured 53-file gallery covering desktop, portal, mobile, localization,
  and engineering evidence.

### Changed

- Rebuilt the README as a visual engineering landing page.
- Replaced stale demo credentials with password-at-rebuild guidance.
- Updated the demo scenario to Northline Performance Club.
- Recorded exact source revisions, validation scope, provider status, and
  artifact boundaries.
- Reframed production claims as production-oriented architecture plus
  deployment-specific operational verification.
- Added professional messaging, staff presence, portal settings, real-time
  behavior, and guarded demo infrastructure to the public system description.
- Recorded the hosted-runner restriction without claiming green CI that did not execute.
- Replaced the obsolete 19-image gallery with the structured 53-file gallery.

### Removed

- Stale status tables and old demo account values.
- Repetitive feature inventories that did not explain decisions or evidence.
- Unsupported live-provider and production-operation claims.
- Editor-specific configuration and internal capture instructions.
- The obsolete empty video placeholder.

## 0.1.0 — 2026-07-05

### Added

- Initial public showcase structure.
- Product, architecture, security, demo, and release documentation.
- Nineteen screenshots representing the earlier product generation.

### Known limitation

This release predated the dashboard redesign, professional messaging, hardened
staff presence, guarded deterministic demo environment, and current portal architecture.