# FAIR² Access Agreement Levels 

## Overview

FAIR² defines six standardized Access Agreement Levels (0–5) to govern dataset use, extending the FAIR principles with Responsible AI, modern governance requirements, and machine-actionable policies. These levels span from embargoed early-visibility records to secure/federated environments for sensitive data. Each level includes human-readable obligations and machine-readable metadata expressions (JSON-LD, ODRL, PROV-O, schema.org).

The Access Agreement Levels ensure:

- Early discoverability without premature disclosure  
- Reusability aligned with community norms, governance structures, and sovereignty  
- Responsible AI considerations where datasets may train or inform ML systems  
- Enforceable conditions of access across federated repositories  
- Full traceability and accountability through provenance and access logging  

---

## Agreement Levels

### Level 0 – Embargoed Access

**Definition**  
Metadata are publicly visible; the dataset itself is inaccessible until a specified release date (e.g., pending publication or peer review). Enables discoverability and citation without exposing data prematurely.

**Agreement Text**  
By viewing this dataset record, you agree to:

- Cite and acknowledge the dataset and its creators.  
- Respect the embargo period and refrain from downloading or redistributing data prior to release.  
- Preserve metadata and provenance when referencing this record.  

The dataset will be released under **ODC-BY 1.0** and the **FAIR² sDUA v1.0** on the date specified in the metadata.

---

### Level 1 – Open Access

**Definition**  
Anyone may access and reuse the dataset without registration or identification. Aligns with FAIR² principles of maximum reuse, transparency, and interoperability.

**Agreement Text**  
By accessing this dataset, you acknowledge that it is openly available under **ODC-BY 1.0**.  
You may use, share, and build upon the data, provided that you:

- Attribute the dataset and its creators.  
- Preserve contextual metadata and provenance.  
- Avoid redistribution or transfer of data outside the FAIR² or sovereign hosting environment; link to the canonical FAIR² record for reuse.

---

### Level 2 – Collaborative Access

**Definition**  
Access remains open but encourages engagement with dataset owners or contributors. Suitable for contextual, community-generated, or complex datasets where reciprocal communication is beneficial.

**Agreement Text**  
By downloading or using this dataset, you agree to:

- Cite and acknowledge the dataset and its creators.  
- Preserve contextual metadata and provenance.  
- Consider collaboration or consultation with dataset owners for substantial reuse or derivative research.  
- Communicate significant results or derived outputs back to the creators.  
- Avoid redistribution or transfer of data outside the FAIR² or sovereign hosting environment.

---

### Level 3 – Trusted Access

**Definition**  
Access requires verified researcher identity (e.g., ORCID) and acceptance of a Responsible Use Agreement (RUA). Enables accountability through access logging.

**Agreement Text**  
By requesting access to this dataset, you agree to:

- Authenticate via ORCID or institutional credentials.  
- Use the data responsibly and ethically, aligned with FAIR² and Responsible AI principles.  
- Handle data securely; do not attempt re-identification or unauthorized dataset linkage.  
- Permit access logging for compliance and reproducibility.  
- Cite and acknowledge the dataset and its creators.  
- Preserve contextual metadata and provenance.  
- Avoid redistribution or transfer outside the FAIR² or sovereign hosting environment; share only derived or aggregated results.

**Repository Requirement**  
Repositories implementing Level 3 must log ORCID-authenticated access and provide auditable reuse metrics.

---

### Level 4 – Community-Governed Access (CARE)

**Definition**  
For datasets governed by recognized communities under CARE Principles (Collective Benefit, Authority to Control, Responsibility, Ethics). Discoverable under ODC-BY 1.0, but substantial reuse requires community consultation and adherence to governance protocols.

**Agreement Text**  
By accessing this dataset, you agree to:

- Use data responsibly and ethically in alignment with FAIR² and CARE Principles.  
- Acknowledge the dataset, its creators, and its governing community.  
- Preserve contextual metadata and provenance.  
- Consult the designated community authority before substantial reuse, derivative research, or commercial application.  
- Respect cultural, ethical, or spiritual restrictions specified by the community.  
- Communicate outcomes and benefits back to the community.  
- Avoid redistribution outside the FAIR² or sovereign hosting environment or beyond the community’s jurisdiction.

**Metadata Requirement**  
Level 4 datasets must include a **Community Governance Protocol** URI describing consultation processes and contact details.

---

### Level 5 – Secure / Federated Access

**Definition**  
For sensitive, human-derived, or legally regulated data. Access occurs only within a controlled, audited, or federated environment. Raw data cannot be downloaded. Requires a formal DUA and verified human-data handling credentials.

**Agreement Text**  
By requesting access to this dataset, you agree to:

- Hold verified human-data or ethics credentials linked to your ORCID profile.  
- Accept and comply with the FAIR² Data Use Agreement (DUA).  
- Work solely within the approved secure or federated environment; downloads are prohibited.  
- Not attempt re-identification, extraction, or redistribution of raw data.  
- Permit comprehensive audit logging for compliance and reproducibility.  
- Cite and acknowledge the dataset and its creators.  
- Preserve contextual metadata and provenance.  
- Avoid redistribution or transfer of data outside the FAIR² or sovereign hosting environment.

Only aggregated or anonymized outputs may leave the secure environment.

---

## AI-Specific and Responsible Reuse Metadata Extensions

FAIR² supports optional AI-specific attributes to ensure compliance with Responsible AI:

| Property | Description |
|---------|-------------|
| **fair2:AItrainingPermitted** | Indicates whether the dataset may be used for ML/AI training (`true`/`false`). |
| **fair2:AIethicalUse** | Describes Responsible AI expectations, including limitations, bias-mitigation duties, and attribution expectations for model cards. |
| **fair2:reuseLogging** | States whether the repository logs and reports reuse events automatically. |

---

## Standards Alignment

FAIR² Access Levels align with:

- **schema.org**  
- **DCAT / DCTERMS**  
- **DataCite Metadata Schema**  
- **ODRL**  
- **CARE Principles**  
- Controlled vocabularies for `conditionsOfAccess` and `sovereignLocationType`

---

## Key Vocabulary Terms

| Property | Description |
|----------|-------------|
| `dct:license` | Canonical license URI (e.g., ODC-BY 1.0) |
| `dct:accessRights` | Reference to FAIR² Agreement Level (0–5) |
| `fair2:conditionsOfAccess` | Text summary (Embargoed / Open / Collaborative / Trusted / Community-Governed / Secure) |
| `odrl:hasPolicy` | Machine-readable obligations and permissions |
| `fair2:sovereignLocation` | Sovereign hosting environment URI |
| `fair2:AItrainingPermitted` | Indicates whether dataset can be used for AI training |
| `fair2:governanceProtocol` | Link to governance policy |
| `fair2:redistributionPolicy` | Rules restricting transfer outside FAIR² environments |

---

## Vocabulary Publication

```
https://fair2.ai/terms/AgreementLevels
```

---

## Example: Level 4 – Community-Governed Access (DefinedTerm)

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@id": "fair2:AgreementLevel4",
  "@type": "DefinedTerm",
  "schema:name": "Community-Governed Access (CARE)",
  "skos:definition": "Governed by a recognized community under CARE Principles. Consultation required before reuse. Redistribution beyond FAIR² or sovereign hosting is prohibited.",
  "skos:note": "By accessing this dataset, you confirm adherence to FAIR² and CARE principles, including consultation and collective acknowledgment before substantial reuse.",
  "schema:url": "https://fair2.ai/ns/AgreementLevels/4"
}
```

---

## Example: Dataset Metadata Referencing Agreement Level 2

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Marine Biodiversity Dataset",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": {
    "@id": "https://fair2.ai/ns/AgreementLevels2",
    "@type": "schema:DefinedTerm",
    "schema:name": "Collaborative Access",
    "skos:definition": "Access requires acknowledgment of data owners and encourages collaboration while maintaining broad reusability.",
    "skos:note": "By downloading this dataset, you agree to attribute the data, preserve context, and consider collaboration with the dataset owners in any substantial reuse.",
    "schema:url": "https://fair2.ai/spec/AgreementLevels/2"
  },
  "fair2:sovereignLocation": "https://datarepository.example.org",
  "fair2:AItrainingPermitted": true
}
```
