# Quality and verification

GymFlow is tested at the Flutter, API, database, and release boundaries. Automated checks cover repeatable failure modes; manual review is still required for interface quality, external providers, and operating environments.

## Application checks

| Layer | Validation |
| --- | --- |
| Flutter | Format and static analysis, localization, route contracts, widget and controller tests, Web build |
| FastAPI | Python tests, typed API contracts, authorization, rate limits, errors, and service behavior |
| Database | PostgreSQL/Redis integration, migration graph, schema contracts, isolation checks |
| Providers | Configuration and callback contracts, webhook signatures, duplicate-state handling |
| Demo | Protected seed/reset commands, relational and financial invariants |

The private code repositories contain these checks and their CI configurations.

**Backend (from the Backend checkout)**

```sh
python scripts/run_backend_quality_checks.py
```

**Frontend (from the Frontend checkout)**

```sh
python tool/run_frontend_quality_checks.py
python tool/run_frontend_api_sync_tests.py
python tool/run_portal_quality_checks.py
python tool/run_frontend_all_tests.py
flutter analyze
flutter test
```

A passing source test does not establish hosted reliability or provider behavior in a different environment.

## High-risk regression areas

- Tenant isolation and workspace membership must be enforced on server-side queries.
- Staff and client-portal credentials must not be interchangeable.
- Role permissions must reject unauthorized operations even if a UI control is visible.
- Bookings must respect availability, duration, recurrence, and lifecycle rules.
- Payment and messaging retries must not duplicate state transitions.
- Staff-only notes must not enter client-visible responses.
- Demo reset commands must refuse live or non-demo data targets.

Tests include both permitted operations and denied, expired, duplicate, and conflicting requests.

## Manual acceptance

Review authentication and session expiry, staff workflows, scheduling and attendance, finance, messaging, and client self-service across relevant devices. Verify desktop and narrow layouts, French text expansion, and Arabic right-to-left behavior. Include empty, error, and provider-cancellation states.

## Showcase checks

The public repository validates documentation links, tracked-file safety, tagged source provenance, and the approved media inventory.

```sh
python -m unittest discover -s tests -p "test_*.py"
python scripts/check_showcase.py
python scripts/check_release.py
```

The strict release gate (`python scripts/check_release.py --release`) is intended for a clean checkout of the matching release tag; subsequent documentation commits on `main` do not redefine that tag.

The canonical source revisions and 53 screenshot hashes are recorded in the [Build Manifest](../BUILD_MANIFEST.md) and [evidence manifest](../release/evidence-manifest.json).

## Outside the demonstrated scope

Live Stripe, OAuth and email configuration, backups and restore tests, production monitoring, external security assessments, load testing, and jurisdiction-specific policies require deployment-specific verification.

See [Operations](OPERATIONS.md) and [Releases](../RELEASES.md).