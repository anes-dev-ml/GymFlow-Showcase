# GymFlow Demo Guide

This guide defines the canonical professional demo flow for GymFlow.

The demo uses a dedicated, deterministic PostgreSQL database and fictional identities. It is designed for repeatable product review, screenshot capture, and video recording without touching normal development data or processing real money.

## Demo environment

| Item | Value |
|---|---|
| Workspace | Northline Performance Club |
| Database | `gymflow_demo` |
| Environment | `demo` |
| Payments | Manual/test records; Stripe test or Connect demo mode only |
| Email identities | Reserved `.test` addresses |
| Real client data | None |
| Real payment data | None |

## Scenario summary

A successful rebuild creates:

| Data area | Expected story |
|---|---|
| Staff | 1 owner, 1 manager, 3 trainers, 2 reception staff |
| Presence | Online, away, and offline examples |
| Invitations | 1 pending trainer invitation |
| Clients | 24 total: 20 active and 4 archived |
| Plans | 5 total, 4 active |
| Services | 7 total, 6 active |
| Memberships | 18 active plus pending/expired/cancelled history |
| Bookings | 72 total: scheduled, completed, cancelled, no-show |
| Check-ins | 58 recent, including 4 today |
| Revenue | Six months of non-flat history; 3,402.00 CAD current month target |
| Pending payments | 377.00 CAD target |
| Notifications | Staff/client examples; 6 unread for owner |
| Messaging | One professional support workflow |
| Client portal | Two connected client stories |

## Safety contract

The destructive rebuild refuses to execute unless all of these are true:

1. `ENVIRONMENT=demo`;
2. database name is `gymflow_demo` or an approved `_demo` name;
3. database host is local or the Docker `postgres` service;
4. Stripe mode is `test`;
5. no live Stripe secret is loaded;
6. no stored live Stripe webhook event exists;
7. every application table belongs to the reviewed allowlist;
8. the exact confirmation value is supplied.

The rebuild never:

- drops tables;
- drops schemas;
- rolls migrations backward;
- runs `TRUNCATE ... CASCADE`;
- clears unknown tables dynamically;
- changes `alembic_version`;
- flushes Redis globally;
- creates a live Stripe charge.

## Select the demo database

In the backend `.env`:

```dotenv
GYMFLOW_DATABASE=gymflow_demo
```

Start the stack:

```powershell
docker compose up --build -d
```

The same stack can return to normal development data by changing only:

```dotenv
GYMFLOW_DATABASE=gymflow
```

and running the same Compose command.

## Inspect before changing data

Read-only reset inspection:

```powershell
docker compose exec backend sh scripts/run_local_command.sh python scripts/reset_demo_data.py
```

Read-only complete rebuild plan:

```powershell
docker compose exec backend sh scripts/run_local_command.sh python scripts/seed_demo_data.py --rebuild
```

Without `--execute`, these commands do not delete or create data.

## Rebuild the canonical scenario

Supply the confirmation and password only to the explicit command. Do not store them in `.env`.

```powershell
docker compose exec `
  -e GYMFLOW_DEMO_RESET_CONFIRM=RESET_GYMFLOW_DEMO `
  -e GYMFLOW_DEMO_PASSWORD=Choose-A-Local-Demo-Password `
  backend sh scripts/run_local_command.sh `
  python scripts/seed_demo_data.py --rebuild --execute
```

The seed performs one transaction:

1. verify environment, host, database, Stripe mode, migration state, and table allowlist;
2. acquire a PostgreSQL advisory transaction lock;
3. delete reviewed application data in foreign-key-safe order;
4. create the complete connected scenario;
5. validate metrics, relationships, reports, payments, presence, and portal stories;
6. commit only after all validation succeeds.

Any failure rolls the transaction back.

## Validate the environment

```powershell
docker compose exec backend sh scripts/run_local_command.sh python scripts/validate_demo_data.py
```

Machine-readable output:

```powershell
docker compose exec backend sh scripts/run_local_command.sh python scripts/validate_demo_data.py --json
```

Expected core metrics:

| Metric | Expected |
|---|---:|
| Total clients | 24 |
| Active clients | 20 |
| Archived clients | 4 |
| Staff | 7 |
| Active memberships | 18 |
| Active plans | 4 |
| Active services | 6 |
| Total bookings | 72 |
| Today's bookings | 5 |
| Recent check-ins | 58 |
| Today's check-ins | 4 |
| Current-month revenue | 340,200 cents |
| Pending payments | 37,700 cents |
| Owner unread notifications | 6 |

## Demo identities

The rebuild prints the password-independent account manifest. Stable staff emails include:

```text
owner@gymflow-demo.test
manager@gymflow-demo.test
sofia.trainer@gymflow-demo.test
reception@gymflow-demo.test
```

All seeded staff accounts use the password supplied through `GYMFLOW_DEMO_PASSWORD` for that rebuild.

Do not publish a permanent password in this repository. The person preparing a temporary demo should choose a local password and share it only through the intended review channel.

## Client portal stories

### Lena Martin

```text
lena.martin@gymflow-demo.test
```

Lena demonstrates:

- valid membership;
- recent successful payments;
- attendance history;
- future bookings;
- receipts and progress;
- complete healthy-client portal experience.

### Amina Haddad

```text
amina.haddad@gymflow-demo.test
```

Amina demonstrates:

- expiring membership;
- failed payment;
- pending renewal;
- cancellation and no-show history;
- meaningful staff follow-up.

Portal codes expire after 15 minutes. Request fresh codes immediately before recording portal access.

In guarded demo mode, codes for reserved `.test` identities are returned to the frontend and filled into the portal form. Production never exposes those codes.

## Full pre-recording checklist

### Backend and data

- [ ] Backend branch/commit matches `BUILD_MANIFEST.md`.
- [ ] `GYMFLOW_DATABASE=gymflow_demo`.
- [ ] `docker compose up --build -d` completed.
- [ ] Full guarded rebuild completed.
- [ ] Demo validator passed.
- [ ] Backend logs show `environment=demo` and `database=gymflow_demo`.
- [ ] No repeated 404, 422, or 500 responses during rehearsal.

### Staff application

- [ ] Owner login succeeds.
- [ ] Workspace is Northline Performance Club.
- [ ] Dashboard values match expected targets.
- [ ] Client list and client detail load.
- [ ] Plans and services load.
- [ ] Staff presence shows online, away, and offline examples.
- [ ] Bookings include all important lifecycle states.
- [ ] Check-ins and attendance load.
- [ ] Payments show paid, pending, failed, refunded, and cancelled examples.
- [ ] Reports contain non-flat charts.
- [ ] Messages, notifications, and activity logs load.
- [ ] Settings and billing states are credible.

### Client portal

- [ ] Request a fresh Lena code.
- [ ] Development/demo code appears and auto-fills.
- [ ] Portal opens without exposing staff navigation.
- [ ] Home, bookings, membership, payments, receipt, progress, pass, profile, settings, support, and messages load.
- [ ] Repeat with Amina if the video includes the at-risk client story.
- [ ] Portal token cannot open staff routes.

### Visual quality

- [ ] English desktop reviewed.
- [ ] French long-copy reviewed.
- [ ] Arabic RTL reviewed.
- [ ] Mobile widths reviewed.
- [ ] No overflow stripe, clipped dialog, loading hang, or empty chart.
- [ ] Browser console contains no serious repeated errors.
- [ ] Screens contain only fictional data.

### Provider safety

- [ ] No live Stripe key loaded.
- [ ] No real card entered.
- [ ] No real identity verification attempted.
- [ ] Email remains disabled or intentionally configured.
- [ ] OAuth is shown only if configured for the exact demo environment.

## Recommended product video order

| Time | Area | Story |
|---|---|---|
| 0:00–0:20 | Title/public home | What GymFlow solves |
| 0:20–0:45 | Public features/security/pricing | Product completeness |
| 0:45–1:05 | Authentication | Staff versus client access |
| 1:05–1:40 | Dashboard | Business and operational overview |
| 1:40–2:20 | Clients/client detail | Connected domain depth |
| 2:20–2:55 | Staff/presence | Roles and real-time status |
| 2:55–3:35 | Bookings/check-ins | Scheduling and physical operations |
| 3:35–4:10 | Payments/reports | Financial lifecycle and analytics |
| 4:10–4:45 | Messaging/notifications | Collaboration and auditability |
| 4:45–5:45 | Client portal | Separate trust domain and self-service |
| 5:45–6:15 | Mobile/Arabic | Responsive and international product |
| 6:15–6:40 | Architecture/quality close | Engineering summary |

## Recommended engineering video order

1. System context and trust boundaries.
2. Workspace and role model.
3. Staff JWT versus portal token.
4. Domain model and migrations.
5. Booking and recurring scheduling.
6. Payment/webhook idempotency.
7. Messaging audience safety and optimistic concurrency.
8. Staff presence design.
9. Request IDs, structured logs, liveness/readiness.
10. CI and contract checks.
11. Docker environment selector.
12. Guarded demo reset and validation.
13. Production boundary and remaining operational verification.

## After recording

- update screenshot and video files according to their capture guides;
- update `BUILD_MANIFEST.md` with final artifact names and checksums;
- update `CHANGELOG.md` and release notes;
- run showcase quality checks;
- create the tagged GitHub release.
