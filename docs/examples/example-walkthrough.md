# FAIR² Example Walkthrough (Updated)

This walkthrough illustrates how the FAIR² ontology and metadata model are applied in a real dataset. The examples below are drawn directly from the **Borja et al. (2025)** FAIR² dataset (`borja2025.json`) and demonstrate how constrained shapes and entities interlink across submissions, data articles, methods, contributors, and results.

All examples are truncated to 1–2 representative instances for clarity.

---

## Data Article

The FAIR² Data Article describes the dataset and its scientific context.

```json
{
  "@id": "https://doi.org/10.3389/focsu.2024.1528837",
  "@type": "fair2:DataArticle",
  "schema:name": "Structure-Based Prediction of SARS-CoV-2 Variant Properties Using Machine Learning on Mutational Neighborhoods",
  "schema:publisher": {
    "@type": "schema:Organization",
    "schema:name": "Frontiers in Ocean Sustainability"
  },
  "schema:author": [
    {
      "@type": "schema:Person",
      "schema:name": "Borja, Efren"
    },
    {
      "@type": "schema:Person",
      "schema:name": "Schultes, Erik"
    }
  ]
}
```

This JSON-LD fragment illustrates how a `fair2:DataArticle` aligns with `schema:ScholarlyArticle` while referencing real contributors.

---

## Method

Methods in FAIR² are structured hierarchically as `fair2:Section` objects containing ordered `fair2:Step` and `fair2:Substep` items.

```json
{
  "@id": "https://fair2.ai/examples/borja2025#method",
  "@type": "fair2:Section",
  "schema:name": "Machine Learning Workflow",
  "schema:description": "End-to-end workflow from Bio2Byte feature extraction to model evaluation.",
  "fair2:step": [
    {
      "@type": "fair2:Step",
      "schema:name": "Feature Extraction",
      "schema:description": "Bio2Byte descriptors were extracted for each protein variant.",
      "fair2:step": [
        {
          "@type": "fair2:Substep",
          "schema:name": "Normalization",
          "schema:description": "Features were normalized using z-scores."
        }
      ]
    }
  ]
}
```

This structure demonstrates how the FAIR² Method representation supports multi-level procedural hierarchy and captures computational steps with clarity.

---

## Contributors and Roles

Contributor information in FAIR² uses `schema:Contribution` entities enriched with role identifiers from the Contributor Role Ontology and FAIR² extensions.

```json
{
  "@type": "schema:Contribution",
  "schema:agent": {
    "@type": "schema:Person",
    "schema:name": "Efren Borja",
    "schema:identifier": {
      "@type": "PropertyValue",
      "propertyID": "ORCID",
      "value": "https://orcid.org/0000-0002-1825-0097"
    },
    "schema:affiliation": {
      "@type": "schema:Organization",
      "schema:name": "Frontiers"
    }
  },
  "prov:hadRole": [
    {
      "@id": "https://credit.niso.org/contributor-roles/data-curation/",
      "rdfs:label": "Data Curation"
    },
    {
      "@id": "https://credit.niso.org/contributor-roles/formal-analysis/",
      "rdfs:label": "Formal Analysis"
    }
  ]
}
```

This example shows how FAIR² contributions maintain explicit attribution through PROV-compatible `prov:hadRole` relationships.

---

## RecordSet and Statistics

FAIR² datasets include RecordSets linked to computed statistics and variable definitions.

```json
{
  "@id": "https://fair2.ai/examples/borja2025#recordset",
  "@type": "cr:RecordSet",
  "schema:name": "RBD Variant Features",
  "field": [
    {
      "@id": "https://fair2.ai/examples/borja2025#field",
      "@type": "cr:Field",
      "description": "Variant name",
      "dataType": "schema:Text",
      "fair2:statistics": {
        ...
      }
    }
  ]
}
```

This section exemplifies how FAIR² captures analytical data products, linking them to their computed statistics and variable-level metadata.

---

## Visualization

Access conditions are stated by the dataset's [governance blocks](../specification/governance.md). This dataset is open, so it states the open tier, `L0`, in `fair2:access`, and names the same tier in `accessRights` for consumers that read Dataset metadata alone:

```json
"accessRights": {
  "@id": "https://fair2.ai/ns/L0",
  "@type": "DefinedTerm",
  "name": "L0 — Open",
  "definition": "No authentication is required. The data is distributed unencrypted; the licence and use terms apply, but do not gate access.",
  "url": "https://fair2.ai/spec/v1.7.0/specification/governance/#access-tiers"
},
"fair2:access": { "tier": "L0" }
```

A governed dataset adds the conditions and use constraints in the same blocks: see the [complete example](../specification/governance.md#complete-example).

---

## Summary

These examples illustrate the implementation of the FAIR² ontology in a real dataset. The JSON-LD structures demonstrate how methods, data, contributors, and derived outputs are interconnected through consistent FAIR² linking properties, enabling full traceability and AI-ready reuse.
