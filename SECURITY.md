# Security Policy

GymFlow's implementation is private, while this repository publishes the product and engineering showcase. Security documentation, release assets, and demonstration material can still receive vulnerability reports when they expose a real issue in the represented system or public repository.

## Supported versions

| Version | Supported |
|---|---|
| Latest tagged showcase release | Yes |
| Current reviewed content on `main` | Yes |
| Active temporary hosted review | Yes, during the stated review window |
| Older screenshots, binaries, or archived releases | Best effort |
| Unofficial copies or modified artifacts | No |

## Reporting a vulnerability

Use GitHub's private vulnerability-reporting flow when it is available:

1. open the repository's **Security** tab;
2. choose **Advisories**;
3. select **Report a vulnerability**;
4. submit the report privately rather than opening a public issue.

If that control is unavailable, contact the repository owner through the GitHub profile and ask for a private reporting channel. Please keep exploit details, credentials, tokens, personal information, and payment data out of public issues.

A useful report includes:

- the affected GymFlow surface or release;
- the route, workflow, artifact, or document involved;
- clear reproduction steps;
- expected and actual behavior;
- security impact;
- sanitized screenshots, request IDs, or logs;
- whether the issue occurred in a local, demo, or hosted environment.

## Coordinated disclosure

Please allow reasonable time to investigate and address a confirmed issue before publishing details. The project owner will aim to:

1. acknowledge a complete report within five business days;
2. confirm whether the issue can be reproduced;
3. communicate the expected remediation or documentation plan;
4. credit the reporter when requested and appropriate.

These response targets are provided for this independent project and are not a commercial SLA.

## Scope

In-scope concerns include:

- unauthorized cross-workspace access;
- portal access to staff/admin data or the reverse;
- authentication, reset, invitation, or portal-code bypass;
- account/client enumeration;
- exposed secrets in source, documentation, images, QR codes, or release assets;
- unsafe redirect or callback handling;
- payment or webhook state manipulation;
- internal staff notes exposed to clients;
- sensitive data in logs, health responses, or error payloads;
- artifact tampering or incorrect release provenance.

Out-of-scope examples include:

- denial-of-service testing against infrastructure not explicitly authorized;
- social engineering;
- attacks against Stripe, Google, GitHub, email, or hosting providers themselves;
- reports based only on infrastructure that has not been deployed for the portfolio environment;
- vulnerabilities in modified third-party copies.

## Safe testing expectations

- Use fictional data only.
- Do not attempt real payments or upload identity documents.
- Do not access another person's account or data.
- Stop when the vulnerability has been demonstrated.
- Preserve request IDs and sanitized context rather than collecting unnecessary data.

## Application security documentation

- [Security Overview](docs/SECURITY_OVERVIEW.md)
- [Threat Model](docs/THREAT_MODEL.md)
- [Architecture](ARCHITECTURE.md)
- [Operations](docs/OPERATIONS.md)

## Secret exposure

If a credential is accidentally published, do not reuse or test it. Report the exact file, commit, release asset, or image privately so it can be revoked and removed from active use.
