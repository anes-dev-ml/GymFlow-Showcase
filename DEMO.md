# GymFlow Demo Guide

This guide explains how to review GymFlow as a complete full-stack SaaS product demo.

GymFlow is not only a UI prototype. The demo is designed to show a connected product experience across public pages, authentication, owner/staff operations, client portal workflows, bookings, payments, localization, responsive layouts, and demo-safe provider integrations.

---

## Demo Goal

The goal of the demo is to show that GymFlow can operate like a real SaaS gym management platform.

The walkthrough should prove:

| Area | What the Demo Should Show |
|---|---|
| Product thinking | The app has a clear purpose and realistic gym/studio workflows |
| Frontend engineering | The Flutter app supports public, dashboard, and portal surfaces |
| Backend engineering | The FastAPI backend exposes protected business APIs |
| Database design | The app is built around real relational entities |
| Authentication | Users can log in and access role-specific areas |
| Authorization | Owners, staff, and clients do not share the same access model |
| Client portal | Clients have their own private portal experience |
| Payments | Stripe test flows work without real money |
| Localization | English, French, and Arabic are supported |
| Responsive design | The app works across desktop, tablet, and mobile sizes |
| QA discipline | The app was prepared with automated and manual checks |

---

## Recommended Demo Order

Use this order for a clean 3 to 5 minute product walkthrough.

| Step | Area | What to Show |
|---|---|---|
| 1 | Public website | Home page, product positioning, navigation, pricing/security pages |
| 2 | Authentication | Login page, Google login option, forgot/reset password routes if needed |
| 3 | Owner dashboard | Metrics, operational overview, recent activity, clean SaaS layout |
| 4 | Clients | Client list, search/filter UI, client profile |
| 5 | Client profile | Memberships, bookings, payments, activity, portal actions |
| 6 | Memberships | Plans and client membership assignment/status |
| 7 | Staff | Staff roles, trainers, manager/receptionist-style access |
| 8 | Bookings | Scheduling, trainer availability, booking states, recurring booking concept |
| 9 | Check-ins | Daily attendance or front-desk check-in/out workflow |
| 10 | Payments | Pending/paid payments, payment status labels, receipt concept |
| 11 | Reports | Reports and export-ready business view |
| 12 | Billing | SaaS billing settings and Stripe Connect demo mode |
| 13 | Client portal | Client home, bookings, membership, payments, profile, support |
| 14 | Localization | Switch between English, French, and Arabic |
| 15 | Responsive UI | Resize desktop to tablet/mobile or show Android build |
| 16 | Final summary | Show stack, architecture, and private source boundary |

---

## Demo Accounts

Use demo-only accounts and fictional data.

### Studio Owner

| Field | Value |
|---|---|
| Email | owner@gymflow.demo |
| Password | DemoOwner123! |
| Purpose | Full dashboard access for the main walkthrough |

### Staff Member

| Field | Value |
|---|---|
| Email | staff@gymflow.demo |
| Password | DemoStaff123! |
| Purpose | Staff/role-based access demonstration |

### Client Portal

| Field | Value |
|---|---|
| Access type | Client portal access link |
| Purpose | Client-only portal experience |
| Status | Final demo link will be added before release |

---

## Public Website Walkthrough

Start with the public website because it makes the app feel like a real product.

Show:

| Page | What to Highlight |
|---|---|
| Home | Main product positioning and SaaS-style landing page |
| Features | Real feature areas connected to the built app |
| Pricing | SaaS product structure and billing concept |
| Security | Workspace isolation, roles, and client portal separation |
| Contact | Product support or demo contact path |
| Privacy / Terms | Product completeness and public-site polish |

Important: public marketing copy should only claim features that are actually implemented or clearly demo-scoped.

---

## Authentication Walkthrough

Show that the app supports real SaaS access flows.

Highlight:

| Flow | Purpose |
|---|---|
| Email/password login | Standard access |
| Google OAuth | Provider-based login option |
| Forgot password | Account recovery route |
| Reset password | Password recovery completion |
| Email verification | Account verification concept |
| Staff invitation acceptance | Workspace team onboarding |

For the video, do not spend too long on authentication. Show enough to prove it exists, then move into the dashboard.

---

## Owner Dashboard Walkthrough

After login, show the dashboard as the first major product screen.

Highlight:

| Dashboard Area | What It Proves |
|---|---|
| Metrics cards | Business summary and backend data aggregation |
| Recent activity | Operational audit trail concept |
| Revenue/booking/client widgets | SaaS dashboard thinking |
| Sidebar navigation | Complete product shell |
| Loading/empty/ready states | Real app state handling |

This should be one of the strongest screenshots/video moments.

---

## Clients Walkthrough

Open the Clients module.

Show:

| Feature | What It Proves |
|---|---|
| Client list | Real operational data model |
| Search/filter | Usable admin workflow |
| Client status | Localized readable statuses |
| Client detail navigation | Connected data relationships |
| Portal action | Client portal integration |

Then open one client profile.

---

## Client Profile Walkthrough

The client profile is one of the best places to show depth.

Show:

| Section | What It Proves |
|---|---|
| Profile summary | Client identity and operational context |
| Memberships | Relationship between clients and plans |
| Bookings | Scheduling history and upcoming sessions |
| Payments | Payment history and statuses |
| Activity | Audit trail and recent operations |
| Portal access | Client-facing access workflow |
| QR/pass concept | Check-in and front-desk workflow thinking |

A single client profile screenshot can show many domains at once.

---

## Bookings Walkthrough

Open the booking area and show scheduling logic.

Highlight:

| Booking Feature | What It Proves |
|---|---|
| Service types | Studio-configurable booking options |
| Trainer availability | Scheduling constraints |
| Booking creation | Operational workflow |
| Edit/cancel states | Lifecycle handling |
| Recurring booking concept | More advanced scheduling design |
| Client portal booking | Client-facing booking flow |

For the video, demonstrate one clean booking action if the demo data supports it.

---

## Check-ins Walkthrough

Show attendance or front-desk check-in.

Highlight:

| Feature | What It Proves |
|---|---|
| Daily attendance | Real gym workflow |
| Saved attendance visibility | Data persistence |
| Present/absent state | Simple operational UX |
| Front-desk check-in/out | Reception workflow |
| QR/pass direction | Real-world check-in concept |

This section shows that the app is not only billing and dashboards. It handles physical gym operations too.

---

## Payments Walkthrough

Show the payments module and client payment flow.

Highlight:

| Payment Area | What It Proves |
|---|---|
| Pending payments | Payment lifecycle |
| Paid payments | Status tracking |
| Manual payment support | Offline/admin flexibility |
| Stripe checkout | Online payment integration |
| Receipt detail | Client-safe payment history |
| Payment provider labels | Localization and display polish |

---

## Billing Walkthrough

Open billing/settings billing.

Show:

| Billing Area | What It Proves |
|---|---|
| Current plan | SaaS subscription concept |
| Billing settings | Product monetization layer |
| Stripe test mode | Safe payment demonstration |
| Stripe Connect demo mode | Marketplace/studio payment routing concept |
| Demo-safe onboarding | Reviewer can test without identity verification |

Make it clear that the public demo uses test mode and does not process real money.

---

## Client Portal Walkthrough

The client portal should be a major part of the video.

Show:

| Portal Page | What to Highlight |
|---|---|
| Portal access | Clients use a separate access path |
| Portal home | Client-specific summary |
| Portal bookings | Upcoming/history/book/cancel/reschedule states |
| Portal membership | Membership status and benefits |
| Portal payments | Pending/paid payments and checkout |
| Receipt detail | Safe receipt display |
| Portal profile | Client-owned profile view |
| Portal progress | Client-facing progress/demo page |
| Portal support | Client-safe support path |

Important point to mention:

Clients do not enter the owner/staff dashboard. They have a separate portal experience.

---

## Localization Walkthrough

Show language switching.

Languages:

| Language | Code |
|---|---|
| English | en |
| French | fr |
| Arabic | ar |

Highlight:

| Localization Area | What It Proves |
|---|---|
| Public site | Marketing localization |
| Dashboard labels | App-wide localization |
| Portal copy | Client-facing localization |
| Status labels | Backend enum values are displayed cleanly |
| Arabic layout | RTL/demo internationalization effort |

Do not spend too much time here. A quick switch is enough.

---

## Responsive Walkthrough

Show desktop first, then mobile.

Recommended widths:

| Device Type | Width |
|---|---|
| Desktop | 1440px |
| Laptop | 1280px |
| Tablet | 768px |
| Mobile large | 430px |
| Mobile common | 390px |
| Mobile small | 360px |

Show:

| Area | What to Check |
|---|---|
| Public site | Header, hero, CTA, footer |
| Dashboard | Sidebar/shell adapts |
| Client portal | Mobile-first portal layout |
| Booking dialog | Dialogs fit small screens |
| Bottom navigation | Does not cover content |
| Arabic/French | Text does not overflow badly |

---

## Stripe Test Mode

The demo uses Stripe Test Mode.

### Test Payment Data

| Field | Value |
|---|---|
| Card number | 4242 4242 4242 4242 |
| Expiry date | Any future date |
| CVC | Any 3 digits |
| Postal code | Any valid postal code |

No real money is processed.

---

## Demo Limitations

The demo is intentionally scoped.

| Limitation | Explanation |
|---|---|
| Source code is private | The app is a complete product-style project |
| Demo data is fictional | No real gym or client data is used |
| Stripe is test/demo only | No real payments are processed |
| Stripe Connect is simulated | No identity verification is required |
| Email may be limited | Email can be disabled or provider-limited in demo |
| Hosted demo may be temporary | Live demo access can be enabled only during review periods |
| Production is not claimed by default | Production readiness requires provider, hosting, monitoring, and backup verification |

---

## Suggested Video Script

Use this structure for a 3 to 5 minute video.

| Time | Section |
|---|---|
| 0:00 - 0:15 | Project title and short explanation |
| 0:15 - 0:40 | Public website and product positioning |
| 0:40 - 1:00 | Login/authentication |
| 1:00 - 1:30 | Owner dashboard |
| 1:30 - 2:00 | Clients and client profile |
| 2:00 - 2:30 | Bookings and check-ins |
| 2:30 - 3:00 | Payments and billing |
| 3:00 - 3:40 | Client portal |
| 3:40 - 4:10 | Localization and responsive layout |
| 4:10 - 4:40 | Architecture/stack summary |
| 4:40 - 5:00 | Closing screen |

---

## Closing Message

End the video with a simple technical summary:

| Layer | Implementation |
|---|---|
| Frontend | Flutter Web, Android, Windows |
| Backend | FastAPI |
| Database | PostgreSQL |
| Auth | JWT and Google OAuth |
| Payments | Stripe Test Mode |
| Portal | Separate client access model |
| Localization | English, French, Arabic |
| QA | Automated checks and manual QA checklist |

Final message:

GymFlow was built from scratch as a full-stack SaaS product showcase.
