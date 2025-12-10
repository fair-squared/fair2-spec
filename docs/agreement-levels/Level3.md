# FAIR² Access Governance Documentation  
## **Level 3 – Trusted Access**

This document provides the **case scenario matrix** for Level-3 access, together with **metadata examples** for each variant.  
It follows the FAIR² interpretation:

> **Level 3 – Trusted Access**  
> Access requires verified researcher identification (e.g. ORCID) and acceptance of a Responsible Use Agreement (RUA). Use is logged for accountability and reproducibility. Redistribution outside the FAIR² or sovereign hosting environment is restricted.

---

# **1. Overview of Level 3 (Trusted Access)**

Level 3 datasets are **not fully open**.  
They require:

- Verified identity (e.g. ORCID, institutional login)  
- Acceptance of a Responsible Use Agreement (RUA)  
- Access logging and traceability  

FAIR² models Trusted Access using a **base profile** refined by these constraint axes:

- **identity**: ORCID / institutionalLogin / both  
- **environment**: open / secureHuman / computeToData / hybrid  
- **communityGovernance**: none / consultationRecommended / consultationRequired  
- **aiTraining**: allowed / restrictedWithConditions / prohibited  
- **exportRestriction**: none / aggregated-only / anonymized-only / derived-parameters-only  
- **distribution-level constraints**: for datasets with mixed-access files

---

# **2. Level 3 Case Scenario Matrix**

| Variant | Description | identity | environment | governance | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|-------------|------------|------------|------------------|-------------------------------|
| **3.1** | Trusted access with ORCID, no secure env | ORCID | open | none | allowed | none | none |
| **3.2** | Trusted, ORCID + secure workspace | ORCID | secureHuman | none | allowed | anonymized-only | none |
| **3.3** | Trusted, AI training prohibited | ORCID | secureHuman | none | prohibited | anonymized-only | none |
| **3.4** | Trusted + compute-to-data (federated) | ORCID | computeToData | none | allowed | derived-parameters-only | none |
| **3.5** | Trusted, community consultation required | ORCID | secureHuman | consultationRequired | restrictedWithConditions | aggregated-only | none |
| **3.6** | Metadata public; some files trusted-only | ORCID | hybrid | none | allowed | none | present |

---

# **3. Metadata Examples for Each Level-3 Variant**

All examples use the FAIR² JSON-LD namespace:
```
fair2: https://fair2.ai/ns/
```

---

## **Variant 3.1 — Trusted Access with ORCID, No Secure Environment**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Regional Health Service Utilization Statistics",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 3.2 — Trusted, ORCID + Secure Workspace, Anonymized Export Only**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Clinical Outcomes Registry (De-identified)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "anonymized-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 3.3 — Trusted, AI Training Prohibited**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Sensitive Social Survey Responses",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "communityGovernance": "none",
    "aiTraining": "prohibited",
    "exportRestriction": "anonymized-only"
  },
  "fair2:reuseLogging": true,
  "fair2:AIethicalUse": "Analysis limited to pre-approved social research questions; AI model training not permitted."
}
```

---

## **Variant 3.4 — Trusted + Federated Compute-to-Data**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Multi-site Hospital Readmission Dataset (Federated)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "derived-parameters-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 3.5 — Trusted with Community Consultation Required**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Community Health and Environment Survey",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "communityGovernance": "consultationRequired",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/health-governance",
  "fair2:reuseLogging": true
}
```

---

## **Variant 3.6 — Metadata Public, Some Files Trusted-Only (Hybrid Environment)**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Trusted Mobility and Air Quality Dataset",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel3",

  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "hybrid",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },

  "distribution": [
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/air_quality_summary.csv",
      "fair2:constraints": {
        "environment": "open"
      }
    },
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://secure.example.org/files/gps_tracks.parquet",
      "fair2:constraints": {
        "identity": "ORCID",
        "environment": "secureHuman",
        "exportRestriction": "aggregated-only"
      }
    }
  ],

  "fair2:reuseLogging": true
}
```

---

# **4. Summary Table**

| Variant | Meaning | Key FAIR² Constraint |
|--------|---------|----------------------|
| **3.1** | Trusted, ORCID only | `identity = ORCID` |
| **3.2** | Trusted, ORCID + secure environment | `environment = secureHuman`, `exportRestriction = anonymized-only` |
| **3.3** | Trusted, no AI training | `aiTraining = prohibited` |
| **3.4** | Trusted, federated compute-to-data | `environment = computeToData` |
| **3.5** | Trusted with community consultation | `communityGovernance = consultationRequired` |
| **3.6** | Trusted, hybrid public/restricted data | Distribution-level constraints, `environment = hybrid` |

---

# **Navigation**

**[← Level 2](Level2.md) | [Level 4 →](Level4.md)**

---

**End of Level 3 Documentation — FAIR² Access Governance**
