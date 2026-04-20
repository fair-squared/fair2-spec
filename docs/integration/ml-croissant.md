# FAIR² and ML Croissant Integration

## Overview

FAIR² (FAIR Squared) builds directly on ML Croissant, extending its capabilities to ensure that datasets are both FAIR (Findable, Accessible, Interoperable, and Reusable) and AI-ready.

ML Croissant is a metadata standard for machine learning datasets developed by MLCommons. FAIR² enhances this foundation by adding:

- SHACL validation for structured dataset metadata
- Support for AI/ML methodologies using `MethodSectionShape` and `MethodStepShape`
- Compliance features aligned with Responsible AI through explicit tracking of dataset provenance and usage

This document outlines how FAIR² builds upon and extends ML Croissant to provide machine-actionable metadata for AI workflows.

---

## Required Properties in ML Croissant

| Property       | Description                                       | Type             | Example                                       |
|----------------|---------------------------------------------------|------------------|-----------------------------------------------|
| `@type`        | Specifies the type of the dataset (typically `Dataset`) | `sc:Dataset`     | `"@type": "sc:Dataset"`                        |
| `name`         | The title of the dataset                          | `xsd:string`     | `"name": "FAIR AI Benchmark Dataset"`         |
| `description`  | Explanation of the dataset’s content and purpose | `xsd:string`     | `"description": "A dataset for AI fairness"`  |
| `license`      | Dataset license URI                              | `xsd:anyURI`     | `"license": "https://creativecommons.org/licenses/by/4.0/"` |
| `url`          | Landing page or repository URL                   | `xsd:anyURI`     | `"url": "https://example.com/dataset"`        |
| `distribution` | Description of downloadable files                | Array<FileObject> | Refer to FileObject structure below           |
| `recordSet`    | Defines logical data structure                   | Array<RecordSet>  | Refer to RecordSet section                    |

### FileObject (Inside `distribution`)

| Property        | Description                            | Type           | Example                                       |
|----------------|----------------------------------------|----------------|-----------------------------------------------|
| `@type`        | Specifies file type                    | `cr:FileObject`| `"@type": "cr:FileObject"`                    |
| `@id`          | Unique file identifier                 | `xsd:string`   | `"@id": "file1"`                              |
| `name`         | Filename                               | `xsd:string`   | `"name": "data.csv"`                          |
| `contentUrl`   | URL of hosted file                     | `xsd:anyURI`   | `"contentUrl": "https://example.com/data.csv"`|
| `encodingFormat`| File format (e.g., text/csv)           | `xsd:string`   | `"encodingFormat": "text/csv"`               |
| `sha256`       | File checksum                          | `xsd:string`   | `"sha256": "abc123..."`                       |

### RecordSet (Inside `recordSet`)

| Property     | Description                              | Type             | Example                                       |
|--------------|------------------------------------------|------------------|-----------------------------------------------|
| `@type`     | Declares a record set                    | `cr:RecordSet`   | `"@type": "cr:RecordSet"`                     |
| `name`      | Name of the record set                   | `xsd:string`     | `"name": "User Data"`                         |
| `description`| Textual summary of the records           | `xsd:string`     | `"description": "Demographic information"`    |
| `field`     | List of field definitions                | Array<Field>     | Refer to Field section                        |

### Field (Inside `field`)

| Property     | Description                              | Type           | Example                                       |
|--------------|------------------------------------------|----------------|-----------------------------------------------|
| `@type`     | Field object                             | `cr:Field`     | `"@type": "cr:Field"`                         |
| `name`      | Field name                               | `xsd:string`   | `"name": "age"`                               |
| `description`| Field explanation                        | `xsd:string`   | `"description": "Age of participant"`         |
| `dataType`  | Expected data type                       | `sc:DataType`  | `"dataType": "sc:Integer"`                    |
| `references`| How the field maps to a file             | Object         | `"references": { "fileObject": "file1" }`     |

---

## Extensions Provided by FAIR²

| ML Croissant Feature      | FAIR² Enhancement                                              |
|---------------------------|----------------------------------------------------------------|
| Dataset metadata          | SHACL validation for compliance and consistency                |
| AI methodology support    | Structured method tracking for data processing and modeling    |
| Schema.org compatibility  | Alignment with linked data vocabularies                        |
| Provenance and licensing  | Integration of provenance and citation tracking mechanisms     |

FAIR² ensures that metadata not only meets FAIR requirements but also enables seamless integration with modern machine learning workflows.

---

## Example: FAIR² Metadata with Croissant Extensions

```json
{
  "@context": [
    "https://fair2.ai/ns/",
    "https://mlcroissant.org/"
  ],
  "@type": "Dataset",
  "name": "AI-ready Dataset",
  "description": "A dataset structured for AI and machine learning workflows.",
  "license": "https://creativecommons.org/licenses/by/4.0/",
  "cr:features": [
    {
      "@type": "Feature",
      "name": "Image",
      "dataType": "image/png"
    },
    {
      "@type": "Feature",
      "name": "Label",
      "dataType": "string"
    }
  ],
  "cr:citeAs": "Doe, J. AI Dataset (2025)",
  "fair2:method": {
    "@type": "fair2:Section",
    "name": "Data Preprocessing",
    "step": [
      {
        "@type": "fair2:Step",
        "name": "Normalization",
        "description": "Rescaling image pixel values between 0 and 1."
      }
    ]
  }
}
```

---

## Loading FAIR² Datasets in AI Frameworks

Datasets described using FAIR² and ML Croissant metadata can be loaded directly into AI frameworks:

```python
from mlcroissant import Dataset
from torch.utils.data import DataLoader

dataset = Dataset("fair2.json")
dataloader = DataLoader(dataset)

for batch in dataloader:
    images, labels = batch
    # Training logic here
```

---

## Validation of FAIR² Metadata

FAIR² uses SHACL to validate ML Croissant-based metadata:

```bash
pyshacl -s fair2_dataset.json -d mydata.json
```

Typical validation errors and solutions:

| Error Message                                  | Cause                         | Recommended Fix                                     |
|------------------------------------------------|-------------------------------|-----------------------------------------------------|
| Missing required property `cr:citeAs`          | Citation field not provided   | Add `"cr:citeAs": "Your citation"` to metadata      |
| `schema:distribution` must be present          | No file references defined    | Include at least one `schema:distribution` object   |
| Invalid datatype for `schema:datePublished`    | Incorrect date format         | Use `YYYY-MM-DD` format                             |

---

## Compatibility Rules

FAIR² metadata files MUST satisfy the rules below in order to load cleanly
with the `mlcroissant` Python library. These rules were established by
validating real FAIR² packages against `mlcroissant`'s JSON-LD processor and
identifying reproducible crash modes.

### Rule 1 — No shared-node `@id` references

A node whose `@id` appears as a top-level `@graph` member MUST NOT be
referenced from more than one other place via a bare `{"@id": "X"}` object.
The `mlcroissant` traversal function visits shared nodes twice and raises a
`KeyError`. To describe the same entity at multiple points in the graph,
embed it as a fresh blank-node object without `@id` at each usage site
(see Rule 4).

### Rule 2 — No `"@type": "@id"` on cross-graph properties

Properties whose values reference other `@graph` entries MUST NOT carry
`"@type": "@id"` in the `@context`. The underlying `rdflib` JSON-LD parser
silently converts string values with this coercion back into bare
`{"@id": "..."}` dicts, reintroducing the shared-node crash described in
Rule 1. Affected properties include `citation`, `dataArticle`, `dataPortal`,
`dataArchive`, `dataset`, `wasAssociatedWith`, `wasGeneratedBy`,
`wasDerivedFrom`, `wasRevisionOf`, `generated`, `next`, and `url`.

### Rule 3 — No circular self-references via `@id`

A Dataset node MUST NOT reference its own `@id` as the value of any of its
own properties. In particular, `changeLog[].wasRevisionOf["@id"]` MUST NOT
equal the Dataset's `@id`. To represent a revision that chains back to the
same logical entity without the cycle, embed the revision target as an
object without an `@id`, or omit the cross-reference entirely.

### Rule 4 — Repeated entities MUST be blank nodes

When the same logical entity (an author, an organization, a software agent)
appears in multiple locations in the graph, each occurrence MUST be a fresh
object without `@id`. This is the corollary of Rule 1: without an `@id`,
the JSON-LD processor treats each occurrence as a distinct blank node and
the shared-node crash cannot be triggered.

### Rule 5 — Distribution `@id` MUST match FileObject source exactly

The `@id` value of each `distribution[]` entry MUST exactly match the value
used in `recordSet[].field[].source.fileObject["@id"]`. Any mismatch causes
`mlcroissant` to silently drop the source mapping; the RecordSet will be
unloadable without any validation error.

### Rule 6 — FileObject `@type` MUST be `cr:FileObject`

Distribution entries MUST declare `"@type": "cr:FileObject"` (which resolves
to `http://mlcommons.org/croissant/FileObject`). Legacy types such as
`schema:DataDownload` or `sc:FileObject` are silently ignored by
`mlcroissant` and the distribution will not be indexed.

---

## Summary

FAIR² provides the following enhancements to ML Croissant:

- Structured metadata validation using SHACL
- Provenance tracking and citation support
- Interoperable format for use with AI training pipelines
- Integrated methodology documentation for reproducibility

For further details, refer to the FAIR² schema documentation and validator tools.