# FAIR² and GO FAIR Integration

## 🎯 Overview

FAIR² (**FAIR Squared**) is aligned with the **GO FAIR** initiative, ensuring that datasets are **Findable, Accessible, Interoperable, and Reusable (FAIR)** while also being **AI-ready and machine-actionable**.

GO FAIR provides a global framework for **FAIR data principles**, and FAIR² builds on this foundation by incorporating **AI/ML-specific metadata, structured validation (SHACL), and linked data interoperability**.

This document explains how FAIR² extends GO FAIR principles and enhances **machine learning readiness**.

---

## 📌 **FAIR² and the GO FAIR Principles**

| **GO FAIR Principle** | **How FAIR² Enhances It** |
|----------------------|-------------------------|
| **Findable (F)** | ✅ Uses **FAIR Signposting, PIDs, and Schema.org metadata** to improve dataset discovery. |
| **Accessible (A)** | ✅ Ensures dataset access is **machine-actionable** using **structured JSON-LD metadata**. |
| **Interoperable (I)** | ✅ Standardizes metadata with **ML Croissant, Schema.org, and RDF/SHACL** for AI/ML compatibility. |
| **Reusable (R)** | ✅ Adds **data article metadata, methodology tracking, and validation rules** for high-quality datasets. |

FAIR² maintains **full compatibility** with GO FAIR principles while focusing on **AI-driven research needs**.

---

## 🚀 **How FAIR² Extends GO FAIR**

### 1️⃣ **FAIR² Uses Linked Data for Interoperability**
- **Built on RDF & JSON-LD** to support semantic data integration.
- Uses **persistent identifiers (PIDs)** for dataset tracking.
- Supports **Schema.org & ML Croissant metadata** for AI-driven research.

### 2️⃣ **FAIR² Enhances AI/ML Dataset Documentation**
- Introduces **ML Croissant extensions** to describe **AI model training datasets**.
- Standardizes **methodology tracking** with `MethodSectionShape` & `MethodStepShape`.
- Supports **FAIR AI metadata** to ensure **bias, ethics, and reproducibility** are documented.

### 3️⃣ **FAIR² Implements SHACL Validation**
- Uses **SHACL constraints** to enforce structured metadata.
- Provides **machine-readable validation rules** for **dataset quality control**.
- Ensures datasets conform to **GO FAIR's Interoperability guidelines**.
