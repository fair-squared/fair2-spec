# Versioning & spec conformance

## Declaring the spec version — `dct:conformsTo`

Every FAIR² document declares which version of the specification it was
produced against, as one of the Dataset's `conformsTo` values:

```json
{
  "@context": { "...": "..." },
  "@id": "https://doi.org/10.1234/dataset",
  "@type": "Dataset",
  "conformsTo": [
    "http://mlcommons.org/croissant/1.0",
    "https://fair2.ai/spec/v1.4.0"
  ],
  "version": "1.2",
  "dateCreated": "2025-02-05",
  "datePublished": "2025-03-03",
  "dateUpdated": "2025-11-19"
}
```

`dct:conformsTo` is multi-valued by design, so one Dataset can declare both
the Croissant version and the FAIR² spec version without a second mechanism.

- **the FAIR² spec version** is a URL of the form
  `https://fair2.ai/spec/v<MAJOR>.<MINOR>.<PATCH>`, matching the `fair2-spec`
  release tag, and resolving to that version's documentation. It is
  **required**, and `fair2s:DatasetShape` enforces it with a pattern.
- **`version`** is the dataset's own release.
- **`dateCreated` / `datePublished` / `dateUpdated`** are its lifecycle dates.

## Two versions, deliberately

The dataset and the document describing it change on different schedules, so
they carry separate version lines:

| Property | Versions | Bumped when |
|---|---|---|
| `version` | the **dataset** | the data itself changes |
| `fair2:metadataVersion` | the **`fair2.json` document** | the description changes |
| `dateUpdated` | the dataset | the data last changed |
| `fair2:metadataModified` | the document | the file was last edited |

A dataset at `1.2` may have a metadata document at `1.3.2` after several
corrections. `metadataVersion` follows `MAJOR.MINOR.PATCH`:

| Bump | For |
|---|---|
| Patch | a metadata-only correction — typo, URL fix, date fix |
| Minor | an additive change — a new contributor, distribution or field |
| Major | a structural change — entity model redesign, context change |

Both are required, and `fair2s:DatasetShape` enforces the version pattern.
Fixing a typo in a description must not bump `version`, because the data did
not change.

!!! note "Changed in v1.4.0 — the `_meta` block is gone"
    Up to v1.3.0 these lived in a `_meta` object outside `@graph`,
    deliberately kept out of the RDF. That had three costs. The fields
    duplicated Dataset properties and could disagree with them silently — in
    the reference example `_meta` claimed version `1.0.0` and a modification
    date of `2026-04-20` while the Dataset and its own changelog said `1.2`
    and `2025-11-19`. Spec conformance could not be checked by SHACL, so it
    needed deterministic enforcement in a separate validator. And because
    `_meta` produced no triples, it was invisible to any digest taken over
    the graph.

    The spec version became a `conformsTo` value and the file's own version
    and edit date became `fair2:metadataVersion` and
    `fair2:metadataModified`, so the file-versus-dataset distinction `_meta`
    drew is preserved — now in RDF, visible to a digest and checkable by
    SHACL. `_meta.dateCreated` is the one field not carried over; in practice
    it recorded the first release date, which `datePublished` already holds.
    Consumers reading pre-v1.4.0 documents will still find `_meta` at the
    root.

## Versioned documentation

The specification site is versioned with
[mike](https://github.com/jimporter/mike). Each `fair2-spec` release tag `vX.Y.Z`
publishes a corresponding docs version:

| URL | Points to |
|---|---|
| `https://fair2.ai/spec/v1.2.0/` | the docs for release `v1.2.0` |
| `https://fair2.ai/spec/latest/` | the newest release (moving alias) |
| `https://fair2.ai/spec/` | redirects to `latest` |

Only **tagged releases** are published — there is no intermediate/dev docs
channel. Each `_meta.conformsTo` therefore always resolves to a real release.

So a document's `_meta.conformsTo` URL is a stable, resolvable link to the exact
spec version it was built against, and `…/spec/latest/` always redirects readers
to the current release.

## Cutting a new spec version

1. Land the spec changes on `main`.
2. Tag the release: `git tag -a vX.Y.Z -m "…" && git push origin vX.Y.Z`.
   The docs workflow publishes `vX.Y.Z`, updates the `latest` alias, and sets it
   as the site default.
3. Bump `_meta.conformsTo` in the example(s) to `https://fair2.ai/spec/vX.Y.Z`.
4. In consumers, pin/advance the `fair2-spec` reference to the new tag.
