---
name: Croissant / mlcroissant compatibility
about: Report a FAIR²-to-Croissant (mlcroissant) loading or validation incompatibility
title: "[croissant] "
labels: ["bug", "integration:croissant"]
assignees: []
---

## Summary

<!-- One or two sentences: which file, and what fails. -->

- Affected file(s):
- `mlcroissant` version:
- SHACL validation status (passes? `pyshacl -s <shapes> -d <file>`):

## Reproduction

```python
import mlcroissant as mlc
mlc.Dataset(jsonld="examples/.../<file>.json")
```

Error / traceback:

```
<paste the exception here>
```

## Background — known limitation

`mlcroissant`'s JSON-LD loader (`recursively_populate_jsonld`) flattens the graph
with `rdflib`, then re-nests it by **inlining every `{"@id": "X"}` reference and
mutating the target node in place**. As a result it raises a `KeyError` whenever a
node is reached more than once from the entry `Dataset` — i.e. when a node is:

1. part of a reference **cycle** (e.g. `Dataset.url` equal to the dataset's own
   `@id`; a `geoWithin` back-link that mirrors a `containsPlace`; a
   `DataArticle.wasDerivedFrom` / `DataPortal.dataset` / `DataArchive.dataset`
   pointing back at the `Dataset`); or
2. referenced via **two different paths** (a shared `@graph` node referenced from
   more than one place).

These are the failure modes documented in
[`docs/integration/ml-croissant.md`](../../docs/integration/ml-croissant.md)
(Compatibility Rules 1–6). The FAIR² normalized `@graph` serialization can hit
them because it cross-links extension entities (`DataPortal`, `DataArchive`,
`DataArticle`, `Activity`, `SoftwareAgent`, method `source/*`).

## Checklist before filing

- [ ] No node forms a reference cycle (no self-referential `url`, no
      `geoWithin`⇄`containsPlace`, no back-links to the `Dataset` `@id`).
- [ ] Cross-graph reference properties do **not** use `"@type": "@id"` in the
      `@context` (Rule 2).
- [ ] Repeated entities are emitted as fresh blank nodes, or referenced exactly
      once (Rules 1 & 4).
- [ ] `@context` includes `@language` (mlcroissant requires it).
- [ ] FileObject checksums use `schema:sha256` (or `md5`), and `@type` is
      `cr:FileObject` (Rules 5 & 6).
- [ ] SHACL validation (`pyshacl`) still reports `Conforms: True`.

## Proposed fix / acceptance criteria

- [ ] `mlcroissant.Dataset(jsonld=...)` loads with no exception and exposes
      `metadata.name`, `record_sets`, and `distribution`.
- [ ] SHACL validation continues to pass.
- [ ] (If applicable) a regression test loads every `examples/**` file through
      `mlcroissant`.
