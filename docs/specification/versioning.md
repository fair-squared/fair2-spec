# Versioning & spec conformance

## Declaring the spec version — `_meta.conformsTo`

Every FAIR² document declares which version of the FAIR² specification it was
produced against, at the **root** of the document, in the `_meta` block:

```json
{
  "@context": { ... },
  "_meta": {
    "conformsTo": "https://fair2.ai/spec/v1.2.0",
    "version": "1.0.0",
    "dateCreated": "2025-03-03",
    "dateModified": "2026-04-20"
  },
  "@graph": [ { "@type": "Dataset", ... } ]
}
```

- **`_meta.conformsTo`** — the FAIR² **spec** version, as a URL of the form
  `https://fair2.ai/spec/v<MAJOR>.<MINOR>.<PATCH>`. The version segment **matches
  the `fair2-spec` repository release tag** (e.g. tag `v1.2.0` ↔
  `https://fair2.ai/spec/v1.2.0`), and resolves to that version's documentation
  (see below).
- **`_meta.version`** — the *data package* version (the dataset's own release),
  distinct from the spec version.
- `_meta.dateCreated` / `_meta.dateModified` — package lifecycle dates.

`_meta` is document-level package metadata; it sits at the root, **outside
`@graph`**, so it does not affect how the Dataset is parsed by mlcroissant or
Google Dataset Search. It is complementary to the Dataset node's own
`schema:conformsTo` (which declares Croissant conformance).

> `_meta.conformsTo` is **required**. The `fair2-validator` tool checks for it
> deterministically and fails a document that omits it or whose value is not a
> `https://fair2.ai/spec/vX.Y.Z` URL. (It is not a SHACL constraint, because
> `_meta` is document metadata rather than an RDF graph node.)

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
