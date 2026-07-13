# GymFlow Quality Strategy

GymFlow uses layered automated checks and manual product QA. The goal is not to maximize a test-count number. The goal is to protect the risks that can make a multi-surface SaaS unreliable, unsafe, or embarrassing during release.

## Quality objectives

- Keep frontend and backend contracts synchronized.
- Prevent authorization regressions.
- Protect migration history and database metadata.
- Detect unsafe environment configuration.
- Keep demo data repeatable and internally consistent.
- Prevent localization and responsive-layout regressions.
- Make failures diagnosable through compact logs and request IDs.
- Verify negative and edge states, not only happy paths.

## Quality layers

| Layer | Purpose |
|---|---|
| Static analysis | Catch language, type, lint, and source-structure problems |
| Unit/model tests | Validate parsing, calculations, state transitions, display mapping |
| API tests | Verify HTTP contracts and business behavior |
| Authorization tests | Protect workspace, role, portal, and messaging boundaries |
| Contract scripts | Enforce architectural requirements without full runtime setup |
| Integration checks | Exercise PostgreSQL, Redis, migrations, and route registration |
| Frontend/backend sync | Detect route and payload drift |
| Manual QA | Validate visuals, responsiveness, localization, and provider workflows |
| Demo validation | Verify deterministic counts, relationships, trends, and credentials |
| Showcase validation | Prevent broken documentation and unsafe release assets |

## Risk-to-evidence matrix

| Risk | Protection |
|---|---|
| Frontend calls removed or renamed endpoint | API-sync tests and route contract checks |
| Raw enum appears in UI | Localization/display checks and manual language QA |
| Workspace A accesses Workspace B | Backend scope and authorization tests |
| Portal token accesses staff data | Credential-isolation tests |
| Staff token accesses portal-only data | Portal dependency tests |
| Role sees forbidden route/action | Backend permission tests and frontend permission guards |
| Migration graph becomes inconsistent | Alembic graph audit and one-head checks |
| Model metadata diverges from migrations | Database contract checks |
| Production starts with weak settings | Production configuration tests |
| Debug/docs exposed in production | Deployment/security contract tests |
| Public route accepts oversized abuse payload | Request-size middleware tests |
| Public auth/access is brute-forced | Rate-limit tests |
| Stripe webhook is delivered twice | Event idempotency tests |
| Message retry creates duplicate | Retry-safe message tests |
| Internal note appears in portal | Audience-schema and participant tests |
| Two staff overwrite workflow state | Optimistic version conflict tests |
| Staff presence is wrong across devices | Presence aggregation/lifecycle tests |
| Demo reset targets unsafe database | Reset safety tests and static contract |
| Demo dashboard/report is empty or flat | Seed validation targets |
| French/Arabic overflows | Responsive and localization manual QA |
| README references missing image | Showcase repository validation |
| Release contains secret | Source/showcase secret scanners |

## Backend quality pipeline

The backend GitHub Actions job starts PostgreSQL 16 and Redis 7 services, installs dependencies, and runs the unified quality runner.

The runner includes:

- secret scanner;
- Alembic migration audit;
- database metadata contract;
- Stripe environment smoke check;
- security contract;
- observability contract;
- deployment contract;
- API contract;
- demo-seed contract;
- documentation contract;
- backend QA contract;
- route authorization inspection;
- portal route inspection;
- smoke import/registration checks;
- pytest suite.

### Why static contracts exist

Some architectural failures are faster and clearer to detect statically than through a full runtime scenario.

Examples:

- a required middleware is removed;
- debug routes are no longer guarded;
- a migration creates multiple heads;
- a production Compose artifact disappears;
- a required portal route is not registered;
- the demo reset introduces a forbidden destructive operation.

Static contracts complement behavioral tests. They do not replace them.

## Frontend quality pipeline

The frontend GitHub Actions job runs on both the primary and active release branch.

It includes:

- secret scanning;
- `flutter pub get`;
- localization generation;
- `flutter analyze`;
- source and UI consistency checks;
- frontend/backend API-sync tests;
- uploaded compact failure logs.

Additional local runners group portal and full frontend tests so terminal output remains readable and raw logs are preserved under `build/test_logs`.

## Frontend test categories

### Models and repositories

Protect:

- response parsing;
- null/default handling;
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

Source-level tests are used where a stable headless rendering environment would be disproportionately expensive. They should be complemented over time by broader widget, golden, and integration coverage.

## Authorization test strategy

Authorization tests should cover both positive and negative access.

Minimum matrix:

| Actor | Allowed | Denied |
|---|---|---|
| Owner | Full workspace operations | Other workspace without membership |
| Manager | Broad operations | Owner-only billing/config where restricted |
| Trainer | Assigned/permitted schedule and clients | Unrelated conversations/admin controls |
| Receptionist | Front desk, supported bookings/check-ins/payments | Sensitive owner-only operations |
| Portal client | Own portal data | Other clients and all staff routes |
| Unauthenticated | Public routes | Staff and protected portal data |

## Demo-data validation

The deterministic demo validator checks more than row counts.

It validates:

- workspace identity;
- user and role relationships;
- active/archive client totals;
- membership states;
- service states;
- booking lifecycle counts;
- check-in history;
- monthly revenue and pending payment totals;
- notification counts;
- presence sessions;
- portal settings and valid access links;
- external payment ID safety;
- report history and non-flat trends.

The rebuild is one transaction and commits only after validation.

## Manual QA matrix

### Product workflows

- register, verify, log in, log out, recover password;
- create/select workspace;
- client create/edit/archive/detail;
- plan and membership lifecycle;
- staff/invitation/availability;
- booking create/edit/cancel/recurrence/no-show;
- attendance and front-desk check-in/out;
- payment collection/cancel/refund/display;
- reports and CSV export;
- notifications and activity logs;
- messaging assignment, notes, replies, conflicts;
- client portal access and isolation.

### Screen sizes

- 1440 desktop;
- 1280 laptop;
- 1024 compressed desktop;
- 768 tablet portrait/landscape;
- 430, 390, 375, and 360 mobile widths.

### Languages

- English;
- French with long copy;
- Arabic with RTL direction and alignment.

### Failure states

- backend unavailable;
- unauthorized/forbidden;
- expired session;
- empty workspace;
- no data;
- invalid form;
- rate limit;
- provider cancel/error;
- stale messaging workflow version;
- invalid/expired portal code.

## Release evidence

A final showcase release should record:

- frontend commit and branch;
- backend commit and branch;
- Alembic head;
- demo validation result;
- CI run links/status;
- Flutter, Dart, Python, PostgreSQL, and Redis versions;
- build date;
- artifact checksums;
- known limitations.

See [Build Manifest](../BUILD_MANIFEST.md).

## Quality gates by environment

| Environment | Minimum gate |
|---|---|
| Development | Targeted tests, Flutter analyze, relevant contract checks |
| Pull request | Full repository CI for changed source repository |
| Demo | CI green, deterministic rebuild, validator green, full route rehearsal |
| Production package | CI green, production settings tests, image build, migration check |
| Production launch | Provider E2E, deployed isolation tests, monitoring, backup/restore drill |

## Current evidence and honest gaps

Strong current evidence:

- backend and frontend CI;
- broad contract checks;
- route and token isolation tests;
- deterministic demo validation;
- extensive portal source/regression tests;
- manual multi-language and responsive QA process.

Areas that would strengthen a commercial production program:

- automated accessibility audits;
- browser/device matrix automation;
- performance budgets and load tests;
- database query-plan regression review;
- container/dependency vulnerability scanning;
- signed provenance and SBOM attachment;
- scheduled backup restore drills;
- hosted synthetic monitoring.

These are tracked as production/release work rather than presented as already completed.

## Showcase repository quality

The public showcase workflow checks:

- required documentation exists;
- local Markdown links resolve;
- referenced assets exist;
- no environment/database dump/private key file is committed;
- stale demo credentials are not reintroduced;
- common API key and private-key patterns are absent;
- the build manifest and capture guides remain present.

This protects the portfolio surface itself, not only the application code.
