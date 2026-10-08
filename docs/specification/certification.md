# FAIR² Certification

## Overview

FAIR² defines two distinct statuses for a dataset package:

- **FAIR²-Validated** — a *quality status* asserting that all automated
  conformance checks pass.
- **FAIR²-Certified** — an *authority assertion* backed by a
  cryptographically signed credential from an authorised certifier.

The distinction is **who vouches for the package**, not the level of
automation used during verification. A fully automated pipeline operated by
an authorised certifier produces a valid FAIR²-Certified credential.

---

## FAIR²-Validated

An assertion that the following automated checks all passed:

- SHACL validation against the declared FAIR² compliance level — 0 errors,
  0 warnings
- All required metadata fields present and correctly typed
- `_meta.version` and `_meta.dateModified` current
- `license` URI resolves and is consistent with the declared `accessRights`
- All `distribution` SHA-256 checksums declared (not necessarily verified
  against actual file downloads)

FAIR²-Validated is **self-assertable**: any producer may run a conformant
validator and embed the claim, with no authorised issuer involved
(Decision B). What it must carry instead is its evidence — the profile
validated against, the validation run and its software agent, and the
report — so that a consumer can inspect the claim rather than trust it.
See [Making the claim inspectable](#making-the-claim-inspectable).

It is a status flag in the metadata, not a signed credential, and carries
no legal or contractual standing.

---

## FAIR²-Certified

An assertion backed by a cryptographically signed credential issued by an
authorised certifier. In addition to everything required for
FAIR²-Validated:

- The credential is signed by a DID listed in the FAIR² authorised-certifier
  registry (see [Authorised certifiers](#authorised-certifiers))
- `certificationScope` is explicitly declared (see below)
- `certificationDocument` points at an external `fair2-cert.json` file whose
  signature verifies
- `certifiedBy` references an authorised `Organization` with a resolvable
  identifier

---

## `certificationScope`

`certificationScope` is a required array of tokens on both the
`Certification` pointer node (inside `fair2.json`) and the full credential
(in `fair2-cert.json`). It declares exactly what was verified during
certification, so consumers can make access decisions without fetching the
external credential.

### Canonical vocabulary

| Token | Meaning |
|-------|---------|
| `metadataConformance` | SHACL validation passed at the declared compliance level |
| `dataIntegrity` | SHA-256 checksums verified against actual file downloads |
| `licenseVerification` | License URI resolves; access rights consistent with declared level |
| `processAttestation` | Provenance activity and software-agent records reviewed |
| `temporalProof` | RFC 3161 timestamp or blockchain anchor attached |

### Standard scope combinations

- **Full scope** (recommended for Level 0 / open access):
  `["metadataConformance", "dataIntegrity", "licenseVerification", "processAttestation"]`
- **Metadata-only** (restricted datasets where the certifier has no access
  to the files): `["metadataConformance", "licenseVerification"]`

---

## The pointer node in `fair2.json`

A lightweight `Certification` node is embedded in the Dataset's graph so
consumers can assess certification status without fetching the full
credential:

```json
{
  "@id": "certification/fair2-cert-2026",
  "@type": "Certification",
  "certifiedBy": {
    "@type": "Organization",
    "name": "Senscience",
    "identifier": "https://sen.science/"
  },
  "dateIssued": "2026-04-16",
  "fair2ComplianceLevel": "fair2:Certified",
  "certificationDocument": "https://sen.science/certifications/10.71728/r1rj-f947/fair2-cert.json",
  "verificationEndpoint": "https://sen.science/certifications/10.71728/r1rj-f947",
  "certificationScope": [
    "metadataConformance",
    "dataIntegrity",
    "licenseVerification",
    "processAttestation"
  ]
}
```

---

## Making the claim inspectable

`fair2ComplianceLevel` on its own is a single token: a consumer can trust it or
re-run the checks, but cannot inspect it. A `Certification` node SHOULD
therefore also record **what was checked, by what, and where the evidence is**,
using vocabulary FAIR² already uses elsewhere:

| Property | Meaning |
|---|---|
| `dct:conformsTo` | The spec or profile version validated against, as a resolvable `https://fair2.ai/spec/vX.Y.Z` URI |
| `prov:wasGeneratedBy` | The validation run, carrying the validator as a `prov:SoftwareAgent` with its version |
| `fair2:validationReport` | The report backing the claim |

This is the same provenance pattern the Data Dictionary uses for descriptive
statistics, so consumers that already read one can read the other.

```json
{
  "@id": "certification/fair2-cert-2026",
  "@type": "Certification",
  "fair2ComplianceLevel": "fair2:Validated",
  "conformsTo": "https://fair2.ai/spec/v1.3.0",
  "validationReport": "https://sen.science/certifications/10.71728/r1rj-f947/report.json",
  "wasGeneratedBy": {
    "@type": "Activity",
    "label": "FAIR2 conformance validation",
    "endedAtTime": "2026-04-16",
    "wasAssociatedWith": {
      "@type": "SoftwareAgent",
      "name": "fair2-validator",
      "softwareVersion": "0.9.2",
      "identifier": "https://github.com/fair-squared/fair2-validator"
    }
  }
}
```

These three properties are **optional** in `fair2s:CertificationShape`.
Requiring them would invalidate every certification issued to date; they are
expected to become required in a later release.

---

## Authorised certifiers

`fair2:AuthorizedCertifier` is a governance concept. An authorised certifier
is any entity whose DID appears in the FAIR² certifier registry, maintained
by the FAIR² governance body. Senscience is the primary authorised
certifier; third parties may apply for certification authority under a
trademark licence.

### Governance rules

- **Conflict of interest.** A funder of a dataset MUST NOT be the certifier
  of that same dataset. The `funding[].funder` list MUST NOT overlap with
  `certifiedBy`.
- **Scope limitation for restricted data.** Certifiers without access to
  the data files MUST declare `certificationScope` as
  `["metadataConformance", "licenseVerification"]` only.
- **Non-commercial licence rule.** Third-party certifiers operating under
  the non-commercial FAIR² trademark licence MUST NOT certify datasets
  hosted on commercial platforms without upgrading to a commercial licence.

### Registry format

The registry is a JSON-LD document published at
`https://fair2.ai/certifiers/registry.json`. Each entry carries the
certifier's DID, organisation name, licence tier, allowed certification
scope, and validity period.

!!! warning "Formats not yet published"
    The credential document and the registry do not yet have published
    schemas or examples. The governance decisions they depend on are settled
    (see below) and the formats follow from them: `fair2-cert.json` will be a
    W3C Verifiable Credential (VC Data Model 2.0) with the certifier's DID as
    `issuer`, carrying `validFrom` and no `validUntil` per Decision C, and
    revocation through a Bitstring Status List. Implementers should not build
    against the exact shape until it is published. The `Certification`
    pointer node inside `fair2.json`, described above, is stable.


---

## Verifying a certification

Given a `Certification` pointer node in a `fair2.json`:

1. **Resolve the issuer.** Fetch `certificationDocument`, read its `issuer`
   DID, and resolve the DID document to obtain the signing key.
2. **Check authority at the issuance date.** Fetch the
   [certifier registry](#registry-format) and confirm the issuer DID has an
   entry whose `validFrom`/`validUntil` span the credential's `validFrom`,
   and whose `allowedScopes` cover the declared `certificationScope`.
   Authority is checked at **issuance**, not at verification time — a
   certification issued while the certifier was authorised stays valid after
   that authority lapses (Decision C).
3. **Verify the proof** on the credential against the resolved key.
4. **Check revocation** through the credential's `credentialStatus`
   Bitstring Status List. There is no expiry to check; `validUntil` is
   deliberately absent.
5. **Recompute the digests** and compare, in the order given under
   [What a certification is bound to](#what-a-certification-is-bound-to):
   the byte digest first, the graph digest only if it fails.

A **FAIR²-Validated** claim is verified differently, because it has no
issuer and no credential: re-run the validator named in `wasGeneratedBy`
against the profile named in `conformsTo`, and compare with
`validationReport`. It cannot be revoked — only contradicted.


---

## What a certification is bound to

Decision C binds a certification to one exact package version: the DOI, the
package version, and a digest of the `fair2.json`. It carries **two**
digests, because "the same file" and "the same content" are different
claims and neither alone is enough.

| Property | Covers | Cost to verify |
|---|---|---|
| `sec:digestMultibase` | the published bytes | ~0.1 ms, `sha256sum` |
| `fair2:graphDigestMultibase` | the RDFC-1.0 canonical graph | ~90 ms, needs a JSON-LD processor |

```json
"credentialSubject": {
  "id": "https://doi.org/10.71728/r1rj-f947",
  "conformsTo": "https://fair2.ai/spec/v1.4.0",
  "metadataVersion": "1.0.0",
  "digestMultibase":      "uEiDixlVqFfWrgYrq6dQttW6sa336WgzxLL3YxsyIxAFsYQ",
  "graphDigestMultibase": "uEiCdaRhI_cl636VHp2O5fmXhaTiciRWa40UiHLMl5JoVAQ"
}
```

Both are multibase-encoded multihashes (`u` = base64url, `0x12 0x20` =
sha2-256). The graph digest is taken over the canonical n-quads produced by
[RDFC-1.0](https://www.w3.org/TR/rdf-canon/).

### Verify in that order

1. **Byte digest matches.** Done. This is the common case and it costs
   nothing — anyone with `sha256sum` can check it, with no JSON-LD stack and
   no network.
2. **Byte digest fails, graph digest matches.** The file was reformatted,
   minified or round-tripped through a JSON-LD tool; the description is
   intact. Report **equivalent, not identical** — a warning, not a failure.
3. **Both fail.** The package has changed. Per Decision C the certification
   no longer applies, and the new version needs its own.

### Why not one digest

A byte digest alone reports any reserialisation as tampering: pretty-print
the file, or let a JSON-LD library round-trip it, and verification fails
although nothing changed. A graph digest alone is blind to anything outside
the RDF — and is 900× more expensive, which matters when the check runs on a
landing page or in a crawler.

!!! note "Why the graph digest became worth having"
    Before v1.4.0 a graph digest would have been actively misleading: the
    `_meta` block was deliberately outside the RDF, so changing
    `_meta.version` left the graph digest untouched. With `_meta` folded onto
    the Dataset, everything material is in the graph, and the two digests
    now differ only in what kind of change they tolerate rather than in what
    they can see.

---

## Governance decisions

These were open questions in v1.3.0 and are now settled. They are recorded
here because they determine what a certification means.

### A — One label; the scope says what was checked

There is a single compliance level, `fair2:Certified`, and no
`-Metadata` variant. `certificationScope` (already required) is how a
certification says what was checked.

When the scope does not include `dataIntegrity`, any human-readable
rendering — badges, landing pages, search snippets — **MUST** display
**"FAIR²-Certified (metadata only)"**.

A certifier without access to the files **MUST** use the metadata-only
scope.

*Rationale:* the label says who vouches, the scope says what was checked.
A restricted dataset is not downgraded because its certifier cannot read
the files.

!!! note "This rule is on consumers, not on documents"
    SHACL constrains `certificationScope` to the four canonical tokens, so a
    typo fails validation. It cannot check how a badge is rendered. The
    display rule is a requirement on consuming software and nothing in this
    repository can enforce it.

### B — FAIR²-Validated can be self-asserted, as an inspectable claim

Any producer may run a validator and embed `fair2:Validated`. No
authorised issuer is needed.

A Validated node **MUST** carry:

- `conformsTo` — a resolvable `https://fair2.ai/spec/vX.Y.Z` URI;
- `wasGeneratedBy` — an Activity with `endedAtTime`, associated with a
  SoftwareAgent that has `name` and `softwareVersion`;
- `validationReport`.

It needs no `certifiedBy`, no `certificationDocument` and no signature,
and makes no trademark claim beyond "these open checks passed".

**Transition.** Existing Validated nodes that carry `certifiedBy` and
`dateIssued` but lack the evidence properties stay valid for now. That
path is deprecated, raises a SHACL warning, and will be removed in a later
release.

*Rationale:* the difference between the two statuses is who vouches. The
brand is protected by Certified's signature, and Validated by being
re-runnable.

!!! note "Two consequences worth stating"
    `fair2s:ActivityShape` requires `rdfs:label`, so the evidence Activity
    needs a label as well as the properties listed above.

    A self-asserted Validated claim has no issuer and no credential, so it
    **cannot be revoked** — Decision C's revocation model reaches Certified
    only. A Validated claim is withdrawn by re-running the checks and
    finding they no longer pass.

### C — Bound to the package version, not to the calendar

A certification attests to one exact package version: the DOI, the package
version and a digest of `fair2.json`. It has no calendar expiry
(`validUntil` is omitted).

It stops applying when either:

- it is revoked through a Bitstring Status List; or
- the package changes, so the digest no longer matches and the new version
  needs a new certification.

Certifier authority entries in the registry have `validFrom` / `validUntil`
and are renewed annually. A certification issued while the certifier was
authorised stays valid after that authority lapses, unless it is revoked —
**verifiers check authority at the issuance date**.

A newer spec version does not invalidate a certification; `conformsTo`
records which version applied.
