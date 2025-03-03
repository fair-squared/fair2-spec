# FAIR² Schema

## 📌 Overview

The core of FAIR² is the **DatasetShape**, which extends existing metadata standards to support AI applications.

---

## 📂 **Dataset Schema (`DatasetShape`)**
The `DatasetShape` is the main schema used in FAIR² to describe datasets.

### **Key Properties**
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `schema:author` | `AuthorShape` | The author(s) of the dataset. | Required (min 1) |
| `schema:citation` | `xsd:string` | A reference to another creative work. | Required (min 1) |
| `mlc:citeAs` | `xsd:string` | The preferred way to cite the dataset. | Required (min 1, max 1) |
| `schema:conformsTo` | `xsd:anyURI` | The standard the dataset conforms to. | Required (min 1, max 1) |
| `schema:contentUrl` | `xsd:anyURI` | Direct link to the dataset. | Required (min 1) |
| `schema:datePublished` | `xsd:date` | Date the dataset was published. | Required (min 1, max 1) |
| `schema:description` | `xsd:string` | A textual description of the dataset. | Required (min 1, max 1) |
| `schema:distribution` | `DistributionShape` | Details about dataset distribution. | Required (min 1) |
| `schema:funding` | `GrantShape` | Funding information. | Required (min 1) |
| `schema:identifier` | `xsd:anyURI` | A unique identifier for the dataset. | Required (min 1) |
| `schema:keywords` | `xsd:string` | Keywords or tags describing the dataset. | Required (min 1) |
| `schema:license` | `xsd:anyURI` | The dataset's license. | Required (min 1) |
| `schema:name` | `xsd:string` | The dataset's name. | Required (min 1) |
| `fair2:dataArticle` | `DataArticleShape` | Metadata of a related data article. | Optional |
| `mlc:recordSet` | `RecordSetShape` | The dataset’s record set. | Required (min 1) |

---

## 📂 **Dataset Distribution Schema**
The **`schema:distribution`** property defines the dataset files.

### **Key Properties**
| Property | Type | Description |
|----------|------|-------------|
| `schema:contentSize` | `xsd:integer` | File size in bytes. |
| `schema:contentUrl` | `xsd:anyURI` | URL to download the file. |
| `schema:description` | `xsd:string` | A description of the dataset file. |
| `schema:encodingFormat` | `xsd:string` | The file format (e.g., CSV, JSON). |
| `schema:name` | `xsd:string` | The name of the dataset file. |
| `mlc:sha256` | `xsd:string` | SHA-256 hash for data integrity. |

---

## 📂 **Data Article Schema (`DataArticleShape`)**
The `DataArticleShape` extends **Schema.org’s `ScholarlyArticle`** to describe a research article related to the dataset.

### **Key Properties**
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `schema:name` | `xsd:string` | The article’s title. | Required |
| `fair2:methodSection` | `MethodSectionShape` | Details on the methodology used. | Required (min 1) |

---

## 📂 **Methodology Schema (`MethodSectionShape` & `MethodStepShape`)**
The **`MethodSectionShape`** and **`MethodStepShape`** document the dataset’s methodology.

### **MethodSectionShape**
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `schema:name` | `xsd:string` | Section title. | Required |
| `fair2:step` | `MethodStepShape` | Steps in the methodology. | Required (min 1) |

### **MethodStepShape**
| Property | Type | Description | Constraints |
|----------|------|-------------|-------------|
| `schema:name` | `xsd:string` | Step title. | Required |
| `schema:description` | `xsd:string` | Step details. | Required |
| `schema:nextItem` | `IRI` | Reference to the next step. | Optional |
| `fair2:substep` | `IRI` | Reference to a sub-step. | Optional |

---

## 🎯 **Why Use FAIR² Schema?**
✅ **Extends ML Croissant** – Built on a widely adopted AI metadata framework.  
✅ **AI-Ready** – Structured metadata makes datasets easy to use in **PyTorch** & **TensorFlow**.  
✅ **Validation with SHACL** – Ensures datasets meet compliance and interoperability standards.  
✅ **Supports Research Integrity** – Includes metadata for **data articles and methodologies**.  

---

## 🚀 **Next Steps**
- **[Validate your dataset](shacl-validation.md)** with SHACL.
- **[See dataset examples](examples.md)** to understand real-world usage.
- **[Learn about JSON-LD & RDF](../technical/json-ld.md)** for AI-ready metadata.

---
_Last updated: [03/03/2025]_  