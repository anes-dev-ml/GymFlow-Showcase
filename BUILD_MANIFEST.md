# GymFlow Build Manifest

This manifest connects the GymFlow engineering case study to exact application revisions, deterministic demo expectations, release validation, and the declared public artifact set.

The machine-readable authority is [`release/evidence-manifest.json`](release/evidence-manifest.json).

## Release identity

| Field | Value |
|---|---|
| Current release record | `v1.0.4-showcase` |
| Previous immutable release | `v1.0.3-showcase` at `7262227bdc925f236f2c1c4257c8630513931b64` |
| Record state | Release record; release mode verifies the current tag on clean reviewed `HEAD` |
| Record date | 2026-08-16 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual, simulated, or Stripe test-mode state; no real charges |
| Source access | Application implementation remains private; selected read-only review may be considered |

`v1.0.4-showcase` is a presentation-focused patch. It keeps the same application snapshot and 53-image gallery as `v1.0.3-showcase` while refining the public narrative, information hierarchy, source-access language, roadmap, and supporting documentation.

## Canonical source snapshot

| Component | Repository/ref | Revision | Role in this showcase |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `b73a623c3985e4bc458d04b4b484887ada593fa5` | Responsive multilingual GymFlow product snapshot |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | API, data, security, demo, and operational snapshot |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Current reviewed record `HEAD` | Public case study, gallery, architecture, and release record |

The showcase commit is identified by its release tag after publication. A file inside a commit does not attempt to contain its own commit SHA.

## Application and schema versions

| Component | Version / constraint |
|---|---|
| Frontend application | `1.0.0+1` |
| Backend API | `1.0.0` |
| Dart SDK | `^3.9.0` |
| Python application runtime | 3.10 |
| Showcase validation runtime | Python 3.10+ |
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

## Deterministic demo targets

These values describe the state immediately after a successful guarded rebuild and validation transaction.

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

The deterministic validator defines exact post-rebuild counts and relationships. Screenshots show representative fictional states, so date-relative values, active presence, temporary notifications, and capture-time state can naturally differ after review actions.

## Provider status

| Provider | Implemented boundary | Deployment configuration |
|---|---|---|
| Stripe | Checkout, billing, Connect-aware demo behavior, webhook validation, idempotency | Target keys, price IDs, webhook rehearsal, KYC, and Connect model |
| Email | Verification, recovery, invitation, and portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android token path, Windows PKCE and loopback path | Real client IDs, redirects, package fingerprints, and end-to-end verification |

## Public artifact inventory

| Artifact | Status | Release role |
|---|---|---|
| Engineering case study | Included | Versioned public product and engineering documentation |
| Architecture and security documentation | Included | System design, controls, trade-offs, and deployment boundaries |
| Screenshot gallery | Included | 53 reviewed files with exact SHA-256 records |
| Release manifest | Included | Machine-readable source, gallery, boundary, and validation record |
| Product walkthrough video | Optional future artifact | Not part of this release |
| Android or Windows binary | Optional review artifact | Not distributed by this showcase release |
| Application source | Private | Selected read-only review may be considered separately |
| Social preview | Repository metadata | Presentation metadata outside the versioned application snapshot |

## Screenshot inventory

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

The gallery release process checks that:

- canonical application revisions remain unchanged;
- identities and records are fictional;
- no token, password, secret, live provider identifier, or valid QR credential is visible;
- every filename matches the gallery contract;
- all 53 image files are unique;
- all 53 image files match their recorded SHA-256 values;
- known rejected hashes remain absent;
- manual privacy, localization, responsive, and visual review is complete.

## Local release validation

| Gate | Command | Expectation |
|---|---|---|
| Validator tests | `python -m unittest discover -s tests -p "test_*.py"` | Pass |
| Showcase base | `python scripts/check_showcase.py` | Pass |
| Release record | `python scripts/check_release.py` | Pass before tagging |
| Release tag | `python scripts/check_release.py --release` | Pass after tagging |
| Combined PowerShell gate | `.\scripts\validate_release.ps1` | Pass |
| Combined POSIX gate | `bash scripts/validate_release.sh` | Pass |

This release line uses local PowerShell/POSIX validation rather than GitHub Actions. The validators inspect tracked Git content, local links, release-state consistency, source provenance, screenshot inventory, dimensions, duplicate hashes, blocked media, exact media hashes, public wording, and release-tag alignment.

## Release procedure

For `v1.0.4-showcase`:

1. keep the canonical frontend/backend revisions and existing 53-image gallery unchanged;
2. run the validator tests and base showcase checks;
3. run record-mode release validation;
4. complete the final documentation and privacy review;
5. merge the reviewed release record into `main`;
6. create `v1.0.4-showcase` on that exact commit;
7. run release-mode validation.

The tag, canonical source revisions, deterministic demo targets, manifest, and reviewed gallery together identify the public snapshot.
