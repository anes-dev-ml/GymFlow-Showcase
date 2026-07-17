# Changelog

All notable changes to the GymFlow showcase are documented here. The application
source repositories maintain their own histories; this changelog tracks the case
study, diagrams, screenshots, manifests, validation contracts, and release
artifacts.

## Unreleased — `v1.0.1-showcase` candidate

### Changed

- Updated the canonical frontend provenance to
  `b73a623c3985e4bc458d04b4b484887ada593fa5`, which includes the final mobile
  dashboard, professional messaging, zoom-responsive, payment-copy, attendance,
  portal-architecture, and regression-suite hardening.
- Reconciled obsolete source-string tests with the final frontend architecture,
  replacing superseded portal guards with consolidated current contracts rather
  than retaining assumptions about removed classes and implementation files.
- Updated the evidence date to 2026-07-16 and separated the historical
  `v1.0.0-showcase` tag from the current release candidate.
- Replaced the rejected mobile dashboard with the compact four-metric layout and
  workspace-readiness evidence.
- Replaced the empty desktop portal-bookings capture with populated upcoming
  sessions and schedule evidence.
- Defined distinct replacement evidence for duplicate client, messaging, and
  payment engineering images.
- Replaced raw IDE, Docker, and source-history captures with curated engineering
  summaries that are explicitly distinguished from raw command output.
- Added a safe static-QR requirement that rejects the previously published
  token-bearing check-in image.
- Strengthened the screenshot validator to enforce exact filenames, unique image
  hashes, valid dimensions, rejected-media hashes, and release-candidate values.
- Clarified that deterministic validator output is authoritative for exact counts;
  screenshots provide representative fictional product evidence.
- Added a concrete GitHub private-vulnerability-reporting path to the security policy.
- Clarified that an older standalone walkthrough release is historical media and
  is not evidence for the current provenance-bound candidate.

### Remaining release gates

The candidate must not be tagged until the following evidence is aligned with the
canonical frontend revision:

- `screenshots/desktop/07-professional-messaging.png` — recapture the final
  dedicated communication workspace rather than the previous metric-heavy page;
- `screenshots/engineering/15-frontend-commit-history.png` — regenerate the
  curated provenance image with frontend revision
  `b73a623c3985e4bc458d04b4b484887ada593fa5`;
- `screenshots/mobile/04-check-in-pass.png` — commit the reviewed full-height pass
  containing only a deliberately invalid static demo QR payload and no raw token;
- `screenshots/mobile/02-portal-bookings.png` — commit the refreshed populated
  mobile bookings capture;
- run the full frontend release-quality commands on the canonical frontend SHA;
- run `python scripts/check_showcase.py` on the exact final showcase commit;
- complete a final privacy and visual review, then create `v1.0.1-showcase` on
  that exact commit.

The existing `v1.0.0-showcase` tag remains historical and must not be moved.

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

- Initial public portfolio showcase structure.
