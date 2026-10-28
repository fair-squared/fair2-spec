# JSON Schemas

| File | Defines | Source |
|---|---|---|
| `fair2-cert.schema.json` | A FAIR² certification | this specification |
| `certifier-registry.schema.json` | The registry of authorised certifiers | this specification |
| `fair2-governance.schema.json` | The governance blocks (`fair2:access`, `fair2:constraints`, …) — see `docs/specification/governance.md` | Vendored, unchanged, from the FAIR² governance model, document schema v1.13 (fair2-governance 0899d37, 2026-10-10) |

The governance schema describes a governance service's signed document, whose
root also carries `fair2:id`, `fair2:version` and `fair2:proof`. In a
`fair2.json` the blocks are properties of the Dataset, so each is checked
against its own definition (`fair2:access` against `$defs/AccessBlock`, and so
on), not against the schema's root.

Update it by copying the governance model's `documentation/fair2-json.schema.json`
and recording the new version and commit here.
