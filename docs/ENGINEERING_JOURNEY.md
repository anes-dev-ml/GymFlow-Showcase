# GymFlow Engineering Journey

GymFlow began as a portfolio goal: build one application broad enough to demonstrate real software engineering, not only isolated framework exercises.

This document explains how the system evolved, which problems changed the architecture, and what was learned during stabilization.

## 1. Initial goal

The original objective was to create a credible full-stack gym management application with:

- a Flutter frontend;
- a FastAPI backend;
- PostgreSQL persistence;
- authentication;
- clients, plans, bookings, attendance, and payments;
- a polished product presentation.

The important constraint was that the result had to feel like one product. A collection of disconnected screens would not demonstrate system design or operational depth.

## 2. Moving from screens to a domain model

Early implementation naturally began with visible areas such as clients, plans, staff, and bookings.

The project became more serious when those screens were treated as relationships:

- clients receive memberships;
- memberships reference plans;
- bookings connect clients, services, and trainers;
- trainers publish availability;
- check-ins record physical attendance;
- payments connect to clients and membership context;
- reports aggregate the same operational data.

This changed the work from “build a page” to “preserve business invariants across UI, API, and database.”

## 3. Choosing a workspace-based SaaS boundary

A gym-management product needs a tenant model.

The workspace became the ownership boundary for business data. Users join workspaces through membership records, and roles belong to those memberships.

Why this mattered:

- one user can belong to multiple studios;
- roles can differ by studio;
- business queries have an explicit tenant scope;
- authorization is more meaningful than one global `admin` flag.

The cost is discipline: every route and query must preserve workspace scope.

## 4. Separating the client portal

One of the most important product and security decisions was not to treat clients as lower-privilege dashboard users.

Clients need a different experience:

- simpler navigation;
- only their own information;
- client-safe receipts and messages;
- no staff tools or workspace selection;
- a different access mechanism.

GymFlow therefore developed a separate portal route surface and token model.

This created additional complexity—two session types, two route families, and audience-specific schemas—but produced a safer and more believable product.

## 5. Authentication becoming a system

Authentication expanded beyond login:

- registration;
- verification;
- password recovery;
- Google OAuth;
- staff invitations;
- client one-time portal access;
- session-expiry recovery.

Each flow introduced different trust and failure conditions.

A key lesson was that identity-sensitive public routes must not reveal whether a user or client exists. Neutral responses, rate limits, expiry, one-time use, and environment-specific demo behavior became part of the design.

## 6. Frontend architecture under product growth

As product scope grew, large pages and duplicated UI patterns became harder to maintain.

The frontend moved toward feature slices:

- data models and repositories;
- controllers/coordinators;
- pages and reusable widgets;
- targeted localization and tests.

The router also became an application boundary for:

- authentication;
- workspace selection;
- role permissions;
- portal session separation;
- billing gates;
- safe redirects.

## 7. Responsive Flutter engineering

A major stabilization challenge was layout behavior across:

- large desktop;
- compressed browser windows;
- tablet widths;
- mobile;
- long French text;
- Arabic RTL.

Problems included:

- horizontal `RenderFlex` overflow;
- cards with unused internal space;
- desktop assumptions at tablet widths;
- intrinsic-height layouts inside unbounded viewports;
- dialogs that fit one language but not another;
- navigation that covered content.

The solution was not one global breakpoint. Individual surfaces received explicit responsive tiers, flexible constraints, scroll behavior, and mobile-specific composition.

The lesson: responsive design is part of application architecture, not a final CSS-style patch.

## 8. Localization as product architecture

GymFlow supports English, French, and Arabic.

Localization work exposed several engineering concerns:

- hardcoded visible text;
- duplicated translation sources;
- broken encoding;
- raw backend enum values;
- RTL alignment and ordering;
- text expansion;
- date, money, and status display.

The project consolidated visible copy around Flutter localization and shared display helpers. Quality scripts were added to detect hardcoded or missing coverage.

## 9. Booking complexity

Bookings evolved from basic date records into a real scheduling workflow:

- service duration;
- trainer-required services;
- trainer availability;
- overlap and conflict handling;
- recurring series;
- cancellation of future occurrences;
- client portal booking;
- completed, cancelled, and no-show states.

The system had to keep the frontend, API, database, and reports synchronized. A no-show parsing/reporting regression near demo completion reinforced why API-sync tests and seeded report targets matter.

## 10. Attendance and physical operations

GymFlow needed to represent a physical gym, not only online subscriptions.

Two attendance ideas were separated:

- daily attendance sheet decisions;
- front-desk check-in/check-out visits.

The UI also had to preserve saved state, avoid resetting the current day unexpectedly, and provide readable history.

This area demonstrated that deceptively simple UX can hide important persistence semantics.

## 11. Payments and provider boundaries

Payments introduced two different domains:

- client-to-studio payments;
- studio-to-GymFlow SaaS billing.

The product supports manual collection and Stripe-oriented online flows. The engineering work included:

- provider/method labels;
- payment states;
- checkout return paths;
- receipts;
- Stripe webhook processing;
- duplicate-event protection;
- live/test configuration separation;
- Connect-aware demo behavior.

A key product decision was to keep the portfolio demonstration safe: no real money, no real card storage, and no reviewer identity-verification requirement.

## 12. From notifications to professional messaging

A simple notification list did not cover client support and staff collaboration.

Messaging grew into a professional workflow with:

- conversations and participants;
- staff assignment/claiming;
- priorities and statuses;
- client-visible replies;
- internal staff notes;
- retry-safe sends;
- optimistic concurrency;
- pagination;
- portal abuse limits.

The hardest part was not message display. It was audience safety and permission design.

The system had to guarantee that internal notes and operational metadata could not leak into client-facing responses.

## 13. Staff presence

“Online/offline” initially sounds like a boolean.

A correct implementation needed to answer:

- What if one person has multiple devices?
- What if the connection is alive but the user is inactive?
- Who is allowed to see last-seen information?
- How is an administrative reset different from natural timeout?

The final model separates connection heartbeat, user activity, aggregation, derived state, and visibility policy.

## 14. Observability after real failures

During integration, generic “network error” UI states were sometimes caused by backend response validation or dependent requests rather than an unavailable network.

This reinforced the need for:

- consistent API error envelopes;
- request IDs;
- structured access/error logs;
- liveness and readiness;
- provider-specific diagnostics.

A concrete example was the reserved `.test` email suffix. The deterministic user existed and the password was correct, but strict response validation caused a 500 in the staff endpoint. That single dependency then made staff, bookings, and messages pages appear offline.

The durable fix was not to hide the page error. It was to define the correct demo-compatible response validation while keeping new registration input strict.

## 15. Schema and migration discipline

As the model expanded, migration safety became critical.

The project added:

- Alembic graph checks;
- metadata contracts;
- separate migration execution;
- published-history preservation;
- tests around expected tables and routes.

The principle became: schema changes are release events, not invisible application side effects.

## 16. From manual demo setup to release engineering

A polished application can still fail a portfolio review if the database is empty, duplicated, or inconsistent.

The initial idea of “seed some demo data” became a guarded professional environment.

The final system:

- preserves the normal development database;
- uses a separate `gymflow_demo` database;
- has fixed fictional identities and relationships;
- creates meaningful edge cases and trends;
- refuses unsafe environment/host/name/Stripe combinations;
- uses an explicit table allowlist;
- deletes in dependency order;
- uses a PostgreSQL advisory lock;
- validates before commit;
- can run repeatedly without duplication.

This was a shift from feature engineering to release engineering.

## 17. Docker environment recovery

Local development initially relied on a familiar `docker compose up --build` workflow.

Adding a second database risked making local operation more confusing. The final approach introduced one safe selector:

```text
GYMFLOW_DATABASE=gymflow
GYMFLOW_DATABASE=gymflow_demo
```

The same Compose command works for both. Both databases remain in the shared PostgreSQL volume, and only approved names are accepted.

This preserved developer ergonomics without weakening safety.

## 18. Quality system evolution

Testing evolved in response to real failure classes.

The project added checks for:

- secrets;
- migrations;
- database metadata;
- security middleware;
- observability;
- deployment contracts;
- API routes;
- portal routes;
- frontend/backend synchronization;
- localization;
- portal privacy;
- demo reset/seed behavior.

The lesson was that a large application needs multiple forms of evidence. Unit tests alone do not catch missing routes, unsafe environment settings, stale documentation, or responsive overflow.

## 19. Stabilization and credibility

Late-stage work focused less on adding modules and more on removing reasons a reviewer might distrust the product:

- duplicated content;
- fake dashboard progress;
- empty reports;
- raw backend values;
- stale state after updates;
- error pages caused by one dependent API;
- weak demo credentials;
- hidden demo access codes;
- repeated failed presence calls;
- inconsistent responsive spacing.

This phase often creates less visible code than a new feature, but it is what turns a project into a credible product demonstration.

## 20. Major lessons

### A working feature is not finished until its failure states are understandable

The page, API, logs, and tests must tell the same story.

### Authorization is a data-access problem, not a navigation problem

Hiding a button is useful UX. Scoped backend queries and dependencies are the security boundary.

### Demo and production are different environments, not different marketing labels

A demo needs fictional data and safe shortcuts. Production needs stricter configuration, providers, monitoring, and operations.

### Cross-platform reduces duplication but does not remove platform differences

OAuth, camera, redirects, desktop packaging, and mobile navigation still need platform-aware handling.

### Database reset code deserves production-level caution

Anything that deletes data needs explicit scope, reviewed targets, transactionality, and validation—even when called a demo script.

### Documentation should explain decisions and evidence

A feature inventory shows breadth. Decisions, failure handling, trade-offs, and validation show engineering depth.

## 21. What remains outside the codebase

A live commercial launch still requires:

- selected hosting providers;
- managed PostgreSQL and Redis;
- real domains and TLS;
- verified Stripe, email, and OAuth configuration;
- monitoring and alerts;
- backup and restore drills;
- vulnerability scanning and supply-chain hardening;
- organization-specific privacy/legal operations.

These are not hidden. They are tracked in the roadmap and separated from implemented application architecture.

## 22. Final outcome

GymFlow now demonstrates more than framework familiarity.

It demonstrates the ability to:

- model a business domain;
- evolve architecture under product growth;
- diagnose cross-layer failures;
- design tenant and trust boundaries;
- secure public and authenticated workflows;
- handle provider and environment differences;
- build repeatable quality and release systems;
- communicate limitations honestly.
