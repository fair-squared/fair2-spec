# FAIR² and ML Croissant Integration

## 🎯 Overview

FAIR² (**FAIR Squared**) builds directly on **ML Croissant**, extending its capabilities to ensure that datasets are **FAIR (Findable, Accessible, Interoperable, and Reusable) and AI-ready**.

ML Croissant is a **metadata standard for machine learning datasets** developed by MLCommons. FAIR² enhances this by adding:
✅ **SHACL validation** for structured dataset metadata.  
✅ **Support for AI/ML methodologies** using `MethodSectionShape` and `MethodStepShape`.  
✅ **FAIR AI compliance** by tracking dataset provenance and usage.  

This document explains how FAIR² extends **ML Croissant** to provide **machine-actionable AI metadata**.

---

## ML Croissant Dataset: High-Level Required Properties

| **Property**      | **Description** | **Type** | **Example** |
|------------------|---------------|----------|-------------|
| `@type` | Specifies the type of the dataset. Always `sc:Dataset`. | `sc:Dataset` | `"@type": "sc:Dataset"` |
| `name` | The title of the dataset. | `xsd:string` | `"name": "FAIR AI Benchmark Dataset"` |
| `description` | A detailed explanation of the dataset’s contents and purpose. | `xsd:string` | `"description": "A dataset for evaluating AI fairness."` |
| `license` | The license under which the dataset is released. | `xsd:anyURI` | `"license": "https://creativecommons.org/licenses/by/4.0/"` |
| `url` | A link to the dataset’s landing page or repository. | `xsd:anyURI` | `"url": "https://example.com/dataset"` |
| `distribution` | An array describing dataset files. | `Array<FileObject>` | See **FileObject** section below. |
| `recordSet` | Defines the structure of the dataset. | `Array<RecordSet>` | See **RecordSet** section below. |

## FileObject (Inside `distribution`)
| **Property** | **Description** | **Type** | **Example** |
|-------------|---------------|----------|-------------|
| `@type` | Specifies that the entry is a file. | `cr:FileObject` | `"@type": "cr:FileObject"` |
| `@id` | Unique identifier for the file. | `xsd:string` | `"@id": "file1"` |
| `name` | The filename. | `xsd:string` | `"name": "data.csv"` |
| `contentUrl` | URL where the file is hosted. | `xsd:anyURI` | `"contentUrl": "https://example.com/data.csv"` |
| `encodingFormat` | File format (e.g., CSV, JSON). | `xsd:string` | `"encodingFormat": "text/csv"` |
| `sha256` | SHA-256 checksum for file integrity. | `xsd:string` | `"sha256": "abc123..."` |

## RecordSet (Inside `recordSet`)
| **Property** | **Description** | **Type** | **Example** |
|-------------|---------------|----------|-------------|
| `@type` | Specifies a collection of records. | `cr:RecordSet` | `"@type": "cr:RecordSet"` |
| `name` | The name of the record set. | `xsd:string` | `"name": "User Data"` |
| `description` | A description of the records. | `xsd:string` | `"description": "Contains demographic information."` |
| `field` | Array defining the dataset fields. | `Array<Field>` | See **Field** section below. |

## Field (Inside `field`)
| **Property** | **Description** | **Type** | **Example** |
|-------------|---------------|----------|-------------|
| `@type` | Specifies a dataset field. | `cr:Field` | `"@type": "cr:Field"` |
| `name` | The field name. | `xsd:string` | `"name": "age"` |
| `description` | Description of the field. | `xsd:string` | `"description": "Age of the individual."` |
| `dataType` | The expected data type. | `sc:DataType` | `"dataType": "sc:Integer"` |
| `references` | How to extract the field from a file. | `Object` | `"references": { "fileObject": "file1" }` |

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
  "fair2:method": {
    "@type": "fair2:Section",
    "name": "Data Preprocessing",
    "step": [
      {
        "@type": "fair2:Step",
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

dataset = Dataset("fair2.json")
dataloader = DataLoader(dataset)

for batch in dataloader:
    images, labels = batch
    # Train your AI model here...
```

FAIR² ensures that datasets are machine-actionable and seamlessly integrate into AI pipelines.

---

## 🔍 FAIR² SHACL Validation for ML Croissant Metadata

FAIR² uses SHACL validation to ensure ML Croissant metadata is correctly structured.

To validate a ML Croissant dataset using pySHACL, run:
```bash
pyshacl -s cr_dataset.json -d mydata.json
```

The FAIR2 dataset schema extends the ML Croissant shape. You can ensure all constraints are applied simply by using the `fair2s:DatasetShape` defined in `fair2_dataset.json` :
```bash
pyshacl -s fair2_dataset.json -d mydata.json

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