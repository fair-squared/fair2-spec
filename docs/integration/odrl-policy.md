# ODRL Policies

The [W3C Open Digital Rights Language](https://www.w3.org/TR/odrl-model/)
(ODRL 2.2) expresses permissions, prohibitions and duties in a form many policy
systems read. In FAIR² it is an **export format**: a dataset's terms are stated
in its [governance blocks](../specification/governance.md), and an ODRL policy
is derived from them for systems that consume ODRL.

!!! note "Changed in v1.7.0"
    Up to v1.6.3 this page described embedding a hand-written ODRL `policy` in
    `fair2.json` as the statement of a dataset's terms. Governance blocks
    replace it: they are what governance services enforce, and they carry terms
    ODRL cannot.

## Which form is authoritative

1. **`fair2:access`** and the other governance blocks are the canonical form.
   When they are present, a consumer reads them.
2. An **ODRL policy** is read only when a document has no `fair2:access` —
   for example one produced by a system outside FAIR².

A governance service may publish the ODRL rendering of a dataset's governance
(for instance from a policy endpoint), marked as derived from `fair2:access`.

## Mapping

| FAIR² governance | ODRL |
|---|---|
| Access tier (`L0`–`L2`) | `odrl:Permission` with a credential-tier constraint |
| +G community governance | `odrl:Duty` to obtain community approval |
| +S environment | `odrl:Constraint` on the attested environment |
| +P purpose binding | `odrl:purpose` constraint; per-column purposes target the column, with DPV purpose IRIs |
| +J jurisdiction | `odrl:spatial` constraint |
| `aiTraining: "prohibited"` | `odrl:Prohibition` of `odrl:derive` |
| Embargo | `odrl:dateTime` constraint |
| Data use agreement | `odrl:Duty` to accept the agreement |
| Ethics training | `odrl:Duty` to hold the training |

The tier, approval, environment, agreement and training terms on the ODRL side
belong to the FAIR² governance model's **ODRL profile**. They appear only in
exported policies and are not part of the `fair2:` vocabulary this
specification defines.

## What does not survive the export

The mapping is **lossy**. ODRL has no equivalent for, among others:

- the difference between a declared and a verified purpose;
- the people exempt from an embargo (`exemptSubjectIds`);
- accepted identity providers and identity-assurance levels;
- the agent ceiling tier and agent policy;
- temporal phases;
- query governance: granularity, group sizes, linkage policy;
- Indigenous governance bodies and cultural protocols;
- the approvers and approval threshold of community governance.

A system that enforces a dataset's terms must therefore read the governance
blocks, not the ODRL rendering.
