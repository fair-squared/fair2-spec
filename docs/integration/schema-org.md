# FAIR² and Schema.org Integration

## 🎯 Overview

FAIR² (**FAIR Squared**) builds upon **Schema.org**, ensuring that datasets are **Findable, Accessible, Interoperable, and Reusable (FAIR)** while also being **AI-ready and machine-actionable**.

Schema.org is a widely used **structured data vocabulary** that enhances dataset discoverability. FAIR² extends Schema.org by:
✅ **Adding SHACL validation** for metadata consistency.  
✅ **Enabling AI/ML-specific metadata** to describe datasets.  
✅ **Improving machine-actionability** with linked data principles.  

This document explains how FAIR² leverages **Schema.org metadata** to improve dataset interoperability.

---

## 📌 **How FAIR² Uses Schema.org**
FAIR² extends Schema.org by adding **structured AI-specific metadata**.

| **Schema.org Term** | **Usage in FAIR²** | **Example** |
|---------------------|------------------|-------------|
| `schema:Dataset` | Defines datasets in FAIR². | `"@type": "Dataset"` |
| `schema:author` | Specifies dataset authorship. | `"author": { "@type": "Person", "name": "Dr. Jane Doe" }` |
| `schema:citation` | Links to related publications. | `"citation": "Doe et al. (2025)"` |
| `schema:datePublished` | Specifies dataset publication date. | `"datePublished": "2025-03-01"` |
| `schema:distribution` | Describes dataset access links. | `"distribution": { "contentUrl": "https://example.com/data.csv" }` |
| `schema:license` | Specifies dataset licensing. | `"license": "https://creativecommons.org/licenses/by/4.0/"` |

FAIR² **remains fully compatible with Schema.org** while adding **AI-specific metadata and validation rules**.

---

## 📌 Why Schema.org Matters for FAIR²

✅ **Enhances dataset discoverability** – Improves indexing by search engines & AI platforms.
✅ **Ensures machine-actionability** – Provides structured metadata for ML workflows.
✅ **Supports FAIR principles** – Aligns with linked data & persistent identifiers.
✅ **Interoperable with ML Croissant** – Works within AI-ready metadata frameworks.

---

## 🚀 Next Steps

1️⃣ [Explore the FAIR² Schema](../specification/schema.md)
2️⃣ [Learn about SHACL Validation](../specification/shacl-validation.md)
3️⃣ [Contribute to FAIR²](../community/contributing.md)