# FAIR² Schema

## 📌 Overview

The core of FAIR² is the **DatasetShape**, which extends existing metadata standards to support AI applications.

---

## 🎯 Resource Types Covered in FAIR²

FAIR² supports a broad range of **research resources** to ensure **AI-ready, FAIR-compliant data management**. These include datasets, metadata records, methodology descriptions, and file structures.


| **Resource Type** | **Description** | **Schema Mapping** |
|------------------|---------------|--------------------|
| **Datasets (`schema:Dataset`)** | Primary research datasets, including structured and unstructured data files. | `schema:Dataset`, `mlc:DatasetShape` |
| **Scholarly Articles (`schema:ScholarlyArticle`)** | Research publications describing datasets, methodologies, or findings. | `schema:ScholarlyArticle`, `fair2:DataArticleShape` |
| **Methodology & Workflows (`fair2:MethodSection`)** | Descriptions of methods used in research, including computational workflows. | `fair2:MethodSectionShape`, `fair2:MethodStepShape` |
| **Visualizations (`fair2:Visualization`)** | Graphs, plots, and interactive visual representations of datasets. | `fair2:Visualization`, `schema:ImageObject` |
| **Data Records (`mlc:RecordSet`)** | Individual data points, records, or observations within datasets. | `mlc:RecordSet`, `fair2:RecordSetShape` |
| **Fields (`mlc:Field`)** | Metadata describing **individual attributes/columns** in tabular datasets. | `mlc:Field`, `schema:PropertyValue` |
| **Files (`mlc:FileObject`)** | Individual files within a dataset (e.g., CSV, images, logs). | `mlc:FileObject`, `schema:MediaObject` |

### 🔍 **How FAIR² Extends These Resource Types**
- **AI/ML Ready** – Ensures datasets, fields, and file objects are **structured for AI workflows**.
- **Methodology Tracking** – Captures **research steps, data transformations, and provenance**.
- **Visualization Support** – Enables **dataset interpretability with graphical outputs**.
- **SHACL Validation** – Ensures **schema consistency across datasets**.

---

## 📂 **Dataset Schema (`DatasetShape`)**
The `DatasetShape` is the main schema used in FAIR² to describe datasets.

### 🎯 Key Properties of FAIR² Datasets

| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `@context` | `URL` | JSON-LD context definitions for metadata. | Required (exactly 1) |
| `@type` | `Text` | Declares the type of dataset (e.g., `schema:Dataset`). | Required (exactly 1) |
| `dct:conformsTo` | `URL` | Declares conformance to FAIR² and ML Croissant specifications. | Required (min 1) |
| `schema:name` | `xsd:string` | The name of the dataset. | Required (exactly 1) |
| `schema:description` | `xsd:string` | A short textual description of the dataset. | Required (exactly 1) |
| `schema:version` | `xsd:string` | Version identifier for the dataset. | Required (exactly 1) |
| `schema:distribution` | `mlc:FileObject` or `mlc:FileSet` | Describes the dataset’s distribution resources. | Required (min 1) |
| `schema:author` | `fair2:AuthorShape` | The author(s) of the dataset. | Required (min 1) |
| `schema:creator` | `schema:Person` or `schema:Organization` | Identifies dataset creators (with CRediT roles). | Required (min 1) |
| `schema:methods` | `fair2:MethodShape` | Details the methods used to generate the dataset. | Required (min 1) |
| `mlc:recordSet` | `mlc:RecordSet` | Represents structured data in the dataset. | Required (min 1) |
| `schema:funding` | `schema:GrantShape` | Funding information for the dataset. | Required (min 1) |
| `schema:datePublished` | `xsd:date` | Date the dataset was published. | Required (exactly 1) |
| `schema:identifier` | `xsd:anyURI` | A unique identifier for the dataset (DOI, URL, etc.). | Required (min 1) |
| `schema:license` | `xsd:anyURI` | The dataset's license. | Required (min 1) |
| `schema:citation` | `xsd:string` | A reference to another creative work citing this dataset. | Required (min 1) |
| `mlc:citeAs` | `xsd:string` | The preferred way to cite this dataset. | Required (min 1, max 1) |
| `schema:conformsTo` | `xsd:anyURI` | The standard the dataset conforms to. | Required (min 1, max 1) |

---

### 🎯 **Recommended Properties**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `schema:keywords` | `xsd:string`, `URL`, `DefinedTerm` | Keywords or tags describing the dataset. | Recommended (min 1) |
| `schema:publisher` | `schema:Person` or `schema:Organization` | Entity responsible for publishing the dataset. | Recommended (min 1) |
| `schema:dateCreated` | `xsd:date` | The date the dataset was first created. | Recommended (exactly 1) |
| `schema:dateModified` | `xsd:date` | The date the dataset was last modified. | Recommended (exactly 1) |
| `schema:sameAs` | `xsd:anyURI` | URL of another resource representing the same dataset. | Recommended (min 1) |

---

### 🎯 **Optional Properties**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `fair2:dataArticle` | `fair2:DataArticleShape` | Metadata of a related data article. | Optional |
| `schema:ethicsReview` | `fair2:EthicsReview` | Ethical assessments related to the dataset. | Optional (min 1) |
| `fair2:dataBiases` | `fair2:DataBiases` | Documents known biases in the dataset. | Optional (min 1) |
| `fair2:dataLimitations` | `fair2:DataLimitations` | Specifies known limitations or constraints of the dataset. | Optional (min 1) |
| `mlc:citeAs` | `xsd:string` | Citation for the dataset, ideally in BibTeX format. | Optional (exactly 1) |
| `fair2:isLiveDataset` | `xsd:boolean` | Indicates whether the dataset is live and subject to updates. | Optional (exactly 1) |

---|

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

# 📂 Data Article Schema (`DataArticleShape`)

## 🎯 Overview
The `DataArticleShape` extends **Schema.org’s `ScholarlyArticle`** to describe **a research article related to a dataset**.  
This includes metadata about the article, **authorship, publication details, methodology, and citation relationships**.

---

## 📌 **Key Properties**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `schema:name` | `xsd:string` | The title of the article. | Required |
| `schema:headline` | `xsd:string` | The headline or key summary of the article. | Optional |
| `schema:abstract` | `xsd:string` | A textual abstract summarizing the article. | Optional |
| `schema:author` | `schema:Person` or `schema:Organization` | The author(s) of the article. | Required (min 1) |
| `schema:datePublished` | `xsd:date` | The publication date of the article. | Required (exactly 1) |
| `schema:isPartOf` | `schema:PublicationIssue` | The issue in which the article was published. | Optional |

---

## 📌 **Publication Information**
Since **articles are often part of journals, books, or conference proceedings**, `schema:isPartOf` allows linking the article to its **publication issue, volume, and periodical**.

### 📂 **Publication Issue (`schema:PublicationIssue`)**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `schema:issueNumber` | `xsd:string` | The issue number where the article is published. | Optional |
| `schema:isPartOf` | `schema:PublicationVolume` | The publication volume containing the issue. | Optional |

### 📂 **Publication Volume (`schema:PublicationVolume`)**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `schema:volumeNumber` | `xsd:string` | The volume number where the article is published. | Optional |
| `schema:isPartOf` | `schema:Periodical` | The periodical in which the volume is published. | Optional |

### 📂 **Periodical (Journal, Conference, or Book Series) (`schema:Periodical`)**
| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `schema:name` | `xsd:string` | The name of the journal, book series, or conference. | Required |
| `schema:issn` | `xsd:string` | The ISSN of the journal (if applicable). | Optional |
| `schema:publisher` | `schema:Organization` | The entity responsible for publishing the periodical. | Optional |

---

## 🔍 **Example: JSON-LD Representation of a Data Article**
```json
{
  "@context": [
    "https://schema.org/",
    "https://fair2.ai/ns/"
  ],
  "@type": "ScholarlyArticle",
  "name": "AI-driven Data Processing Techniques",
  "headline": "A novel approach to AI-enhanced data curation.",
  "abstract": "This paper explores AI-driven methodologies for large-scale data curation...",
  "author": {
    "@type": "Person",
    "name": "Dr. Jane Doe",
    "affiliation": {
      "@type": "Organization",
      "name": "AI Research Lab"
    }
  },
  "datePublished": "2025-03-01",
  "isPartOf": {
    "@type": "PublicationIssue",
    "issueNumber": "4",
    "isPartOf": {
      "@type": "PublicationVolume",
      "volumeNumber": "15",
      "isPartOf": {
        "@type": "Periodical",
        "name": "Journal of Machine Learning",
        "issn": "1234-5678",
        "publisher": {
          "@type": "Organization",
          "name": "ML Publications",
          "url": "https://mlpublications.org"
        }
      }
    }
  }
}
```
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

## 🎯 Resource Types: RecordSet, Field, and FileObject

FAIR² builds on **ML Croissant's metadata model**, integrating **structured representations** for **datasets, records, features, and file distributions**.

Below is a detailed breakdown of **key properties** for ML Croissant’s **`RecordSet`**, **`Field`**, and **`FileObject`** resources.

---

## 📌 **RecordSet Properties (`mlc:RecordSet`)**

A **`RecordSet`** represents structured data, such as tabular datasets, containing individual **data records**.

| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `@context` | `URL` | JSON-LD context definitions for metadata. | Required (exactly 1) |
| `@type` | `Text` | Declares the type as `mlc:RecordSet`. | Required (exactly 1) |
| `schema:name` | `xsd:string` | The name of the record set. | Required (exactly 1) |
| `schema:description` | `xsd:string` | A textual description of the record set. | Required (exactly 1) |
| `mlc:fields` | `mlc:Field` | The list of fields (columns) in the record set. | Required (min 1) |
| `schema:identifier` | `xsd:anyURI` | A unique identifier for the record set. | Recommended (min 1) |
| `schema:keywords` | `xsd:string`, `URL`, `DefinedTerm` | Keywords describing the record set. | Recommended (min 1) |
| `mlc:source` | `mlc:FileObject` | Reference to the data file containing the record set. | Recommended (min 1) |

---

## 📌 **Field Properties (`mlc:Field`)**

A **`Field`** describes **an individual attribute/column** within a `RecordSet`, specifying **data types, descriptions, and relationships**.

| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `@context` | `URL` | JSON-LD context definitions for metadata. | Required (exactly 1) |
| `@type` | `Text` | Declares the type as `mlc:Field`. | Required (exactly 1) |
| `schema:name` | `xsd:string` | The name of the field. | Required (exactly 1) |
| `schema:description` | `xsd:string` | A description of what the field represents. | Required (exactly 1) |
| `mlc:dataType` | `Text` | Data type of the field (e.g., `Integer`, `String`, `Boolean`). | Required (exactly 1) |
| `mlc:example` | `Any` | Example values demonstrating typical field content. | Recommended (min 1) |
| `mlc:unitCode` | `Text` | The unit of measurement (if applicable). | Optional |
| `mlc:format` | `Text` | The expected format of the data (e.g., `ISO-8601`, `float`). | Optional |
| `mlc:isRequired` | `Boolean` | Indicates if the field is mandatory. | Optional |
| `mlc:hasCategory` | `URL` | Link to an external vocabulary defining field values. | Optional |

---

## 📌 **FileObject Properties (`mlc:FileObject`)**

A **`FileObject`** represents **a file containing dataset records**, including its **format, location, and checksum validation**.

| **Property** | **Type** | **Description** | **Constraints** |
|-------------|---------|----------------|----------------|
| `@context` | `URL` | JSON-LD context definitions for metadata. | Required (exactly 1) |
| `@type` | `Text` | Declares the type as `mlc:FileObject`. | Required (exactly 1) |
| `schema:name` | `xsd:string` | The name of the file. | Required (exactly 1) |
| `schema:description` | `xsd:string` | A textual description of the file contents. | Required (exactly 1) |
| `schema:contentUrl` | `xsd:anyURI` | The URL or file path where the file can be accessed. | Required (exactly 1) |
| `schema:encodingFormat` | `xsd:string` | File format (e.g., `text/csv`, `application/json`). | Required (exactly 1) |
| `mlc:sha256` | `xsd:string` | SHA-256 hash of the file for integrity verification. | Recommended (exactly 1) |
| `schema:contentSize` | `xsd:integer` | Size of the file in bytes. | Recommended (exactly 1) |
| `schema:dateCreated` | `xsd:date` | The date the file was created. | Optional |
| `schema:dateModified` | `xsd:date` | The date the file was last modified. | Optional |

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