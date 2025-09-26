# Provenance and Citation in FAIR²

The FAIR² specification enables **transparent, machine-readable tracking of provenance and citations** at both the **methodological** and **data transformation** levels. This ensures reproducibility, trust, and responsible reuse.

## Scope of Provenance Tracking

| Target Element | Purpose |
|----------------|---------|
| **Method Steps** (`HowToStep`) | To document the origin, tools, agents, and citations for each procedure. |
| **RecordSets / Variables** | To track mappings, transformations, or derivations applied to specific variables or files. |

---

## 1. Provenance in Method Descriptions

FAIR² extends `schema:HowToStep` with `prov:` properties and citation support. You may annotate each `Step`, `Substep`, or `StepCase` with:

- **`prov:wasAssociatedWith`**: the agent (tool, person, organization) that performed or is responsible for the step.
- **`prov:used`**: input files, tools, or parameters used.
- **`prov:generated`**: output entities (optional).
- **`prov:wasDerivedFrom`**: to describe derivation from prior methods or protocols.
- **`schema:citation`**: to include a scholarly or persistent reference (DOI, paper, or dataset).

###  Example: Method Step with Provenance and Citation

```json
{
  "@type": "HowToStep",
  "text": "Run AlphaFold prediction using ColabFold pipeline.",
  "prov:wasAssociatedWith": {
    "@type": "prov:SoftwareAgent",
    "name": "ColabFold v1.5",
    "identifier": "https://github.com/sokrypton/ColabFold"
  },
  "prov:used": [
    { "@type": "schema:Dataset", "name": "FASTA input", "identifier": "input.fasta" }
  ],
  "schema:citation": {
    "@type": "ScholarlyArticle",
    "name": "AlphaFold: Highly accurate protein structure prediction",
    "identifier": "https://doi.org/10.1038/s41586-021-03819-2"
  }
}
```

---

## 2. Provenance in RecordSets and Variable Transformations

To capture how variables were derived, mapped, or transformed, FAIR² supports the use of `prov:wasDerivedFrom`, `prov:wasGeneratedBy`, and `schema:citation` at the **variable** and **RecordSet** levels.

###  Use Cases

| Case | Recommended Pattern |
|------|----------------------|
| Variable mapped to ontology | `prov:wasDerivedFrom` + citation of the ontology |
| Normalization or scaling | `prov:wasGeneratedBy` linked to `prov:Activity` describing the transformation |
| Derived variable | `prov:wasDerivedFrom` other variable(s) or dataset(s) |
| Manual curation | `prov:wasAssociatedWith` = person or tool |
| Scripted transformation | Link to script or GitHub repository using `prov:used` or `schema:codeRepository` |

###  Example: Transformed Variable in RecordSet

```json
{
  "@type": "PropertyValue",
  "name": "scaled_binding_affinity",
  "value": "0.75",
  "unitText": "relative",
  "prov:wasDerivedFrom": {
    "@type": "PropertyValue",
    "name": "raw_binding_affinity",
    "value": "-8.2",
    "unitText": "kcal/mol"
  },
  "prov:wasGeneratedBy": {
    "@type": "prov:Activity",
    "name": "Z-score normalization",
    "description": "Normalized binding affinities across BA.1 variants",
    "prov:used": {
      "@type": "SoftwareSourceCode",
      "name": "normalize.py",
      "codeRepository": "https://github.com/example/lab-scripts"
    }
  },
  "schema:citation": {
    "@type": "CreativeWork",
    "name": "Normalized binding data",
    "identifier": "https://doi.org/10.5281/zenodo.1234567"
  }
}
```

---

## 3. Representing Agents and Activities

Agents and activities should be typed using the [PROV Ontology](https://www.w3.org/TR/prov-o/):

| PROV Type | Description |
|-----------|-------------|
| `prov:SoftwareAgent` | Software tool or script |
| `prov:Person` | Individual contributor |
| `prov:Organization` | Institutional contributor |
| `prov:Activity` | Process applied to produce, transform, or derive data |

These elements can be reused across steps, variables, and datasets to support consistent provenance graphs.

---

## 4. SHACL Validation Rules (Provenance)

To ensure consistency and validity, FAIR² SHACL includes these optional rules:

- `schema:HowToStep` MAY include `prov:wasAssociatedWith`, `prov:used`, and `schema:citation`.
- `schema:PropertyValue` SHOULD include `prov:wasDerivedFrom` or `prov:wasGeneratedBy` if `name` suggests derivation.
- All `prov:Activity` entities MUST include `name` and SHOULD include `description`.

---

## 5. Citation Formats

- All citations should use persistent identifiers where possible (`doi`, `url`, or `identifier` fields).
- `schema:citation` accepts:
  - `ScholarlyArticle`
  - `CreativeWork`
  - `Dataset`
  - `SoftwareSourceCode`

---

By explicitly modeling provenance and citations, FAIR² enhances transparency, encourages responsible reuse, and enables reproducible AI workflows.