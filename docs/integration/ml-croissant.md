# FAIR² and ML Croissant Integration

## 🎯 Overview

FAIR² (**FAIR Squared**) builds directly on **ML Croissant**, extending its capabilities to ensure that datasets are **FAIR (Findable, Accessible, Interoperable, and Reusable) and AI-ready**.

ML Croissant is a **metadata standard for machine learning datasets** developed by MLCommons. FAIR² enhances this by adding:
✅ **SHACL validation** for structured dataset metadata.  
✅ **Support for AI/ML methodologies** using `MethodSectionShape` and `MethodStepShape`.  
✅ **FAIR AI compliance** by tracking dataset provenance and usage.  

This document explains how FAIR² extends **ML Croissant** to provide **machine-actionable AI metadata**.

---

## 📌 **How FAIR² Enhances ML Croissant**

| **ML Croissant Feature** | **How FAIR² Extends It** |
|----------------------|-------------------------|
| **Dataset Metadata** | ✅ Adds **SHACL validation** to enforce structured metadata. |
| **ML-Specific Features** | ✅ Supports **structured methodology tracking** for AI models. |
| **Schema.org Compatibility** | ✅ Aligns metadata with **linked data & FAIR principles**. |
| **Provenance & Licensing** | ✅ Adds **FAIR² certification tracking** for AI-ready datasets. |

FAIR² ensures that **ML Croissant metadata is fully validated and AI/ML workflows are documented**.

---

## 🚀 **Using FAIR² with ML Croissant**

### 1️⃣ **FAIR² Metadata Example (JSON-LD)**  
FAIR² extends **ML Croissant** by adding **SHACL validation & methodology tracking**.

```json
{
  "@context": [
    "https://fair2.ai/ns/",
    "https://mlcroissant.org/"
  ],
  "@type": "Dataset",
  "name": "AI-ready Dataset",
  "description": "A dataset structured for AI and machine learning workflows.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "cr:features": [
    {
      "@type": "Feature",
      "name": "Image",
      "dataType": "image/png"
    },
    {
      "@type": "Feature",
      "name": "Label",
      "dataType": "string"
    }
  ],
  "cr:citeAs": "Doe, J. AI Dataset (2025)",
  "fair2:methodSection": {
    "@type": "MethodSection",
    "name": "Data Preprocessing",
    "step": [
      {
        "@type": "MethodStep",
        "name": "Normalization",
        "description": "Rescaling image pixel values between 0 and 1."
      }
    ]
  }
}
```

✅ ML Croissant-compatible – Uses cr:features for structured metadata.
✅ FAIR² extensions – Adds methodology tracking for AI workflows.
✅ FAIR AI principles – Supports citation tracking & licensing compliance.

---

## 📂 Loading FAIR² Metadata in ML Frameworks

One of the key advantages of ML Croissant + FAIR² is that datasets can be loaded directly into AI frameworks like PyTorch and TensorFlow.

### Loading a FAIR² Dataset in PyTorch
```python
from mlcroissant import Dataset
from torch.utils.data import DataLoader

dataset = Dataset("fair2.jsonld")
dataloader = DataLoader(dataset)

for batch in dataloader:
    images, labels = batch
    # Train your AI model here...
```

FAIR² ensures that datasets are machine-actionable and seamlessly integrate into AI pipelines.

---

## 🔍 FAIR² SHACL Validation for ML Croissant Metadata

FAIR² uses SHACL validation to ensure ML Croissant metadata is correctly structured.

To validate a dataset using pySHACL, run:
```bash
pyshacl -s fair2-shapes.ttl -d fair2.jsonld
```

### Common Validation Errors & Fixes

| **Error** | **Cause** | **Fix** |
|-----------|----------|---------|
| **"Missing required property cr:citeAs"** | Dataset lacks citation metadata. | Add `"cr:citeAs": "Your citation format"`. |
| **"schema:distribution must be at least 1"** | No dataset file provided. | Add `"schema:distribution": { "contentUrl": "your_file_url" }`. |
| **"Invalid datatype for schema:datePublished"** | Incorrect date format. | Use `YYYY-MM-DD` format. |

## 📌 FAIR² + ML Croissant: Key Benefits

✅ Ensures datasets are AI-ready with structured metadata.
✅ Supports PyTorch & TensorFlow integration.
✅ Provides SHACL validation for metadata consistency.
✅ Tracks methodology to ensure reproducibility in AI research.

---

## 🚀 Next Steps

1️⃣ [Explore the FAIR² Schema](../specification/schema.md)
2️⃣ [Learn about SHACL Validation](../specification/shacl-validation.md)
3️⃣ [Contribute to FAIR²](../community/contributing.md)

Together, FAIR² and ML Croissant make AI datasets more FAIR and machine-actionable! 🚀