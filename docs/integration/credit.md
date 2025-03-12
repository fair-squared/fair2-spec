
# FAIR² and CRediT Integration

## 🎯 Overview

FAIR² integrates **CRediT (Contributor Roles Taxonomy)** to **attribute dataset contributions** transparently.  
This ensures that **researchers, curators, and developers receive proper recognition**.

---

## 📌 **How FAIR² Uses CRediT**
CRediT enables **structured contributor roles** in FAIR² metadata.

| **FAIR² Property** | **CRediT Mapping** | **Description** |
|-----------------|----------------|----------------|
| `schema:creator` | `credit:ContributorRole` | Defines **individual roles in dataset creation**. |
| `schema:contributor` | `credit:ContributorRole` | Specifies **additional dataset contributors**. |
| `schema:curator` | `credit:Curation` | Documents **data curation efforts**. |

---

## 🔍 **Example: JSON-LD with CRediT**
```json
{
  "@context": [
    "https://credit.niso.org/",
    "https://fair2.ai/ns/"
  ],
  "@type": "Dataset",
  "name": "FAIR AI Benchmark Dataset",
  "creator": [
    {
      "@type": "Person",
      "name": "Dr. Alice Smith",
      "credit:role": "Conceptualization"
    },
    {
      "@type": "Person",
      "name": "John Doe",
      "credit:role": "Data Curation"
    }
  ]
}