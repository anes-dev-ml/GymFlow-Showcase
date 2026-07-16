# GymFlow Build Manifest

This manifest ties the public GymFlow engineering case study to exact source
revisions and an explicit release-asset inventory.

## Release identity

| Field | Value |
|---|---|
| Release tag | `v1.0.0-showcase` |
| Evidence date | 2026-07-15 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual/test/demo state; no real charges |
| Public source boundary | Showcase content only; application source remains private |

The release tag is authoritative for the showcase commit. Its own commit SHA is
not duplicated inside the commit it identifies.

## Canonical source snapshot

| Component | Repository/ref | Revision | Release evidence |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `489a82e03059465755c74b1be39ae7c05f98fb9b` | Final frontend release audit merged into `main` |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | Final backend release audit merged into `main` |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Release tag target | Engineering case study, screenshot gallery, provenance, and release contract |

The merged application audit work was based directly on frontend
`a0ab421b45c447dd710ce8c53cf97edcb7c85e1a` and backend
`9d131982a161d22a56efeda8ef47805ee7e9dca6`.

## Application and schema versions

| Component | Version / constraint |
|---|---|
| Frontend application | `1.0.0+1` |
| Backend API | `1.0.0` |
| Flutter | Stable channel used for release validation |
| Dart SDK | `^3.9.0` |
| Python | 3.10 application runtime; Python 3.12 showcase validation |
| FastAPI | 0.136.3 |
| Pydantic | 2.13.4 |
| SQLAlchemy | 2.0.50 |
| Alembic | 1.18.4 |
| Alembic head | `9e4f6a8c2d1b` |
| PostgreSQL | 16 |
| Redis | 7 Alpine |
| Stripe Python SDK | 14.4.1 |
| `go_router` | 17.2.3 |
| Flutter `http` | 1.6.0 |
| WebSocket channel | 3.0.3 |

## Canonical environment

| Field | Value |
|---|---|
| Development database | `gymflow` |
| Demo database | `gymflow_demo` |
| Demo runtime | `ENVIRONMENT=demo` through the guarded selector |
| Demo identities | Reserved `.test` addresses |
| Demo payments | Fictional manual/test records; no live external IDs |
| Demo email | Disabled or guarded demo-assisted behavior |

## Expected deterministic validation

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

## Provider status

| Provider | Repository evidence | External evidence required for deployment |
|---|---|---|
| Stripe | Checkout, billing, Connect-aware demo boundary, webhook validation, idempotency | Target account keys, price IDs, webhook rehearsal, KYC/Connect decision |
| Email | Verification, recovery, invitation, portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android token path, Windows PKCE/loopback path | Real client IDs, redirects, package fingerprints, end-to-end verification |

## Public artifact inventory

| Artifact | Status in this release | Integrity statement |
|---|---|---|
| Engineering case study | Included | Versioned in this repository |
| Architecture and threat-model documentation | Included | Versioned in this repository |
| Current application screenshots | Included | 53 tracked screenshots across desktop, portal, mobile, localization, and engineering galleries |
| Product walkthrough video | Not included | No public URL, binary, duration, thumbnail, or checksum is claimed |
| Android or Windows binary | Not included | No installable artifact or checksum is claimed |
| Social preview | Repository-setting task | Configure from an approved current-release design before public promotion |

The screenshot inventory is defined in `screenshots/README.md` and enforced by
`scripts/check_showcase.py`. The release includes no public video binary.

## Verification evidence

| Gate | Command or evidence | Release rule |
|---|---|---|
| Frontend | Equivalent release validation completed locally | Completed before frontend audit merge |
| Backend | Equivalent release validation completed locally | Completed before backend audit merge |
| Showcase | `python scripts/check_showcase.py` completed locally | Required before tagging |
| Hosted Actions | Jobs were blocked before checkout by the account spending policy | No green hosted-CI claim is made for this release |
| Screenshot inventory | 53 tracked images across 5 approved galleries | Must match validator counts exactly |
| Demo rebuild | Guarded rebuild and `validate_demo_data.py` | Required again before replacing release screenshots or recording video |
| Route rehearsal | `DEMO.md` walkthrough | Required again before replacing release screenshots or recording video |
| Release tag | `v1.0.0-showcase` | Create after final `main` validation succeeds |

The account-level GitHub Actions restriction prevented hosted jobs from starting.
The workflows remain defined, but this release relies on documented equivalent
local validation rather than claiming successful hosted CI runs.

## Release completion checklist

- [x] Record the exact audited frontend revision.
- [x] Record the exact audited backend revision.
- [x] Record the Alembic head and evidence date.
- [x] State provider and production boundaries accurately.
- [x] Record and validate the 53-screenshot release inventory.
- [x] State that no public video or installable binary is included.
- [x] Complete frontend, backend, and showcase validation locally.
- [x] Merge the frontend and backend audit pull requests.
- [x] Publish the finalized showcase snapshot to `main`.
- [x] Close the superseded showcase audit pull request without merging its obsolete history.
- [ ] Create `v1.0.0-showcase` on the final validated showcase commit.
- [ ] Configure the GitHub social preview from an approved release design.

## Integrity note

A filename containing “final” is not release evidence. Exact source revisions,
the release tag, validation record, declared screenshot inventory, and checksums
for any future downloadable files are authoritative.
