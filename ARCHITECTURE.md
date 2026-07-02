# GymFlow Architecture

GymFlow is a full-stack SaaS gym management platform built around a multi-surface architecture:

- Public marketing website
- Owner/staff SaaS dashboard
- Client portal
- FastAPI backend
- PostgreSQL database
- Stripe test payment flows
- Email and OAuth provider integrations
- Automated quality and contract checks

The architecture demonstrates how a real SaaS product can be structured across frontend, backend, database, security, payments, localization, and release readiness.

---

## High-Level Architecture

| Layer | Technology | Responsibility |
|---|---|---|
| Public Client | Flutter Web | Landing pages, product positioning, public navigation |
| Admin/Staff App | Flutter Web, Android, Windows | Studio operations dashboard |
| Client Portal | Flutter Web and mobile layouts | Client-safe booking, membership, payment, and profile experience |
| Backend API | FastAPI | Business logic, authentication, authorization, route protection |
| Database | PostgreSQL | Persistent relational storage |
| ORM | SQLAlchemy | Database model mapping |
| Migrations | Alembic | Database schema versioning |
| Authentication | JWT | Protected dashboard and API access |
| OAuth | Google OAuth | External identity provider login |
| Payments | Stripe Test Mode | Checkout, billing, and demo-safe payment flows |
| Email | Transactional email provider support | Verification, password reset, portal access, staff invitations |
| QA | Python and Dart test/contract scripts | Demo readiness and regression protection |

---

## System Flow

Flutter Web, Android, and Windows clients communicate with the FastAPI backend through HTTP API calls.

The FastAPI backend applies authentication, authorization, workspace scoping, business rules, and provider logic.

The backend stores persistent data in PostgreSQL through SQLAlchemy models and Alembic migrations.

External integrations include Google OAuth, Stripe Test Mode, Stripe Connect demo mode, and email provider support.

---

## Application Surfaces

GymFlow is separated into three major user-facing surfaces.

| Surface | Description |
|---|---|
| Public Website | Marketing pages for visitors and product positioning |
| Owner/Staff Dashboard | Authenticated workspace dashboard for gym operations |
| Client Portal | Separate client-facing experience for bookings, membership, payments, and profile |

This separation is important because clients should not be treated as dashboard users.

A client can interact with their own data through the portal without accessing owner/staff routes.

---

## Frontend Architecture

The frontend is built with Flutter and Dart.

It is organized around feature areas instead of one large flat UI.

| Responsibility | Description |
|---|---|
| Routing | Handles public, auth, dashboard, settings, billing, and portal routes |
| State handling | Manages loading, empty, error, and ready states |
| API integration | Calls backend endpoints through service/repository layers |
| Localization | Uses Flutter localization and ARB files |
| Responsive UI | Adapts layouts across desktop, tablet, and mobile |
| Role-aware UX | Shows different navigation and actions depending on user context |
| Portal UX | Provides a client-safe experience separate from staff/admin dashboard |
| Payment redirects | Handles Stripe checkout and return flows |
| Demo polish | Provides stable demo-ready UI states for showcase recording |

---

## Frontend Route Groups

| Group | Example Routes |
|---|---|
| Public | Home, features, pricing, security, contact, privacy, terms |
| Auth | Login/register, forgot password, reset password, verify email |
| OAuth | Google OAuth callback |
| Invitation | Staff invitation acceptance |
| Dashboard | Dashboard, clients, client detail, membership plans, service types |
| Staff Operations | Staff, trainer availability, invitations |
| Scheduling | Bookings and recurring booking flows |
| Attendance | Check-ins and attendance sheet |
| Financial | Payments, billing settings, reports, CSV export |
| Communication | Notifications and activity logs |
| Settings | Account, workspace, billing, preferences |
| Client Portal | Portal access, home, bookings, membership, payments, receipts, profile, progress, support |

---

## Backend Architecture

The backend is built with FastAPI.

It provides protected REST APIs for dashboard users and separate portal APIs for clients.

| Responsibility | Description |
|---|---|
| Authentication | Login, registration, JWT handling, password recovery |
| Authorization | Role and workspace-aware access protection |
| Workspace isolation | Keeps studio data scoped to the correct workspace |
| Business logic | Clients, memberships, bookings, check-ins, payments, reports |
| Portal access | Client-safe access flow and portal-specific APIs |
| Provider integration | Google OAuth, Stripe, email provider support |
| Webhooks | Stripe webhook handling for payment/billing events |
| Health checks | Live/readiness endpoints for deployment checks |
| Contracts | API, route, auth, migration, security, and deployment checks |

---

## Backend Modules

| Module | Purpose |
|---|---|
| Auth | Login, registration, JWT, password reset, email verification |
| Google OAuth | OAuth provider handoff and login support |
| Workspaces | Studio workspace model |
| Workspace Members | Owner/staff membership inside a workspace |
| Staff Invitations | Invite staff into a workspace |
| Clients | Client records and profile data |
| Client Portal Access | Client portal request/confirm flows |
| Membership Plans | Studio membership plan management |
| Client Memberships | Membership assignment and tracking |
| Staff and Trainers | Staff records, roles, trainers |
| Trainer Availability | Scheduling availability constraints |
| Service Types | Bookable services/classes |
| Bookings | Booking lifecycle and recurring booking support |
| Check-ins | Daily attendance and front-desk check-in/out |
| Payments | Payment records and status tracking |
| SaaS Billing | Subscription-style billing configuration |
| Stripe Webhooks | Payment and billing synchronization |
| Reports | Business reporting and CSV export |
| Notifications | User notification records |
| Activity Logs | Operational audit history |
| Health / Readiness | Runtime and deployment health checks |

---

## Database Architecture

GymFlow uses PostgreSQL as the main database.

The schema is relational because the product has connected business entities.

| Relationship | Example |
|---|---|
| Workspace to clients | A studio owns many client records |
| Workspace to staff | A studio has owners, managers, trainers, receptionists |
| Client to memberships | A client can have membership assignments |
| Client to bookings | A client can book services or classes |
| Trainer to availability | Trainers have availability constraints |
| Service type to bookings | Bookings are based on services/classes |
| Client to payments | Payments are attached to client records |
| Payment to receipt | Client portal can show safe receipt data |
| Workspace to reports | Reports aggregate workspace-owned business data |
| User to activity logs | Operational changes can be recorded in audit history |

Alembic is used to version schema changes and keep database evolution controlled.

---

## Authentication Architecture

GymFlow supports several authentication and access flows.

| Flow | Purpose |
|---|---|
| Email/password login | Standard owner/staff authentication |
| JWT access tokens | API authorization after login |
| Google OAuth | External identity provider login |
| Email verification | Verify account ownership |
| Password reset | Recover user access |
| Staff invitation | Bring staff into a workspace |
| Client portal access | Let clients enter the portal without becoming staff users |

The important design choice is that client portal access is separate from staff dashboard access.

---

## Authorization Model

Authorization is based on user identity, workspace membership, role, route type, and resource ownership.

| Token Type | Allowed Area |
|---|---|
| Staff/admin JWT | Dashboard and workspace routes depending on role |
| Client portal token | Client portal routes only |
| Unauthenticated visitor | Public site and public auth flows only |

Expected access rule:

A user from Workspace A should not read or modify Workspace B data.

A client portal token should not access staff/admin dashboard APIs.

A staff dashboard token should not access private client portal `/portal/me` APIs.

---

## Role Model

| Role | Main Capabilities |
|---|---|
| Owner | Full workspace control, billing, staff, clients, bookings, settings |
| Manager | Operational management across the studio |
| Trainer | Schedule, availability, bookings, and attendance-related workflows |
| Receptionist | Front-desk client support, bookings, and check-ins |
| Client | Portal-only access to own bookings, membership, payments, and profile |

This role model allows GymFlow to demonstrate real SaaS access control instead of a simple single-user dashboard.

---

## Client Portal Architecture

The client portal is designed as a separate product area.

| Portal Page | Purpose |
|---|---|
| Portal Access | Request or confirm client access |
| Portal Home | Client-specific summary and next actions |
| Portal Bookings | Upcoming bookings, history, booking/cancel/reschedule flows |
| Portal Membership | Membership status, benefits, and pass-style information |
| Portal Payments | Pending and paid client payments |
| Receipt Detail | Safe payment receipt view |
| Portal Profile | Client profile data |
| Portal Progress | Client-facing progress/demo experience |
| Portal Support | Client-safe support path |
| QR Check-in Pass | Client check-in pass concept for front-desk workflows |

The portal exists so clients can use the system without entering the studio owner/staff dashboard.

---

## Booking Architecture

GymFlow booking logic connects several product areas.

| Entity | Booking Role |
|---|---|
| Client | Person booking or attending |
| Service Type | What is being booked |
| Trainer | Optional trainer assigned to the booking |
| Trainer Availability | Constraint for available slots |
| Membership | Can influence client access/status |
| Payment | Can be connected to booking-related charges |
| Portal | Lets clients book or manage supported bookings |

Booking flows include admin booking, client portal booking, cancellation, rescheduling, recurring booking concepts, and availability-aware slot selection.

---

## Check-in Architecture

GymFlow includes gym-specific attendance workflows.

| Feature | Purpose |
|---|---|
| Daily attendance sheet | Mark attendance for the day |
| Present/absent state | Quick operational tracking |
| Saved attendance records | Persist daily attendance decisions |
| Front-desk check-in/out | Reception workflow |
| QR check-in pass concept | Client-friendly check-in direction |

This shows that the app covers real physical gym operations, not only online subscription pages.

---

## Payment and Billing Architecture

GymFlow includes two payment-related layers.

| Layer | Purpose |
|---|---|
| Client payments | Payments between clients and the studio |
| SaaS billing | Billing/subscription concept for the studio using GymFlow |

Payment-related architecture includes:

| Feature | Description |
|---|---|
| Manual payment records | Admin/staff can track offline payments |
| Stripe checkout | Online payment test flow |
| Stripe webhook | Backend can receive payment events |
| Receipt display | Client-safe receipt information |
| Billing settings | Studio subscription and billing state |
| Stripe Connect demo mode | Demo-safe marketplace/studio payment routing concept |

For the showcase, Stripe runs in test/demo mode and does not process real money.

---

## Stripe Connect Demo Mode

Stripe Connect normally requires account onboarding and identity verification.

For a public showcase, that would create a bad demo experience.

GymFlow includes a demo-safe Connect mode so reviewers can see the billing/payment UI without uploading official identity documents.

| Production Concept | Showcase Behavior |
|---|---|
| Real connected account | Demo connected-account state |
| Identity verification | Skipped in demo mode |
| Real transfers | Not performed in demo mode |
| Platform fee | Demo-safe configuration only |
| Checkout | Stripe Test Mode checkout |

This keeps the demo realistic while avoiding real financial onboarding.

---

## Localization Architecture

The frontend supports English, French, and Arabic.

| Language | Code |
|---|---|
| English | en |
| French | fr |
| Arabic | ar |

Localization responsibilities include public copy, dashboard labels, portal copy, status display, RTL support, and long text handling.

The frontend avoids showing raw backend values such as `active`, `paid`, `manual`, `monthly`, or `trainer` directly in user-facing UI.

---

## API Contract and Quality Architecture

GymFlow uses quality gates to protect the project from regressions.

Backend quality checks cover:

| Check | Purpose |
|---|---|
| Secret scanner | Prevent accidental secret commits |
| Migration checks | Validate Alembic migration health |
| DB contract checks | Validate model/table expectations |
| Security contract checks | Validate security-sensitive rules |
| Observability contract checks | Validate request/debug behavior expectations |
| Deployment contract checks | Validate production configuration assumptions |
| API contract checks | Validate critical route and OpenAPI behavior |
| Route auth checks | Inspect protected route behavior |
| Portal route checks | Validate client portal route surface |
| Smoke check | Confirm app imports and routes register |
| Pytest | Backend behavior tests |

Frontend quality checks cover:

| Check | Purpose |
|---|---|
| Flutter analyze | Dart/Flutter static analysis |
| Frontend quality runner | Source and UI consistency checks |
| API sync tests | Frontend/backend contract alignment |
| Portal quality runner | Portal privacy, layout, and safety checks |
| Frontend full test runner | Grouped frontend test execution |
| Manual QA checklist | End-to-end product verification |

---

## Manual QA Scope

The manual QA checklist covers public site, auth, onboarding, admin dashboard, clients, memberships, services, staff, bookings, check-ins, payments, reports, notifications, activity logs, settings, client portal, security behavior, provider flows, responsive layouts, localization, and final demo readiness.

---

## Deployment Model

GymFlow can be demonstrated in several modes.

| Mode | Description |
|---|---|
| Local Demo | Backend, database, and frontend run locally |
| Temporary Hosted Demo | Backend/frontend can be hosted for a review window |
| Recorded Demo | Video walkthrough demonstrates main workflows |
| Screenshot Showcase | Static visuals show the product clearly |
| APK Build | Android installable demo artifact |
| Windows Build | Windows desktop demo artifact |

For the final portfolio-style release, the recommended strategy is screenshots plus video plus optional temporary hosted access.

---

## Production Readiness Boundary

GymFlow is strong as a showcase/demo project.

A production launch would require final verification of:

| Area | Required Before Production Claim |
|---|---|
| Hosting | Backend and frontend hosted with HTTPS |
| Database | Managed PostgreSQL with backups |
| Redis/rate limits | Production rate limiting configured |
| Stripe | Real Stripe mode and webhooks verified |
| Email | Verified sender domain and real inbox tests |
| OAuth | Production Google OAuth redirects verified |
| Monitoring | Logs, errors, uptime checks |
| Backups | Backup schedule and restore drill |
| Security | Final isolation and provider configuration tests |

The showcase should be honest: it proves engineering capability and product depth, while production deployment is a separate final operations phase.

---

## Engineering Summary

GymFlow demonstrates architecture across:

- Flutter multi-surface frontend
- FastAPI backend
- PostgreSQL relational database design
- Alembic migrations
- JWT authentication
- Google OAuth
- Role-based authorization
- Workspace isolation
- Client portal separation
- Booking and recurring booking workflows
- Trainer availability
- Check-in and attendance workflows
- Payments and receipts
- Stripe Test Mode
- Stripe Connect demo mode
- Email verification and invitations
- Reports and CSV exports
- Notifications and activity logs
- Localization across English, French, and Arabic
- Responsive web/mobile UI
- Automated backend and frontend quality gates
- Manual QA and demo release preparation
