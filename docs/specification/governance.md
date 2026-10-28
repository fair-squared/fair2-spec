# Governance

A `fair2.json` can declare **who may access the data and on what terms**: an
access tier, the conditions layered on top of it, the uses the data may and may
not be put to, and finer rules for individual columns, files or records. These
declarations are the dataset's **governance blocks**.

Governance is **optional**. A document without governance blocks is valid, and
is read as open data.

The blocks follow the FAIR² governance model, which governance services
enforce: they encrypt governed data, release keys only to requesters who meet
every declared requirement, and keep an audit trail. This page defines what a
`fair2.json` declares and how a reader interprets it. How a service enforces it
(key hierarchies, custodians, signing ceremonies, audit) is outside this
specification.

!!! note "New in v1.7.0 — replaces the Agreement Levels"
    Up to v1.6.3 access was described by Agreement Levels 0–6 under
    `dct:accessRights`. They had no machine-readable form beyond a label, and
    governance services do not read them. They are deprecated; see
    [Migrating from Agreement Levels](#migrating-from-agreement-levels).

---

## Where the blocks go

Governance blocks are properties of the Dataset, at the top level of
`fair2.json` beside `license` and `accessRights`:

```json
{
  "@context": { "...": "..." },
  "@id": "https://doi.org/10.1234/dataset",
  "@type": "Dataset",
  "name": "...",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "fair2:access": { "tier": "L1" },
  "fair2:constraints": { "aiTraining": "prohibited" }
}
```

Write the keys **with their prefix** (`fair2:access`, not `access`). That is the
form governance services, FAIR² Discovery and the data wrangler read.

Each block is a **JSON value**: the context types it `@json`, so in RDF it is a
single `rdf:JSON` literal and the keys inside it (`tier`, `purposeBinding`, …)
are data, not vocabulary terms. That keeps a block byte-for-byte what its author
wrote — governance services sign the JSON — and lets the governance model add
fields without a new release of this vocabulary. The contents of each block are
defined by the governance JSON Schema
(`schemas/fair2-governance.schema.json`; see [Validation](#validation)).

| Key | Declares |
|---|---|
| `fair2:access` | The access tier, and the conditions on access (modifiers +G, +S, +C, +P, +J, +Q) |
| `fair2:constraints` | Use constraints: AI training, export, commercial use, combination with other data |
| `fair2:embargo` | A date before which governed data is not released |
| `fair2:variableGovernance` | Tiers and rules for individual columns, files, asset classes and record partitions |
| `fair2:temporalGovernance` | Access that changes over time |
| `fair2:agentGovernance` | Whether and how AI agents may use the data |
| `fair2:consentGovernance` | How participants' consent withdrawals affect access |
| `fair2:indigenousGovernance` | Indigenous governance framework, bodies and cultural protocols |
| `fair2:distributionGovernance` | How keys reach recipients when data is shipped outside a broker network |
| `fair2:encryption` | How the data is encrypted — written by the governance service, not by hand |

---

## Reading rules

These rules are normative. They match how governance services and FAIR²
Discovery read a document.

1. **No tier means L0.** A document without `fair2:access`, or whose
   `fair2:access` has no `tier` (or a `tier` of `null` or `""`), is **L0 —
   open**.
2. **A published dataset states its tier.** A document submitted to a
   governance service for publication MUST carry `fair2:access` with an
   explicit `tier`, including `"L0"`, so that the access level is a decision
   rather than a default. A document that declares any restriction (a modifier,
   an embargo, use constraints) SHOULD state its tier.
3. **There are three tiers:** `L0`, `L1`, `L2`. Any other value (`L3`, an
   Agreement Level) is invalid.
4. **Restrictions need governed data.** Modifiers, embargo and consent
   enforcement act through key release, so they apply only to data at L1 or
   above. On a dataset whose data is all L0 they are an error. A dataset may
   mix tiers: L0 columns are served openly while the restrictions govern its
   L1+ columns.
5. **Use constraints always apply.** `fair2:constraints` binds every use,
   including of L0 data, contractually; for L1+ data a governance service also
   checks some of them before releasing keys.

---

## Access tiers

`fair2:access.tier` is the dataset's **floor**: a requester below it receives
nothing. Above it, a requester reaches every asset tagged at or below their own
standing, so per-asset tiers (see [Per-asset governance](#per-asset-governance))
apply to whoever qualifies.

| Tier | Label | Requires |
|---|---|---|
| `L0` | Open | Nothing. Data is distributed unencrypted; the governance blocks carry licence, citation and use terms but do not gate access. |
| `L1` | Registered | An authenticated identity (login) and acceptance of the terms. |
| `L2` | Credentialed | The dataset's `credentialRequirements` — by default a signed data use agreement (DUA). |

`fair2:access` refines the identity a requester must present:

| Field | Meaning |
|---|---|
| `credentialRequirements` | What L2 requires, composed from `dua_acceptance`, `institutional_affiliation`, `ethics_training` and `identity_assurance:<level>`. Default `["dua_acceptance"]`. |
| `identityAssurance` | Minimum assurance, from weakest to strongest: `authenticated`, `provider_verified`, `institutional`, `independent`. |
| `identity.required` | Credentials required at any tier: `verified_identity`, `institutional_affiliation`, `dua`, `ethics_training`. |
| `identity.acceptedIssuers` | Identity providers accepted, e.g. `https://orcid.org`. |

```json
"fair2:access": {
  "tier": "L2",
  "credentialRequirements": ["dua_acceptance", "institutional_affiliation", "ethics_training"],
  "identityAssurance": "institutional"
}
```

The tiers are also published as terms — `fair2:L0`, `fair2:L1`, `fair2:L2` —
so that `accessRights` can name one for consumers that read Dataset metadata
without the governance blocks (see [Related properties](#related-properties)).

---

## Modifiers

Six modifiers add conditions to access, inside `fair2:access`. They compose
freely with any tier from L1 up and with each other, and are evaluated after the
tier and identity checks: meeting the tier never bypasses a modifier.

### +G — community governance

`communityGovernance` puts access under community oversight, the principal
mechanism for the CARE principle of Authority to Control.

| Value | Effect |
|---|---|
| `none` | No community governance. |
| `consultationRecommended` | Advisory; does not gate access. |
| `consultationRequired` | Access needs community approval (by default one approval). |
| `communityApprovalRequired` | As `consultationRequired`. |

The value is a string, or an object naming the approvers:

```json
"communityGovernance": {
  "requirement": "consultationRequired",
  "requiredApprovers": ["0000-0002-1825-0097"],
  "minimumApprovals": 2
}
```

### +S — secure environment

`environment` constrains where the data may be processed.

| Value | Effect |
|---|---|
| `open` | No restriction (default). |
| `secureHuman` | A secure, human-operated environment. |
| `computeToData` | Computation goes to the data; only results leave. |
| `hybrid` | Some operations local, some in a secure environment. |
| `verified` | A registered, hardware-attested environment (TEE or TRE); `environmentPolicy` lists the accepted types (`tee`, `tre`) and environments. |

### +C — client certification

`clientCertification: "required"` limits access to client software holding a
valid certificate; `acceptedCertifiers` lists the certifiers' DIDs.

### +P — purpose binding

`purposeBinding` requires the requester to state why they need the data.

| `requirement` | Effect |
|---|---|
| `none` | No purpose needed. |
| `declared` | At least one purpose; it must match `allowed` (when listed) and none may match `prohibited`. |
| `verified` | As `declared`, and the purpose must have been independently verified, e.g. by an ethics board. |

Purposes are W3C [DPV](https://w3id.org/dpv) terms (`dpv:AcademicResearch`,
`dpv:ClinicalResearch`, …). Codes from GA4GH DUO, HIPAA and GDPR are accepted
and read as their DPV equivalents; a narrower purpose satisfies a broader one
(`dpv:ClinicalResearch` meets `dpv:AcademicResearch`).

### +J — jurisdiction

`jurisdiction` restricts where processing may happen — a property of the
processing environment, not of the requester.

```json
"jurisdiction": { "requirement": "required", "accepted": ["EU", "CA"] }
```

`accepted` holds ISO 3166-1 alpha-2 codes or region identifiers such as `EU`.

### +Q — query governance

`queryGovernance` controls how the data may be queried.

| Field | Meaning |
|---|---|
| `enabled` | Whether query governance applies. |
| `tierRules` | Per tier (`L1`, `L2`): `granularity` (`individual`, `grouped`, `aggregated`, `none`), `minGroupSize`, `allowedOperations`, `deniedColumns`. |
| `linkagePolicy` | Joining with other datasets: `unrestricted`, `sameStudy` (same `studyId`), `approved` (listed in `approvedLinkages`), `prohibited`. |
| `derivationRegistration` | Whether query results must be registered as governed derivations: `none`, `encouraged`, `required`. |

---

## Use constraints

`fair2:constraints` states how the data may be used, whatever the tier.

| Field | Values | Default |
|---|---|---|
| `aiTraining` | `allowed`, `restrictedWithConditions`, `prohibited` | `allowed` |
| `exportRestriction` | `none`, `aggregated-only`, `anonymized-only`, `derived-parameters-only` | `none` |
| `commercialUse` | `allowed`, `nonCommercialOnly` | `allowed` |
| `combination` | an object, below | — |

`combination.policy` governs combining the dataset with others:
`unrestricted`, `sameSteward`, `approved` (with the datasets in
`approvedDatasets`, or after approval from `requiresApprovalFrom`), or
`prohibited`.

The constraints bind through the data use agreement. For governed data a
governance service also refuses keys when a request conflicts with
`aiTraining: "prohibited"` or `commercialUse: "nonCommercialOnly"`, and both
propagate to derived datasets, most restrictive first.

`aiTraining: "prohibited"` is equivalent to prohibiting the purpose
`dpv:AITraining`, and `commercialUse: "nonCommercialOnly"` to prohibiting
`dpv:CommercialResearch`.

---

## Embargo

`fair2:embargo` withholds governed data until a date. Metadata stays public,
so the dataset remains discoverable and citable.

```json
"fair2:embargo": {
  "until": "2027-02-11T00:00:00Z",
  "exemptSubjectIds": ["0000-0002-3606-7974"]
}
```

`exemptSubjectIds` names the people the embargo does not apply to, such as the
team that produced the data. An embargo applies to L1+ data only.

---

## Per-asset governance

`fair2:variableGovernance` sets tiers below the dataset level. Despite the
name, an entry may be a column, a file, a directory or any other asset.

| Field | Meaning |
|---|---|
| `floorTier` | The tier of any asset not listed, or listed without a `tier`. Default **`L1`**; `L0` leaves unlisted assets unencrypted. A listed tier below the floor is raised to it. |
| `variables` | Per asset, keyed by column name or path: `tier`, `encrypted` (default `true`; `false` publishes it in the clear), `exportRestriction`, `allowedPurposes`, `prohibitedPurposes`, `personalDataCategory` (a DPV personal-data category such as `dpv-pd:Health`) and `legalBasis`. |
| `assetClasses` | Tiers by kind of asset: `tier` (required), `formats`, `description`. |
| `partitions` | Tiers for sets of records: `name` and `tier` (required), the `table` they apply to, and `criteria` — conditions on columns (`column`, `op`, `value`, `includeNull`) with operators `=`, `!=`, `<`, `>`, `<=`, `>=`, `in`, `not_in`. |

```json
"fair2:variableGovernance": {
  "floorTier": "L1",
  "variables": {
    "year": { "encrypted": false },
    "diagnosis": { "tier": "L1" },
    "patient_id": { "tier": "L2" },
    "scan_images/": { "tier": "L2" }
  },
  "partitions": [
    { "name": "pediatric", "tier": "L2", "table": "patients",
      "criteria": [{ "column": "age", "op": "<", "value": 18 }] }
  ]
}
```

A partition with no `table` applies to every table, and must be evaluable on
each: a table that lacks a criteria column is refused rather than served
unfiltered.

---

## Temporal governance

`fair2:temporalGovernance.phases` changes access over time. The first phase
that matches the current date applies; each phase has `until` or `after`, and
overrides the `tier` and, optionally, the `environment`.

```json
"fair2:temporalGovernance": {
  "phases": [
    { "until": "2027-01-01T00:00:00Z", "tier": "L2" },
    { "after": "2027-01-01T00:00:00Z", "tier": "L1" }
  ]
}
```

---

## Agents, consent and Indigenous governance

**`fair2:agentGovernance`** governs AI agents acting for a person.

| Field | Meaning |
|---|---|
| `policy` | `direct`, `planOnly`, `planAndApprove` (default), `algorithmicOnly`, `prohibited`. Only `prohibited` is enforced at key release; the others bind the client that runs the agent. |
| `ceilingTier` | The highest tier an agent may reach, whatever its principal's standing. Default `L2`. |
| `purposeBinding` | The DPV purposes an agent may declare. |

**`fair2:consentGovernance`** sets how participants' consent withdrawals act:
`enforcement` is `informational` (default), `enforced` (withdrawals above
`blockThreshold` block access) or `row_level` (withdrawn records are excluded);
`withdrawalPolicy` names the handling, e.g. `block_future_releases`.

**`fair2:indigenousGovernance`** records the `framework` (e.g. `CARE`, `OCAP`),
the `governanceBodies` with their roles (`advisory`, `veto`, `approval`) and
`culturalProtocols`, such as a seasonal restriction on access. Naming a
framework does not by itself configure community control: combine it with +G
and L1+ data.

---

## Encryption and distribution

These blocks are written by a governance service, not by the dataset's author.

**`fair2:encryption`** records how governed data is encrypted: the `algorithm`
(e.g. `AES-256-GCM`), the `keyBrokers` that release keys, the key `governance`
model and its `threshold` (`k` of `n`), and `distributions` — per file, its key,
tier and `format` (`envelope`, a whole-file key, or `parquet-modular`, a key per
column). A file listed there is encrypted; a file absent from it is not.

**`fair2:distributionGovernance`** applies when data is shipped outside a broker
network: the `mode` (default `broker-network`), named `recipients`, the DUA
(`duaReference`), a `withdrawalChannel` and, for community-governed data, the
`communityResolution` that approved the recipients.

A governance service may also add `fair2:retraction` or `fair2:tombstone` when a
dataset is withdrawn or erased, and signs the document (`fair2:proof`). These
are part of the service's lifecycle, not of what an author declares.

---

## Complete example

```json
{
  "@context": { "...": "..." },
  "@id": "https://doi.org/10.1234/cohort",
  "@type": "Dataset",
  "name": "Regional Clinical Cohort",
  "license": "https://creativecommons.org/licenses/by-nc/4.0/",
  "accessRights": { "@id": "fair2:L2" },
  "fair2:access": {
    "tier": "L2",
    "credentialRequirements": ["dua_acceptance", "institutional_affiliation", "ethics_training"],
    "identityAssurance": "institutional",
    "communityGovernance": "consultationRequired",
    "environment": "secureHuman",
    "purposeBinding": {
      "requirement": "verified",
      "allowed": ["dpv:AcademicResearch", "dpv:ClinicalResearch"],
      "prohibited": ["dpv:CommercialResearch"]
    },
    "jurisdiction": { "requirement": "required", "accepted": ["CA", "EU"] },
    "queryGovernance": {
      "enabled": true,
      "linkagePolicy": "sameStudy",
      "studyId": "STUDY-2026-001",
      "derivationRegistration": "required",
      "tierRules": {
        "L1": { "granularity": "aggregated", "minGroupSize": 10, "deniedColumns": ["patient_id"] },
        "L2": { "granularity": "grouped", "minGroupSize": 5, "deniedColumns": ["patient_id"] }
      }
    }
  },
  "fair2:constraints": {
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "anonymized-only",
    "commercialUse": "nonCommercialOnly",
    "combination": { "policy": "sameSteward" }
  },
  "fair2:embargo": { "until": "2027-01-01T00:00:00Z" },
  "fair2:variableGovernance": {
    "floorTier": "L1",
    "variables": {
      "year": { "encrypted": false },
      "diagnosis": { "tier": "L1" },
      "patient_id": { "tier": "L2" }
    }
  },
  "fair2:agentGovernance": { "policy": "planAndApprove", "ceilingTier": "L1" },
  "fair2:consentGovernance": { "enforcement": "enforced", "blockThreshold": 0 }
}
```

---

## Related properties

- **`license`** states the licence; governance blocks add conditions, they do
  not replace it. An `L0` dataset is governed by its licence and
  `fair2:constraints` alone.
- **`accessRights`** (`dct:accessRights`) may name the tier as a term —
  `{ "@id": "fair2:L1" }` — for consumers that read Dataset metadata without the
  governance blocks. When both are present they must agree; `fair2:access.tier`
  is the one governance services act on.
- **Responsible AI** (`rai:` properties, see [Responsible AI](responsible-ai.md))
  describes the data — its collection, biases, limitations. `fair2:constraints`
  states what reuse is permitted. A dataset may need both.
- **ODRL** is an export format, not a source: see
  [ODRL Policies](../integration/odrl-policy.md).

---

## Validation

`schemas/fair2-governance.schema.json` is the JSON Schema for the governance
blocks, vendored from the FAIR² governance model (schema version 1.13). Each
block is checked against the definition of the same name (`fair2:access`
against `AccessBlock`, `fair2:constraints` against `ConstraintsBlock`, and so
on); the schema's document-level properties (`fair2:id`, `fair2:version`,
`fair2:proof`) belong to the signed form a governance service keeps, and do not
apply to a `fair2.json` as a whole.

SHACL does not reach inside a block — it is a JSON literal — and the Dataset
shape requires none of them.

---

## Migrating from Agreement Levels

Agreement Levels 0–6 are deprecated. Their identifiers — `fair2:AgreementLevel0`
to `6`, and the `fair2:AgreementLevels0` to `6` spelling used by the reference
example until v1.6.3 — stay defined with status `deprecated` and a
`dct:isReplacedBy` naming the closest tier, so existing documents still
resolve; new documents state a tier and the blocks above. The closest
equivalents:

| Agreement Level | Governance blocks |
|---|---|
| 0 — Embargoed | `L1` or `L2` with `fair2:embargo`. An embargo applies only to governed data, so data that should be open after release needs `fair2:temporalGovernance` to lower the tier, or a new version. |
| 1 — Open | `L0` |
| 2 — Collaborative | `L0`; attribution and reciprocity are licence and agreement terms, and `fair2:constraints` carries what can be stated (e.g. `commercialUse`). |
| 3 — Trusted | `L2` with `credentialRequirements` (the Responsible Use Agreement is the DUA); `L1` where registration alone is enough. |
| 4 — Community-governed (CARE) | `L1` or `L2` with `communityGovernance` (+G) and `fair2:indigenousGovernance`. |
| 5 — Secure environment | `L2` with `environment: "secureHuman"` (+S), usually with `exportRestriction`. |
| 6 — Federated compute-to-data | `L2` with `environment: "computeToData"` (+S) and `queryGovernance` (+Q). |

The Agreement Levels' constraint axes carry over: `aiTraining` and
`exportRestriction` are use constraints; `identity`, `environment` and
`communityGovernance` became `fair2:access` fields.

`fair2:reuseLogging`, `fair2:AIethicalUse` and `fair2:governanceProtocol`,
which appeared only in the Agreement Level examples, were never defined terms.
Access to governed data is always logged by the governance service, and
conditions belong in `restrictedWithConditions` with the agreement that states
them.

---

## Source

This page follows the FAIR² governance model version 1.16 and its document
schema version 1.13.

!!! warning "Namespace"
    Documents issued by a governance service before this release may bind
    `fair2:` to `https://fair2.ai/ns/v1/`. The JSON is the same, but in RDF
    those keys expand to different IRIs from the ones defined here. Read them by
    key, or rewrite the context to this specification's.
