# FAIR² Access Governance Documentation  
## **Level 2 – Collaborative Access**

This document provides the **case scenario matrix** for Level-2 access, together with **metadata examples** for each variant.  
It follows the official FAIR² interpretation:

> **Level 2 – Collaborative Access**  
> Access remains open, but users are expected to acknowledge dataset creators, preserve provenance, consider collaboration, and communicate significant results back. Redistribution outside sovereign hosting is discouraged.

---

# **1. Overview of Level 2 (Collaborative Access)**

Level 2 datasets are freely downloadable.  
No authentication is required.  
However, reuse is guided by norms of **reciprocity, acknowledgment, and scientific collaboration**.

FAIR² models Collaborative Access using a **base profile** refined by constraint axes:

- **identity**: none (baseline), ORCID if encouraged  
- **environment**: open (baseline), hybrid if file-level restrictions exist  
- **communityGovernance**: none / consultationRecommended  
- **aiTraining**: allowed / restricted / prohibited  
- **exportRestriction**: none / aggregated-only / derived-only  
- **distribution-level constraints**: for mixed datasets

---

# **2. Level 2 Case Scenario Matrix**

| Variant | Description | identity | governance | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|------------|------------|------------------|-------------------------------|
| **2.1** | Collaborative open dataset | none | none | allowed | none | none |
| **2.2** | Collaborative + ORCID encouraged | ORCID | none | allowed | none | none |
| **2.3** | Collaborative with community consultation | none | consultationRecommended | allowed | none | none |
| **2.4** | Collaborative, AI training restricted | none | none | restrictedWithConditions | none | none |
| **2.5** | Collaborative with export restrictions | none | none | allowed | aggregated-only | none |
| **2.6** | Metadata open; some files restricted | none | none | allowed | none | present |

---

# **3. Metadata Examples for Each Level-2 Variant**

All examples use the FAIR² JSON-LD namespace:
```
fair2: https://fair2.ai/ns/
```

---

## **Variant 2.1 — Collaborative, Fully Open**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Marine Habitat Observations",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 2.2 — Collaborative with ORCID Encouraged**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Urban Soundscape Recordings",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",
  "fair2:constraints": {
    "identity": "ORCID",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 2.3 — Collaborative with Community Consultation Recommended**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Traditional Crop Knowledge Registry",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "consultationRecommended",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },
  "fair2:governanceProtocol": "https://community.example.org/consultation"
}
```

---

## **Variant 2.4 — Collaborative, AI Training Restricted**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Historical Manuscript Transcriptions",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 2.5 — Collaborative with Export Restrictions (Aggregated Only)**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Field Biodiversity Transects",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "aggregated-only"
  }
}
```

---

## **Variant 2.6 — Metadata Public, Mixed Distribution-Level Access**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Collaborative Wildlife Monitoring Dataset",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel2",

  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },

  "distribution": [
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/species_counts.csv",
      "fair2:constraints": {
        "environment": "open"
      }
    },
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/nest_location_raw.csv",
      "fair2:constraints": {
        "identity": "ORCID",
        "environment": "secureHuman",
        "exportRestriction": "aggregated-only"
      }
    }
  ]
}
```

---

# **4. Summary Table**

| Variant | Meaning | Key FAIR² Constraint |
|--------|---------|----------------------|
| **2.1** | Pure collaborative reuse | None |
| **2.2** | Collaboration with identity encouraged | `identity = ORCID` |
| **2.3** | Consultation encouraged | `communityGovernance = consultationRecommended` |
| **2.4** | AI training conditionally restricted | `aiTraining = restrictedWithConditions` |
| **2.5** | Aggregated-output-only reuse | `exportRestriction = aggregated-only` |
| **2.6** | Mixed-access dataset | Distribution-level constraints |

---

# **Navigation**

**[← Level 1](Level1.md) | [Level 3 →](Level3.md)**

---

**End of Level 2 Documentation — FAIR² Access Governance**
