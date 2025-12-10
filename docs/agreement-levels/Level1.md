# FAIR² Access Governance Documentation  
## **Level 1 – Open Access**

This document provides a consolidated representation of the **case scenario matrix** for Level‑1 access, together with **metadata examples** for each variant.  
It is intended for FAIR²’s public GitHub documentation.

---

# **1. Overview of Level 1 (Open Access)**

Level 1 datasets are publicly accessible without registration or authentication.  
However, FAIR² recognizes that even “open” datasets may require ethical, technical, or governance-based **constraints**.

FAIR² therefore models Open Access as a **profile**, refined by a set of controlled constraint axes:

- **identity**: none  
- **environment**: open  
- **communityGovernance**: none / consultationRecommended  
- **aiTraining**: allowed / prohibited  
- **exportRestriction**: none / derived-parameters-only  
- **distribution-level constraints** (optional, for mixed-access datasets)

---

# **2. Level 1 Case Scenario Matrix**

| Variant | Description | identity | governance | aiTraining | exportRestriction | distribution-level constraints |
|--------|-------------|----------|------------|------------|------------------|-------------------------------|
| **1.1** | Fully open, no restrictions | none | none | allowed | none | none |
| **1.2** | Open, but AI training prohibited | none | none | prohibited | none | none |
| **1.3** | Open, but only derived parameters may be reused | none | none | allowed | derived-parameters-only | none |
| **1.4** | Open, but community consultation recommended | none | consultationRecommended | allowed | none | none |
| **1.5** | Metadata fully open; some files restricted | none | none | allowed | none | present at distribution level |

---

# **3. Metadata Examples for Each Level‑1 Variant**

All examples use the FAIR² JSON‑LD namespace:
```
fair2: https://fair2.ai/ns/
```

---

## **Variant 1.1 — Fully Open, No Restrictions**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Open Climate Indicators Dataset",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel1",
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

## **Variant 1.2 — Open, but AI Training Prohibited**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Open Literary Corpus (Human Reading Only)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel1",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "prohibited",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 1.3 — Open, but Only Derived Parameters May Be Reused**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Open Satellite Imagery (Derived Outputs Only)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel1",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "derived-parameters-only"
  }
}
```

---

## **Variant 1.4 — Open, but Community Consultation Recommended**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Open Traditional Ecological Knowledge Summaries",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel1",
  "fair2:constraints": {
    "identity": "none",
    "environment": "open",
    "communityGovernance": "consultationRecommended",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  },
  "fair2:governanceProtocol": "https://community.example.org/governance"
}
```

---

## **Variant 1.5 — Metadata Fully Public, Some Files Restricted**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Open Biodiversity Observations with Restricted Coordinates",

  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel1",

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
      "schema:contentUrl": "https://example.org/files/species_list.csv",
      "fair2:constraints": {
        "environment": "open"
      }
    },
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/precise_coordinates.csv",
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

| Variant | Meaning | Constraint |
|--------|---------|-----------|
| **1.1** | Fully open | None |
| **1.2** | Open but AI training disallowed | `aiTraining = prohibited` |
| **1.3** | Open but only derived outputs allowed | `exportRestriction = derived-parameters-only` |
| **1.4** | Open with community consultation recommended | `communityGovernance = consultationRecommended` |
| **1.5** | Mixed-access dataset with public metadata | Distribution-level constraints |

---
# **Navigation**

**[← Level 0](Level0.md) | [Level 2 →](Level2.md)**

---

**End of Level 1 Documentation — FAIR² Access Governance**
