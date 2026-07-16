# GymFlow Build Manifest

This manifest ties the public GymFlow engineering case study to exact source
revisions, deterministic demo expectations, validation evidence, and a declared
artifact inventory.

## Release identity

| Field | Value |
|---|---|
| Release identifier | `v1.0.0-showcase` |
| Evidence date | 2026-07-15 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual, simulated, or Stripe test-mode state; no real charges |
| Public source boundary | Showcase content only; application source remains private |

The release identifier is authoritative for the showcase snapshot. Its commit
SHA is not duplicated inside the commit it identifies.

## Canonical source snapshot

| Component | Repository/ref | Revision | Evidence |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `489a82e03059465755c74b1be39ae7c05f98fb9b` | Final frontend release audit merged into `main` |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | Final backend release audit merged into `main` |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Release identifier target | Case study, gallery, provenance, and release validation |

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
| Demo payments | Fictional records with no live external identifiers |
| Demo email | Disabled or guarded demo-assisted behavior |

## Deterministic validation targets

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

| Provider | Repository evidence | Deployment-specific verification |
|---|---|---|
| Stripe | Checkout, billing, Connect-aware demo behavior, webhook validation, idempotency | Target account keys, price IDs, webhook rehearsal, KYC and Connect model |
| Email | Verification, recovery, invitation, and portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android token path, Windows PKCE and loopback path | Real client IDs, redirects, package fingerprints, end-to-end verification |

## Public artifact inventory

| Artifact | Status | Integrity statement |
|---|---|---|
| Engineering case study | Included | Versioned in this repository |
| Architecture and threat-model documentation | Included | Versioned in this repository |
| Screenshot gallery | Included | 53 tracked images across desktop, portal, mobile, localization, and engineering galleries |
| Product walkthrough video | Not included | No public URL, binary, duration, thumbnail, captions file, or checksum is claimed |
| Android or Windows binary | Not included | No installable artifact or checksum is claimed |
| Social preview | External repository metadata | Not part of the source or artifact provenance record |

### Screenshot inventory

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

The visual inventory is described in
[`screenshots/README.md`](screenshots/README.md) and enforced by
[`scripts/check_showcase.py`](scripts/check_showcase.py).

## Validation evidence

| Gate | Evidence | Recorded result |
|---|---|---|
| Frontend | Equivalent release validation completed locally | Completed before the frontend audit merge |
| Backend | Equivalent release validation completed locally | Completed before the backend audit merge |
| Showcase | `python scripts/check_showcase.py` | Required to pass on the final showcase snapshot |
| Hosted Actions | Jobs were blocked before checkout by the account spending policy | No green hosted-CI claim is made for this release |
| Screenshot inventory | 53 tracked images across 5 approved galleries | Exact directory and count contract |

The account-level GitHub Actions restriction prevented hosted jobs from reaching
checkout or source execution. The workflows remain defined, while the release
record relies on equivalent local validation and explicitly avoids claiming
successful hosted CI runs.

## Integrity statement

The release identifier, exact source revisions, deterministic targets,
validation record, and declared artifact inventory are the authoritative
release evidence. Filenames or informal descriptions do not replace that
provenance.
