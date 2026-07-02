# GymFlow Security Overview

GymFlow was designed as a product-style SaaS application with authentication, authorization, workspace isolation, client portal separation, payment safety, provider boundaries, and demo-safe release behavior.

This document explains the main security and privacy decisions used in the project showcase.

---

## Security Goals

| Goal | Description |
|---|---|
| Authentication | Users must authenticate before accessing protected studio or portal features |
| Authorization | Each role only receives access to the workflows required for that role |
| Workspace isolation | One studio workspace should not access another workspace's data |
| Client privacy | Client portal users only access their own client-facing information |
| Route protection | Staff/admin routes and client portal routes are separated |
| Payment safety | Demo payments use Stripe Test Mode and never process real money |
| Secret protection | API keys, tokens, database credentials, and environment files are not committed |
| Production hardening | Production configuration is stricter than development configuration |
| Demo honesty | The showcase clearly separates demo behavior from production behavior |

---

## Authentication Model

GymFlow supports multiple authentication and access flows.

| Flow | Purpose |
|---|---|
| Email/password login | Standard owner, manager, trainer, receptionist access |
| JWT access tokens | Protected API access after login |
| Google OAuth | Optional provider-based login |
| Email verification | Confirms account email ownership |
| Password reset | Allows secure account recovery |
| Staff invitation | Allows workspace owners/managers to invite team members |
| Client portal access link | Allows clients to access their portal without becoming staff users |

The backend uses protected API routes and token-based access control.

The important architectural decision is that the client portal is not the same security surface as the owner/staff dashboard.

---

## Role-Based Access Control

GymFlow separates access by role.

| Role | Main Access |
|---|---|
| Owner | Full workspace control, billing, staff, clients, bookings, settings |
| Manager | Operational management across the workspace |
| Trainer | Schedule, availability, bookings, and attendance-related workflows |
| Receptionist | Front-desk workflows such as clients, check-ins, and booking support |
| Client | Private client portal only |

This role model prevents the app from behaving like a single flat dashboard where every authenticated user can see everything.

---

## Workspace Isolation

GymFlow is built as a workspace-based SaaS system.

Workspace-scoped data includes:

| Data Area | Isolation Rule |
|---|---|
| Clients | Clients belong to a specific workspace |
| Staff | Staff members belong to a specific workspace |
| Membership plans | Plans are owned by a workspace |
| Client memberships | Membership assignments belong to workspace-owned clients |
| Services | Service types are configured per workspace |
| Trainer availability | Availability belongs to workspace staff/trainers |
| Bookings | Bookings are tied to workspace clients, services, and trainers |
| Check-ins | Attendance records are scoped to the workspace |
| Payments | Payments are tied to workspace-owned client records |
| Reports | Reports aggregate workspace-specific data |
| Notifications | Notifications belong to the correct user/workspace context |
| Activity logs | Activity history is scoped to the workspace context |

Expected security rule:

A user from Workspace A should not be able to read or mutate Workspace B data.

---

## Client Portal Separation

The client portal is intentionally separated from the owner/staff dashboard.

Client portal functionality includes:

| Portal Area | Purpose |
|---|---|
| Portal access request | Allows a client to request or confirm access |
| Portal home | Shows a client-specific summary |
| Portal bookings | Lets clients view, book, cancel, or reschedule supported bookings |
| Portal membership | Shows the client's membership status and benefits |
| Portal payments | Shows pending and completed client payments |
| Portal receipts | Shows safe receipt information |
| Portal profile | Shows client profile information |
| Portal progress | Shows client-facing progress or demo information |
| Portal support | Provides a support path without exposing admin tools |
| QR check-in pass | Supports client-facing check-in concepts |

Expected portal security rules:

| Token Type | Should Access | Should Not Access |
|---|---|---|
| Staff/admin JWT | Workspace dashboard APIs depending on role | Private client portal `/portal/me` APIs |
| Client portal token | Client portal APIs for that client | Staff/admin workspace APIs |
| Unauthenticated visitor | Public pages and public auth flows | Protected dashboard or portal data |

This protects client privacy and keeps portal access limited.

---

## Route Protection

GymFlow uses protected backend route groups.

Security-sensitive route categories include:

| Route Area | Protection Expectation |
|---|---|
| Dashboard routes | Require authenticated staff/admin access |
| Workspace routes | Require membership in the correct workspace |
| Staff routes | Require role-aware workspace access |
| Client routes | Require workspace access and resource ownership |
| Billing routes | Require authorized workspace access |
| Payment routes | Require authorized workspace or portal access depending on flow |
| Portal access routes | Use portal-safe request/confirmation behavior |
| Portal `/me` routes | Require client portal access only |
| Webhooks | Must validate provider signatures when configured |
| Health routes | Should expose only safe environment-appropriate information |

---

## Payment Safety

GymFlow includes Stripe-based payment and billing flows.

For the showcase version:

| Payment Area | Demo Behavior |
|---|---|
| Stripe mode | Stripe Test Mode |
| Real money | Not processed |
| Test card | Supported |
| Client checkout | Demo/test payment flow |
| SaaS billing | Demo/test billing flow |
| Stripe Connect | Simulated through demo mode |
| Identity verification | Not required in demo mode |
| Webhooks | Designed for payment status synchronization |
| Receipts | Client portal can show safe receipt information |

Stripe Connect demo mode exists so reviewers can experience the payment-related UI without uploading identity documents or completing real financial onboarding.

---

## Stripe Connect Demo Boundary

Stripe Connect normally requires connected account onboarding and identity verification.

For a public showcase, that would create a bad user experience because a reviewer may be sent to identity verification instead of seeing the product.

GymFlow therefore includes a demo-safe Connect mode.

| Production Concept | Showcase Behavior |
|---|---|
| Connected Stripe account | Demo connected-account state |
| Identity verification | Skipped in demo mode |
| Real transfers | Not performed in demo mode |
| Application fees | Demo-safe configuration only |
| Checkout | Stripe Test Mode checkout |
| Real payments | Not processed |

This keeps the payment flow realistic while avoiding real financial operations.

---

## Email Safety

GymFlow includes several email-related flows.

| Email Flow | Purpose |
|---|---|
| Email verification | Verify account ownership |
| Forgot password | Send reset instructions |
| Client portal access | Send client portal links |
| Staff invitation | Invite workspace team members |

For public demo usage, email delivery can be disabled, redirected, or limited to verified sender domains.

The showcase should not claim unrestricted production email delivery unless the provider configuration has been verified.

---

## OAuth Safety

GymFlow includes Google OAuth support.

OAuth security expectations include:

| Area | Rule |
|---|---|
| Redirect URLs | Production redirects should use HTTPS |
| Client secrets | OAuth secrets should never be committed |
| Android configuration | Android OAuth metadata should match the package and signing fingerprint |
| Callback handling | OAuth callback and frontend handoff must match configured URLs |
| Error handling | Missing, invalid, or expired handoff codes should fail safely |

For showcase usage, OAuth can be demonstrated only when provider configuration is prepared correctly.

---

## Secret Handling

The showcase repository must not contain secrets.

Secrets that must stay private include:

| Secret Type | Example |
|---|---|
| Backend secret key | JWT signing secret |
| Database URL | PostgreSQL credentials |
| OAuth credentials | Google OAuth client secret |
| Stripe credentials | Stripe secret key and webhook secret |
| Email provider credentials | SMTP or Resend API keys |
| Portal signing secrets | Portal token or QR pass signing material |
| Production domain config | Trusted hosts and CORS origins |
| Environment files | `.env` and local secret configuration |

This showcase repository should contain documentation, screenshots, videos, and release notes only.

---

## Production Configuration Rules

GymFlow separates local development behavior from stricter production behavior.

Production configuration should enforce:

| Rule | Purpose |
|---|---|
| Strong secret key | Protect JWT/session signing |
| Exact CORS origins | Prevent unauthorized browser origins |
| Trusted hosts | Prevent unexpected host header usage |
| HTTPS frontend URL | Avoid insecure production callbacks |
| HTTPS OAuth redirects | Required for safe OAuth handoff |
| Disabled debug routes | Avoid exposing development-only endpoints |
| Disabled public docs when configured | Avoid exposing OpenAPI/ReDoc unnecessarily |
| Provider validation | Avoid half-configured OAuth, email, or Stripe integrations |
| Stripe live/test separation | Avoid mixing real payments with demo/test payments |
| Rate limiting | Protect public auth and portal access flows |
| Request size limits | Reduce exposure on public POST routes |

---

## API Safety and Observability

The backend API follows predictable API conventions.

| Area | Behavior |
|---|---|
| API prefix | Routes are grouped under `/api/v1` |
| JSON style | API responses use consistent JSON conventions |
| Staff routes | Staff/admin routes require dashboard authentication |
| Portal routes | Client portal routes require portal-safe access |
| Request IDs | Request identifiers support debugging and tracing |
| Validation errors | Validation failures are handled consistently |
| Rate-limit errors | Rate-limit responses can include retry guidance |
| CORS exposure | Frontend can receive safe debugging headers where configured |

These conventions make the API easier to test, debug, and integrate with the Flutter frontend.

---

## Frontend Privacy Rules

The frontend must avoid leaking backend internals to normal users or clients.

Important UI privacy rules include:

| Rule | Reason |
|---|---|
| Do not show raw UUIDs | Internal IDs are not useful to users |
| Do not show raw tokens | Tokens are sensitive implementation details |
| Do not show raw backend enums | Values like `active`, `paid`, `manual`, or `trainer` should be localized |
| Do not expose portal internals | Client portal should remain client-safe |
| Avoid internal auth language in UI | Users should see human-readable copy, not implementation terms |
| Keep destructive actions confirmed | Prevent accidental deletions/cancellations |
| Explain disabled actions | Avoid confusing permission or state restrictions |

---

## Localization and Security

Localization is also part of product safety.

If backend statuses are displayed raw, users may see confusing internal values.

GymFlow uses localization/display helpers so statuses and roles can be shown as readable labels.

Examples of values that should be displayed through localization:

| Internal Meaning | User-Facing Need |
|---|---|
| Membership status | Active, inactive, expired, cancelled |
| Payment status | Pending, paid, failed, cancelled |
| Payment provider | Manual, Stripe |
| Billing status | Active, trialing, past due, canceled |
| Staff role | Owner, manager, trainer, receptionist |
| Booking status | Scheduled, cancelled, completed |

This improves professionalism and avoids exposing implementation details.

---

## Automated Quality Gates

GymFlow includes automated checks around security, API contracts, route protection, deployment configuration, and demo readiness.

Backend quality areas include:

| Check Area | Purpose |
|---|---|
| Secret scanning | Avoid committed secrets |
| Migration checks | Keep database schema changes controlled |
| Database contract checks | Validate expected model/table behavior |
| Security contract checks | Validate security-sensitive expectations |
| Observability contract checks | Validate request/debug behavior expectations |
| Deployment contract checks | Validate production configuration rules |
| API contract checks | Validate critical API surface and OpenAPI behavior |
| Route auth checks | Validate protected route behavior |
| Portal route checks | Validate client portal route availability |
| Smoke checks | Confirm app imports and expected routes register |
| Pytest suite | Exercise backend behavior |

Frontend quality areas include:

| Check Area | Purpose |
|---|---|
| Flutter analysis | Static Dart and Flutter validation |
| Frontend quality checks | UI/source consistency checks |
| API sync tests | Keep frontend/backend expectations aligned |
| Portal quality checks | Validate client portal privacy, layout, and source rules |
| Full test runner | Run grouped frontend tests with readable logs |
| Manual QA checklist | Validate full product behavior across roles, routes, languages, and screen sizes |

---

## Manual Security QA

Manual QA should verify security-sensitive behavior.

| Area | Expected Result |
|---|---|
| Logged-out visitor | Cannot access dashboard routes |
| Client portal user | Cannot access admin/staff dashboard |
| Staff/admin user | Does not accidentally enter private client portal routes |
| Workspace isolation | Workspace A cannot access Workspace B data |
| Role restrictions | Trainer/receptionist/manager permissions behave correctly |
| Expired portal access | Shows safe error and does not expose data |
| Invalid portal token | Shows safe error and does not expose data |
| Password reset | Does not reveal whether an account exists in unsafe ways |
| Email verification | Uses safe success/error handling |
| Stripe checkout cancel | Returns to safe UI state |
| Webhook duplicate | Should not create unsafe duplicate payment state |
| Public pages | Do not contain private environment or provider data |
| UI labels | Do not expose raw backend internal values |
| Browser console | Does not expose secrets or sensitive tokens |

---

## Demo Boundary

The showcase version is designed to demonstrate engineering capability safely.

| Area | Showcase Position |
|---|---|
| Source code | Private |
| Demo data | Fictional |
| Payments | Stripe Test Mode |
| Stripe Connect | Demo mode |
| Emails | Test, disabled, or provider-limited |
| OAuth | Demo/provider-configured only |
| Hosting | Optional temporary demo access |
| Production claim | Not claimed unless provider and deployment checks pass |

This allows GymFlow to be shown as a serious full-stack SaaS project without exposing private source code, credentials, or production infrastructure.

---

## Production Readiness Boundary

GymFlow should only be described as production-ready after final provider and operations verification.

Production readiness would require:

| Area | Required Verification |
|---|---|
| Hosting | Backend and frontend hosted with HTTPS |
| Database | Managed database, backups, and restore process |
| Redis/rate limits | Production rate limiting enabled |
| Stripe | Live/test separation and webhook verification |
| Email | Verified sender domain and real inbox tests |
| OAuth | Production redirect URLs verified |
| Monitoring | Logs, uptime checks, and error review |
| Backups | Backup schedule and restore drill |
| Security | Final workspace, role, and portal isolation checks |
| Vulnerability scanning | Dependencies and images reviewed |

---

## Security Summary

GymFlow demonstrates security-aware software engineering across:

- JWT authentication
- Google OAuth support
- Email verification
- Password reset
- Staff invitation flows
- Client portal access links
- Role-based access control
- Workspace-scoped data isolation
- Client portal separation
- Protected backend routes
- Stripe Test Mode payment safety
- Stripe Connect demo handling
- Secret and environment boundary discipline
- Frontend privacy guards
- Localized display values
- Automated security and API contract checks
- Manual QA for security-sensitive flows
