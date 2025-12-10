# FAIR² Access Governance Documentation  
## **Level 6 – Federated Compute-to-Data Access**

This document provides the **case scenario matrix** for Level-6 access, together with **metadata examples** for each variant.  
It follows the FAIR² interpretation:

> **Level 6 – Federated Compute-to-Data Access**  
> Data cannot be downloaded.  
> Algorithms are sent to the data (“compute-to-data”).  
> Strict identity, authorization, environment, and export rules apply.  
> Only aggregated or model-derived outputs may leave the secure compute environment.  
> Suitable for highly sensitive, multi-institutional, cross-jurisdiction datasets.

---

# **1. Overview of Level 6 (Federated Compute-to-Data)**

Level 6 introduces the **strongest technical controls** short of Level 5’s secure human environment.  
The key characteristic is:

### ❗ **No raw data leaves the sovereign hosting environment.**

FAIR² models Level 6 using these constraint axes:

- **identity**: ORCID / institutionalLogin / both  
- **environment**: computeToData (primary), hybrid if mixtures exist  
- **communityGovernance**: none / consultationRequired / communityApprovalRequired  
- **aiTraining**: allowed / restricted / prohibited  
- **exportRestriction**: derived-parameters-only / aggregated-only  
- **distribution-level constraints**: for multi-file governance

---

# **2. Level 6 Case Scenario Matrix**

| Variant | Description | identity | environment | governance | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|-------------|------------|------------|------------------|-------------------------------|
| **6.1** | Pure federated compute-to-data | ORCID | computeToData | none | allowed | derived-parameters-only | none |
| **6.2** | Federated compute + restricted AI training | ORCID | computeToData | none | restrictedWithConditions | aggregated-only | none |
| **6.3** | Federated compute + AI training prohibited | ORCID | computeToData | none | prohibited | aggregated-only | none |
| **6.4** | Federated compute + community consultation | ORCID | computeToData | consultationRequired | restrictedWithConditions | aggregated-only | none |
| **6.5** | Federated compute + community approval required | ORCID | computeToData | communityApprovalRequired | prohibited | aggregated-only | none |
| **6.6** | Hybrid dataset (some files open, core data compute-only) | ORCID | hybrid | consultationRequired | allowed | derived-parameters-only | present |

---

# **3. Metadata Examples for Each Level-6 Variant**

All examples use the FAIR² JSON-LD namespace:
```
fair2: https://fair2.ai/ns/
```

---

## **Variant 6.1 — Pure Federated Compute-to-Data**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Hospital Network Readmission Dataset (Federated Access)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",
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

## **Variant 6.2 — Federated Compute with Restricted AI Training**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Cross-Institutional Laboratory Data (Federated, Restricted AI Use)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "none",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:reuseLogging": true
}
```

---

## **Variant 6.3 — Federated Compute, AI Training Prohibited**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Sensitive Genomic Variation Set (Federated, No Training)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "none",
    "aiTraining": "prohibited",
    "exportRestriction": "aggregated-only"
  },
  "fair2:AIethicalUse": "Output limited to aggregated statistics; no AI training permitted.",
  "fair2:reuseLogging": true
}
```

---

## **Variant 6.4 — Federated Compute + Community Consultation Required**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Traditional Knowledge Biodiversity Database (Federated Access)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "consultationRequired",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/biodiversity-governance",
  "fair2:reuseLogging": true
}
```

---

## **Variant 6.5 — Federated Compute + Community Approval Required**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Indigenous Genomics Panel (Federated + Approval)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "computeToData",
    "communityGovernance": "communityApprovalRequired",
    "aiTraining": "prohibited",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/genomics-governance",
  "fair2:reuseLogging": true
}
```

---

## **Variant 6.6 — Hybrid Dataset: Public Metadata + Federated Raw Data**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Urban Mobility + Environmental Sensors (Hybrid Federated Access)",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel6",

  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "hybrid",
    "communityGovernance": "consultationRequired",
    "aiTraining": "allowed",
    "exportRestriction": "derived-parameters-only"
  },

  "distribution": [
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/open_air_quality_summary.csv",
      "fair2:constraints": {
        "environment": "open"
      }
    },
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://secure.example.org/federated/mobility_data",
      "fair2:constraints": {
        "identity": "ORCID",
        "environment": "computeToData",
        "exportRestriction": "derived-parameters-only"
      }
    }
  ],

  "fair2:governanceProtocol": "https://community.example.org/sensor-governance",
  "fair2:reuseLogging": true
}
```

---

# **4. Summary Table**

| Variant | Meaning | Key FAIR² Constraint |
|--------|---------|----------------------|
| **6.1** | Pure compute-to-data | `environment = computeToData` |
| **6.2** | Federated + limited AI training | `aiTraining = restrictedWithConditions` |
| **6.3** | Federated + no AI training | `aiTraining = prohibited` |
| **6.4** | Federated + community consultation | `communityGovernance = consultationRequired` |
| **6.5** | Federated + community approval | `communityGovernance = communityApprovalRequired` |
| **6.6** | Hybrid public/restricted | distribution-level constraints |

---

# **Navigation**

**[← Level 5](Level5.md)**

---

**End of Level 6 Documentation — FAIR² Access Governance**
