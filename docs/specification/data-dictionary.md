# FAIR² Data Dictionary
**Specification and Implementation Guide**

---

## 1. Purpose and Scope

The FAIR² Core Data Dictionary defines the **minimum interoperable metadata model**
for describing dataset variables in a way that is:

- Human-readable
- Machine-actionable
- Mappable to existing standards (REDCap, ISO/IEC 11179, DDI, DCAT, ML Croissant)
- Compatible with spreadsheet (CSV/Excel) workflows
- Extensible without breaking backward compatibility

The Core profile intentionally avoids domain ontologies, UI logic, or mandatory statistics,
while remaining ready to accommodate them.

---

## 2. Conceptual Model

Each **variable** is treated as a first-class entity that has:

1. A **technical identifier**
2. A **human-readable name**
3. A **semantic definition**
4. A **data type and optional value domain**
5. A **provenance link** to the method step that produced it
6. Optional **descriptive statistics** with provenance

Variables are attached to a dataset using the standard Schema.org property:

```
schema:variableMeasured
```

---

## 3. Terminology (Normative)

### 3.1 Technical Identifier
- **Definition:** Machine-facing, stable identifier used in files, schemas, and code.
- **Mapping:** `schema:identifier`
- **Source (UI):** `variable_name`
- **Requirements:**
  - Unique within the dataset
  - Stable across versions

### 3.2 Human Label
- **Definition:** Human-readable name shown in UIs and documentation.
- **Mapping:** `schema:name`
- **Source (UI):** `variable`

### 3.3 Semantic Definition
- **Definition:** Precise, unambiguous statement of what the variable means.
- **Mapping:** `skos:definition`
- **Source (UI):** `description`
- **Normative rule:** In FAIR² Core, the UI field *description* **IS** the semantic definition.

### 3.4 Usage Description (Optional)
- **Definition:** Contextual or interpretive notes about usage.
- **Mapping:** `schema:description`
- **Status:** Optional; may be added without breaking Core compliance.

---

## 4. Core Properties

### 4.1 Required (FAIR²-Core)

| Property | Vocabulary | Meaning |
|--------|-----------|--------|
| `@id` | RDF | Persistent variable identifier |
| `schema:identifier` | schema.org | Technical name |
| `schema:name` | schema.org | Human label |
| `skos:definition` | SKOS | Semantic definition |
| `cr:dataType` | ML Croissant | Primitive data type |
| `prov:wasGeneratedBy` | PROV-O | Method step provenance |
| `qudt:unit` | QUDT | Unit of measurement (IRI reference) |
| `schema:unitCode` | schema.org | Unit symbol/code |

### 4.2 Strongly Recommended (FAIR²-Core+)

| Property | Vocabulary | Meaning |
|--------|-----------|--------|
| `fair2:format` | FAIR² | Expected format/pattern |
| `fair2:valueDomain` | FAIR² | Permitted values or ranges |
| `fair2:missingValueCode` | FAIR² | Explicit missing codes |
| `fair2:exampleValue` | FAIR² | Example value |

---

## 5. Statistics Model (Optional but Supported)

Statistics are **derived metadata** about variables. They are:

- Optional
- Repeatable
- Provenance-bearing
- Variable-specific

Statistics MUST NOT be encoded as fixed columns in the Core dictionary.

### 5.1 JSON-LD Statistics Pattern (Normative)

Statistics are represented as a `schema:DescriptiveStatistics` object attached to a variable.

```jsonld
"fair2:statistics": {
  "@type": "fair2:DescriptiveStatistics",
  "schema:variableMeasured": [
    { "@type": "schema:PropertyValue", "schema:name": "count", "schema:value": 4 },
    { "@type": "schema:PropertyValue", "schema:name": "unique", "schema:value": 4 },
    { "@type": "schema:PropertyValue", "schema:name": "missing_values", "schema:value": 36 }
  ],
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "schema:name": "Pandas statistics computation",
    "prov:wasAssociatedWith": {
      "@type": "prov:SoftwareAgent",
      "schema:name": "Pandas",
      "schema:softwareVersion": "2.1.1",
      "schema:programmingLanguage": "Python",
      "schema:identifier": {
        "@id": "https://pandas.pydata.org/",
        "schema:propertyID": "URL"
      }
    }
  }
}
```

### 5.2 CSV / Excel Statistics Table (Normative)

Statistics MUST be exported as a **separate long-form table**.

| Column | Description |
|------|------------|
| variable_id | Variable identifier |
| statistic_name | Name of statistic (`count`, `mean`, `unique`, etc.) |
| statistic_value | Value (numeric or string) |
| statistic_unit | Unit (if applicable) |
| statistic_description | Optional notes |
| generated_by_activity | Provenance activity ID |
| software_name | Software used |
| software_version | Software version |
| programming_language | Language/environment |

---

## 6. Canonical JSON-LD Example

```jsonld
{
  "@context": {
    "schema": "https://schema.org/",
    "skos": "http://www.w3.org/2004/02/skos/core#",
    "prov": "http://www.w3.org/ns/prov#",
    "fair2": "https://fair2.ai/ns/",
    "cr": "http://mlcommons.org/croissant/",
    "qudt": "http://qudt.org/schema/qudt/",
    "unit": "http://qudt.org/vocab/unit/",
    "xsd": "http://www.w3.org/2001/XMLSchema#"
  },
  "@id": "fair2:var:rmsd",
  "@type": ["fair2:Variable", "skos:Concept", "prov:Entity"],
  "schema:identifier": "rmsd",
  "schema:name": "RMSD",
  "skos:definition": "Root-mean-square deviation between two aligned molecular structures.",
  "cr:dataType": {"@id": "xsd:double"},
  "qudt:unit": {"@id": "unit:Angstrom"},
  "schema:unitCode": "A",
  "prov:wasGeneratedBy": "fair2:method:step3"
}
```

---

## 7. CSV / Excel Core Dictionary Columns

| Column | Meaning |
|------|--------|
| variable_id | Persistent variable identifier |
| technical_name | `schema:identifier` |
| human_label | `schema:name` |
| definition | `skos:definition` |
| value_type | `cr:dataType` |
| format | `fair2:format` |
| unit | `qudt:unit` |
| unit_code | `schema:unitCode` |
| method_step_id | `prov:wasGeneratedBy` |

---

## 8. Compliance Levels

| Level | Requirements |
|-----|-------------|
| FAIR²-Core | All required properties |
| FAIR²-Core+ | Core + recommended properties |
| FAIR²-Extended | Core/Core+ + extension profiles |

---

## 9. Normative Rules Summary

- Variables MUST be enumerated using `schema:variableMeasured`
- Technical identifiers MUST use `schema:identifier`
- Human labels MUST use `schema:name`
- Semantic definitions MUST use `skos:definition`
- Data types MUST use `cr:dataType` (ML Croissant)
- Units MUST use `qudt:unit` with a QUDT unit IRI
- FAIR² properties MUST be singular
- Statistics MUST be optional and provenance-bearing

---

## 10. Design Rationale (Informative)

This specification:

- Aligns with REDCap variable dictionaries
- Matches ISO/IEC 11179 semantic expectations
- Is compatible with ML Croissant field metadata
- Supports FAIR and Responsible AI principles
- Avoids premature ontology or analytics lock-in

---

**End of FAIR² Data Dictionary Specification**
