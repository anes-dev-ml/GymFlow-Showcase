# Security Policy

GymFlow is a private-source product showcase. This public repository contains documentation and demonstration assets rather than the application source code or production credentials.

## Supported versions

Security reports are accepted for the latest published GymFlow showcase release and any temporarily hosted review environment explicitly identified as current.

| Version | Supported |
|---|---|
| Latest showcase release | Yes |
| Active temporary hosted review | Yes, during the stated review window |
| Older screenshots, binaries, or archived releases | Best effort |
| Unofficial copies or modified artifacts | No |

## Reporting a vulnerability

Please report suspected vulnerabilities privately to the repository owner instead of opening a public issue.

A useful report includes:

- the affected GymFlow surface or release;
- the route, workflow, artifact, or document involved;
- clear reproduction steps;
- expected and actual behavior;
- security impact;
- screenshots, request IDs, or sanitized logs where relevant;
- whether the issue was observed in a local, demo, or hosted environment.

Do not include real passwords, access tokens, payment data, API keys, or personal information in the report.

## Coordinated disclosure

Please allow reasonable time to investigate and address a confirmed issue before publishing details. The project owner will aim to:

1. acknowledge a complete report within 5 business days;
2. confirm whether the issue can be reproduced;
3. communicate the expected remediation or documentation plan;
4. credit the reporter when requested and appropriate.

These targets are best-effort commitments for a portfolio project, not a commercial security-service SLA.

## Scope

Examples of in-scope concerns include:

- unauthorized cross-workspace access;
- client portal access to staff/admin data;
- staff credentials accessing client-only protected routes;
- authentication, password reset, invitation, or portal-code bypass;
- account/client enumeration in public flows;
- exposed secrets or credentials in this repository or release assets;
- unsafe redirect or callback handling;
- payment or webhook state manipulation;
- internal staff notes exposed to clients;
- sensitive data in logs, screenshots, health responses, or error payloads;
- downloadable artifact tampering or misleading checksums.

Out-of-scope examples include:

- denial-of-service testing against infrastructure not explicitly authorized for testing;
- social engineering;
- attacks against Stripe, Google, GitHub, email providers, or hosting vendors themselves;
- reports based only on missing production infrastructure in a local/demo release;
- vulnerabilities in modified third-party copies of GymFlow artifacts.

## Safe testing expectations

- Use fictional data only.
- Do not attempt real payments.
- Do not upload identity documents.
- Do not access another person's account or data.
- Stop testing when a vulnerability has been demonstrated.
- Preserve request IDs and sanitized evidence rather than collecting unnecessary data.

## Application security documentation

The engineering controls and threat model are documented separately:

- [Security Overview](docs/SECURITY_OVERVIEW.md)
- [Threat Model](docs/THREAT_MODEL.md)
- [Architecture](ARCHITECTURE.md)
- [Operations](docs/OPERATIONS.md)

## Secret exposure

If a credential is accidentally published, do not reuse or test it. Report the exact file, commit, or release asset privately so it can be revoked and removed from active use.
