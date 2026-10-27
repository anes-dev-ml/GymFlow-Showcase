# Security design

GymFlow's implementation separates public, staff, and member-portal access and applies workspace-scoped authorization, request safeguards, and environment configuration controls. This document explains those boundaries. The [Threat model](THREAT_MODEL.md) contains the detailed abuse cases, mitigations, and residual risks.

The design of a security control is not certification of a deployed environment.

## Identity and access

| Surface | Access model |
| --- | --- |
| Public | Unauthenticated routes with validation, rate limiting, and neutral responses for identity-sensitive flows |
| Staff | JWT, active workspace membership, role and operation checks, resource workspace scope |
| Client portal | Portal-specific token, client/workspace identity derived from the session, client-safe responses |

The backend enforces authorization; frontend permissions affect navigation only. New API routes must preserve workspace isolation and ensure that staff credentials and portal credentials cannot be exchanged.

Password login, email verification and recovery, Google OAuth handoff, staff invitations, and one-time portal access have separate expiry and validation rules. Production responses do not expose demo-only access codes.

## Request protections

The FastAPI application includes host and CORS restrictions, security headers, request-size limits for sensitive endpoints, rate limits backed by Redis in production, and structured request IDs.

API responses use audience-specific schemas. Portal responses exclude internal staff notes and private operational fields. Presence and last-seen data follow role and visibility rules.

Unhandled errors are logged with diagnostic context while clients receive a limited error response rather than stack traces. Identity-sensitive public requests use neutral responses where appropriate to reduce enumeration risks.

## Payments and external providers

Stripe callbacks are signature-checked and processed with duplicate-event protection. Client payments and GymFlow subscriptions remain distinct domains. The demo operates with fictional data and test-mode safeguards and must reject production-like reset targets or live payment settings.

Credentials, authentication secrets, signing keys, and provider tokens must remain outside tracked source and public artifacts. The application does not collect payment card numbers directly.

## Deployment requirements

A production operator must still verify TLS, network isolation, database and Redis access, secret rotation, exact configured origins, live provider accounts, logging and alerting, dependency scanning, and backup/restore processes.

These external checks are tracked in [Operations](OPERATIONS.md) and the backend deployment completion plan. For responsible vulnerability reporting, see [SECURITY.md](../SECURITY.md).
