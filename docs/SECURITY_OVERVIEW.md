# GymFlow Security Overview

GymFlow was designed around authentication, authorization, tenant isolation, portal separation, payment safety, abuse protection, provider boundaries, and environment-specific configuration.

This document describes the security controls implemented in the application architecture and the deployment controls expected around them. Formal security certification would be a separate assessment of a specific operated environment.

## Security objectives

| Objective | System expectation |
|---|---|
| Authenticate staff | Protected staff APIs require a valid staff JWT |
| Authenticate portal clients | Protected portal APIs require a client-scoped portal token |
| Enforce least privilege | Capabilities depend on role, workspace membership, resource ownership, and route type |
| Isolate tenants | Workspace A cannot access Workspace B data |
| Protect client privacy | A portal client sees only portal-safe data belonging to that client |
| Avoid enumeration | Public recovery/access responses do not reveal whether an identity exists |
| Protect provider secrets | Credentials remain in environment configuration, never in the showcase |
| Prevent real demo charges | Demo uses fictional records and Stripe test/demo behavior |
| Support incident diagnosis | Request IDs correlate client failures with structured backend logs |
| Fail closed in production | Debug/docs/local origins and weak provider combinations are rejected |

## Identity and access surfaces

GymFlow has three distinct trust domains.

| Surface | Credential | Main protection |
|---|---|---|
| Public | None | Neutral responses, validation, rate limits, request-size limits |
| Staff/admin | JWT | User identity, workspace membership, role, membership status |
| Client portal | Portal token | Token type, workspace ID, client ID, expiry, route dependency |

A staff JWT is not treated as a portal credential. A portal token is not treated as a staff JWT.

## Authentication

Implemented flows include:

- email/password login;
- password hashing and verification;
- email verification;
- forgot/reset password;
- Google OAuth handoff;
- staff invitation acceptance;
- one-time client portal access.

### Client portal access

Portal access uses an identity-sensitive request followed by one-time confirmation. The flow is designed to preserve a neutral public response, limit attempts, expire access records, and mark a successful code as consumed.

Development and guarded demo environments may expose a generated code for fictional `.test` identities. Production responses do not expose that code.

## Authorization

Authorization is evaluated from more than a visible frontend role.

Relevant factors include:

- authenticated user or portal subject;
- credential type;
- active workspace membership;
- role;
- workspace membership status;
- requested operation;
- resource workspace ownership;
- client ownership for portal data;
- message audience and participant rules.

The Flutter router and action permissions prevent confusing navigation, but backend route dependencies and scoped queries are the security boundary.

## Workspace isolation

Business entities carry or derive workspace ownership. Queries and mutations are expected to verify the active workspace and user membership before returning or changing records.

Workspace-scoped areas include:

- clients and client memberships;
- plans and services;
- staff, invitations, availability, and presence;
- bookings and check-ins;
- payments and reports;
- notifications and activity logs;
- messaging;
- portal settings and access records.

## Client portal privacy

Portal response shapes are intentionally narrower than staff response shapes.

Portal protections include:

- client-scoped token dependencies;
- protected `/portal/me...` routes;
- no trust in client-supplied workspace/client IDs after authentication;
- receipt views that avoid exposing provider secrets or internal identifiers;
- audience-safe messaging responses;
- separation of staff-only internal notes;
- safe handling of expired, invalid, or consumed access credentials.

## Messaging security

Messaging introduces risks beyond ordinary CRUD because multiple staff roles and a client can participate in one workflow.

Controls include:

- participant authorization;
- role-restricted conversation access;
- assigned staff/trainer access rules;
- internal-note versus client-message separation;
- audience-specific schemas;
- retry-safe send identifiers;
- optimistic workflow versions for conflicting updates;
- cursor pagination;
- portal abuse limits;
- lifecycle cleanup.

## Staff presence privacy

Presence data can reveal work patterns. GymFlow separates:

- connection state;
- recent user activity;
- visibility policy;
- last-seen visibility;
- administrative reset operations.

Multiple devices are aggregated so one disconnected tab does not incorrectly force a person offline. Presence detail is returned according to role and configured visibility.

## Public abuse protection

Sensitive public POST routes are protected by request-size limits before endpoint parsing.

Covered flows include:

- registration;
- login;
- forgot/reset password;
- Google OAuth exchange;
- email verification;
- portal access request/confirmation;
- invitation acceptance.

Auth-style rate limits cover registration, login, password recovery, OAuth, portal access, and email verification. Redis is required in production so limits work across application instances.

## API and middleware protections

The FastAPI application wires:

- `TrustedHostMiddleware`;
- controlled CORS;
- request IDs;
- structured access logging;
- sensitive request-size middleware;
- security headers;
- consistent validation and HTTP errors;
- generic unhandled-error responses.

### Security headers

All responses are expected to include controls such as:

- `X-Content-Type-Options: nosniff`;
- `X-Frame-Options: DENY`;
- `Referrer-Policy: no-referrer`;
- restrictive `Permissions-Policy`;
- `Cache-Control: no-store` for sensitive API responses.

Production additionally applies HSTS and a restrictive API-oriented Content Security Policy.

## Error handling and enumeration resistance

Public identity-sensitive flows use neutral responses where appropriate, including:

- forgot password;
- resend verification;
- portal access request.

Unhandled exceptions return a generic client message and request ID. Full exception details remain in structured server logs.

## Payment safety

GymFlow does not store card numbers.

Payment controls include:

- explicit Stripe test/live environment separation;
- webhook signature verification when Stripe is enabled;
- webhook event persistence and duplicate detection;
- idempotent processing behavior;
- fictional demo payments without live Stripe identifiers;
- demo refusal when live Stripe configuration or stored live events are detected;
- separation between client payment records and SaaS billing state.

Stripe Connect demo behavior uses test-mode architecture and fictional identities, keeping the provider workflow reviewable without involving real KYC or real money.

## Secret handling

Secrets that remain outside source and showcase assets include:

- JWT signing keys;
- database and Redis URLs;
- OAuth client secrets;
- Stripe secret and webhook keys;
- email provider keys;
- production host/origin configuration;
- portal signing material.

Both source repositories include lightweight secret scanners in their quality pipelines. The showcase repository also scans documentation and asset names for common accidental credential patterns.

## Environment hardening

### Development

Allows local origins and debug tooling needed for engineering work.

### Test

Uses isolated settings and service containers for repeatable CI.

### Demo

Uses a dedicated approved database, fictional `.test` identities, test payments, and a guarded reset. Demo mode is not an alias for development.

### Production

Configuration validation requires:

- a strong secret key;
- Redis;
- HTTPS non-local frontend and CORS origins;
- explicit trusted hosts;
- disabled debug routes and API documentation;
- production-safe OAuth redirects when enabled;
- production-safe email sender configuration when enabled;
- live Stripe mode and complete live configuration when Stripe is enabled.

## Security verification

Automated protection includes:

- static security-contract checks;
- production-settings tests;
- route authorization inspection;
- portal route and token-isolation tests;
- request-size tests;
- rate-limit behavior tests;
- workspace and participant authorization tests;
- webhook duplicate/idempotency tests;
- secret scans;
- migration and database contract checks.

Manual security QA includes:

- cross-workspace attempts;
- portal-to-staff and staff-to-portal access attempts;
- role restriction checks;
- expired/invalid portal credentials;
- unknown-identity public flows;
- provider cancel/error paths;
- browser console and log review;
- screenshot review for private data.

## OWASP alignment

The project uses relevant OWASP ASVS themes as a review framework for:

- architecture and threat modeling;
- authentication;
- session and token handling;
- access control;
- validation;
- data protection;
- logging and error handling;
- API security;
- configuration;
- business logic.

This is an engineering-control mapping. A formal ASVS assessment or certification would be a separate independent activity.

## Deployment security

A commercial deployment would verify and operate:

- managed database and Redis security;
- TLS and domain configuration;
- real provider credentials and callbacks;
- dependency and container vulnerability scanning;
- monitoring and alerting;
- backup encryption and restore drills;
- incident-response contacts and rotation procedures;
- periodic authorization regression testing.

See [Threat Model](THREAT_MODEL.md), [Operations](OPERATIONS.md), and the root [Security Policy](../SECURITY.md).
