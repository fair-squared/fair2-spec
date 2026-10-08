# `fair2.json` File Format

A FAIR² data package is serialised as a single JSON-LD document named
`fair2.json`. This page defines the file's required top-level structure.

## Top-level structure

A `fair2.json` file is a single JSON-LD node object describing the Dataset.
It MUST carry `@context` and `_meta`, followed by the Dataset's own
properties:

```json
{
  "@context": { ... },
  "_meta":    { ... },
  "@id":      "https://doi.org/10.1234/dataset",
  "@type":    "Dataset",
  "...":      "..."
}
```

| Key | Purpose |
|-----|---------|
| `@context` | JSON-LD context. Aliases every term used in the payload so property names appear without bare prefixes. |
| `_meta` | File-level metadata (version, dates). See below. Mapped to `null` in the context, so it produces no RDF. |
| `@type` | `Dataset`. The document *is* the Dataset. |
| `included` | Optional. Bodies of nodes referenced from more than one place. See below. |

---

## Document structure

A `fair2.json` is **single-rooted**: the document *is* the Dataset. Its
properties sit at the top level, alongside `@context` and `_meta`.

```json
{
  "@context": { "...": "..." },
  "_meta": { "...": "..." },
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

## The `_meta` block

`_meta` carries file-level administrative information. It is deliberately
outside `@graph` and the FAIR² context maps `_meta` to `null`, which is what
keeps it out of the RDF; it therefore needs no SHACL shape. The mapping is
required, not cosmetic: the context sets `@vocab`, so an unmapped top-level
key would **not** be ignored — it would expand to `https://schema.org/_meta`
and emit a triple against a property that does not exist. The leading
underscore signals to human readers that this block is not part of the
linked-data model.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| `conformsTo` | string (URL) | Yes | The FAIR² **spec** version this file was produced against, as `https://fair2.ai/spec/v<MAJOR>.<MINOR>.<PATCH>` — matching the `fair2-spec` release tag. Distinct from `version` (the file version) and from `Dataset.conformsTo` (Croissant). See [Versioning & Conformance](versioning.md). |
| `version` | string (semver) | Yes | Version of the `fair2.json` file itself. Follows `MAJOR.MINOR.PATCH`. Independent of `Dataset.version`. |
| `dateCreated` | string (ISO 8601 date) | Yes | Date the file was first created. Set once. |
| `dateModified` | string (ISO 8601 date) | Yes | Date of the most recent modification. MUST be updated on every edit. |

### Versioning rules for `_meta.version`

| Change type | Bump | Examples |
|-------------|------|----------|
| **Patch** (`x.x.N`) | metadata-only correction | typo fix, URL correction, date fix |
| **Minor** (`x.N.0`) | additive change | new contributor, new distribution file, new field, new entity added |
| **Major** (`N.0.0`) | breaking structural change | entity model redesign, `@context` schema change, entity removal |

`_meta.version` is independent of `Dataset.version`. A dataset published at
`"1.1"` may have a `fair2.json` file at `_meta.version: "1.3.2"` after several
metadata corrections.

### Example

```json
{
  "@context": { "...": "..." },
  "_meta": {
    "conformsTo": "https://fair2.ai/spec/v1.2.0",
    "version": "1.0.0",
    "dateCreated": "2025-03-03",
    "dateModified": "2026-04-20"
  },
  "@type": "Dataset",
  "...": "..."
}
```

### Validation

`_meta` is validated outside of SHACL (it is document metadata, not an RDF
graph node) — the `fair2-validator` tool checks it deterministically, and
producer-side linting or a JSON Schema check is equivalent. Required checks:

- All four fields are present
- `conformsTo` matches `https://fair2.ai/spec/vMAJOR.MINOR.PATCH`
- `version` matches the `MAJOR.MINOR.PATCH` regex
- `dateCreated` and `dateModified` are valid ISO 8601 dates
- `dateModified >= dateCreated`
