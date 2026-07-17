# GymFlow Build Manifest

This manifest connects the GymFlow engineering case study to exact application revisions, deterministic demo expectations, validation evidence, and a declared artifact inventory.

The machine-readable companion record is [`release/evidence-manifest.json`](release/evidence-manifest.json).

## Release identity

| Field | Value |
|---|---|
| Target release | `v1.0.2-showcase` |
| Current state | Release candidate on `main` |
| Latest immutable release | `v1.0.1-showcase` at `53aa79d5124902fc689c4f7b121c7d4b1fdccdc9` |
| Evidence date | 2026-07-17 |
| Demo workspace | Northline Performance Club |
| Data boundary | Fictional deterministic demo data only |
| Payment boundary | Manual, simulated, or Stripe test-mode state; no real charges |
| Public source boundary | Showcase content only; application source remains private |

`v1.0.2-showcase` is a patch-level evidence-integrity correction. It preserves the canonical frontend and backend snapshots while correcting release-state wording, centralizing provenance, strengthening tracked-file validation, adding local release runners, and testing the validation tooling itself.

## Canonical source snapshot

| Component | Repository/ref | Revision | Evidence |
|---|---|---|---|
| Frontend | `anes-dev-ml/Gymflow-Frontend` / `main` | `b73a623c3985e4bc458d04b4b484887ada593fa5` | Final responsive and regression-reconciled product snapshot |
| Backend | `anes-dev-ml/Gymflow-Backend` / `main` | `2234af20d1d9dd143bcac22edc699d3ee7fe515f` | Final audited API, data, security, demo, and operational snapshot |
| Showcase | `anes-dev-ml/GymFlow-Showcase` / `main` | Current reviewed candidate HEAD | Documentation, gallery, provenance, and local release validation |

The showcase commit is identified by the immutable release tag. A document inside a Git commit does not attempt to contain its own SHA; the target tag is the authoritative pointer to the reviewed commit.

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

## Deterministic validation targets

These values describe the authoritative result immediately after a successful guarded rebuild and validation transaction.

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

The deterministic validator is authoritative for exact counts and relationships. Screenshots demonstrate representative fictional states; date-relative values, live presence, temporary notifications, and capture-time UI state can differ after review actions.

## Provider status

| Provider | Repository evidence | Deployment-specific verification |
|---|---|---|
| Stripe | Checkout, billing, Connect-aware demo behavior, webhook validation, idempotency | Target keys, price IDs, webhook rehearsal, KYC, and Connect model |
| Email | Verification, recovery, invitation, and portal-access workflows | Verified sender domain and real inbox delivery |
| Google OAuth | Web handoff, Android token path, Windows PKCE and loopback path | Real client IDs, redirects, package fingerprints, and end-to-end verification |

## Public artifact inventory

| Artifact | Status | Integrity statement |
|---|---|---|
| Engineering case study | Included | Versioned in this repository |
| Architecture and security documentation | Included | Versioned in this repository |
| Screenshot gallery | Included | 53 tracked files across five galleries with 53 unique screenshots |
| Evidence manifest | Included | Machine-readable source, gallery, boundary, and validation record |
| Product walkthrough video | Not included | No current provenance-bound walkthrough is claimed |
| Android or Windows binary | Not included | No installable artifact or checksum is claimed |
| Social preview | Repository metadata | Outside the source-provenance contract |

An older standalone non-showcase release may contain historical media. It is not evidence for the current source snapshot and must not be described as the current walkthrough.

## Screenshot inventory

| Gallery | Count |
|---|---:|
| Desktop | 22 |
| Client portal | 10 |
| Mobile | 7 |
| Localization | 4 |
| Engineering | 10 |
| **Total** | **53** |

Every release screenshot must satisfy all of these rules:

- the canonical application revisions remain unchanged;
- identities and records are fictional;
- no token, password, secret, live provider identifier, or valid QR credential is visible;
- every filename matches the declared gallery contract;
- all 53 image files have unique content hashes;
- known rejected media hashes remain absent;
- high-risk reviewed images retain their exact approved SHA-256 values;
- the gallery passes manual privacy, localization, responsive, and visual review.

## Local validation evidence

| Gate | Command | Release expectation |
|---|---|---|
| Validator tests | `python -m unittest discover -s tests -p "test_*.py"` | Must pass |
| Showcase base | `python scripts/check_showcase.py` | Must pass |
| Final candidate | `python scripts/check_release_candidate.py` | Must pass |
| Release tag | `python scripts/check_release_candidate.py --release` | Must pass after tagging |
| Combined PowerShell gate | `./scripts/validate_release.ps1` | Must pass |
| Combined shell gate | `./scripts/validate_release.sh` | Must pass |

Validation for this showcase release line is local and traditional. GitHub-hosted Actions are not used as release evidence. **No green hosted-CI claim is made.**

The validators inspect tracked Git content, local links, release-state consistency, source provenance, screenshot inventory, dimensions, duplicate hashes, blocked media, exact approved media, public wording, and release-tag alignment. Unit tests protect the validator behavior that previously caused false failures.

## Release rule

Create `v1.0.2-showcase` only when:

1. the frontend and backend revisions still match this manifest;
2. validator unit tests pass;
3. `python scripts/check_showcase.py` passes;
4. `python scripts/check_release_candidate.py` passes;
5. the candidate commit has received a final privacy and visual review;
6. the working tree is clean;
7. the tag is created on that exact reviewed commit;
8. `python scripts/check_release_candidate.py --release` passes.

The immutable tag, canonical source revisions, deterministic targets, evidence manifest, and reviewed image set together form the authoritative release record.
