# GymFlow Quality Strategy

GymFlow uses layered automated checks and manual product QA. The goal is not to
maximize a test-count number. The goal is to protect the risks that can make a
multi-surface SaaS unreliable, unsafe, or embarrassing during release.

## Quality objectives

- Keep frontend and backend contracts synchronized.
- Prevent authorization regressions.
- Protect migration history and database metadata.
- Detect unsafe environment configuration.
- Keep demo data repeatable and internally consistent.
- Prevent localization and responsive-layout regressions.
- Make failures diagnosable through compact logs and request IDs.
- Verify negative and edge states, not only happy paths.
- Record release evidence without claiming checks that did not execute.

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
| Manual QA | Validate visuals, responsiveness, localization, and provider workflows |
| Demo validation | Verify deterministic counts, relationships, trends, and identities |
| Showcase validation | Prevent broken documentation and unsafe release assets |

## Risk-to-evidence matrix

| Risk | Protection |
|---|---|
| Frontend calls a removed or renamed endpoint | API-sync tests and route-contract checks |
| Raw enum appears in UI | Localization and display checks plus manual language QA |
| Workspace A accesses Workspace B | Backend scope and authorization tests |
| Portal token accesses staff data | Credential-isolation tests |
| Staff token accesses portal-only data | Portal dependency tests |
| Role sees a forbidden route or action | Backend permission tests and frontend permission guards |
| Migration graph becomes inconsistent | Alembic graph audit and one-head checks |
| Model metadata diverges from migrations | Database contract checks |
| Production starts with weak settings | Production configuration tests |
| Debug or docs endpoints are exposed in production | Deployment and security contract tests |
| Public route accepts an oversized abuse payload | Request-size middleware tests |
| Public authentication or access is brute-forced | Rate-limit tests |
| Stripe webhook is delivered twice | Event-idempotency tests |
| Message retry creates a duplicate | Retry-safe message tests |
| Internal note appears in the portal | Audience-schema and participant tests |
| Two staff overwrite workflow state | Optimistic-version conflict tests |
| Staff presence is wrong across devices | Presence aggregation and lifecycle tests |
| Demo reset targets an unsafe database | Reset-safety tests and static contract |
| Demo dashboard or report is empty or flat | Seed-validation targets |
| French or Arabic layout overflows | Responsive and localization manual QA |
| README references a missing file | Showcase repository validation |
| Release contains a secret | Source and showcase secret scanners |
| Release claims evidence that did not run | Manifest contract and wording checks |

## Backend quality pipeline

The backend GitHub Actions workflow is designed to start PostgreSQL 16 and Redis
7 services, install dependencies, validate dependency consistency, build the
production Docker image, and run the unified backend quality bundle.

The bundle covers:

- secret scanning;
- Alembic migration audit;
- database metadata contract;
- Stripe environment smoke checks;
- security and observability contracts;
- deployment and API contracts;
- demo-seed and documentation contracts;
- route-authorization inspection;
- portal-route inspection;
- smoke import and registration checks;
- pytest behavior tests.

### Why static contracts exist

Some architectural failures are faster and clearer to detect statically than
through a full runtime scenario. Examples include:

- a required middleware is removed;
- debug routes are no longer guarded;
- a migration creates multiple heads;
- a production Compose artifact disappears;
- a required portal route is not registered;
- the demo reset introduces a forbidden destructive operation.

Static contracts complement behavioral tests. They do not replace them.

## Frontend quality pipeline

The frontend GitHub Actions workflow is designed to cover:

- secret scanning;
- dependency installation;
- localization generation and parity;
- `flutter analyze`;
- source and UI consistency checks;
- frontend and backend API-sync tests;
- portal privacy and regression tests;
- the full Flutter test suite;
- a release web build.

Additional local runners group portal and full frontend checks so terminal output
remains readable and raw logs can be preserved under `build/test_logs`.

## Frontend test categories

### Models and repositories

Protect:

- response parsing;
- null and default handling;
- API error envelopes;
- payment and membership lifecycle mapping;
- report calculations;
- receipt and booking reconstruction.

### Controllers

Protect:

- loading and refresh lifecycle;
- optimistic UI updates;
- mutation rollback;
- pagination;
- notification grouping;
- messaging workflow changes.

### Widget and source regressions

Protect:

- route presence;
- portal privacy rules;
- mobile navigation;
- Material composition requirements;
- localization key usage;
- dashboard setup behavior;
- messaging viewport constraints;
- staff presence wiring.

Source-level tests are used where a stable headless rendering environment would
be disproportionately expensive. They should be complemented over time by
broader widget, golden, and integration coverage.

## Authorization test strategy

Authorization tests should cover both positive and negative access.

| Actor | Allowed | Denied |
|---|---|---|
| Owner | Full workspace operations | Another workspace without membership |
| Manager | Broad operations | Owner-only billing or configuration where restricted |
| Trainer | Assigned or permitted schedule and clients | Unrelated conversations and administrative controls |
| Receptionist | Front desk, supported bookings, check-ins, and payments | Sensitive owner-only operations |
| Portal client | Own portal data | Other clients and all staff routes |
| Unauthenticated | Public routes | Staff and protected portal data |

## Demo-data validation

The deterministic demo validator checks more than row counts. It validates:

- workspace identity;
- user and role relationships;
- active and archived client totals;
- membership and service states;
- booking lifecycle counts;
- check-in history;
- monthly revenue and pending-payment totals;
- notification counts;
- presence sessions;
- portal settings and valid access links;
- external payment-ID safety;
- report history and non-flat trends.

The rebuild is one transaction and commits only after validation.

## Manual QA matrix

### Product workflows

- register, verify, log in, log out, and recover password;
- create and select workspace;
- client create, edit, archive, and detail;
- plan and membership lifecycle;
- staff, invitation, and availability;
- booking create, edit, cancel, recurrence, and no-show;
- attendance and front-desk check-in and check-out;
- payment collection, cancellation, refund, and display;
- reports and CSV export;
- notifications and activity logs;
- messaging assignment, notes, replies, retries, and conflicts;
- client-portal access and isolation.

### Screen sizes

- 1440 desktop;
- 1280 laptop;
- 1024 compressed desktop;
- 768 tablet portrait and landscape;
- 430, 390, 375, and 360 mobile widths.

### Languages

- English;
- French with long copy;
- Arabic with RTL direction and alignment.

### Failure states

- backend unavailable;
- unauthorized or forbidden;
- expired session;
- empty workspace;
- no data;
- invalid form;
- rate limit;
- provider cancellation or error;
- stale messaging workflow version;
- invalid or expired portal code.

## Release evidence

A final showcase release should record:

- frontend commit and branch;
- backend commit and branch;
- showcase tag or commit;
- Alembic head;
- demo-validation scope and result;
- hosted CI status or the documented reason equivalent local validation was used;
- relevant runtime and dependency versions;
- evidence date;
- included and omitted artifact inventory;
- checksums for any downloadable artifacts;
- known limitations.

See the [Build Manifest](../BUILD_MANIFEST.md).

### Hosted-runner exception

Green hosted CI is preferred. Equivalent local validation is acceptable only
when the hosted job fails before checkout or code execution for a documented
account-level or platform reason. The release must record the limitation and
must not claim green hosted CI.

A running job that reaches source checkout and then fails is a real quality
failure and cannot use this exception.

## Quality gates by environment

| Environment | Minimum gate |
|---|---|
| Development | Targeted tests, Flutter analysis, relevant contract checks |
| Pull request | Full repository CI when hosted execution is available |
| Documentation-only showcase tag | Exact source snapshot, applicable source validation, showcase validator, honest artifact inventory |
| Media-bearing showcase tag | Source validation, fresh demo rebuild, demo validator, route rehearsal, media privacy review, showcase validator |
| Production package | Green CI, production-setting tests, image build, migration check, supply-chain evidence |
| Production launch | Provider E2E, deployed isolation tests, monitoring, backup and restore drill |

## Current `v1.0.0-showcase` evidence

The tagged documentation-only release records:

- exact merged frontend and backend `main` commits;
- the single Alembic head;
- equivalent frontend and backend release validation completed locally;
- showcase validation completed locally;
- an account-level GitHub Actions restriction that prevented jobs from starting before checkout;
- no claim that hosted CI was green;
- removal of the stale 19-image screenshot set;
- explicit omission of video, thumbnails, binaries, and checksums;
- private-source, fictional-data, and provider boundaries.

Areas that would strengthen a commercial production program include:

- automated accessibility audits;
- browser and device matrix automation;
- performance budgets and load tests;
- database query-plan regression review;
- container and dependency vulnerability scanning;
- signed provenance and SBOM attachment;
- scheduled backup restore drills;
- hosted synthetic monitoring.

These are tracked as future deployment or release work rather than presented as
already complete.

## Showcase repository quality

The showcase validator checks:

- required documentation exists;
- local Markdown links resolve;
- unsafe file names and artifact types are absent;
- stale credentials and source values are not reintroduced;
- common API-key and private-key patterns are absent;
- exact frontend and backend revisions remain recorded;
- release wording does not claim pending or unexecuted evidence;
- no undeclared screenshot or video asset remains;
- README positioning and artifact boundaries remain explicit.

This protects the portfolio surface itself, not only the application code.