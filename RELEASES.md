# GymFlow Releases

This document defines how GymFlow showcase and review releases are versioned, built, verified, and distributed.

## Release goals

A GymFlow release should prove that:

- the documented product exists and works;
- screenshots and video represent a known source state;
- downloadable artifacts are built from that same state;
- demo data is fictional and repeatable;
- provider and production boundaries are stated honestly;
- no source code, credentials, or real client/payment data are exposed.

## Release types

| Release | Purpose | Typical assets |
|---|---|---|
| Showcase | Main public portfolio package | README, docs, screenshots, product video |
| Technical walkthrough | Deeper engineering review | Architecture video, diagrams, manifest |
| Android preview | Installable mobile evaluation | APK, checksum, backend requirement note |
| Windows preview | Desktop evaluation | ZIP/MSIX as applicable, checksum, backend note |
| Hosted review | Temporary interactive review | Time-limited URL and private credentials |
| Documentation-only | Architecture/security update | Docs and diagrams without new binaries |

## Versioning

Recommended naming:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.1.0-showcase
```

Use semantic meaning:

- major: important architecture/product generation;
- minor: significant new product capability or refreshed visual release;
- patch: documentation, release packaging, or non-breaking fixes.

Do not create separate tags for every screenshot update. Keep the release coherent.

## Canonical source snapshot

Every public release must identify:

- showcase repository commit;
- frontend branch and commit;
- backend branch and commit;
- Alembic head revision;
- demo seed contract version/date;
- Flutter/Dart/Python/PostgreSQL/Redis versions;
- build date and operator;
- CI status or run references.

The source snapshot is recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md).

## Required release artifacts

### Always include

- product README;
- architecture, engineering, security, quality, operations, and demo documentation;
- release manifest;
- release notes or changelog;
- known limitations and provider boundary;
- an explicit artifact inventory.

A documentation-only engineering case-study release may omit screenshots and
video when the manifest states that clearly and no stale media remains. A
media-bearing showcase release must include the refreshed screenshot set and
edited product walkthrough.

### Optional

- engineering walkthrough video;
- Android APK;
- Windows build archive;
- screenshot ZIP;
- architecture diagram pack;
- SBOM;
- checksums file;
- temporary hosted review instructions.

## Artifact rules

### Screenshots

- must use fictional deterministic data;
- must come from the release source snapshot;
- must not expose browser tokens, environment files, local user directories, or real identities;
- should use consistent viewport and naming;
- should be reviewed for stale UI and visible errors.

### Video

- must state that payment operations are test/demo only;
- must not show real secrets or card data;
- must not claim provider verification that was not performed;
- should include version/source information in description or closing frame;
- should follow the capture guide in `video/README.md`.

### Android and Windows builds

Installable clients require a reachable backend for full functionality.

Each artifact note must state:

- expected API base URL behavior;
- whether OAuth is configured for that platform;
- whether Stripe redirects work in that release;
- whether the build is for demonstration only;
- checksum;
- exact frontend source commit.

### Hosted review

A temporary hosted demo requires:

- HTTPS frontend and API;
- managed/isolated PostgreSQL;
- managed Redis when production rate limits are expected;
- fictional demo database;
- exact CORS and trusted hosts;
- no live payment processing unless explicitly authorized and verified;
- credentials shared privately, never committed;
- shutdown/cleanup date.

## Release readiness matrix

| Area | Required before showcase tag |
|---|---|
| Frontend CI | Green on canonical frontend commit |
| Backend CI | Green on canonical backend commit |
| Showcase CI | Green on release commit |
| Demo rebuild | Completed successfully |
| Demo validation | All target metrics pass |
| Route rehearsal | No blocking error across recorded routes |
| Logs | No unexplained repeated 404/422/500 during walkthrough |
| Media inventory | Exact included/omitted status recorded |
| Screenshots | Required only for a media-bearing release; then refreshed and privacy-reviewed |
| Product video | Required only for a media-bearing release; then edited and reviewed |
| Manifest | Exact commits and artifacts recorded |
| Secrets | Source/showcase scans pass |
| Provider claims | Match actual release configuration |

## Production-oriented versus production-operated

GymFlow implements:

- strict production settings;
- non-root container packaging;
- separate migration execution;
- liveness/readiness;
- PostgreSQL and Redis expectations;
- security middleware;
- provider configuration validation;
- deployment and incident runbooks.

A live commercial release additionally requires deployment-specific verification:

- hosting and domains;
- managed database/Redis;
- Stripe live/test webhooks;
- verified email sender;
- Google OAuth redirects;
- monitoring and alerting;
- backups and restore drill;
- vulnerability scanning;
- organization-specific legal/privacy operations.

Release notes must not collapse those two states into one unsupported “production-ready” claim.

## Payment release boundary

The public showcase uses:

- fictional payment records;
- Stripe test mode when real provider checkout is shown;
- simulated Connect state when identity onboarding is intentionally skipped;
- no stored payment-card data;
- no real charges.

The well-known Stripe test card may be used only in Stripe's test environment and should not be embedded as a credential or real payment recommendation.

## Email and OAuth release boundary

Email and OAuth status must be declared per release:

| Status | Meaning |
|---|---|
| Disabled | UI/API behavior shown without provider delivery |
| Demo-assisted | Reserved identities use safe code/display behavior |
| Provider test verified | Real test account/inbox and callback verified |
| Production verified | Target production domains/credentials verified |

Do not write “supports email/OAuth” without explaining which release status applies.

## Supply-chain evidence

For releases containing binaries, the target process is:

1. build from documented source commit;
2. run source CI and release checks;
3. generate SHA-256 checksums;
4. generate an SBOM when tooling is available;
5. attach build manifest and checksums;
6. sign/provide provenance when practical;
7. verify downloaded artifact against checksum.

Controls such as CodeQL, dependency review, image scanning, signed provenance, and SBOM publication should only be marked complete after they are enabled.

## Release notes template

```markdown
# GymFlow vX.Y.Z-showcase

## Summary

## Source snapshot
- Showcase:
- Frontend:
- Backend:
- Alembic head:

## Product highlights

## Engineering highlights

## Included assets

## Demo environment

## Verification
- Frontend CI:
- Backend CI:
- Showcase CI:
- Demo validation:
- Manual rehearsal:

## Provider status
- Stripe:
- Email:
- Google OAuth:

## Known limitations

## Security and data statement

## Artifact checksums
```

## Release publication sequence

1. Freeze canonical frontend/backend commits.
2. Update `BUILD_MANIFEST.md`.
3. Rebuild and validate `gymflow_demo`.
4. Run a complete route rehearsal.
5. Capture screenshots.
6. Record and edit videos.
7. Add artifact checksums.
8. Run showcase quality workflow.
9. Review every public claim.
10. Create the Git tag and GitHub release.
11. Verify links and downloads from a logged-out/private-review perspective.

## Rollback and correction

If a published release contains a broken link, leaked information, or misleading claim:

1. remove or replace the affected asset immediately;
2. revoke any exposed credential;
3. publish corrected release notes;
4. create a patch release when artifacts changed;
5. document the correction in `CHANGELOG.md`;
6. do not silently keep a compromised binary available.
