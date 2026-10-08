# FAIR² Certification

!!! warning "Draft — pending governance"
    The two-tier certification model and the `fair2s:CertificationShape`
    SHACL shape in this document are **drafts**. Three governance questions
    (Decisions A, B, and C at the end of this page) are unresolved. Producers
    and consumers SHOULD NOT rely on the binding semantics of
    `fair2:Certified` or `fair2:Validated` until these decisions
    are finalised by the FAIR² governance body.

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

FAIR²-Validated can be asserted by any FAIR² validator authorised by the
governance body (Clara, or any licensed toolchain). It is a status flag in
the metadata, not a signed credential. It carries no legal or contractual
standing.

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
| `temporal-proof` | RFC 3161 timestamp or blockchain anchor attached |

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

!!! warning "No schema yet for `fair2-cert.json` or the registry"
    Neither the credential document nor the registry has a published schema or
    example, and whether `fair2-cert.json` is a W3C Verifiable Credential (VC
    Data Model 2.0, with the certifier DID as `issuer` and a `proof`) is **not
    yet decided** — it depends on Decisions A, B and C below. Implementers
    should not build against either format until that is settled. The
    `Certification` pointer node inside `fair2.json`, described above, is
    stable and can be relied on.

---

## Open governance decisions

The following design questions are **unresolved**. The certification
semantics described above are provisional pending these decisions.

### Decision A — Scope label for partial certification

Does metadata-only scope still carry the `fair2:Certified` compliance
level, or should restricted-data packages receive a distinct label (e.g.,
`fair2:FAIR2-Certified-Metadata`)? Implications: discoverability, consumer
trust, and whether partial certification is a first-class status or a
downgrade.

### Decision B — Self-assertability of FAIR²-Validated

Can a data producer run a conformant validator locally and embed
`fair2ComplianceLevel: "fair2:Validated"` in their own metadata
without involving an authorised validator? If yes, Validated is a
declaration, not a credential — low trademark exposure but potential brand
dilution. If no, even Validated requires an authorised issuer (a
lighter-weight one), which adds friction but protects the brand.

### Decision C — Expiry model

Are certifications permanent (revocation-only invalidation) or do they
expire annually and require re-certification? Annual expiry strengthens
trust but imposes ongoing operational burden on producers and certifiers.
