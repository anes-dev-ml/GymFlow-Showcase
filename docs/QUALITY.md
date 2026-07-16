# GymFlow Quality Strategy

GymFlow uses layered automated checks and manual product review. The objective is
not to maximize a test-count number; it is to protect the risks that could make a
multi-surface SaaS unreliable, unsafe, misleading, or difficult to operate.

## Quality objectives

- Keep frontend and backend contracts synchronized.
- Prevent authorization and tenant-isolation regressions.
- Protect migration history and database metadata.
- Reject unsafe environment and provider configuration.
- Keep demo data repeatable and internally consistent.
- Protect localization and responsive behavior.
- Make failures diagnosable through request IDs and structured logs.
- Verify denied, empty, error, conflict, and expiry states—not only happy paths.
- Record only validation that actually executed.
- Tie public evidence to exact source revisions and reviewed artifacts.

## Quality layers

| Layer | Purpose |
|---|---|
| Static analysis | Catch language, type, lint, and source-structure problems |
| Unit/model tests | Validate parsing, calculations, mapping, and lifecycle transitions |
| API behavior tests | Verify contracts, business outcomes, and errors |
| Authorization tests | Protect workspace, role, portal, resource, and participant boundaries |
| Contract scripts | Enforce architectural and release requirements quickly |
| Integration checks | Exercise PostgreSQL, Redis, migrations, and route registration |
| API synchronization | Detect frontend/backend route and payload drift |
| Manual product review | Validate visuals, responsiveness, localization, and provider flows |
| Demo validation | Verify deterministic counts, relationships, trends, and identities |
| Showcase validation | Protect documentation, provenance, privacy, and media integrity |

## Risk-to-evidence matrix

| Risk | Protection |
|---|---|
| Frontend calls a removed endpoint | API-sync and route-contract checks |
| Raw backend enum reaches UI | Localization/display contracts plus language review |
| Workspace A accesses Workspace B | Scope dependencies, query review, isolation tests |
| Portal credential accesses staff data | Separate token dependencies and denied-access tests |
| Role sees a forbidden action | Backend permission tests and frontend guards |
| Migration graph diverges | Alembic graph, one-head, and metadata checks |
| Production starts with weak settings | Fail-fast production configuration tests |
| Public auth is brute-forced or oversized | Redis-backed rate limits and pre-parse body limits |
| Stripe webhook is replayed | Signature checks, stored event IDs, idempotent transitions |
| Message retry creates a duplicate | Retry-safe identifiers |
| Internal note reaches a client | Audience-specific schemas and participant tests |
| Concurrent workflow update is lost | Optimistic version conflicts |
| Presence is incorrect across devices | Heartbeat/activity aggregation tests |
| Demo reset targets unsafe data | Environment, host, name, allowlist, and confirmation guards |
| Demo reports are empty or flat | Seed-validation targets |
| French or Arabic layout regresses | Responsive and localization review |
| Public repository leaks a secret | Source and showcase secret checks |
| Screenshot inventory drifts | Exact filenames, dimensions, hashes, and rejected-media checks |
| Release tag misrepresents evidence | Candidate manifest and tag-on-final-commit policy |

## Backend validation

The backend quality path is designed to start PostgreSQL 16 and Redis 7, install
the development dependencies, validate dependency consistency, build the
production image, and execute the unified backend quality bundle.

The bundle covers:

- secret scanning;
- Alembic graph and one-head validation;
- model/migration metadata contracts;
- production settings and provider-mode checks;
- security and observability contracts;
- deterministic demo guards and validation;
- route authorization and portal isolation;
- application import/registration smoke checks;
- pytest behavior tests.

Static contracts complement behavioral tests by failing quickly when required
middleware, migrations, routes, provider boundaries, or demo guards disappear.

## Frontend validation

The frontend quality path is designed to cover:

- secret scanning and dependency installation;
- localization generation and parity;
- `flutter analyze`;
- source and UI consistency contracts;
- frontend/backend API synchronization;
- portal privacy and mobile-navigation regressions;
- the full Flutter test suite;
- a release web build.

Coverage includes models, repositories, API error envelopes, controllers,
optimistic updates and rollback, pagination, messaging conflicts, payment and
membership lifecycle mapping, route access, responsive navigation, localization,
and dashboard/setup behavior.

Source-level UI contracts remain useful where stable headless rendering would be
disproportionately expensive. Broader golden, accessibility, and integration
coverage remain valuable future additions.

## Authorization strategy

Authorization evidence includes successful and denied access.

| Actor | Allowed | Denied |
|---|---|---|
| Owner | Full workspace operations | Another workspace without membership |
| Manager | Broad operations | Owner-only billing and ownership controls |
| Trainer | Assigned/permitted schedules and clients | Unrelated conversations and administration |
| Receptionist | Front desk, bookings, check-ins, supported payments | Sensitive owner-only operations |
| Portal client | Own portal-safe data | Other clients and every staff route |
| Public visitor | Public routes | Protected staff and portal data |

## Deterministic demo validation

The demo validator checks more than row counts:

- workspace identity and user/role relationships;
- active and archived clients;
- plan, membership, and service states;
- booking lifecycle counts and recurrence context;
- check-in history;
- monthly revenue and pending-payment totals;
- notification and presence state;
- portal settings and access records;
- payment-identifier safety;
- non-flat reporting history.

The reset, seed, and validation run inside one transaction and commit only after
every invariant passes.

## Manual product review

The release review covers:

### Workflows

- registration, verification, login, recovery, and logout;
- workspace creation and selection;
- client, plan, membership, and service lifecycle;
- invitations, trainer availability, and staff presence;
- booking creation, recurrence, cancellation, completion, and no-show behavior;
- daily attendance and front-desk check-in/out;
- payment collection, cancellation, refund, receipt, and reporting;
- notifications, audit history, messaging, and portal access.

### Viewports and languages

- 1440 and 1280 desktop;
- 1024 compressed desktop;
- tablet portrait and landscape;
- 430, 390, 375, and 360 mobile widths;
- English, expanded French copy, and Arabic RTL.

### Failure states

- backend unavailable;
- unauthorized or forbidden;
- expired sessions and portal codes;
- empty workspace/data;
- invalid forms and rate limits;
- provider cancellation/error;
- stale messaging workflow version.

## Showcase media validation

The `v1.0.1-showcase` candidate strengthens the gallery contract. The validator
now checks:

- the exact 53 approved paths;
- supported file formats;
- readable dimensions and expected orientation;
- 53 unique content hashes;
- known rejected media hashes;
- stale source revisions and release values;
- common text-secret and JWT-like patterns;
- local Markdown links and public-facing wording;
- the absence of undeclared video assets.

Binary checks do not replace human review. Every screenshot still requires a
manual inspection for visible credentials, QR payloads, local paths, browser
overlays, private data, broken localization, and misleading product state.

## Release evidence model

A showcase release records:

- frontend, backend, and showcase revisions;
- Alembic head;
- deterministic targets;
- validation scope and result;
- hosted-CI status or the precise reason it did not execute;
- runtime/dependency versions;
- evidence date;
- included and omitted artifacts;
- known provider and production limitations.

The authoritative record is the [Build Manifest](../BUILD_MANIFEST.md).

## Hosted-runner boundary

Green hosted CI is preferred. Equivalent local validation is acceptable only
when the hosted job fails before checkout or code execution for a documented
account/platform reason. A job that reaches source and then fails represents a
real quality failure and cannot use this exception.

For the current release line, GitHub-hosted jobs were blocked before checkout by
an account-level spending policy. The repository does not claim green hosted CI.

## Candidate release gate

`v1.0.1-showcase` may be tagged only after:

1. all prepared and manually recaptured images are committed;
2. the image set has 53 unique hashes and no rejected media;
3. the showcase validator passes on the exact final commit;
4. the same commit receives a manual privacy and visual review;
5. the tag points to that exact commit.

Commercial production assurance would additionally benefit from accessibility
automation, browser/device matrix execution, performance budgets, load and query
analysis, dependency/container scanning, SBOM and signed provenance, backup
restore drills, and hosted synthetic monitoring.