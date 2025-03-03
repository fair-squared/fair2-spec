# FAIR² and PROV-O Integration

## 🎯 Overview

FAIR² (**FAIR Squared**) adopts **PROV-O (Provenance Ontology)** to provide **structured provenance metadata**, ensuring datasets are:
- **Findable** – Tracking dataset origins and modifications.
- **Accessible** – Providing machine-readable provenance records.
- **Interoperable** – Using **linked data** for provenance documentation.
- **Reusable** – Ensuring transparency and reproducibility in AI/ML research.

PROV-O is a **W3C standard ontology** for representing **data lineage, authorship, and transformation processes**.  
FAIR² enhances **dataset provenance** using PROV-O within **JSON-LD metadata**.

---

## 📌 **How FAIR² Uses PROV-O**
FAIR² integrates **PROV-O concepts** to **track dataset creation, modifications, and usage**.

| **PROV-O Term** | **Usage in FAIR²** | **Example** |
|----------------|------------------|-------------|
| `prov:Entity` | Represents a dataset or data file. | `"@type": "prov:Entity"` |
| `prov:Agent` | Describes authors, organizations, or software involved. | `"@type": "prov:Agent"` |
| `prov:Activity` | Captures actions like dataset creation or transformation. | `"@type": "prov:Activity"` |
| `prov:wasGeneratedBy` | Links a dataset to the process that created it. | `"wasGeneratedBy": { "@type": "prov:Activity", "name": "Data Collection" }` |
| `prov:wasAttributedTo` | Assigns authorship or ownership to an entity. | `"wasAttributedTo": { "@type": "prov:Agent", "name": "Research Lab X" }` |
| `prov:wasDerivedFrom` | Links derived datasets to their original sources. | `"wasDerivedFrom": "https://doi.org/10.1234/original-dataset"` |

By incorporating PROV-O, FAIR² ensures **provenance metadata is machine-actionable and AI-compatible**.

---

## 🚀 **FAIR² Provenance Metadata Example (JSON-LD)**
Here’s how a **FAIR²-compliant dataset** includes **PROV-O metadata**:

```json
{
  "@context": [
    "https://www.w3.org/ns/prov",
    "https://fair2.ai/ns/"
  ],
  "@type": "Dataset",
  "name": "AI-ready Dataset",
  "description": "A dataset aligned with PROV-O for provenance tracking.",
  "author": {
    "@type": "prov:Agent",
    "name": "Dr. Jane Doe",
    "affiliation": {
      "@type": "Organization",
      "name": "AI Research Lab"
    }
  },
  "wasGeneratedBy": {
    "@type": "prov:Activity",
    "name": "Dataset Preprocessing",
    "startTime": "2025-01-15T10:00:00Z",
    "endTime": "2025-01-15T12:00:00Z"
  },
  "wasAttributedTo": {
    "@type": "prov:Agent",
    "name": "AI Research Lab",
    "role": "Data Curator"
  },
  "wasDerivedFrom": "https://doi.org/10.1234/original-dataset"
}

```

✅ PROV-O-compatible – Uses standard provenance terms.
✅ FAIR²-compliant – Tracks dataset lineage and transformation.
✅ Machine-actionable – Enhances AI/ML data transparency.

## 📌 Why PROV-O Matters for FAIR²

✅ Ensures dataset transparency – Tracks who created, modified, or curated the dataset.
✅ Improves AI/ML model reproducibility – Documents data transformations and derivations.
✅ Aligns with Open Science – Supports provenance tracking for research integrity.
✅ Enhances metadata interoperability – Uses W3C standards for global adoption.

---

## 🚀 Next Steps

1️⃣ [Explore the FAIR² Schema](../specification/schema.md)
2️⃣ [Learn about SHACL Validation](../specification/shacl-validation.md)
3️⃣ [Contribute to FAIR²](../community/contributing.md)