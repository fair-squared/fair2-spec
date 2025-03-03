# FAIR² Specification Overview

## 🔍 What is FAIR²?

FAIR² (**FAIR Squared**) is an extension of the **FAIR principles** (Findable, Accessible, Interoperable, Reusable), designed to make datasets **AI-ready, context-rich, and machine-actionable**. 

While traditional FAIR principles focus on making data discoverable and reusable, **FAIR² goes further** by ensuring that datasets:
- Are **natively structured** for machine learning workflows.
- Include **rich metadata** for better context and provenance.
- Are **validated using SHACL** for interoperability and quality control.
- Align with **responsible AI principles** to promote transparency and ethical AI use.

FAIR² is **built on top of ML Croissant**, ensuring compatibility with widely accepted machine learning dataset descriptions.

---

## 📚 **Core Components of FAIR²**

FAIR² enhances the original FAIR framework with **three key components**:

### 1️⃣ **Context-Rich Metadata**
- Supports **domain-specific annotations** to provide deeper semantic meaning.
- Utilizes **structured metadata formats** compatible with **ML Croissant** and **Schema.org**.
- Ensures proper documentation of **data provenance, licensing, and ethical considerations**.

### 2️⃣ **AI-Ready Design**
- Adapts to **machine learning workflows** by specifying metadata in **JSON-LD** and **RDF** formats.
- Leverages **structured schemas** for seamless integration into ML models and AI pipelines.
- Supports **automated data validation** using SHACL constraints.

### 3️⃣ **Responsible AI Alignment**
- Promotes **transparent, bias-aware** dataset documentation.
- Incorporates **ethics and governance metadata** for AI fairness assessments.
- Ensures compliance with **open and reproducible AI research** best practices.

---

## 🌍 **How FAIR² Builds on ML Croissant**
FAIR² **extends** the [ML Croissant](https://mlcommons.org/croissant/) specification by:
- Adding **SHACL validation** for stricter compliance with structured metadata rules.
- Enhancing **AI-specific metadata** for better integration into ML pipelines.
- Strengthening **data governance and ethical AI considerations**.

FAIR² remains **fully compatible** with ML Croissant and Schema.org, ensuring seamless interoperability.

---

## 📌 **Technical Highlights**
FAIR² relies on:
✅ **JSON-LD & RDF** for machine-readable metadata.  
✅ **SHACL** (Shapes Constraint Language) for schema validation.  
✅ **Schema.org extensions** to provide rich, AI-specific annotations.  
✅ **FAIR Signposting & Persistent Identifiers** for dataset discoverability.  

For more details, see:
- [FAIR² Schema](schema.md)
- [SHACL Validation](shacl-validation.md)
- [JSON-LD & RDF](../technical/json-ld.md)

---

## 🚀 **Next Steps**
To start using FAIR²:
1. Read the [Getting Started Guide](../getting-started.md).
2. Explore the [FAIR² Schema](schema.md).
3. Check out [Example Datasets](examples.md).

Want to contribute? See [Contributing](../community/contributing.md).

---
_Last updated: [03/03/2025]_