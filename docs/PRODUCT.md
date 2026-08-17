# GymFlow Product Model

GymFlow is a gym and fitness-studio operations platform designed as one connected SaaS product rather than a collection of unrelated CRUD pages.

## Product surfaces

| Surface | Primary users | Purpose |
|---|---|---|
| Public website | Prospective studios and visitors | Product discovery, pricing, security, contact, legal information |
| Studio application | Owner, manager, trainer, receptionist | Daily business and operational workflows |
| Client portal | Gym clients | Private self-service without staff/admin access |

## Users and jobs to be done

### Owner

The owner can:

- create and select workspaces;
- understand business performance;
- manage staff and roles;
- configure memberships and services;
- oversee clients, bookings, attendance, and payments;
- manage GymFlow billing and provider configuration;
- review reports and audit history.

### Manager

The manager has broad studio control while remaining separate from account ownership and sensitive SaaS billing responsibilities.

### Trainer

The trainer can:

- publish availability;
- see assigned bookings;
- manage relevant attendance;
- communicate with permitted clients and staff;
- understand current online/away presence where policy allows.

### Receptionist

Reception staff have fast front-desk access to:

- clients;
- bookings;
- check-ins;
- payments;
- membership status;
- support and operational communication.

### Client

The client receives a private experience for:

- upcoming and historical bookings;
- membership status and benefits;
- payments and receipts;
- progress and check-in pass;
- profile and preferences;
- support and messaging.

## Product areas

### Public website

- home and product positioning;
- features;
- pricing;
- security;
- contact/support;
- privacy and terms;
- language switching.

### Authentication and onboarding

- registration;
- email/password login;
- Google OAuth handoff;
- email verification;
- forgot/reset password;
- workspace creation and selection;
- staff invitation acceptance;
- session-expiry handling.

### Dashboard

- active client and membership totals;
- current revenue and pending payment signals;
- today's bookings and check-ins;
- recent operational activity;
- trend and summary widgets;
- onboarding progress based on real workspace setup state.

### Clients

- create, edit, search, filter, activate/deactivate/archive;
- client detail command center;
- memberships, bookings, payments, check-ins;
- portal access actions;
- meaningful active/new/archived states.

### Memberships

- membership plan creation and management;
- activation/deactivation;
- membership assignment;
- pending, active, expiring, expired, cancelled, and historical states;
- renewal and payment context.

### Services

- bookable service types;
- duration and pricing context;
- trainer-required and active/inactive behavior;
- use across staff and portal booking flows.

### Staff

- owner, manager, trainer, receptionist;
- staff profile and lifecycle;
- invitations;
- trainer availability;
- presence and last-seen visibility;
- role-aware operations.

### Bookings

- staff-created bookings;
- portal booking;
- trainer availability validation;
- service-duration handling;
- recurring series;
- cancellation and future-series cancellation;
- scheduled, completed, cancelled, and no-show states;
- calendar and operational views.

### Attendance and check-ins

- daily attendance sheet;
- saved present/absent state;
- front-desk check-in and check-out;
- check-in history;
- portal check-in pass and QR direction.

### Payments

- client payment ledger;
- manual/offline collection;
- Stripe test checkout;
- paid, pending, failed, cancelled, and refunded states;
- client-safe receipts;
- payment actions and history.

### SaaS billing

- workspace subscription state;
- plan selection;
- billing portal/checkout foundation;
- test/live provider separation;
- Stripe Connect-aware demonstration boundary.

### Reports

- date filters;
- grouping and comparative trends;
- revenue, client, booking, and attendance stories;
- CSV export;
- non-flat seeded history for meaningful demonstration.

### Notifications and audit history

- read/unread and grouped notifications;
- operational activity logs;
- human-readable event labels;
- workspace and user context.

### Messaging

- staff/client conversations;
- assignment and queue workflow;
- priorities and statuses;
- staff-only internal notes;
- client-visible messages;
- retry-safe send behavior;
- pagination and workflow conflict handling.

### Client portal

- one-time access request and confirmation;
- dashboard and next actions;
- bookings;
- membership;
- payments and receipts;
- progress;
- check-in pass;
- profile and settings;
- support;
- messaging;
- responsive mobile-first navigation.

## Connected workflow examples

### New client onboarding

```text
Create client
→ assign membership
→ record/collect payment
→ schedule first booking
→ issue portal access
→ client receives dashboard and check-in pass
```

### Trainer scheduling

```text
Trainer publishes availability
→ service requires trainer
→ staff/client selects slot
→ API validates conflicts and duration
→ booking is created
→ trainer and client see the result
```

### Front-desk visit

```text
Reception finds client
→ checks membership state
→ checks client in
→ attendance is persisted
→ dashboard/report totals update
→ activity history records the operation
```

### Client support conversation

```text
Client opens support conversation
→ conversation enters staff workflow
→ authorized staff claims/assigns it
→ internal note remains staff-only
→ client receives audience-safe reply
```

### Payment lifecycle

```text
Pending obligation
→ manual or Stripe collection
→ provider/webhook result
→ payment state update
→ receipt available in portal
→ dashboard and reports reflect outcome
```

## Demo scenario

The deterministic scenario is built around **Northline Performance Club**, a fictional Montréal gym.

It includes a useful mix of everyday and edge-case operational states:

- highly active and newly joined clients;
- archived/inactive clients;
- active, expiring, expired, pending, and cancelled memberships;
- upcoming, completed, cancelled, and no-show bookings;
- online, away, and offline staff;
- paid, pending, failed, refunded, and cancelled payments;
- unread notifications and audit history;
- a professional support conversation;
- two client portal stories.

### Lena Martin

Lena represents a healthy client relationship:

- valid membership;
- recent successful payments;
- attendance history;
- future bookings;
- receipts and progress;
- full portal experience.

### Amina Haddad

Amina represents a client who needs operational attention:

- expiring membership;
- failed payment;
- pending renewal;
- cancellation and no-show history;
- useful staff follow-up context.

## Product principles

### Connected data over decorative dashboards

Dashboard cards and report charts are backed by seeded business records and API aggregation rather than static mock values.

### Role-appropriate complexity

Owners see broad administration. Trainers and receptionists see the workflows relevant to them. Clients use a separate self-service portal rather than entering the staff application.

### Clear provider boundaries

Provider-dependent behavior is separated from core product logic. Test payments, demo state, and production provider configuration are represented distinctly so the same architecture can move between environments cleanly.

### Safe defaults

Sensitive actions require explicit confirmation, protected routes fail closed, public identity flows avoid enumeration, and the demo rebuild stays within approved targets.

### International and responsive design

The same product remains understandable in English, French, and Arabic across desktop, tablet, and mobile layouts.

## Product stage

GymFlow is complete as a controlled professional demonstration and production-oriented SaaS implementation. Its product flows, architecture, configuration, and deployment artifacts are in place; commercial operation would add target hosting, verified provider accounts, monitoring, backup and restore processes, and the legal/support responsibilities of the chosen deployment.
