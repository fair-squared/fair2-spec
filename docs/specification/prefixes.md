# Namespace Prefixes

The FAIR² specification reuses terms from several external vocabularies. Every
`fair2.json` producer SHOULD declare the prefixes below in their `@context`, and
consumers SHOULD expect these bindings to resolve to the URIs given here.

## Canonical prefix table

| Prefix | URI |
|--------|-----|
| `cr:` | `http://mlcommons.org/croissant/` |
| `cro:` | `http://purl.obolibrary.org/obo/CRO_` |
| `credit:` | `http://purl.org/credit/ontology#CREDIT_` |
| `dct:` | `http://purl.org/dc/terms/` |
| `fair2:` | `https://fair2.ai/ns/` |
| `fair2s:` | `https://fair2.ai/shapes/` |
| `prov:` | `http://www.w3.org/ns/prov#` |
| `rai:` | `http://mlcommons.org/croissant/RAI/` |
| `rdfs:` | `http://www.w3.org/2000/01/rdf-schema#` |
| `sc:` / `schema:` | `https://schema.org/` |
| `skos:` | `http://www.w3.org/2004/02/skos/core#` |
| `xsd:` | `http://www.w3.org/2001/XMLSchema#` |

## Retired prefixes

- **`mlc:`** — previously used for MLCommons Croissant terms. Retired in favour
  of `cr:` (same target URI). Any `mlc:` occurrence in producer output is an
  error.

## Notes on specific prefixes

- **`credit:`** resolves to the CRediT taxonomy hosted at purl.org. Role
  identifiers are of the form `credit:Conceptualization`,
  `credit:DataCuration`, etc. This URI form is the canonical FAIR² binding;
  downstream tooling that historically used the NISO z39.104 URIs
  (`http://www.niso.org/publications/z39104-2022-credit#...`) SHOULD migrate.

- **`fair2:`** terms resolve against the FAIR² ontology. Property and class
  definitions live in
  [`ontologies/fair2_ontology.ttl`](https://github.com/fair-squared/fair2-spec/blob/main/ontologies/fair2_ontology.ttl).

- **`fair2s:`** is reserved for SHACL shape identifiers defined in
  [`shapes/turtle/`](https://github.com/fair-squared/fair2-spec/tree/main/shapes/turtle).
  It is distinct from the data-model prefix `fair2:`.

## Canonical `@context` reference

The authoritative `@context` block FAIR² producers should reference is
[`context/metadata/fair2_context.json`](https://github.com/fair-squared/fair2-spec/blob/main/context/metadata/fair2_context.json).
It aliases every term used in the FAIR² data model so that `fair2.json`
payloads can be written without bare prefixed forms in their bodies.
