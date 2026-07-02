# GymFlow Architecture

GymFlow is a full-stack SaaS gym management platform designed around a professional multi-role architecture.

The application is separated into a Flutter client layer, a FastAPI backend layer, a PostgreSQL persistence layer, and external service integrations for authentication, payments, and email.

---

## High-Level System

| Layer | Technology | Purpose |
|---|---|---|
| Frontend | Flutter | Web, Android, and Windows user interface |
| Backend | FastAPI | REST API, business logic, authentication, authorization |
| Database | PostgreSQL | Persistent relational data storage |
| Migrations | Alembic | Database schema versioning |
| Authentication | JWT and Google OAuth | Secure login and session handling |
| Payments | Stripe Test Mode | Subscription and client payment simulation |
| Email | SMTP or transactional email provider | Account and portal email flows |
| Localization | Flutter ARB files | English, French, and Arabic UI support |

---

## Application Structure

GymFlow is built around several connected product areas:

| Area | Description |
|---|---|
| Public Website | Product landing page, pricing, and marketing content |
| Authentication | Email login, Google OAuth, password reset, email verification |
| Studio Dashboard | Overview of business activity, revenue, clients, and operations |
| Clients | Client records, memberships, bookings, payments, and activity |
| Memberships | Studio plans, client memberships, statuses, and renewals |
| Staff | Staff and role-based access for managers, trainers, and reception |
| Bookings | Scheduling, trainers, available slots, and client reservations |
| Check-ins | Attendance tracking and visit history |
| Payments | Payment records and Stripe test payment flows |
| Billing | Studio subscription billing and Stripe Connect demo mode |
| Client Portal | Client-facing access for bookings, membership, and profile data |
| Settings | Workspace, account, billing, and localization settings |

---

## User Roles

GymFlow supports multiple user experiences instead of a single flat dashboard.

| Role | Main Capabilities |
|---|---|
| Owner | Full workspace control, billing, staff, clients, bookings, settings |
| Manager | Operational management across clients, bookings, and staff workflows |
| Trainer | Schedule-related workflows, bookings, and attendance |
| Receptionist | Client-facing operations such as check-ins and booking support |
| Client | Private portal access for bookings, membership, and personal activity |

---

## Frontend Architecture

The frontend is built with Flutter and organized around product features.

Key frontend responsibilities include:

- Responsive layouts for desktop, tablet, and mobile.
- Role-aware navigation.
- Public website and private SaaS dashboard.
- Client portal experience.
- Localized UI text in English, French, and Arabic.
- API integration with the FastAPI backend.
- Stripe checkout redirection flows.
- Demo-ready UI states for showcase usage.

The frontend is designed to run as:

- Flutter Web
- Android APK
- Windows desktop build

---

## Backend Architecture

The backend is built with FastAPI and provides the main business logic of the application.

Key backend responsibilities include:

- Authentication and token management.
- Workspace and role-based access control.
- Client, staff, membership, booking, check-in, and payment APIs.
- Portal-specific routes for client access.
- Stripe payment and billing integration.
- Email verification and password reset flows.
- Database persistence through PostgreSQL.
- Database migrations through Alembic.
- Production-style route protection and API validation.

---

## Database Architecture

GymFlow uses PostgreSQL as the main relational database.

The database stores product entities such as:

- Users
- Workspaces
- Staff members
- Clients
- Membership plans
- Client memberships
- Bookings
- Check-ins
- Payments
- Billing records
- Notifications
- Activity logs
- Portal access records

Alembic is used to manage schema migrations and keep the database structure versioned.

---

## Authentication and Authorization

GymFlow uses a security model based on authenticated users, workspaces, roles, and protected routes.

Authentication features include:

- Email and password login.
- JWT access tokens.
- Google OAuth support.
- Email verification.
- Password reset.
- Client portal access links.

Authorization features include:

- Owner, manager, trainer, receptionist, and client role separation.
- Protected backend routes.
- Workspace-aware data access.
- Portal-specific client privacy boundaries.

---

## Payments and Billing

GymFlow includes a Stripe-based payment and billing architecture.

The showcase version uses:

- Stripe Test Mode.
- Test checkout sessions.
- Test card payment flows.
- Stripe Connect demo mode.
- No real payment processing.

Stripe Connect is simulated in demo mode so reviewers can experience the payment-related UI without completing real identity verification.

---

## Localization

GymFlow supports three languages:

| Language | Status |
|---|---|
| English | Supported |
| French | Supported |
| Arabic | Supported |

The frontend uses ARB localization files and avoids hardcoded production UI text where possible.

---

## Demo and Showcase Strategy

The public showcase is intentionally separate from the private source repositories.

This allows the project to be presented professionally without exposing the full application source code.

The showcase repository contains:

- Product overview.
- Demo guide.
- Architecture notes.
- Security notes.
- Screenshots.
- Demo video.
- Build and release information.

The frontend and backend source repositories remain private because GymFlow is a complete product-style SaaS project.

---

## Deployment Model

GymFlow can be demonstrated in several ways:

| Mode | Description |
|---|---|
| Local Demo | Backend, database, and frontend run locally |
| Temporary Hosted Demo | Backend and frontend are hosted during review periods |
| Recorded Demo | Product walkthrough shown through video |
| Build Demo | Android and Windows builds provided for installation testing |

For the final showcase, the recommended approach is to use screenshots, a recorded walkthrough, and optional temporary hosted access on request.

---

## Engineering Scope

GymFlow demonstrates software engineering across:

- Frontend application development.
- Backend API development.
- Relational database design.
- Authentication and authorization.
- Payment integration.
- Email workflows.
- Responsive UI.
- Localization.
- SaaS architecture.
- Product documentation.
- Demo release preparation.
