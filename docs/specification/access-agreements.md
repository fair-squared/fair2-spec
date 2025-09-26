
# FAIR² Access Agreement Levels

## Overview

FAIR² introduces four standardized levels of access agreements to govern dataset use, aligned with FAIR principles, Responsible AI, and scalable governance. These levels reflect increasing levels of control, ethical scrutiny, and technical enforcement. Each level includes human-readable and machine-readable metadata support.

## Agreement Levels

### Level 1 – Open Access

**Definition:**  
Anyone can access the dataset without registration or identification; aligned with FAIR² principles of maximum reuse and transparency.

**Agreement Text:**  
By accessing this dataset, you acknowledge that it is made openly available under the stated license. No additional agreement is required. You may use, share, and build upon the dataset in accordance with the license terms, provided that you give appropriate attribution.

---

### Level 2 – Collaborative Access

**Definition:**  
Access requires users to acknowledge the data owner’s role and agree to consider collaboration, ensuring mutual benefit while maintaining broad reusability.

**Agreement Text:**  
By downloading this dataset, you agree to properly attribute the data and to consider collaboration with the dataset owner(s) in any substantial research use.

---

### Level 3 – Trusted Access

**Definition:**  
Access requires researcher identification (e.g., ORCID) and agreement to terms of responsible use, balancing openness with accountability and usage tracking.

**Agreement Text:**  
By accessing this dataset, you confirm that you are a qualified researcher and agree to use the data responsibly, not attempt re-identification, and handle the data securely. Access may be logged and monitored to ensure compliance.

---

### Level 4 – Secure Access

**Definition:**  
Accessible only in a controlled, cloud-based environment; requires a formal Data Use Agreement (DUA), verified human data training, and credentials registered in the researcher’s ORCID profile. No local downloads permitted.

**Agreement Text:**  
By requesting access to this dataset, you agree to:  
• Have up-to-date human data handling training credentials registered in your ORCID profile  
• Accept and comply with the standard Data Use Agreement (DUA) provided by the data owner  
• Work only within the approved secure environment; direct downloads and external storage are not permitted  
• Not attempt to re-identify individuals, share the data, or use it beyond the approved scope

---

## Standards Alignment

FAIR² access levels build on the following standards:

- `schema.org`
- `DCAT` / `DCTERMS`
- `DataCite Metadata Schema`
- `ODRL` (optional for expressiveness)

## Controlled Vocabulary (Machine-Readable)

The FAIR² agreement levels are published as a JSON-LD vocabulary at:

```
https://fair2.ai/terms/AgreementLevels
```

### Key Vocabulary Terms

| Property               | Description                                                            |
|------------------------|------------------------------------------------------------------------|
| `odrl:hasPolicy`       | Points to a machine-readable policy (permissions, prohibitions, duties)|
| `dct:license`          | Canonical license URI                                                  |
| `dct:rights`           | Terms of Use or human-readable policy URI                              |
| `dct:accessRights`     | Reference to FAIR² Agreement Level (1–4)                               |
| `usageInfo`            | Human-readable summary of use conditions                               |
| `conditionsOfAccess`   | Explicit textual summary (Open / Collaborative / Trusted / Secure)     |
| `fair2:agreementLevel` | DefinedTerm reference to a FAIR² Agreement Level                       |

---

## Example: Level 4 Agreement Term (DefinedTerm)

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@id": "fair2:AgreementLevel4",
  "@type": "DefinedTerm",
  "schema:name": "Secure Access",
  "schema:description": "Accessible only in a controlled, cloud-based environment; requires a DUA, human data training, and ORCID-registered credential.",
  "schema:text": "By requesting access, you confirm you have appropriate human data training credentials in your ORCID profile, accept the standard DUA, and will work only in the approved secure environment."
}
```

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
  "schema:license": "https://creativecommons.org/licenses/by/4.0/",
  "dct:rights": "https://fair2.ai/ns/AgreementLevels/2",
  "fair2:agreementLevel": { "@id": "fair2:AgreementLevel2" }
}
```
