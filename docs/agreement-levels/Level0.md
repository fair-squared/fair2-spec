# FAIR² Access Governance Documentation  
## **Level 0 – Embargoed Access**

This document provides the **case scenario matrix** for Level‑0 access, together with **metadata examples** for each variant.  
It follows the FAIR² interpretation:

> **Level 0 – Embargoed Access**  
> Metadata is publicly visible, but the dataset itself is under embargo until a specified release date.  
> Users may discover and cite the dataset but may not download or redistribute the data before the embargo expires.  
> The dataset will be released under ODC‑BY 1.0 and the FAIR² sDUA on the embargo date.

---

# **1. Overview of Level 0 (Embargoed Access)**

Level 0 supports:

- **Early discoverability** (metadata open)  
- **Early citation** without data exposure  
- **Strict non‑access** to raw data until release date  
- **Machine‑readable embargo timers**  
- Optional pre‑registration of AI‑related constraints that will apply *after embargo release*

FAIR² models Level 0 using these constraint axes:

- **identity**: none  
- **environment**: none (no access allowed)  
- **communityGovernance**: none (or minimal consultation if specified)  
- **aiTraining**: irrelevant until release, but may be preset  
- **exportRestriction**: irrelevant until release  
- **distribution‑level availability**: metadata only, no file access  

---

# **2. Level 0 Case Scenario Matrix**

| Variant | Description | metadata | data access | governance | embargo expiration | notes |
|--------|-------------|----------|-------------|------------|-------------------|-------|
| **0.1** | Simple embargoed dataset | public | none | none | fixed date | Standard case |
| **0.2** | Embargoed + planned AI training rules | public | none | none | fixed date | AI rules declared in advance |
| **0.3** | Embargoed until publication (no fixed date) | public | none | none | “upon publication” | Common for manuscripts |
| **0.4** | Embargoed + community consultation required after release | public | none | consultationRequired | fixed date | CARE obligations start after release |
| **0.5** | Embargoed + partial pre‑release (metadata + derived summaries only) | public | derived-only | none | fixed date | Summaries allowed pre‑release |

---

# **3. Metadata Examples for Each Level‑0 Variant**

All examples use the FAIR² JSON‑LD namespace:

```
fair2: https://fair2.ai/ns/
```

---

## **Variant 0.1 — Simple Embargoed Dataset**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Coastal Erosion Imaging Dataset (Embargoed)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel0",
  "fair2:embargoUntil": "2026-12-31",
  "fair2:constraints": {
    "identity": "none",
    "environment": "none",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 0.2 — Embargoed with Declared Post‑Release AI Constraints**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Marine Acoustic Signatures (Embargoed)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel0",
  "fair2:embargoUntil": "2025-09-01",
  "fair2:constraints": {
    "identity": "none",
    "environment": "none",
    "communityGovernance": "none",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  }
}
```

---

## **Variant 0.3 — Embargoed Until Publication (Unknown Date)**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Coral Reef Microbiome Profiles (Pending Publication)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel0",
  "fair2:embargoUntil": "publication",
  "fair2:constraints": {
    "identity": "none",
    "environment": "none",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "none"
  }
}
```

---

## **Variant 0.4 — Embargoed with CARE Requirements After Release**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Traditional Ecological Narratives (Embargoed)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel0",
  "fair2:embargoUntil": "2027-03-15",
  "fair2:constraints": {
    "identity": "none",
    "environment": "none",
    "communityGovernance": "consultationRequired",
    "aiTraining": "restrictedWithConditions",
    "exportRestriction": "aggregated-only"
  },
  "fair2:governanceProtocol": "https://community.example.org/consultation"
}
```

---

## **Variant 0.5 — Embargoed, but Derived Summaries Allowed Pre‑Release**

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "dct": "http://purl.org/dc/terms/",
    "fair2": "https://fair2.ai/ns/"
  },
  "@type": "schema:Dataset",
  "schema:name": "Polar Ice Melt Indicators (Embargoed with Summaries)",
  "dct:license": "https://opendatacommons.org/licenses/by/1-0/",
  "dct:accessRights": "fair2:AgreementLevel0",
  "fair2:embargoUntil": "2026-05-10",
  "fair2:constraints": {
    "identity": "none",
    "environment": "none",
    "communityGovernance": "none",
    "aiTraining": "allowed",
    "exportRestriction": "derived-parameters-only"
  },
  "distribution": [
    {
      "@type": "schema:DataDownload",
      "schema:contentUrl": "https://example.org/files/derived_summary_statistics.csv",
      "fair2:constraints": {
        "environment": "open",
        "exportRestriction": "derived-parameters-only"
      }
    }
  ]
}
```

---

# **4. Summary Table**

| Variant | Meaning | Key FAIR² Constraint |
|--------|---------|----------------------|
| **0.1** | Embargo until fixed date | `fair2:embargoUntil = date` |
| **0.2** | Embargo + post‑release AI limits | preset `aiTraining` + `exportRestriction` |
| **0.3** | Embargo until publication | `fair2:embargoUntil = "publication"` |
| **0.4** | CARE constraints apply after release | `communityGovernance = consultationRequired` |
| **0.5** | Derived outputs allowed pre‑release | distribution-level constraints |

---

# **Navigation**

**[Level 1 →](Level1.md)**

---

**End of Level 0 Documentation — FAIR² Access Governance**
