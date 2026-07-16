# GymFlow Build Manifest

This manifest ties the public engineering case study to an exact, reviewable
application source state. It records what is included and, just as importantly,
what is not included.

## Release identity

| Field | Value |
|---|---|
| Release candidate | `v1.0.0-showcase` |
| Evidence date | 2026-07-15 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual/test/demo state; no real charges |
| Public source boundary | Showcase content only; application source remains private |

The final showcase tag target is authoritative for the showcase commit. Its SHA
is intentionally not duplicated inside the commit it identifies, which would
create a self-referential manifest.

## Canonical source snapshot

| Component | Repository/ref | Revision | Release evidence |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `489a82e03059465755c74b1be39ae7c05f98fb9b` | Runtime release at 1.0.0 plus final documentation, licensing, localization-tool retirement, and regression-contract audit |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | API release at 1.0.0 plus final documentation, licensing, dependency separation, container-build CI, and regression-contract audit |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Release tag target | This manifest, engineering case study, media inventory, and showcase quality contract |

The application audit branches are release candidates based directly on
frontend `a0ab421b45c447dd710ce8c53cf97edcb7c85e1a` and backend
`9d131982a161d22a56efeda8ef47805ee7e9dca6`.

## Application and schema versions

| Component | Version / constraint |
|---|---|
| Frontend application | `1.0.0+1` |
| Backend API | `1.0.0` |
| Flutter | Stable channel in CI |
| Dart SDK | `^3.9.0` |
| Python | 3.10 runtime and CI |
| FastAPI | 0.136.3 |
| Pydantic | 2.13.4 |
| SQLAlchemy | 2.0.50 |
| Alembic | 1.18.4 |
| Alembic head | `9e4f6a8c2d1b` |
| PostgreSQL | 16 in local and CI stacks |
| Redis | 7 Alpine in local and CI stacks |
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
| Stripe | Checkout, billing, Connect-aware demo boundary, webhook validation and idempotency | Target account keys, price IDs, webhook rehearsal, KYC/Connect decision |
| Email | Verification, recovery, invitation, and portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android identity-token path, Windows PKCE/loopback path | Real client IDs, redirects, package fingerprints, and end-to-end verification |

## Public artifact inventory

| Artifact | Status in this release candidate | Integrity statement |
|---|---|---|
| Engineering case study | Included | Versioned in this repository |
| Architecture and threat-model documentation | Included | Versioned in this repository |
| Current application screenshots | Not included | The previous 19-image set was removed because it predates the canonical snapshot |
| Product walkthrough video | Not included | No public URL, binary, duration, or checksum is claimed |
| Video thumbnail | Not included | No thumbnail is presented as release evidence |
| Android or Windows binary | Not included | No installable artifact or checksum is claimed |
| Social preview | Repository-setting task | Must be configured after merge from an approved current-release design |

Screenshot and video specifications remain as release procedures for a later
media-bearing release. They do not imply that the artifacts exist today.

## Verification evidence

| Gate | Command or evidence | Release rule |
|---|---|---|
| Frontend | Local release validation completed | Required before the frontend audit merge |
| Backend | Local release validation completed | Required before the backend audit merge |
| Showcase | `python scripts/check_showcase.py` completed locally | Required before tagging |merge |
| Demo rebuild | Guarded rebuild and `validate_demo_data.py` | Required again before any new screenshots/video |
| Route rehearsal | `DEMO.md` walkthrough | Required again before any new screenshots/video |
| Release tag | `v1.0.0-showcase` | Create only after all three PRs are merged and checks are green |

## Release completion checklist

- [x] Record the exact audited frontend revision.
- [x] Record the exact audited backend revision.
- [x] Record the Alembic head.
- [x] Record the evidence date.
- [x] State provider boundaries without production overclaiming.
- [x] Inventory every public media/binary category.
- [x] Remove the stale screenshot set.
- [x] State that no video URL or checksum is included.
- [x] Run the frontend release validation locally.
- [x] Run the backend release validation locally.
- [x] Run the showcase release validation locally.
- [x] Merge the frontend and backend audit pull requests.
- [x] Publish the finalized showcase snapshot to `main`.
- [ ] Create `v1.0.0-showcase` on the finalized showcase commit.
- [ ] Configure the GitHub social preview from an approved release design.

## Integrity note

A filename containing “final” is not release evidence. The tag, exact source
revisions, CI results, artifact inventory, and checksums for any future
downloadable files are authoritative.
