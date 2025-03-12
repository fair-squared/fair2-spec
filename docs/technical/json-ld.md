# JSON-LD in FAIR²

## 🔍 What is JSON-LD?

**JSON-LD (JavaScript Object Notation for Linked Data)** is a lightweight linked data format used in FAIR² to represent machine-readable metadata. It allows datasets to be:
- **Interoperable** – Ensures compatibility with Schema.org, ML Croissant, and FAIR principles.
- **AI-Ready** – Enables seamless integration into machine learning workflows.
- **Linked Data-Compliant** – Supports globally unique identifiers and structured relationships.

FAIR² uses **JSON-LD** to describe datasets in a way that both **humans and machines can understand**.

---

## 📌 Why JSON-LD for FAIR²?

✅ **Compatible with ML Croissant** – Works with AI dataset metadata standards.  
✅ **Supports Schema.org** – Ensures datasets are discoverable by search engines.  
✅ **Enhances FAIR principles** – Provides rich semantic metadata.  
✅ **Machine-Actionable** – Facilitates AI & ML dataset integration.  

---

## 🚀 **Basic JSON-LD Structure in FAIR²**

A **FAIR² dataset metadata file** (`fair2.json`) follows this structure:

```json
{
  "@context": "https://fair2.ai/spec/fair2_context",
  "@type": "Dataset",
  "name": "Example AI Dataset",
  "description": "A dataset for training AI models.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://example.com/data.csv",
      "encodingFormat": "text/csv"
    }
  ]
}
```

## 📂 FAIR² JSON-LD Context (@context)

The @context defines how terms in the dataset metadata map to standardized vocabularies.

### Example FAIR² Context

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "xsd": "http://www.w3.org/2001/XMLSchema#",
    "cr": "https://mlcommons.org/ns/",
    "fair2": "https://fair2.ai/ns/"
  }
}
```

### How @context Works
- schema → Maps to Schema.org properties (e.g., schema:name).
- xsd → Ensures correct datatypes (e.g., xsd:string).
- mlc → Supports ML Croissant metadata (e.g., cr:citeAs).
- fair2 → Defines FAIR²-specific extensions.

## 📌 FAIR² Metadata Schema in JSON-LD

FAIR² extends Schema.org and ML Croissant to describe AI-ready datasets.

### Dataset Metadata Example

```json
{
  "@context": [
    "https://fair2.ai/spec/fair2_json",
  ],
  "@type": "Dataset",
  "name": "FAIR² AI Dataset",
  "description": "A dataset prepared for machine learning workflows.",
  "author": {
    "@type": "Person",
    "name": "Dr. Jane Doe",
    "affiliation": {
      "@type": "Organization",
      "name": "AI Research Lab"
    }
  },
  "citation": "Doe, J. (2025). FAIR² Dataset for AI Research.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "distribution": [
    {
      "@type": "DataDownload",
      "contentUrl": "https://example.com/data.zip",
      "encodingFormat": "application/zip"
    }
  ],
  "cr:citeAs": "Doe, J. FAIR² AI Dataset (2025)",
  "schema:conformsTo": "https://fair2.ai/spec/"
}
```

---

## 🎯 Why JSON-LD Matters for FAIR²

✅ Enhances dataset discoverability using Schema.org.
✅ Ensures machine-actionable metadata for AI pipelines.
✅ Supports FAIR principles by enabling structured linked data.
✅ Facilitates interoperability with ML Croissant & SHACL validation.

---
## 🚀 Next Steps

1️⃣ Explore the [FAIR² Schema](../specification/schema.md) to structure datasets correctly.
2️⃣ Validate JSON-LD using SHACL & RDF tools.
3️⃣ [Learn about SHACL Validation](../specification/shacl-validation.md) for quality assurance.