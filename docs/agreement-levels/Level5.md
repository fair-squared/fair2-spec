# FAIR² Access Governance Documentation  
## **Level 5 – Secure / Federated Access**

This document provides the **case scenario matrix** for Level-5 access, together with **metadata examples** for each variant.  
It follows the FAIR² interpretation:

> **Level 5 – Secure / Federated Access**  
> Access occurs only within a controlled secure environment or approved federated infrastructure.  
> Raw data **cannot** be downloaded.  
> Users must have verified credentials, appropriate ethics or human-data training, and comply with strict audit logging.  
> Only aggregated, anonymized, or derived outputs may leave the secure system.

---

# **1. Overview of Level 5 (Secure / Controlled Environment)**

Level 5 datasets are highly sensitive and require:

- **Verified identity** (ORCID, institutional login, or both)  
- **Ethics / human-data training** verified  
- **Controlled environment** — secure workstation or federated compute node  
- **No raw data downloads**  
- **Strict audit logging**  
- **Export controls** on derived results  

FAIR² models Level 5 using these constraint axes:

- **identity**: ORCID / institutionalLogin / both  
- **environment**: secureHuman / computeToData / hybrid  
- **aiTraining**: allowed / restricted / prohibited  
- **exportRestriction**: aggregated-only / anonymized-only / derived-parameters-only  
- **distribution-level constraints**: for mixed datasets

---

# **2. Level 5 Case Scenario Matrix**

| Variant | Description | identity | environment | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|-------------|------------|------------------|-------------------------------|
| **5.1** | Secure human environment, ORCID required | ORCID | secureHuman | allowed | anonymized-only | none |
| **5.2** | Secure environment, AI training restricted | ORCID | secureHuman | restrictedWithConditions | aggregated-only | none |
| **5.3** | Secure environment, AI training prohibited | ORCID | secureHuman | prohibited | anonymized-only | none |
| **5.4** | Secure environment + community consultation | ORCID | secureHuman | restrictedWithConditions | aggregated-only | none |
| **5.5** | Federated compute-to-data only | ORCID | computeToData | allowed | derived-parameters-only | none |
| **5.6** | Hybrid environment with mixed file access | ORCID | hybrid | allowed | aggregated-only | present |

---

# **3. Metadata Examples for Each Level-5 Variant**

All examples use the FAIR² JSON-LD namespace:
```
fair2: https://fair2.ai/ns/
```

All Level 5 metadata must explicitly express **secure environment requirements** and **export restrictions**.

---

## **Variant 5.1 — Secure Environment, ORCID Required**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Clinical Imaging Cohort (Secure Access)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "aiTraining": "allowed",
    "exportRestriction": "anonymized-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 5.2 — Secure Environment with Restricted AI Training**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Longitudinal Health Outcomes Registry",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 5.3 — Secure, AI Training Prohibited**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Sensitive Mental Health Assessments",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "aiTraining": "prohibited",
    "exportRestriction": "anonymized-only"
  },
  "fair2:AIethicalUse": "Dataset prohibited from AI model training; analysis must follow human-supervised protocols.",
  "fair2:reuseLogging": true
}
```

---

## **Variant 5.4 — Secure Environment + Community Consultation**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Indigenous Community Health Records (Secure Access)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",
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

## **Variant 5.5 — Federated Compute-to-Data Only**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Multi-Site Hospital Readmission Dataset (Federated)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "aiTraining": "allowed",
    "exportRestriction": "derived-parameters-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 5.6 — Metadata Public; Mixed Secure Access to Files**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Secure Mobility + Air Quality Dataset",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel5",

  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "hybrid",
    "aiTraining": "allowed",
    "exportRestriction": "aggregated-only"
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
      "schema:contentUrl": "https://secure.example.org/files/raw_mobility_tracks.parquet",
      "fair2:constraints": {
        "identity": "ORCID",
        "environment": "secureHuman",
        "exportRestriction": "anonymized-only"
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
| **5.1** | Secure env + ORCID | `environment = secureHuman` |
| **5.2** | Secure env + limited AI training | `aiTraining = restrictedWithConditions` |
| **5.3** | Secure env + no AI training | `aiTraining = prohibited` |
| **5.4** | Secure env + community consultation | `communityGovernance = consultationRequired` |
| **5.5** | Federated compute-only | `environment = computeToData` |
| **5.6** | Hybrid public + secure | distribution-level constraints |

---

# **Navigation**

**[← Level 4](Level4.md) | [Level 6 →](Level6.md)**

---

**End of Level 5 Documentation — FAIR² Access Governance**
