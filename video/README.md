# GymFlow Video Release Procedure

## Current inventory

The `v1.0.0-showcase` engineering case-study candidate includes no public video URL, video binary, duration, thumbnail, captions file, or checksum. A local edited master is not public release evidence until those fields are recorded in `../BUILD_MANIFEST.md`.

For a later media-bearing release, GymFlow should be presented through two complementary videos:

1. a concise product walkthrough for recruiters, hiring managers, and general reviewers;
2. an optional technical walkthrough for engineers who want deeper architecture evidence.

## 1. Main product walkthrough

Recommended duration: **5 to 7 minutes**.

### Goal

Show that GymFlow is a coherent, polished SaaS product with realistic data and working flows. Do not turn the video into a page-by-page inventory.

### Storyboard

| Time | Scene | What to prove |
|---|---|---|
| 0:00–0:20 | Title and public home | Product identity and problem |
| 0:20–0:45 | Features, pricing, security | Complete public product surface |
| 0:45–1:05 | Authentication | Staff/client access separation |
| 1:05–1:40 | Owner dashboard | Business and operational visibility |
| 1:40–2:20 | Clients and client detail | Connected domain model |
| 2:20–2:55 | Staff and presence | Roles, online/away/offline states |
| 2:55–3:35 | Bookings and check-ins | Scheduling and physical operations |
| 3:35–4:10 | Payments and reports | Financial lifecycle and analytics |
| 4:10–4:45 | Messaging and audit | Professional collaboration |
| 4:45–5:45 | Client portal | Separate trust domain and self-service |
| 5:45–6:15 | Mobile, French, Arabic | Responsive and international product |
| 6:15–6:40 | Architecture/quality close | Engineering summary and ownership |

### Opening line

Suggested message:

> GymFlow is a multi-tenant gym operations SaaS I designed and built end to end with Flutter, FastAPI, PostgreSQL, Redis, Stripe, and Docker.

### Product narrative

Use one connected story:

1. Northline Performance Club owner reviews the day.
2. A client profile shows membership, bookings, attendance, and payments.
3. Staff availability and presence explain how the team operates.
4. Booking/check-in/payment/report flows show daily business depth.
5. Messaging shows client support and staff-only workflow.
6. Lena enters the separate client portal and sees only her information.

### Do not spend time on

- every settings field;
- long form-entry sequences;
- every public/legal page;
- raw database tables;
- terminal commands in the main product video;
- provider configuration screens that are not part of the product story.

### Required disclosure

Mention once, clearly:

- all identities are fictional;
- payment demonstrations use test/demo state;
- no real money is processed.

Do not repeat limitations after every payment screen.

## 2. Engineering walkthrough

Recommended duration: **8 to 12 minutes**.

### Goal

Explain the decisions that distinguish GymFlow from a visual prototype.

### Technical chapters

| Chapter | Evidence |
|---|---|
| System context | Public, staff, portal, API, data, providers |
| Multi-tenancy | Workspace membership and scoped business data |
| Trust boundaries | Staff JWT versus client portal token |
| Frontend architecture | Feature slices, repositories, controllers, router guards |
| Backend architecture | Versioned routes, schemas, services, repositories, middleware |
| Relational model | Clients, memberships, bookings, payments, messaging |
| Scheduling | Duration, trainer availability, recurrence, no-show |
| Payments | Client ledger, SaaS billing, webhook idempotency |
| Messaging | Internal notes, audience-safe schemas, retries, workflow versions |
| Presence | Connection, activity, multi-device aggregation, visibility |
| Security | Rate/body limits, CORS, trusted hosts, headers, neutral responses |
| Observability | Request IDs, structured logs, liveness/readiness |
| DevOps | CI, Docker, separate migration job, production settings |
| Demo engineering | Allowlisted transactional rebuild and validation |
| Production boundary | Provider and operational verification still required |

## 3. Capture preparation

Use the exact source snapshot in `../BUILD_MANIFEST.md`.

Before recording:

- rebuild and validate `gymflow_demo`;
- complete the route rehearsal in `../DEMO.md`;
- close unrelated applications and browser tabs;
- disable notifications;
- use one clean browser profile;
- verify audio and screen resolution;
- prepare fresh portal access;
- confirm no repeated serious API/browser errors;
- keep all terminal output free of credentials and personal paths.

## 4. Visual settings

Recommended:

- record at 1920×1080;
- keep browser zoom at 100%;
- use a readable cursor size;
- move the cursor intentionally and slowly;
- avoid rapid scrolling;
- pause briefly when a strong page loads;
- use consistent language, preferably English for the main story;
- switch briefly to French and Arabic near the end;
- show mobile through a real device/emulator or controlled responsive viewport.

## 5. Audio and script style

- Use short, direct sentences.
- Explain the business reason before the implementation detail.
- Avoid reading every label on screen.
- Avoid exaggerated claims.
- State personal ownership clearly: designed and implemented end to end.
- Use “implemented,” “verified,” “demo-assisted,” and “provider-dependent” precisely.

## 6. Suggested voiceover points

### Dashboard

> The owner dashboard is fed by the same booking, attendance, membership, and payment records used throughout the product. The seeded history is intentionally non-flat so the reports tell a real operational story.

### Client detail

> This client command center connects membership state, bookings, payments, visits, and portal access around one client record rather than duplicating data across screens.

### Staff presence

> Presence is derived from secure connection and activity signals, supports multiple devices, and applies role-aware visibility instead of using a simple manual online switch.

### Messaging

> Messaging separates client-visible replies from staff-only notes, restricts conversation access, and protects retries and concurrent workflow updates.

### Client portal

> Clients use a different token and route surface, so they can manage their own experience without becoming dashboard users or receiving administrative data.

### Demo engineering

> The recording environment is rebuilt from a guarded deterministic seed. It refuses production, remote databases, live Stripe state, unknown tables, and unconfirmed destructive execution.

## 7. Editing plan

- Cut loading delays and repeated navigation.
- Add chapter titles sparingly.
- Use subtle zooms only when a small detail matters.
- Add one architecture slide near the close.
- Add captions or subtitles.
- Normalize audio levels.
- Remove any frame containing credentials, codes, unrelated tabs, or private desktop content.
- End with the repository URL and concise stack summary.

## 8. Thumbnail specification

Required path after capture:

```text
video/gymflow-showcase-thumbnail.png
```

Recommended composition:

- GymFlow logo/name;
- owner dashboard crop;
- client portal/mobile crop;
- short title: `Full-Stack SaaS Engineering Case Study`;
- small stack line: `Flutter · FastAPI · PostgreSQL`;
- 16:9 layout.

Avoid dense feature lists on the thumbnail.

## 9. Video description template

```text
GymFlow is a multi-tenant gym operations SaaS built end to end with Flutter,
FastAPI, PostgreSQL, Redis, Stripe, and Docker.

This walkthrough covers the public product site, staff dashboard, client
lifecycle, bookings, attendance, payments, reporting, messaging, staff
presence, and the separate client portal.

All identities and business records are fictional. Payment flows use test/demo
state and do not process real money.

Architecture, security, quality, operations, and release documentation:
<showcase repository URL>

Release source snapshot:
Frontend: <commit>
Backend: <commit>
Showcase: <tag/commit>
```

## 10. Final review checklist

- [ ] The video matches the build manifest.
- [ ] No real identity or credential appears.
- [ ] No visible error/overflow/debug state remains.
- [ ] Test/demo payment boundary is stated.
- [ ] Staff and portal trust separation is explained.
- [ ] Messaging and presence are included.
- [ ] Mobile and Arabic are shown briefly.
- [ ] Audio is clear and captions are available.
- [ ] Repository URL and ownership are clear.
- [ ] Final URL, duration, and checksum/asset metadata are added to the manifest.
