# FAIR² Access Governance Documentation  
## **Level 4 – Community-Governed Access (CARE)**

This document provides the **case scenario matrix** for Level-4 access, together with **metadata examples** for each variant.  
It follows the FAIR² interpretation:

> **Level 4 – Community-Governed Access (CARE)**  
> Applies to datasets governed by recognized communities or collectives.  
> Reuse must respect CARE Principles — Collective Benefit, Authority to Control, Responsibility, and Ethics.  
> Consultation or approval from the community is required for substantial reuse.  
> Redistribution outside sovereign hosting is restricted unless explicitly permitted.

---

# **1. Overview of Level 4 (CARE / Community-Governed Access)**

Level 4 datasets introduce **community-based governance controls**.  
They may be technically accessible but **social, cultural, or governance requirements** must be fulfilled before reuse.

FAIR² models Level 4 using these constraint axes:

- **identity**: none / ORCID / institutionalLogin  
- **environment**: open / secureHuman / computeToData / hybrid  
- **communityGovernance**: consultationRecommended / consultationRequired / communityApprovalRequired  
- **aiTraining**: allowed / restricted / prohibited  
- **exportRestriction**: aggregated-only / anonymized-only / derived-parameters-only  
- **distribution-level constraints**: for mixed datasets

---

# **2. Level 4 Case Scenario Matrix**

| Variant | Description | identity | environment | governance | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|-------------|------------|------------|------------------|-------------------------------|
| **4.1** | CARE dataset, open access but consultation required | none | open | consultationRequired | allowed | none | none |
| **4.2** | CARE dataset, ORCID required for accountability | ORCID | open | consultationRequired | allowed | none | none |
| **4.3** | CARE dataset, secure workspace required | ORCID | secureHuman | consultationRequired | restrictedWithConditions | aggregated-only | none |
| **4.4** | CARE dataset, federated compute (no raw access) | ORCID | computeToData | communityApprovalRequired | prohibited | aggregated-only | none |
| **4.5** | CARE dataset with multiple file-access levels | ORCID | hybrid | consultationRequired | restrictedWithConditions | none | present |
| **4.6** | CARE dataset, high ethics: AI training prohibited | ORCID | secureHuman | communityApprovalRequired | prohibited | anonymized-only | none |

---

# **3. Metadata Examples for Each Level-4 Variant**

All examples use the FAIR² JSON-LD namespace:
```
fair2: https://fair2.ai/ns/
```

---

## **Variant 4.1 — CARE Dataset, Open Access but Consultation Required**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Indigenous Ecological Knowledge Summaries",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "consultationRequired",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },
  "fair2:governanceProtocol": "https://community.example.org/knowledge-governance"
}
```

---

## **Variant 4.2 — CARE Dataset with ORCID for Accountability**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Cultural Landscape Oral Histories",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "open",
    "communityGovernance": "consultationRequired",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },
  "fair2:governanceProtocol": "https://community.example.org/heritage-governance"
}
```

---

## **Variant 4.3 — CARE Dataset with Secure Workspace + Aggregated Output**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Community Health Indicators (Restricted)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "communityGovernance": "consultationRequired",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/health-governance"
}
```

---

## **Variant 4.4 — CARE Dataset, Federated Compute-Only, No AI Training**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Traditional Land Use and Biodiversity Data (Federated Access)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "communityApprovalRequired",
    "aiTraining": "prohibited",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/land-governance"
}
```

---

## **Variant 4.5 — CARE Dataset with Mixed File-Level Access Rules**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Community Environmental Monitoring Records",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",

  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "hybrid",
    "communityGovernance": "consultationRequired",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "none"
  },

  "distribution": [
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/summary_statistics.csv",
      "fair2:constraints": {
        "environment": "open"
      }
    },
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://secure.example.org/files/water_samples_raw.csv",
      "fair2:constraints": {
        "identity": "ORCID",
        "environment": "secureHuman",
        "exportRestriction": "anonymized-only"
      }
    }
  ],

  "fair2:governanceProtocol": "https://community.example.org/env-governance"
}
```

---

## **Variant 4.6 — CARE Dataset with High Ethics: AI Training Prohibited + Secure Environment**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Sacred Site Ecological Observations",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel4",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "secureHuman",
    "communityGovernance": "communityApprovalRequired",
    "aiTraining": "prohibited",
    "exportRestriction": "anonymized-only"
  },
  "fair2:AIethicalUse": "Dataset may not be used for machine learning or models generating predictions; human-guided interpretive research only.",
  "fair2:governanceProtocol": "https://community.example.org/sacred-governance"
}
```

---

# **4. Summary Table**

| Variant | Meaning | Key FAIR² Constraint |
|--------|---------|----------------------|
| **4.1** | Consultation required but technically open | `communityGovernance = consultationRequired` |
| **4.2** | Consultation + identity accountability | `identity = ORCID` |
| **4.3** | CARE + secure Human environment | `environment = secureHuman` |
| **4.4** | CARE + federated compute | `environment = computeToData` |
| **4.5** | Mixed public/restricted files | distribution-level constraints |
| **4.6** | Highest governance & ethics protections | `aiTraining = prohibited`, secure env |

---

# **Navigation**

**[← Level 3](Level3.md) | [Level 5 →](Level5.md)**

---

**End of Level 4 Documentation — FAIR² Access Governance**
