# GymFlow Quality Strategy

GymFlow uses layered automated checks and manual product review. The objective is not to maximize a test-count number; it is to protect the risks that could make a multi-surface SaaS unreliable, unsafe, misleading, or difficult to operate.

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
| Presence is incorrect across devices | Heartbeat and activity aggregation tests |
| Demo reset targets unsafe data | Environment, host, name, allowlist, and confirmation guards |
| French or Arabic layout regresses | Responsive and localization review |
| Public repository leaks a secret | Source and showcase secret checks |
| Screenshot inventory drifts | Exact filenames, dimensions, uniqueness, and full SHA-256 approval |
| Release wording contradicts tag state | Stable current/previous release schema and document contracts |
| Local cache causes a false release failure | Tracked-file discovery and regression tests |
| Release tag misrepresents evidence | Previous-tag verification plus clean-HEAD current-tag verification |

## Application validation

The private backend quality path is designed around PostgreSQL, Redis, migrations, provider configuration, security contracts, route authorization, deterministic demo safeguards, application import checks, and behavior tests.

The private frontend quality path covers localization generation, static analysis, source and UI contracts, frontend/backend API synchronization, portal privacy, responsive navigation, Flutter tests, and a release web build.

The showcase does not claim that private-source checks are independently reproducible from this repository. It records their canonical revisions and the validation boundary honestly.

## Authorization strategy

Authorization evidence includes successful and denied access.

| Actor | Allowed | Denied |
|---|---|---|
| Owner | Full workspace operations | Another workspace without membership |
| Manager | Broad operations | Owner-only billing and ownership controls |
| Trainer | Assigned or permitted schedules and clients | Unrelated conversations and administration |
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

The reset, seed, and validation run inside one transaction and commit only after every invariant passes.

## Manual product review

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
- empty workspace or data;
- invalid forms and rate limits;
- provider cancellation or error;
- stale messaging workflow version.

## Showcase release validation

The `v1.0.3-showcase` release record uses a traditional local gate. The previous immutable release is `v1.0.2-showcase`.

### PowerShell

```powershell
.\scripts\validate_release.ps1
.\scripts\validate_release.ps1 -Release
```

### POSIX shell

```bash
bash scripts/validate_release.sh
bash scripts/validate_release.sh --release
```

The combined gate runs:

1. validator regression tests;
2. base repository and media validation;
3. release-record provenance validation;
4. optional current-tag and clean-worktree verification.

The validator inspects tracked Git content rather than every transient local file. This preserves strict repository hygiene without allowing an untracked `__pycache__` directory to create a false release defect.

## Validator regression tests

The validation tooling is tested for:

- tracked-file discovery and exclusion of untracked bytecode;
- stale release wording in active public documentation;
- safe preservation of historical release wording;
- safe use of detection literals inside validator source;
- machine-readable manifest correctness and source drift;
- malformed nested manifest handling;
- complete 53-file SHA-256 approval;
- previous-tag immutability;
- pre-tag record mode;
- current-tag alignment and clean working-tree enforcement;
- full repository base validation.

## Media validation

The gallery contract checks:

- the exact 53 approved paths;
- supported file formats;
- readable dimensions and expected orientation;
- 53 unique content hashes;
- 53 exact SHA-256 approvals;
- known rejected media hashes;
- common text-secret and JWT-like patterns;
- local Markdown links and repository-root containment;
- the absence of undeclared video assets.

Binary checks do not replace human review. Every screenshot still requires inspection for visible credentials, local paths, browser overlays, private data, broken localization, misleading state, and non-identical visual duplication.

## Release evidence model

The machine-readable [`release/evidence-manifest.json`](../release/evidence-manifest.json) is the central public record for:

- current and previous release identities;
- canonical frontend and backend commits;
- Alembic head;
- evidence date;
- gallery inventory, counts, and exact hashes;
- validation commands;
- included and omitted artifacts;
- data, payment, and production boundaries.

The validator has a small explicit trust root for the expected current release, previous immutable release, canonical source commits, and Alembic head. Human-readable documents are checked against the manifest.

## Hosted-runner boundary

GitHub Actions are not used as release evidence for this showcase line. The prior workflow was removed because hosted execution was unavailable and its bytecode compile step conflicted with the following generated-file check.

The repository therefore makes **no green hosted-CI claim**. The reviewed local gate is the explicit release authority.

## Tag rule

`v1.0.3-showcase` may point to a commit only after:

1. validator tests pass;
2. all 53 declared images are present, unique, and match exact approved hashes;
3. no blocked media is detected;
4. source provenance remains `b73a623c3985e4bc458d04b4b484887ada593fa5` and `2234af20d1d9dd143bcac22edc699d3ee7fe515f`;
5. the record receives manual privacy and visual review;
6. the working tree is clean;
7. the tag points to the reviewed commit;
8. release-mode validation passes.

Commercial production assurance would additionally benefit from accessibility automation, browser/device matrix execution, performance budgets, load and query analysis, dependency/container scanning, SBOM and signed provenance, backup restore drills, and hosted synthetic monitoring.
