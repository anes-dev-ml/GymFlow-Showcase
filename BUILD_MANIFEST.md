# GymFlow Build Manifest

This manifest ties public showcase assets to a known application source state.

It should be updated only when the canonical frontend/backend release snapshot or published artifact set changes.

## Canonical application snapshot

| Component | Repository/ref | Revision | Notes |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `client-dashboard-redesign` | `85fb121968bf862945debf349ce8c28df72c0fdd` | Demo-readiness merge preserving current dashboard, staff presence, messaging, and portal architecture |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `7bef6bfdf7ba1fbd3db9669b59aafa6ce6f2b9ac` | Guarded demo portal-code flow after Docker selector and reserved `.test` identity fixes |
| Showcase baseline | `anes-dev-ml/GymFlow-Showcase` / `main` | `60f9fd3f7f4b4765668640022ad8d71a56fe47d4` | Previous visual/documentation release before case-study overhaul |
| Showcase case study | `anes-dev-ml/GymFlow-Showcase` / `main` | `dfc107ce4042d6f3fd99dc991557d57dd5b0132c` | Merged engineering case study, security/operations documentation, provenance system, and showcase CI |

## Application versions

| Component | Version / constraint |
|---|---|
| Flutter | Stable channel used by frontend CI |
| Dart SDK | `^3.9.0` |
| Python | 3.10 runtime/CI target |
| FastAPI | 0.136.3 |
| Pydantic | 2.13.4 |
| SQLAlchemy | 2.0.50 |
| Alembic | 1.18.4 |
| PostgreSQL | 16 in local/CI stack |
| Redis | 7 Alpine in CI/local-compatible stack |
| Stripe Python SDK | 14.4.1 |
| `go_router` | 17.2.3 |
| Flutter `http` | 1.6.0 |
| WebSocket channel | 3.0.3 |

## Canonical environment

| Field | Value |
|---|---|
| Workspace | Northline Performance Club |
| Development database | `gymflow` |
| Demo database | `gymflow_demo` |
| Demo runtime | `ENVIRONMENT=demo` derived by local Docker selector |
| Demo identities | Reserved `.test` addresses |
| Demo payments | Fictional manual/test records; no live external IDs |
| Demo email | Disabled or demo-assisted for reserved identities |

## Expected demo validation targets

| Metric | Expected |
|---|---:|
| Clients | 24 |
| Active clients | 20 |
| Archived clients | 4 |
| Staff | 7 |
| Active memberships | 18 |
| Active plans | 4 |
| Active services | 6 |
| Bookings | 72 |
| Today's bookings | 5 |
| Recent check-ins | 58 |
| Today's check-ins | 4 |
| Current-month revenue | 340,200 cents |
| Pending payments | 37,700 cents |
| Owner unread notifications | 6 |
| Portal client stories | 2 |

## Source verification

Before final capture:

```text
Backend quality runner: required
Frontend CI/quality runners: required
Demo rebuild: required
Demo validator: required
Full route rehearsal: required
Showcase quality workflow: required
```

## Visual artifacts

The final visual artifacts are intentionally pending capture after this documentation freeze.

| Artifact | Required path/name | Status |
|---|---|---|
| Main video thumbnail | `video/gymflow-showcase-thumbnail.png` | Capture pending |
| Main product walkthrough | External video URL or `video/` release asset reference | Capture pending |
| Engineering walkthrough | Optional external video URL | Capture pending |
| Refreshed screenshots | Paths defined in `screenshots/README.md` | Capture pending |
| Social preview | Repository setting; source file may live in `video/` | Capture pending |

## Installable artifacts

| Artifact | Status | Required metadata before publication |
|---|---|---|
| Android APK | Optional, not yet attached | Frontend commit, API expectation, OAuth status, SHA-256 |
| Windows build archive | Optional, not yet attached | Frontend commit, API expectation, redirect status, SHA-256 |
| Screenshot pack | Optional after capture | Showcase commit, SHA-256 |
| Architecture pack | Optional after final diagrams | Showcase commit, SHA-256 |
| SBOM | Planned for binary release | Generator, format, source revisions |

## Provider status for this snapshot

| Provider | Status |
|---|---|
| Stripe | Architecture and test/demo flows implemented; real target provider verification is release-specific |
| Email | Provider integration implemented; demo `.test` identities use guarded assisted code behavior |
| Google OAuth | Web/native foundations implemented; production client/redirect verification is release-specific |

## Provenance completion checklist

After screenshots and video are finalized:

- [x] Replace the showcase case-study branch entry with the merged showcase commit.
- [ ] Confirm frontend branch has not moved; otherwise record the new exact commit and rerun QA.
- [ ] Confirm backend `main` has not moved; otherwise record the new exact commit and rerun QA.
- [ ] Record Alembic head revision from the final demo database.
- [ ] Record Flutter and Dart versions from `flutter --version`.
- [ ] Record build/capture date.
- [ ] Add video URL and duration.
- [ ] Add final screenshot list.
- [ ] Add SHA-256 checksums for downloadable binaries/archives.
- [ ] Add CI run links or release verification summary.
- [ ] Create the release tag.

## Integrity note

This repository does not claim that a screenshot or binary represents the current source merely because it is named “final.” The manifest, tag, checksums, and source revisions are the authoritative release evidence.
