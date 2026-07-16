# GymFlow Build Manifest

This manifest connects the GymFlow engineering case study to exact application
revisions, deterministic demo expectations, validation evidence, and a declared
artifact inventory.

## Release identity

| Field | Value |
|---|---|
| Target release identifier | `v1.0.1-showcase` |
| Current state | Release candidate on `main`; tag only after every final gate passes |
| Evidence date | 2026-07-16 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual, simulated, or Stripe test-mode state; no real charges |
| Public source boundary | Showcase content only; application source remains private |

`v1.0.0-showcase` is a historical tag that predates the final evidence-hardening
pass. It must not be presented as the commit containing the current gallery.
The next immutable release tag is created only after the final screenshot review
and showcase validator succeed on the same commit.

## Canonical source snapshot

| Component | Repository/ref | Revision | Evidence |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `489a82e03059465755c74b1be39ae7c05f98fb9b` | Final frontend release audit merged into `main` |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | Final backend release audit merged into `main` |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Release-candidate head | Case study, gallery, provenance, and release validation |

The application audit work was based directly on frontend
`a0ab421b45c447dd710ce8c53cf97edcb7c85e1a` and backend
`9d131982a161d22a56efeda8ef47805ee7e9dca6` before the final audit merges.

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
| Demo identities | Reserved `.test` and IANA example-domain addresses only |
| Demo payments | Fictional records with no live external identifiers |
| Demo email | Disabled or guarded demo-assisted behavior |

## Deterministic validation targets

These values describe the authoritative result immediately after a successful
guarded rebuild and validation transaction.

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
| Canonical portal stories | 2 |

## Visual-capture semantics

The deterministic validator is authoritative for exact counts and relationships.
The visual gallery demonstrates product surfaces and representative fictional
states. Date-relative values, active presence, temporary notifications, and
capture-time UI state can change while the application is being reviewed.
Screenshots therefore do not replace machine-readable demo validation.

Every release screenshot must still satisfy all of these rules:

- the application source revisions above are unchanged;
- identities and records are fictional;
- no token, password, secret, live provider identifier, or real QR credential is visible;
- every filename matches the declared gallery contract;
- all 53 image files have unique content hashes;
- the gallery passes manual privacy, localization, responsive, and visual review.

## Provider status

| Provider | Repository evidence | Deployment-specific verification |
|---|---|---|
| Stripe | Checkout, billing, Connect-aware demo behavior, webhook validation, idempotency | Target keys, price IDs, webhook rehearsal, KYC and Connect model |
| Email | Verification, recovery, invitation, and portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android token path, Windows PKCE and loopback path | Real client IDs, redirects, package fingerprints, end-to-end verification |

## Public artifact inventory

| Artifact | Status | Integrity statement |
|---|---|---|
| Engineering case study | Included | Versioned in this repository |
| Architecture and threat-model documentation | Included | Versioned in this repository |
| Screenshot gallery | Included in candidate | 53 tracked files across five galleries; final tag requires unique hashes and all media gates |
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
| Showcase | `python scripts/check_showcase.py` | Must pass on the exact commit selected for the release tag |
| Hosted Actions | Jobs were blocked before checkout by the account spending policy | No green hosted-CI claim is made for this release candidate |
| Screenshot inventory | Exact paths, image formats, dimensions, unique hashes, and blocked-asset checks | Enforced by the showcase validator |

The hosted-runner restriction prevented jobs from reaching checkout or source
execution. The workflows remain defined, while the candidate relies on equivalent
local validation and explicitly avoids claiming successful hosted CI runs.

## Final tag rule

Create `v1.0.1-showcase` only when:

1. frontend and backend revisions still match this manifest;
2. the final screenshot replacements are committed;
3. `python scripts/check_showcase.py` passes locally;
4. the release commit is reviewed for tokens, private data, and misleading claims;
5. the tag points to that exact reviewed commit.

The tag, exact source revisions, deterministic targets, validation record, and
artifact inventory together form the authoritative release evidence.