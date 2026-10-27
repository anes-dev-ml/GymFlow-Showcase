# Product workflows

GymFlow has three interfaces supported by one workspace-scoped operational model: the public website, the staff application, and a private client portal.

## Roles and access

| Role | Typical work |
| --- | --- |
| Owner | Workspace administration, staff, finance, subscriptions, reports |
| Manager | Studio operations, clients, schedules, staff workflows |
| Trainer | Availability, assigned sessions, attendance, permitted communication |
| Receptionist | Front-desk check-ins, client records, bookings, supported payments |
| Client | Own bookings, membership, receipts, profile, check-in pass, support |

Permissions are enforced by the API from the authenticated credential, workspace membership, role, and resource ownership; the interface uses the same capabilities to guide navigation.

## Connected workflows

### Membership and onboarding

A staff member creates a client record, assigns a membership plan, records or requests payment, and can provide access to the client portal. The client then sees membership status, bookings, receipts, and other account information without staff privileges.

### Scheduling and attendance

Services define duration and whether a trainer is required. Trainer availability and existing bookings are checked before creating a session. Recurring bookings share series context while individual occurrences retain their own status. Attendance and physical check-ins are recorded separately from booking status.

### Payments and reporting

The product distinguishes **client-to-studio payments** from **studio-to-GymFlow SaaS billing**. Manual collection and Stripe test flows share a payment lifecycle, while invoices/receipts and reporting present audience-appropriate information. Provider events have duplicate-handling and state-transition rules.

### Communication

Staff and clients can exchange messages through a conversation workflow. Staff assignment, priority, status, and internal notes support operations; clients receive only client-visible messages and portal-safe data. Notifications and activity logs record related events.

## Product surfaces

**Public website:** information about GymFlow, pricing, security, account access, and legal pages.

**Staff application:** dashboard, client lifecycle, membership plans, services, scheduling, trainer availability, attendance, payments, reports, notifications, messaging, and workspace settings.

**Client portal:** private access, dashboard, bookings, membership, payments and receipts, progress, check-in pass, messages, profile, and settings.

The frontend supports desktop, narrow-browser, and mobile layouts in English, French, and Arabic/RTL. Screenshots of representative states appear in the [gallery](../screenshots/README.md).

## Demonstration data

The Northline Performance Club scenario uses fictional identities and fixed business relationships. It includes ordinary states and failures (for example, expired memberships, cancelled bookings, and unsuccessful payments) to exercise the product beyond empty or ideal data.

Counts, safeguards, and reset instructions are documented in [Demo environment](../DEMO.md). The [Build manifest](../BUILD_MANIFEST.md) identifies the exact application revisions represented by the public Showcase.

For implementation details, see [Architecture](../ARCHITECTURE.md) and [Engineering](ENGINEERING.md).