# GymFlow Security Overview

GymFlow was designed as a product-style SaaS application with authentication, authorization, workspace isolation, client portal separation, payment safety, and demo-safe provider configuration.

This document explains the main security decisions used in the project showcase.

---

## Security Goals

GymFlow focuses on the following security goals:

| Goal | Description |
|---|---|
| Authentication | Users must authenticate before accessing protected studio or portal features. |
| Authorization | Each user role only receives access to the actions required for that role. |
| Workspace isolation | One studio workspace should not be able to access another studio workspace's data. |
| Client privacy | Client portal users only access their own portal information. |
| Payment safety | Demo payments use Stripe Test Mode and never process real money. |
| Secret protection | Environment secrets, API keys, tokens, and provider credentials are not committed. |
| Production hardening | Production mode is stricter than local development mode. |

---

## Authentication Model

GymFlow supports multiple authentication flows.

| Flow | Purpose |
|---|---|
| Email and password login | Standard owner, manager, staff, and admin access. |
| JWT access tokens | Protected API access after login. |
| Google OAuth | Optional Google sign-in flow for supported environments. |
| Email verification | Confirms user ownership of an email address. |
| Password reset | Allows users to recover access securely. |
| Client portal access links | Allows clients to access their own portal without becoming studio staff users. |

The backend uses protected API routes and token-based access control.

---

## Role-Based Access Control

GymFlow separates user behavior by role.

| Role | Access Pattern |
|---|---|
| Owner | Full workspace administration, billing, staff, clients, bookings, settings. |
| Manager | Operational management across the studio workspace. |
| Trainer | Booking, schedule, and attendance-related workflows. |
| Receptionist | Front-desk workflows such as clients, check-ins, and booking support. |
| Client | Private client portal access only. |

A key design decision is that clients do not use the same dashboard experience as staff or owners.

This protects the admin workspace from client-facing portal flows.

---

## Workspace Isolation

GymFlow is built as a workspace-based SaaS system.

That means data is scoped to a studio workspace.

Workspace-scoped data includes:

| Data Area | Workspace Boundary |
|---|---|
| Clients | Clients belong to a specific workspace. |
| Staff | Staff members belong to a specific workspace. |
| Membership plans | Plans are created per workspace. |
| Client memberships | Membership assignments belong to a workspace. |
| Bookings | Bookings are scoped to the workspace. |
| Check-ins | Attendance records are scoped to the workspace. |
| Payments | Payments are tied to workspace-owned client records. |
| Reports | Reports are generated from workspace-specific data. |
| Activity logs | Activity history belongs to the workspace context. |

The intended production rule is simple:

A user from Workspace A must not be able to read or modify Workspace B data.

---

## Client Portal Separation

The client portal is intentionally separated from the owner/staff dashboard.

Client portal routes are designed around client-safe access.

Portal capabilities include:

| Portal Area | Purpose |
|---|---|
| Portal access request | Allows a client to request or confirm access. |
| Portal home | Shows a client-specific summary. |
| Portal bookings | Allows clients to view, book, cancel, or reschedule supported bookings. |
| Portal membership | Shows the client's membership status and benefits. |
| Portal payments | Shows pending and completed client payments. |
| Portal receipts | Shows safe receipt information. |
| Portal profile | Shows client profile information. |
| Portal progress | Shows client-facing progress or preview information. |
| Portal support | Gives the client a support path without exposing admin tools. |

Client portal tokens should not grant access to staff or admin routes.

Staff dashboard tokens should not grant access to private `/portal/me` client routes.

---

## Payment Safety

GymFlow includes Stripe-based payment and billing flows.

For the showcase version:

| Payment Area | Demo Behavior |
|---|---|
| Stripe mode | Stripe Test Mode |
| Real money | Not processed |
| Test card | Supported |
| Stripe Connect | Simulated through demo mode |
| Identity verification | Not required in demo mode |
| Webhooks | Designed for payment status synchronization |
| Receipts | Client portal can show safe receipt information |

Stripe Connect demo mode exists so the app can be demonstrated without sending reviewers into a real identity verification process.

---

## Email Safety

GymFlow includes email-related flows such as:

| Email Flow | Purpose |
|---|---|
| Email verification | Verify account ownership. |
| Forgot password | Send password reset instructions. |
| Client portal access | Send client portal access links. |
| Staff invitation | Invite team members into a workspace. |

For public demo usage, email delivery can be disabled, redirected, or limited to verified sender domains.

The showcase should not claim unrestricted production email delivery unless the provider configuration is verified.

---

## Secret Handling

The source repositories are private and environment-specific secrets are not part of the showcase.

Secrets that must stay private include:

| Secret Type | Example |
|---|---|
| Backend secret key | JWT signing secret |
| Database URL | PostgreSQL credentials |
| OAuth credentials | Google OAuth client secret |
| Stripe credentials | Stripe secret key and webhook secret |
| Email provider credentials | SMTP or Resend API keys |
| Portal signing secrets | Token or pass signing material |
| Production domain config | Trusted hosts and CORS origins |

The showcase repository should never contain `.env` files, real API keys, database passwords, private tokens, or production credentials.

---

## Production Environment Rules

GymFlow separates local development behavior from stricter production behavior.

In production, the backend is expected to enforce:

| Rule | Purpose |
|---|---|
| Strong secret key | Protect JWT/session signing. |
| Exact CORS origins | Prevent unauthorized browser origins. |
| Trusted hosts | Prevent unexpected host header usage. |
| HTTPS frontend URL | Avoid insecure production callbacks. |
| HTTPS OAuth redirects | Required for safe OAuth handoff. |
| Disabled debug routes | Avoid exposing internal development endpoints. |
| Disabled public docs when configured | Avoid exposing API documentation unnecessarily. |
| Proper Stripe live/test separation | Avoid mixing demo payments with real payments. |
| Provider-specific validation | Prevent half-configured production integrations. |

---

## API Safety and Observability

The backend API is designed around predictable response and observability rules.

Important conventions include:

| Area | Behavior |
|---|---|
| API prefix | Routes are grouped under `/api/v1`. |
| Response format | JSON responses use consistent conventions. |
| Protected routes | Staff/admin routes require staff JWT access. |
| Portal routes | Client portal routes require portal-safe access. |
| Request IDs | Request identifiers support debugging and tracing. |
| Validation errors | Validation failures are handled consistently. |
| Rate limits | Public auth and portal flows can be rate-limited when configured. |

These rules make the API easier to test, debug, and integrate with the frontend.

---

## Quality Gates

GymFlow includes automated checks around security, API contracts, route protection, deployment configuration, and demo readiness.

Backend quality areas include:

| Check Area | Purpose |
|---|---|
| Secret scanning | Avoid committed secrets. |
| Migration checks | Keep database schema changes controlled. |
| Database contract checks | Validate expected model/table behavior. |
| Security contract checks | Validate security-sensitive expectations. |
| Deployment contract checks | Validate production configuration rules. |
| API contract checks | Validate critical API surface. |
| Route auth checks | Validate protected route behavior. |
| Portal route checks | Validate client portal route availability. |
| Smoke checks | Confirm the app imports and registers expected routes. |
| Pytest suite | Exercise backend behavior. |

Frontend quality areas include:

| Check Area | Purpose |
|---|---|
| Flutter analysis | Static Dart and Flutter validation. |
| Frontend quality checks | UI/source consistency checks. |
| API sync tests | Keep frontend/backend expectations aligned. |
| Portal quality checks | Validate client portal privacy, layout, and source rules. |
| Full test runner | Run grouped frontend tests with readable logs. |
| Manual QA checklist | Validate full product behavior across roles, routes, languages, and screen sizes. |

---

## Demo Boundary

The showcase version is designed to demonstrate engineering capability safely.

The demo boundary is:

| Area | Showcase Position |
|---|---|
| Source code | Private |
| Demo data | Fictional |
| Payments | Stripe Test Mode |
| Stripe Connect | Demo mode |
| Emails | Test, disabled, or provider-limited |
| Hosting | Optional temporary demo access |
| Production claim | Not claimed unless provider and deployment checks pass |

This allows GymFlow to be shown as a serious full-stack SaaS project without exposing private source code or production credentials.

---

## Security Summary

GymFlow demonstrates security-aware software engineering across:

- JWT authentication.
- Google OAuth support.
- Email verification.
- Password reset.
- Role-based access control.
- Workspace-scoped data isolation.
- Client portal separation.
- Stripe Test Mode payment safety.
- Stripe Connect demo handling.
- Protected backend routes.
- Frontend privacy guards.
- Localization-safe display helpers.
- Automated security and API contract checks.
- Manual QA coverage for security-sensitive flows.
