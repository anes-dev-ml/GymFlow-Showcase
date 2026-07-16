# GymFlow Quality Strategy

GymFlow uses layered automated checks and manual product review. The goal is not
to maximize a test-count number; it is to protect the risks that could make a
multi-surface SaaS unreliable, unsafe, or difficult to trust.

## Quality objectives

- Keep frontend and backend contracts synchronized.
- Prevent authorization regressions.
- Protect migration history and database metadata.
- Detect unsafe environment configuration.
- Keep demo data repeatable and internally consistent.
- Prevent localization and responsive-layout regressions.
- Make failures diagnosable through request IDs and structured logs.
- Verify negative and edge states, not only happy paths.
- Record release evidence without claiming checks that did not execute.
- Keep public screenshots and documentation tied to exact source revisions.

## Quality layers

| Layer | Purpose |
|---|---|
| Static analysis | Catch language, type, lint, and source-structure problems |
| Unit and model tests | Validate parsing, calculations, state transitions, and display mapping |
| API tests | Verify HTTP contracts and business behavior |
| Authorization tests | Protect workspace, role, portal, and messaging boundaries |
| Contract scripts | Enforce architectural requirements without full runtime setup |
| Integration checks | Exercise PostgreSQL, Redis, migrations, and route registration |
| Frontend and backend sync | Detect route and payload drift |
| Manual product review | Validate visuals, responsiveness, localization, and provider workflows |
| Demo validation | Verify deterministic counts, relationships, trends, and identities |
| Showcase validation | Protect public documentation, provenance, and release assets |

## Risk-to-evidence matrix

| Risk | Protection |
|---|---|
| Frontend calls a removed or renamed endpoint | API-sync tests and route-contract checks |
| Raw enum appears in the UI | Localization and display checks plus manual language review |
| Workspace A accesses Workspace B | Backend scope and authorization tests |
| Portal token accesses staff data | Credential-isolation tests |
| Staff token accesses portal-only data | Portal dependency tests |
| A role sees a forbidden route or action | Backend permission tests and frontend permission guards |
| Migration graph becomes inconsistent | Alembic graph audit and one-head checks |
| Model metadata diverges from migrations | Database contract checks |
| Production starts with weak settings | Production configuration tests |
| Debug or API docs remain exposed in production | Deployment and security contracts |
| Public route accepts an oversized request | Request-size middleware tests |
| Public authentication is brute-forced | Rate-limit tests |
| Stripe webhook is delivered twice | Event-idempotency tests |
| Message retry creates a duplicate | Retry-safe message tests |
| Internal note appears in the portal | Audience-schema and participant tests |
| Two staff overwrite workflow state | Optimistic-version conflict tests |
| Staff presence is wrong across devices | Presence aggregation and lifecycle tests |
| Demo reset targets an unsafe database | Reset-safety tests and static contracts |
| Demo reports are empty or flat | Seed-validation targets |
| French or Arabic layout overflows | Responsive and localization review |
| README references a missing file | Showcase link validation |
| Release contains a secret | Source and showcase secret scanners |
| Screenshot inventory drifts | Exact gallery directory and count checks |
| Public release claims evidence that did not run | Manifest and wording contracts |

## Backend validation

The backend validation workflow is designed to start PostgreSQL 16 and Redis 7,
install the development dependency layer, verify dependency consistency, build
the production Docker image, and execute the unified backend quality bundle.

The bundle covers:

- secret scanning;
- Alembic migration graph and one-head validation;
- database metadata contracts;
- Stripe environment smoke checks;
- security and observability contracts;
- deployment and API contracts;
- deterministic demo-seed contracts;
- route-authorization and portal-route inspection;
- application import and registration smoke checks;
- pytest behavior tests.

Static contracts complement behavioral tests. They provide fast, explicit
failure messages when required middleware, migrations, routes, production
artifacts, or demo guards disappear.

## Frontend validation

The frontend validation workflow is designed to cover:

- secret scanning;
- dependency installation;
- localization generation and parity;
- `flutter analyze`;
- source and UI consistency checks;
- frontend and backend API synchronization;
- portal privacy and regression tests;
- the full Flutter test suite;
- a release web build.

Local runners group targeted portal and full frontend checks so failure output
remains readable and raw logs can be retained under `build/test_logs`.

## Frontend test areas

### Models and repositories

Coverage includes response parsing, null and default handling, API error
envelopes, payment and membership lifecycle mapping, report calculations,
receipts, and booking reconstruction.

### Controllers

Coverage includes loading and refresh lifecycle, optimistic updates, rollback,
pagination, notification grouping, messaging state, and conflict handling.

### UI and source regressions

Coverage includes route presence, portal privacy, mobile navigation, Material
composition, localization usage, dashboard setup behavior, messaging viewport
constraints, and staff presence wiring.

Source-level contracts are used where stable headless rendering would be
disproportionately expensive. Broader widget, golden, and integration coverage
remain valuable future additions.

## Authorization strategy

Authorization evidence includes both successful and denied access.

| Actor | Allowed | Denied |
|---|---|---|
| Owner | Full workspace operations | Another workspace without membership |
| Manager | Broad operations | Restricted owner-only billing and configuration |
| Trainer | Assigned or permitted schedules and clients | Unrelated conversations and administrative controls |
| Receptionist | Front desk, bookings, check-ins, and supported payments | Sensitive owner-only operations |
| Portal client | Own portal data | Other clients and all staff routes |
| Unauthenticated visitor | Public routes | Staff and protected portal data |

## Deterministic demo validation

The demo validator verifies more than row counts. It checks:

- workspace identity;
- user and role relationships;
- active and archived client totals;
- membership and service states;
- booking lifecycle counts;
- check-in history;
- monthly revenue and pending-payment totals;
- notification counts;
- presence sessions;
- portal settings and valid access records;
- external payment identifier safety;
- report history and non-flat trends.

The rebuild executes as one transaction and commits only after validation.

## Manual product review

The release review covers:

### Product workflows

- registration, verification, login, logout, and password recovery;
- workspace creation and selection;
- client, membership, plan, and service lifecycle;
- staff invitations and trainer availability;
- booking creation, recurrence, cancellation, completion, and no-show states;
- attendance and front-desk check-in and check-out;
- payment collection, cancellation, refund, receipt, and reporting;
- notifications, activity logs, messaging, and portal access.

### Screen sizes

- 1440 desktop;
- 1280 laptop;
- 1024 compressed desktop;
- 768 tablet portrait and landscape;
- 430, 390, 375, and 360 mobile widths.

### Languages

- English;
- French with long-copy expansion;
- Arabic with RTL direction and alignment.

### Failure states

- backend unavailable;
- unauthorized or forbidden;
- expired session;
- empty workspace or no data;
- invalid forms;
- rate limiting;
- provider cancellation or error;
- stale messaging workflow version;
- invalid or expired portal code.

## Release evidence model

A showcase release records:

- frontend, backend, and showcase revisions;
- Alembic head;
- deterministic demo targets;
- validation scope and result;
- hosted CI status or the documented reason equivalent local validation was used;
- relevant runtime and dependency versions;
- evidence date;
- included and omitted artifacts;
- integrity metadata for downloadable files;
- known provider and production limitations.

The authoritative record is the [Build Manifest](../BUILD_MANIFEST.md).

### Hosted-runner exception

Green hosted CI is preferred. Equivalent local validation is acceptable only
when a hosted job fails before checkout or code execution for a documented
account-level or platform reason. The limitation is recorded explicitly, and
the release does not claim green hosted CI.

A job that reaches source checkout and then fails represents a real quality
failure and cannot use this exception.

## Quality gates by environment

| Environment | Minimum gate |
|---|---|
| Development | Targeted tests, Flutter analysis, relevant contracts |
| Pull request | Full repository validation when hosted execution is available |
| Screenshot-bearing showcase | Exact source snapshot, source validation, demo evidence, gallery privacy review, showcase validator |
| Media-bearing showcase | Source validation, fresh demo rebuild, route review, media privacy review, integrity metadata |
| Production package | Green CI, production-setting tests, image build, migration check, supply-chain evidence |
| Production launch | Provider end-to-end validation, deployed isolation, monitoring, backup and restore drill |

## Current `v1.0.0-showcase` evidence

The current release records:

- exact merged frontend and backend `main` commits;
- the single Alembic head;
- equivalent frontend and backend release validation completed locally;
- showcase validation completed locally before release publication;
- the account-level GitHub Actions restriction that prevented jobs from reaching checkout;
- no claim that hosted CI was green;
- 53 screenshots across five validated galleries;
- explicit omission of video, thumbnails, binaries, and checksums;
- private-source, fictional-data, and provider boundaries.

Commercial production assurance would be strengthened further by automated
accessibility audits, browser and device matrix automation, performance budgets,
load testing, database query-plan review, dependency and container scanning,
SBOM and signed provenance, backup restore drills, and hosted synthetic
monitoring.

## Showcase repository validation

The public showcase validator checks:

- required documentation;
- local Markdown links;
- unsafe files and accidental editor state;
- stale credentials and source values;
- common secret patterns;
- canonical frontend and backend revisions;
- exact screenshot gallery counts and directories;
- absence of undeclared video assets;
- reader-facing public documentation tone;
- release and artifact boundary consistency.

This protects the public portfolio surface as well as the application evidence
it represents.
