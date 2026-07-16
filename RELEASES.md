# GymFlow Releases

This document defines how GymFlow showcase and review releases are versioned,
verified, and distributed.

## Release goals

A GymFlow release should prove that:

- the documented product corresponds to an exact source snapshot;
- any included screenshots, video, or binaries represent that same snapshot;
- demo data is fictional and repeatable;
- provider and production boundaries are stated honestly;
- no source code, credentials, or real client or payment data are exposed;
- validation evidence is recorded without claiming checks that did not run.

## Release types

| Release | Purpose | Typical assets |
|---|---|---|
| Documentation-only engineering case study | Architecture, product, security, quality, operations, and provenance review | README, documentation, manifest, changelog |
| Media-bearing showcase | Main visual portfolio package | Documentation, current screenshots, edited product video |
| Technical walkthrough | Deeper engineering review | Architecture video, diagrams, manifest |
| Android preview | Installable mobile evaluation | APK, checksum, backend requirement note |
| Windows preview | Desktop evaluation | ZIP or MSIX, checksum, backend note |
| Hosted review | Temporary interactive review | Time-limited URL and privately shared credentials |

The `v1.0.0-showcase` tag is a documentation-only engineering case study. It
intentionally contains no current screenshots, public video, thumbnail, or
installable binary.

## Versioning

Recommended naming:

```text
v1.0.0-showcase
v1.0.1-showcase
v1.1.0-showcase
```

Use semantic meaning:

- **major**: important architecture or product generation;
- **minor**: significant new product capability or refreshed media release;
- **patch**: documentation, release packaging, or non-breaking corrections.

Do not create separate tags for every screenshot update. Keep each release
coherent and provenance-backed.

## Canonical source snapshot

Every public release must identify:

- showcase repository branch and tag or commit;
- frontend branch and commit;
- backend branch and commit;
- Alembic head revision;
- demo seed contract date or version;
- relevant runtime and dependency versions;
- validation date and evidence;
- exact included and omitted artifacts;
- known limitations and provider boundaries.

The source snapshot is recorded in [BUILD_MANIFEST.md](BUILD_MANIFEST.md).

### Validation evidence rule

The preferred evidence is green GitHub Actions on the canonical commits. When a
hosted runner cannot start because of a documented account-level or platform
restriction, a release may use equivalent local validation only when all of the
following are true:

1. the failure occurs before repository checkout or code execution;
2. the reason is recorded in the build manifest;
3. the equivalent release commands are completed locally;
4. the release does not claim green hosted CI;
5. the source commits and local validation scope are recorded exactly.

A code failure, test failure, configuration failure inside a running job, or
missing local dependency is not an acceptable reason to bypass a quality gate.

## Required release artifacts

### Always include

- product README;
- architecture, engineering, security, quality, operations, and demo documentation;
- release manifest;
- changelog or release notes;
- known limitations and provider boundary;
- explicit artifact inventory;
- validation evidence or an honest validation limitation.

A documentation-only release may omit screenshots and video when the manifest
states that clearly and no stale media remains. A media-bearing showcase must
include only refreshed, privacy-reviewed assets tied to the documented source
snapshot.

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

Screenshots must:

- use fictional deterministic data;
- come from the release source snapshot;
- exclude credentials, access codes, environment values, local user paths, and private browser data;
- avoid error banners, loading hangs, overflow markers, debug overlays, and unfinished dialogs;
- use test or demo payment state only;
- use consistent viewports and filenames;
- be reviewed for stale UI and visible errors.

### Video

Video must:

- state that identities and payments are fictional or test/demo only;
- exclude real secrets, card data, access codes, personal paths, and unrelated desktop content;
- avoid provider claims that were not verified;
- identify the release source snapshot in its description or closing frame;
- follow the capture guide in `video/README.md`.

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
- isolated or managed PostgreSQL;
- managed Redis when production rate limits are expected;
- fictional demo database;
- exact CORS and trusted-host configuration;
- no live payment processing unless explicitly authorized and verified;
- credentials shared privately and never committed;
- a shutdown and cleanup date.

## Release readiness matrix

| Area | Required before a documentation-only showcase tag | Required before a media-bearing tag |
|---|---|---|
| Frontend validation | Green hosted CI, or documented equivalent local validation under the exception rule | Same, rerun on the media source snapshot |
| Backend validation | Green hosted CI, or documented equivalent local validation under the exception rule | Same, rerun on the media source snapshot |
| Showcase validation | Green hosted CI, or `python scripts/check_showcase.py` completed locally under the exception rule | Same, after media is added |
| Demo rebuild | Required when the release claims current demo behavior | Required immediately before capture |
| Demo validation | Required when the release claims deterministic metrics | Required immediately before capture |
| Route rehearsal | Required when product behavior is being demonstrated | Required before capture |
| Error review | No unexplained blocking application error in the validated scope | No repeated 404, 422, or 500 during the recorded walkthrough |
| Media inventory | Exact included and omitted status | Exact filenames, URLs, durations, and checksums where applicable |
| Screenshots | May be explicitly omitted | Refreshed and privacy-reviewed |
| Product video | May be explicitly omitted | Edited and reviewed |
| Manifest | Exact commits, versions, evidence, and artifact boundary | Updated after capture |
| Secrets | Showcase and source safety checks pass | Repeat after all assets are added |
| Provider claims | Match actual release configuration | Match what is visible in captured media |

## Production-oriented versus production-operated

GymFlow implements production-oriented controls such as:

- strict production settings;
- non-root container packaging;
- separate migration execution;
- liveness and readiness checks;
- PostgreSQL and Redis expectations;
- security middleware;
- provider configuration validation;
- deployment and incident runbooks.

A live commercial release additionally requires deployment-specific evidence:

- hosting and domains;
- managed database and Redis;
- Stripe webhooks and account configuration;
- verified email sender;
- Google OAuth redirects;
- monitoring and alerting;
- backups and restore drill;
- vulnerability scanning;
- organization-specific legal and privacy operations.

Release notes must not collapse these states into an unsupported
“production-ready” or “production-operated” claim.

## Payment release boundary

The public showcase uses:

- fictional payment records;
- Stripe test mode when provider checkout is shown;
- simulated Connect state when identity onboarding is intentionally skipped;
- no stored payment-card data;
- no real charges.

The well-known Stripe test card may be used only in Stripe's test environment
and should never be presented as a real credential or payment recommendation.

## Email and OAuth release boundary

Email and OAuth status must be declared per release:

| Status | Meaning |
|---|---|
| Disabled | UI or API behavior is shown without provider delivery |
| Demo-assisted | Reserved identities use guarded code or display behavior |
| Provider test verified | A real test account, inbox, and callback were verified |
| Production verified | Target production domains and credentials were verified |

Do not write that a release “supports email or OAuth” without explaining which
status applies.

## Supply-chain evidence

For releases containing binaries, the target process is:

1. build from the documented source commit;
2. run source and release checks;
3. generate SHA-256 checksums;
4. generate an SBOM when tooling is available;
5. attach the build manifest and checksums;
6. sign or provide provenance when practical;
7. verify the downloaded artifact against its checksum.

CodeQL, dependency review, image scanning, signed provenance, and SBOM
publication must only be marked complete after they are actually enabled and
verified.

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

## Omitted assets

## Demo environment

## Validation
- Frontend:
- Backend:
- Showcase:
- Hosted-runner limitation, if any:
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

## Publication sequence

### Documentation-only release

1. Freeze canonical frontend and backend commits.
2. Complete the applicable frontend and backend validation.
3. Update `BUILD_MANIFEST.md`.
4. Review all public claims and provider boundaries.
5. Remove stale or unproven media.
6. Run the showcase validator.
7. Publish the final showcase snapshot to `main`.
8. Create the Git tag and GitHub release.
9. Verify repository links from a logged-out or private-review perspective.
10. Configure the social preview and repository metadata before public promotion.

### Media-bearing release

1. Complete the documentation-only sequence through manifest preparation.
2. Rebuild and validate `gymflow_demo`.
3. Run a complete route rehearsal.
4. Capture and privacy-review screenshots.
5. Record, edit, caption, and review video.
6. Add exact inventories, URLs, and checksums.
7. Rerun validation after all assets are committed.
8. Create a new semantic tag and release.

## Rollback and correction

If a published release contains a broken link, leaked information, or misleading
claim:

1. remove or replace the affected asset immediately;
2. revoke any exposed credential;
3. publish corrected release notes;
4. create a patch release when public artifacts changed;
5. document the correction in `CHANGELOG.md`;
6. never silently keep a compromised binary available.