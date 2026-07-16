# GymFlow Demo Environment

GymFlow includes a deterministic professional demo built around **Northline
Performance Club**, a fictional Montréal gym. The environment exists to make
product review repeatable while keeping development data, production data, and
real payment activity outside the demonstration boundary.

## Environment profile

| Item | Value |
|---|---|
| Workspace | Northline Performance Club |
| Database | `gymflow_demo` |
| Runtime environment | `demo` |
| Payments | Manual, simulated, or Stripe test-mode records only |
| Identities | Reserved `.test` addresses |
| Real client data | None |
| Real payment data | None |

## Deterministic scenario

A validated rebuild produces the same connected business story:

| Data area | Expected state |
|---|---|
| Staff | 1 owner, 1 manager, 3 trainers, 2 reception staff |
| Presence | Online, away, and offline examples |
| Invitations | 1 pending trainer invitation |
| Clients | 24 total: 20 active and 4 archived |
| Plans | 5 total, 4 active |
| Services | 7 total, 6 active |
| Memberships | 18 active plus pending, expired, and cancelled history |
| Bookings | 72 total across scheduled, completed, cancelled, and no-show states |
| Check-ins | 58 recent, including 4 today |
| Revenue | Six months of non-flat history; 3,402.00 CAD current-month target |
| Pending payments | 377.00 CAD target |
| Notifications | Staff and client examples; 6 unread for the owner |
| Messaging | One professional support workflow |
| Client portal | Two connected client stories |

## Safety contract

The destructive rebuild is intentionally narrow. Execution is refused unless:

1. `ENVIRONMENT=demo`;
2. the database name is `gymflow_demo` or another explicitly approved `_demo`
   name;
3. the database host is local or the Docker `postgres` service;
4. Stripe is in test mode;
5. no live Stripe secret is loaded;
6. no stored live Stripe webhook event exists;
7. every application table belongs to the reviewed allowlist;
8. the exact destructive confirmation value is supplied.

The rebuild does not drop schemas or tables, roll migrations backward, run
`TRUNCATE ... CASCADE`, clear unknown tables dynamically, modify
`alembic_version`, flush Redis globally, or create a live Stripe charge.

## Reproducible local execution

The standard Docker stack supports both the normal development database and the
dedicated demo database through one approved selector.

```dotenv
GYMFLOW_DATABASE=gymflow_demo
```

```powershell
docker compose up --build -d
```

A read-only rebuild plan is available without destructive execution:

```powershell
docker compose exec backend sh scripts/run_local_command.sh \
  python scripts/seed_demo_data.py --rebuild
```

The confirmed rebuild uses values supplied only to the command invocation:

```powershell
docker compose exec `
  -e GYMFLOW_DEMO_RESET_CONFIRM=RESET_GYMFLOW_DEMO `
  -e GYMFLOW_DEMO_PASSWORD=Choose-A-Local-Demo-Password `
  backend sh scripts/run_local_command.sh `
  python scripts/seed_demo_data.py --rebuild --execute
```

The operation runs as one transaction:

1. verify environment, host, database, Stripe mode, migration state, and table
   allowlist;
2. acquire a PostgreSQL advisory transaction lock;
3. delete reviewed application data in foreign-key-safe order;
4. create the complete connected scenario;
5. validate metrics, relationships, reports, payments, presence, and portal
   stories;
6. commit only after every validation succeeds.

Any failure rolls the transaction back.

## Validation

Human-readable validation:

```powershell
docker compose exec backend sh scripts/run_local_command.sh \
  python scripts/validate_demo_data.py
```

Machine-readable validation:

```powershell
docker compose exec backend sh scripts/run_local_command.sh \
  python scripts/validate_demo_data.py --json
```

Core targets include:

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

## Fictional identities

The rebuild prints a password-independent account manifest. Stable staff
identities include:

```text
owner@gymflow-demo.test
manager@gymflow-demo.test
sofia.trainer@gymflow-demo.test
reception@gymflow-demo.test
```

All seeded staff accounts use the password supplied for that rebuild. No
permanent demo password is published in this repository.

## Client portal stories

### Lena Martin

```text
lena.martin@gymflow-demo.test
```

Lena represents a healthy member relationship with a valid membership,
successful payments, attendance history, future bookings, receipts, progress,
and a complete portal experience.

### Amina Haddad

```text
amina.haddad@gymflow-demo.test
```

Amina represents a member who needs operational attention: an expiring
membership, failed payment, pending renewal, cancellation and no-show history,
and meaningful staff follow-up.

Portal codes expire after 15 minutes. In guarded demo mode, codes for reserved
`.test` identities can be returned to the frontend and filled into the access
form. Production never exposes those codes.

## Product review coverage

The deterministic environment supports review of:

- owner dashboard totals and activity;
- client lifecycle, memberships, payments, and portal access;
- staff roles, trainer availability, invitations, and presence;
- booking lifecycle, recurrence, cancellation, and no-show behavior;
- daily attendance and front-desk check-in workflows;
- reports with non-flat historical data;
- professional messaging, notifications, and audit history;
- client portal isolation and self-service;
- desktop, mobile, French, and Arabic/RTL presentation.

The current visual evidence is available in the
[GymFlow Visual Gallery](screenshots/README.md). The exact source revisions and
release boundaries are recorded in the [Build Manifest](BUILD_MANIFEST.md).
