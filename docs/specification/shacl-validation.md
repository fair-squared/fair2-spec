# SHACL Validation in FAIR²

## 🔍 What is SHACL?

**SHACL (Shapes Constraint Language)** is a W3C standard for validating RDF data. FAIR² uses SHACL to ensure that datasets conform to structured metadata requirements, enabling:
- **Schema compliance** – Ensuring datasets follow FAIR² metadata rules.
- **Interoperability** – Enforcing structured descriptions for AI-ready datasets.
- **Automated validation** – Catching missing metadata and inconsistencies.

---

## 📌 Why Validate with SHACL?

FAIR² uses SHACL to:
✅ Ensure datasets **meet FAIR² schema constraints**.  
✅ Detect **missing or incorrect metadata**.  
✅ Standardize metadata across **ML Croissant & Schema.org**.  
✅ Improve **dataset quality & machine-actionability**.  

---

## 🚀 **How to Validate Your Dataset with SHACL**

### 1️⃣ **Install Required Tools**
To validate a dataset against FAIR²’s SHACL rules, install:

```bash
pip install pyshacl rdflib
```
### 2️⃣ **Prepare Your Dataset Metadata**

Make sure you have a FAIR² metadata file (fair2.json), structured according to FAIR² Schema.

Example dataset metadata (fair2.json):

```json
{
  "@context": "https://fair2.ai/ns/",
  "@type": "Dataset",
  "name": "AI-ready Dataset",
  "description": "A dataset for training machine learning models.",
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
### 3️⃣ **Run SHACL Validation**

To validate against FAIR²’s SHACL constraints, run:

```bash
pyshacl -s fair2-shapes.ttl -d fair2.jsonld
```

✅ Valid dataset:
```plaintext
Validation Report
Conforms: True
```

❌ Invalid dataset (e.g., missing schema:license):
```plaintext
Validation Report
Conforms: False
Violation: Missing required property schema:license
```

📂 FAIR² SHACL Rules

FAIR²’s SHACL rules ensure datasets comply with structured metadata requirements.

## 📂 FAIR² SHACL Rules

FAIR²’s SHACL rules ensure datasets comply with structured metadata requirements.

| **Validation Type** | **Requirements** |
|---------------------|-----------------|
| **Dataset Validation (`DatasetShape`)** | - Must include **dataset name, description, author, license, and identifier**. <br> - Must have at least **one distribution file** (`schema:distribution`). <br> - Should include **a citation** (`schema:citation`) and **a preferred citation format** (`cr:citeAs`). |
| **Data Article Validation (`DataArticleShape`)** | - If provided, must **link to a scholarly article** (`schema:ScholarlyArticle`). <br> - Should have **a method section** (`fair2:methodSection`). |
| **Methodology Validation (`MethodSectionShape` & `MethodStepShape`)** | - **Method sections** (`fair2:MethodSectionShape`) must contain at least **one step** (`fair2:step`). <br> - **Method steps** (`fair2:MethodStepShape`) should: <br> &nbsp; - Have a **name** (`schema:name`) and **description** (`schema:description`). <br> &nbsp; - Optionally reference **next steps** (`schema:nextItem`). |

---

## 🎯 **Why SHACL is Essential for FAIR²**

✅ **Guarantees dataset compliance** with FAIR² and ML Croissant.
✅ Reduces metadata errors, improving **dataset usability**.
✅ Ensures AI-ready metadata for machine learning pipelines.
✅ Provides structured validation for **research integrity**.


## 🚀 **Next Steps**
- **[Validate your dataset](shacl-validation.md)** with SHACL.
- **[See dataset examples](examples.md)** to understand real-world usage.
- **[Learn about JSON-LD & RDF](../technical/json-ld.md)** for AI-ready metadata.
