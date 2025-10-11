# FAIR² Responsible AI (RAI) — Integration Guide

This guide explains how **FAIR²** metadata aligns with the **ML Croissant RAI** specification and how to
author, validate, and query Responsible-AI information in your datasets.

> **Scope.** This document uses the exact property names listed in the Croissant RAI “Overview” table
> (e.g., `rai:dataLimitations`, `rai:dataCollection`, `rai:useCases`, etc.) and shows how they fit
> within FAIR² JSON‑LD. See the official spec for authoritative definitions:  
> https://docs.mlcommons.org/croissant/docs/croissant-rai-spec.html#overview-croissant-rai-properties-and-use-cases

---

## 1. Namespaces & Conformance

Use the following prefixes in your dataset JSON‑LD:

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "cr": "http://mlcommons.org/croissant/",
    "rai": "http://mlcommons.org/croissant/rai/",
    "dct": "http://purl.org/dc/terms/"
  }
}
```

We recommend declaring conformance with the RAI profile via `dct:conformsTo`:

```json
{
  "dct:conformsTo": "http://mlcommons.org/croissant/rai/"
}
```

---

## 2. Core RAI Properties (exact names)

The table below lists the **core Croissant RAI properties** this library expects. All are plain strings
unless otherwise noted by your governance process. Your project may adopt additional RAI terms as the
spec evolves—always consult the official spec for the latest guidance.

| Property                         | Purpose (short)                                             | Cardinality | Required?* |
|----------------------------------|-------------------------------------------------------------|-------------|------------|
| `rai:dataLimitations`            | Known gaps, caveats, or limitations of the data            | 0..1        | Recommended |
| `rai:dataCollection`             | How the data was collected (procedures, settings)          | 0..1        | Recommended |
| `rai:useCases`                   | Intended/appropriate uses                                  | 0..1        | Recommended |
| `rai:dataReleaseMaintenance`     | Release cadence, maintenance & support commitments         | 0..1        | Recommended |
| `rai:annotationPlatform`         | Platform(s) used for annotation                            | 0..1        | Optional   |
| `rai:annotationsPerItem`         | How many annotations per item                              | 0..1        | Optional   |
| `rai:annotatorDemographics`      | Demographic info about annotators (if appropriate/allowed) | 0..1        | Optional   |
| `rai:machineAnnotationTools`     | ML tools used to pre‑label or assist annotation            | 0..1        | Optional   |
| `rai:dataBiases`                 | Known or suspected biases                                  | 0..1        | Recommended |
| `rai:personalSensitiveInformation` | Whether/how PII or sensitive info is handled            | 0..1        | Recommended |

\* FAIR² does **not** mandate a minimum set beyond Croissant’s baseline, but strongly encourages filling
all **Recommended** fields to improve transparency and downstream risk assessment.

---

## 3. Minimal JSON‑LD example (FAIR² + Croissant RAI)

Below is a compact, copy‑paste‑ready snippet. You can merge it with your dataset’s main JSON‑LD.

```json
{
  "@context": {
    "schema": "https://schema.org/",
    "cr": "http://mlcommons.org/croissant/",
    "rai": "http://mlcommons.org/croissant/rai/",
    "dct": "http://purl.org/dc/terms/"
  },
  "@type": "schema:Dataset",
  "name": "Example FAIR² Dataset with RAI",
  "version": "1.0",
  "dct:conformsTo": "http://mlcommons.org/croissant/rai/",
  "rai:dataLimitations": "Labels may be noisy for low-light scenes.",
  "rai:dataCollection": "Captured via mobile devices in public indoor spaces.",
  "rai:useCases": "Robust indoor navigation and scene understanding research.",
  "rai:dataReleaseMaintenance": "Quarterly updates; issues tracked in public repository.",
  "rai:annotationPlatform": "In-house tool; audit logs retained.",
  "rai:annotationsPerItem": "3",
  "rai:annotatorDemographics": "Adult bilingual annotators from multiple regions.",
  "rai:machineAnnotationTools": "YOLOv8 for pre‑labels; human review required.",
  "rai:dataBiases": "Over‑representation of shopping malls; under‑representation of hospitals.",
  "rai:personalSensitiveInformation": "PII removed per policy; faces blurred at source."
}
```

---

## 4. Validating RAI with `fair2py`

`Fair2Dataset` loads your JSON‑LD, runs **Croissant validation** and **FAIR² SHACL** checks (including
RAI shape coverage where applicable), and keeps the **full** JSON‑LD in `metadata_full`.

```python
from fair2py.dataset import Fair2Dataset

# Path or URL to your dataset JSON-LD
path = "path/to/dataset.json"

ds = Fair2Dataset(path)

# Full JSON-LD (with RAI) preserved:
rai_fields = {
    k: ds.metadata_full.get(k)
    for k in [
        "rai:dataLimitations",
        "rai:dataCollection",
        "rai:useCases",
        "rai:dataReleaseMaintenance",
        "rai:annotationPlatform",
        "rai:annotationsPerItem",
        "rai:annotatorDemographics",
        "rai:machineAnnotationTools",
        "rai:dataBiases",
        "rai:personalSensitiveInformation",
    ]
}
print({k: v for k, v in rai_fields.items() if v})
```

> If you see a warning about non‑standard `@context`, that is **informative** (from Croissant) and does
> not block FAIR² validation. Ensure that the `rai:` prefix is present and values are strings or IRIs as
> appropriate for your governance rules.

---

## 5. Quick SPARQL to inspect RAI fields

The following SPARQL query enumerates RAI predicates and values when your graph is parsed into `rdflib`.

```python
from rdflib import Namespace, URIRef
from rdflib.namespace import RDF

RAI = Namespace("http://mlcommons.org/croissant/rai/")
SCHEMA = Namespace("https://schema.org/")

q = """
PREFIX schema: <https://schema.org/>
PREFIX rai: <http://mlcommons.org/croissant/rai/>

SELECT ?dataset ?p ?o
WHERE {
  ?dataset a schema:Dataset ;
           ?p ?o .
  FILTER(STRSTARTS(STR(?p), STR(rai:)))
}
ORDER BY ?p
LIMIT 200
"""

for row in ds.graph.query(q):
    print(row)
```

---

## 6) Authoring tips & best practices

- **Be concrete, not generic.** Prefer actionable statements over boilerplate (e.g., name bias sources,
  collection settings, audit processes).
- **Keep provenance.** When feasible, link to documents (IRIs) that describe templated processes or
  internal policies.
- **Avoid sensitive disclosures.** If describing annotator demographics, comply with local privacy laws
  and internal policies. Use aggregated or high‑level descriptors when needed.
- **Version RAI text.** Update RAI fields alongside dataset releases; note changes in your changelog.

---

## 7) Troubleshooting

- **RAI fields missing in `ds.metadata`**: That’s expected—Croissant keeps its own schema. Use
  `ds.metadata_full` to access *all* original JSON‑LD (including RAI).
- **Prefixes look like literals (e.g., "schema:name")**: Ensure your JSON‑LD uses prefix **keys** in
  `@context` and not quoted strings in SHACL/Turtle. If converting shapes, normalize predicates to IRIs.
- **Validation passes but shapes don’t trigger**: Check your target class (`@type: schema:Dataset`) and
  that the RAI predicates are actually used in the data being validated.

---

## 8) References

- **ML Croissant RAI spec (properties & use cases):**  
  https://docs.mlcommons.org/croissant/docs/croissant-rai-spec.html#overview-croissant-rai-properties-and-use-cases
- **ML Croissant (main spec):** https://docs.mlcommons.org/croissant/
- **FAIR² project:** https://fair2.ai/

---

*Last updated:* Generated by `fair2py` docs automation.