# `fair2.json` File Format

A FAIR² data package is serialised as a single JSON-LD document named
`fair2.json`. This page defines the file's required top-level structure.

## Top-level structure

A `fair2.json` file MUST contain exactly three top-level keys, in this order:

```json
{
  "@context": { ... },
  "_meta":    { ... },
  "@graph":   [ ... ]
}
```

| Key | Purpose |
|-----|---------|
| `@context` | JSON-LD context. Aliases every term used in the payload so property names appear without bare prefixes in `@graph`. |
| `_meta` | File-level metadata (version, dates). See below. Ignored by JSON-LD processors. |
| `@graph` | Array of the data-package entities. See below. |

No other top-level keys are permitted.

---

## The FAIR² data package as a graph

The payload is modelled as a single RDF graph containing the full FAIR²
publication set. The `@graph` array MUST contain the following peer entities
as top-level members:

| Entity | Cardinality | `@type` |
|--------|-------------|--------|
| Dataset | exactly one | `Dataset` (= `schema:Dataset`) |
| Data Article | exactly one | `DataArticle` (= `schema:ScholarlyArticle`) |
| Data Portal | zero or more | `DataPortal` (= `fair2:DataPortal`) |
| Data Archive | zero or more | `DataArchive` (= `fair2:DataArchive`) |

Optional additional peer entities:

- `prov:Activity` nodes that describe how data was generated or transformed
- `prov:SoftwareAgent` nodes for software referenced in provenance
- Reusable `Person` / `Organization` nodes when authors or creators are
  shared across multiple entities (see
  [ML Croissant compatibility rules](../integration/ml-croissant.md#compatibility-rules))

Cross-references between peers MUST use bare `{"@id": "..."}` objects; entities
MUST NOT be nested inside one another. For example:

```json
{
  "@graph": [
    {
      "@id": "https://example.org/dataset/123",
      "@type": "Dataset",
      "dataArticle": { "@id": "https://doi.org/10.1234/article" },
      "dataPortal":  { "@id": "https://portal.example.org" }
    },
    {
      "@id": "https://doi.org/10.1234/article",
      "@type": "DataArticle",
      "headline": "Foo dataset: AI-ready release",
      "...": "..."
    },
    {
      "@id": "https://portal.example.org",
      "@type": "DataPortal",
      "...": "..."
    }
  ]
}
```

The structural rule is documented here rather than enforced in SHACL, since
SHACL shapes target nodes by class and are agnostic to whether a node is
serialised inline or as a peer in `@graph`. Producers are still expected to
follow the peer-entity layout so `mlcroissant` and other consumers can
traverse the graph without re-entering shared nodes
(see [compatibility rules](../integration/ml-croissant.md#compatibility-rules)).

---

## The `_meta` block

`_meta` carries file-level administrative information. It is deliberately
outside `@graph` so that it produces no RDF triples and does not need a SHACL
shape. JSON-LD processors (including `mlcroissant`) ignore top-level keys
they do not recognise. The leading underscore signals to human readers that
this block is not part of the linked-data model.

### Fields

| Field | Type | Required | Description |
|-------|------|----------|-------------|
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
    "version": "1.0.0",
    "dateCreated": "2025-03-03",
    "dateModified": "2026-04-20"
  },
  "@graph": [ { "...": "..." } ]
}
```

### Validation

`_meta` is validated outside of SHACL — producer-side linting or a JSON
Schema check is sufficient. Required checks:

- All three fields are present
- `version` matches the `MAJOR.MINOR.PATCH` regex
- `dateCreated` and `dateModified` are valid ISO 8601 dates
- `dateModified >= dateCreated`
