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
5. **Provenance links** to the method step(s) that produced it
6. Optional **descriptive statistics** with provenance

### Where a variable lives (normative)

A FAIR² variable **is** a Croissant field: a `cr:Field` inside a
`cr:RecordSet` on the dataset. This is what `fair2s:FieldShape` enforces and
what every published `fair2.json` contains.

```
Dataset -> cr:recordSet -> cr:RecordSet -> cr:field -> cr:Field
```

Earlier drafts of this page described variables as a flat
`schema:variableMeasured` list on the Dataset, with `skos:definition` and
`qudt:unit`. **That model was never implemented and is not normative.**
Statistics are not variables either: from v1.5.0 they are attached to the
field they describe through `cr:annotation` (§5).

### Mapping the dictionary onto a field

The conceptual slots above map onto `cr:Field` as follows. Use the right-hand
column when writing or reading `fair2.json`.

| Dictionary concept | Property on `cr:Field` |
|---|---|
| Technical identifier | `schema:name` — the column name as it appears in the file |
| Human label | `schema:alternateName` |
| Semantic definition | `schema:description` |
| Data type | `cr:dataType` |
| Physical location | `cr:source` → `cr:fileObject` (or `cr:fileSet`) + `cr:extract`/`cr:column` |
| Unit | `fair2:unit` → the QUDT unit IRI (see §4.3) |
| Experimental flag | `fair2:isExperimentRelated` |
| Statistics | `cr:annotation` (§5) |
| Method provenance | the inverse: `fair2:Step` → `fair2:generated` → the field |

Note the direction of provenance. A field does **not** carry
`prov:wasGeneratedBy`; the method step points forward at the fields it
produced, via `fair2:generated`.

---

## 3. Terminology (Normative)

### 3.1 Technical Identifier
- **Definition:** Machine-facing name used in files, schemas and code — the column name.
- **Mapping:** `schema:name` on the `cr:Field`
- **Source (UI):** `variable_name`
- **Requirements:**
  - Matches the column named in `cr:source` → `cr:extract` → `cr:column`
  - Unique within its record set
  - Stable across versions

### 3.2 Human Label
- **Definition:** Human-readable label shown in UIs and documentation.
- **Mapping:** `schema:alternateName`
- **Source (UI):** `variable`

### 3.3 Semantic Definition
- **Definition:** Precise, unambiguous statement of what the variable means.
- **Mapping:** `schema:description`
- **Source (UI):** `description`
- **Normative rule:** In FAIR² Core the UI field *description* **IS** the
  semantic definition. There is no separate `skos:definition`.

!!! note "Changed in v1.4.0"
    Up to v1.3.0 this section mapped the technical identifier to
    `schema:identifier`, the human label to `schema:name` and the definition
    to `skos:definition`. No `fair2.json` ever used that mapping and no shape
    enforced it. The mappings above describe what `fair2s:FieldShape`
    validates and what published files contain.

---

## 4. Core Properties

### 4.1 Required (FAIR²-Core)

These are the properties `fair2s:FieldShape` enforces. A field missing any of
them fails validation.

| Property | Vocabulary | Meaning |
|--------|-----------|--------|
| `@id` | RDF | Persistent field identifier |
| `schema:name` | schema.org | Column name as it appears in the file |
| `schema:description` | schema.org | What the variable means |
| `cr:dataType` | ML Croissant | Data type |
| `cr:source` | ML Croissant | The file (a FileObject, or a FileSet) and column the values come from |

### 4.2 Strongly Recommended (FAIR²-Core+)

| Property | Vocabulary | Meaning |
|--------|-----------|--------|
| `schema:alternateName` | schema.org | Human-readable label |
| `fair2:unit` | FAIR² | Unit of measurement, as a QUDT IRI |
| `fair2:isExperimentRelated` | FAIR² | Experimental observation rather than descriptive metadata |
| `cr:annotation` | Croissant | Descriptive statistics, one annotation field per statistic (§5) |

### 4.3 Units

`fair2:unit` references the unit **by its QUDT IRI**, and the unit node
carries its own label and symbol:

```jsonld
"unit": {
  "uri": "http://qudt.org/vocab/unit/MicroGM-PER-L",
  "label": "Micrograms per litre",
  "symbol": "µg/L"
}
```

In the FAIR² context `uri` is an alias for `@id`, so this is a reference to
the QUDT unit itself, not a string: it expands to

```
<field> fair2:unit <http://qudt.org/vocab/unit/MicroGM-PER-L> .
<http://qudt.org/vocab/unit/MicroGM-PER-L> rdfs:label "Micrograms per litre" ;
                                           qudt:symbol "µg/L" .
```

Consumers wanting `qudt:unit` semantics can treat `fair2:unit` as equivalent;
the object is the same QUDT resource.

### 4.4 Reserved

`fair2:format`, `fair2:valueDomain`, `fair2:missingValueCode` and
`fair2:exampleValue` appeared in earlier drafts of this page. They have no
shape, no context mapping and no implementation. **Do not emit them.**

---

## 5. Statistics Model

Statistics are **derived metadata** about a field: optional, repeatable,
provenance-bearing.

### Croissant's annotation mechanism (normative)

A statistic is a `cr:Field` attached through `cr:annotation`, carrying a
`value` instead of a `source`. This is
[Croissant 1.1's own representation](https://docs.mlcommons.org/croissant/docs/croissant-spec-1.1.html#application-representing-descriptive-statistics),
and using it means Croissant tooling can read FAIR² statistics — `mlcroissant`
surfaces them on `field.annotations`.

```jsonld
{
  "@id": "record-sets/WATER/fields/parameter_value",
  "@type": "Field",
  "name": "parameter_value",
  "dataType": "Number",
  "source": { "fileObject": { "@id": "resources/WATER" },
              "extract": { "column": "parameter_value" } },

  "annotation": [
    { "@id": "record-sets/WATER/fields/parameter_value/stats/count",
      "@type": "Field", "name": "count", "value": 271925 },
    { "@id": "record-sets/WATER/fields/parameter_value/stats/missing_values",
      "@type": "Field", "name": "missing_values", "value": 0 }
  ],

  "wasGeneratedBy": { "@id": "activities/pandas-statistics" }
}
```

Each annotation needs a stable `@id`, a `name` saying what it reports, and a
`value`. `fair2s:AnnotationShape` enforces that. Note that
`fair2s:FieldShape` targets the objects of `cr:field` rather than every
`cr:Field`, so a data field's `description`, `dataType` and `source`
requirements do not reach an annotation.

### Provenance sits on the field, not on each statistic

One run produces all of a field's statistics, so `prov:wasGeneratedBy` is
stated once per field and points at a single activity held under `included`:

```jsonld
"included": [
  { "@id": "activities/pandas-statistics",
    "@type": "Activity",
    "label": "Pandas .statistics() computation",
    "wasAssociatedWith": { "@id": "agents/pandas" } },
  { "@id": "agents/pandas",
    "@type": "SoftwareAgent",
    "name": "Pandas", "softwareVersion": "2.1.1",
    "programmingLanguage": "Python",
    "identifier": "https://pandas.pydata.org/" }
]
```

### Typing the kind of statistic

Croissant types each statistic with a resolvable term in `cr:dataType` —
its own example uses DDI-CDI `SummaryStatisticType` and Wikidata. FAIR²
permits this and `fair2s:AnnotationShape` accepts an optional `cr:dataType`,
but **does not yet prescribe a vocabulary**. Until one is settled, `name`
carries the kind. Some statistics are unlikely to map: `missing_values` and
`expected_number_of_values` describe completeness of the extraction rather
than a distribution.

!!! note "Changed in v1.5.0"
    Up to v1.4.0 statistics used a FAIR²-specific `fair2:statistics` property
    pointing at a `fair2:DescriptiveStatistics` wrapper whose
    `schema:variableMeasured` held `PropertyValue` pairs. That was a parallel
    mechanism beside one the base specification already had, and it was
    invisible to Croissant consumers: `mlcroissant` exposes
    `field.annotations`, and for FAIR² documents it was empty. Both terms are
    deprecated and retained only so existing references resolve.

---

## 6. Canonical JSON-LD Example

A field as it appears inside a record set, with the context terms FAIR²
documents use:

```jsonld
{
  "@id": "record-sets/WATER/fields/parameter_value",
  "@type": "Field",
  "name": "parameter_value",
  "alternateName": "Parameter Value",
  "description": "Measured value of the parameter, in the unit given by parameter_standardunit.",
  "dataType": "Number",
  "isExperimentRelated": true,
  "source": {
    "fileObject": { "@id": "resources/WATER" },
    "extract": { "column": "parameter_value" }
  },
  "unit": {
    "uri": "http://qudt.org/vocab/unit/MicroGM-PER-L",
    "label": "Micrograms per litre",
    "symbol": "µg/L"
  }
}
```

The method step that produced it points at it, rather than the other way
round:

```jsonld
{
  "@type": "Step",
  "@id": "steps/measure-nutrients",
  "name": "Nutrient determination",
  "description": "Nutrients determined from Niskin-bottle samples under EN 15972:2011.",
  "generated": [ { "@id": "record-sets/WATER/fields/parameter_value" } ]
}
```

---

## 7. CSV / Excel Core Dictionary Columns

| Column | Meaning |
|------|--------|
| variable_id | The field's `@id` |
| technical_name | `schema:name` |
| human_label | `schema:alternateName` |
| definition | `schema:description` |
| value_type | `cr:dataType` |
| unit_uri | the QUDT IRI referenced by `fair2:unit` |
| unit_symbol | `qudt:symbol` on the unit |
| method_step_ids | the steps whose `fair2:generated` names this field (semicolon-delimited) |

---

## 8. Compliance Levels

| Level | Requirements |
|-----|-------------|
| FAIR²-Core | All required properties |
| FAIR²-Core+ | Core + recommended properties |
| FAIR²-Extended | Core/Core+ + extension profiles |

---

## 9. Normative Rules Summary

- A variable MUST be expressed as a `cr:Field` inside a `cr:RecordSet`
- Technical names MUST use `schema:name`; human labels SHOULD use `schema:alternateName`
- Definitions MUST use `schema:description`
- Data types MUST use `cr:dataType`
- Every field MUST declare `cr:source`
- Units SHOULD use `fair2:unit` referencing a QUDT unit IRI
- Method provenance runs from step to field, via `fair2:generated`
- Statistics MUST use `cr:annotation`, each with an `@id`, a `name` and a `value`
- Statistics provenance MUST sit on the field, not on each statistic

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
