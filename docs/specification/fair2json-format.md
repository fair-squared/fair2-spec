# `fair2.json` File Format

A FAIR² data package is serialised as a single JSON-LD document named
`fair2.json`. This page defines the file's required top-level structure.

## Top-level structure

A `fair2.json` file is a single JSON-LD node object describing the Dataset.
It MUST carry `@context`, followed by the Dataset's own properties:

```json
{
  "@context": { ... },
  "@id":      "https://doi.org/10.1234/dataset",
  "@type":    "Dataset",
  "...":      "..."
}
```

| Key | Purpose |
|-----|---------|
| `@context` | JSON-LD context. Aliases every term used in the payload so property names appear without bare prefixes. |
| `@type` | `Dataset`. The document *is* the Dataset. |
| `included` | Optional. Bodies of nodes referenced from more than one place. See below. |

---

## Document structure

A `fair2.json` is **single-rooted**: the document *is* the Dataset. Its
properties sit at the top level, alongside `@context`.

```json
{
  "@context": { "...": "..." },
  "@id": "https://doi.org/10.1234/dataset",
  "@type": "Dataset",
  "name": "...",
  "distribution": [ "..." ],
  "recordSet": [ "..." ],
  "dataArticle": "https://doi.org/10.1234/article",
  "dataArchive": "https://doi.org/10.5281/zenodo.18326712",
  "included": [ "..." ]
}
```

This matches Croissant's own convention, and a consumer reading the file as
plain JSON finds the Dataset where it expects it rather than having to
descend into `@graph` and filter by `@type`.

### Peer artifacts are referenced, not described

A Data Article, Data Archive or Data Portal has its own external identity —
a DOI, in most cases — and its own lifecycle. Each is referenced by a bare
URI string:

| Property | Cardinality | Points at |
|---|---|---|
| `dataArticle` | exactly one | the article's DOI |
| `dataArchive` | zero or more | the archive's identifier |
| `dataPortal` | zero or more | the portal's identifier |

The context coerces these with `"@type": "@id"`, so a plain string expands
to an IRI reference without a `{"@id": ...}` wrapper appearing in the JSON.

Describing those artifacts inline couples their lifecycles to the Dataset's.
A publisher amending an article's title months after the data is finalised
should not oblige a new `fair2.json` — which invalidates the signed
artifact, triggers a new signing ceremony and cascades to consumers. A
property belonging to another artifact must not be able to invalidate this
one.

This does **not** apply to the Dataset's own parts — `methodSection`,
`distribution`, `recordSet`, `spatialCoverage`. Those have no independent
identity and belong in this document.

### Reused bodies go under `included`

Nodes referenced from several places — PROV activities and software agents,
source documents, scripts — are held **once** under `included`, an alias for
JSON-LD's [`@included`](https://www.w3.org/TR/json-ld11/#included-blocks),
and referenced by `@id` from their use sites. Each body must carry its own
`@id`; without one it expands to a blank node and loses the identity its use
sites point at.

```json
{
  "@type": "Dataset",
  "methodSection": [
    { "@type": "Section", "prov:used": { "@id": "source/readme" } }
  ],
  "included": [
    { "@id": "source/readme",
      "@type": "DigitalDocument",
      "name": "Dataset README",
      "encodingFormat": "text/markdown" }
  ]
}
```

!!! note "Changed in v1.4.0"
    Up to v1.3.0 the payload was a top-level `@graph` array whose members
    were peer entities, with the Data Article and Data Archive described
    inline, and cross-references written as `{"@id": "..."}` objects. The
    stated reason was `mlcroissant` traversal; in practice `mlcroissant`
    loads the single-rooted form, which is also what its own example
    datasets use.

---
