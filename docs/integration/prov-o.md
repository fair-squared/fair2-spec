di# FAIR² and PROV-O Integration

## Overview

FAIR² (FAIR Squared) adopts the PROV-O (Provenance Ontology) standard to support structured provenance metadata. This enables datasets to be:

- Findable: by tracking their origins and transformation processes.
- Accessible: by providing machine-readable provenance records.
- Interoperable: through the use of linked data for provenance documentation.
- Reusable: by enabling transparency and reproducibility in AI and machine learning workflows.

PROV-O is a W3C recommendation for representing provenance information, including data lineage, authorship, and transformations. FAIR² incorporates PROV-O in JSON-LD metadata to improve dataset transparency and facilitate auditability in responsible AI.

---

!!! note "On bare PROV-O terms in payloads"
    In `fair2.json` bodies, PROV-O properties such as `wasAttributedTo`,
    `wasGeneratedBy`, `wasDerivedFrom`, and `hadRole` appear *without* the
    `prov:` prefix. This is the canonical form: the
    [FAIR² `@context`](../specification/prefixes.md#canonical-context-reference)
    aliases each bare name to its full `prov:` URI, so the JSON-LD processor
    resolves them identically to the prefixed forms. Producers SHOULD use the
    bare aliases in the payload body to match the rest of the FAIR² data model.

## PROV-O Concepts in FAIR²

The following table summarizes how FAIR² utilizes core PROV-O terms:

| PROV-O Term           | Purpose in FAIR²                                       | Example                                                             |
|-----------------------|--------------------------------------------------------|---------------------------------------------------------------------|
| `prov:Entity`         | Represents a dataset or data file                      | `"@type": "prov:Entity"`                                            |
| `prov:Agent`          | Identifies individuals, organizations, or software     | `"@type": "prov:Agent"`                                             |
| `prov:Activity`       | Describes processes such as data generation or curation| `"@type": "prov:Activity"`                                          |
| `prov:wasGeneratedBy` | Links a dataset to the activity that created it        | `"wasGeneratedBy": { "@type": "prov:Activity", "name": "Collection" }` |
| `prov:wasAttributedTo`| Associates a dataset with its creator or maintainer    | `"wasAttributedTo": { "@type": "prov:Agent", "name": "Research Lab" }` |
| `prov:wasDerivedFrom` | References prior datasets used in derivation           | `"wasDerivedFrom": "https://doi.org/10.1234/original-dataset"`     |

---

## Example: JSON-LD with PROV-O Metadata

```json
{
  "@context": [
    "https://www.w3.org/ns/prov",
    "https://fair2.ai/ns/"
  ],
  "@type": "Dataset",
  "name": "AI-ready Dataset",
  "description": "A dataset aligned with PROV-O for provenance tracking.",
  "author": {
    "@type": "prov:Agent",
    "name": "Dr. Jane Doe",
    "affiliation": {
      "@type": "Organization",
      "name": "AI Research Lab"
    }
  },
  "wasGeneratedBy": {
    "@type": "prov:Activity",
    "name": "Dataset Preprocessing",
    "startTime": "2025-01-15T10:00:00Z",
    "endTime": "2025-01-15T12:00:00Z"
  },
  "wasAttributedTo": {
    "@type": "prov:Agent",
    "name": "AI Research Lab",
    "role": "Data Curator"
  },
  "wasDerivedFrom": "https://doi.org/10.1234/original-dataset"
}
```

---

## Rationale for Using PROV-O

Integrating PROV-O into FAIR² enables:

- Provenance traceability: recording who created, modified, and curated datasets.
- Reproducibility: documenting data transformations and source dependencies.
- Compliance with Open Science and Responsible AI practices.
- Interoperability: aligning with existing W3C standards for metadata reuse.

---

## Next Steps

To include provenance metadata using PROV-O in FAIR²:

1. Refer to the [FAIR² Schema](../specification/schema.md) for relevant properties.
2. Incorporate PROV-O terms into your dataset JSON-LD metadata.
3. Validate using [SHACL rules](../specification/shacl-validation.md).
4. Contribute examples or feedback via [GitHub Issues](https://github.com/fair-squared/fair2-spec/issues) or [feedback@fair2.ai](mailto:feedback@fair2.ai).
