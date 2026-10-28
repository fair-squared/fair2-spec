# FAIR² Access Agreement Levels (deprecated)

!!! warning "Deprecated in v1.7.0"
    Agreement Levels 0–6 are replaced by the [governance blocks](governance.md):
    an access tier — `L0` open, `L1` registered, `L2` credentialed — and the
    conditions and use constraints layered on it. Governance services read
    those, not the Agreement Levels. New documents should not use the levels;
    see [Migrating from Agreement Levels](governance.md#migrating-from-agreement-levels).

    This page and the level pages are kept so that existing links and
    identifiers (`fair2:AgreementLevel1`, `https://fair2.ai/ns/AgreementLevels1`,
    …) still resolve.

| Level | Name | Use instead |
|-------|------|-------------|
| [Level 0](../agreement-levels/Level0.md) | Embargoed Access | `L1` or `L2` with `fair2:embargo` |
| [Level 1](../agreement-levels/Level1.md) | Open Access | `L0` |
| [Level 2](../agreement-levels/Level2.md) | Collaborative Access | `L0`, with the licence and `fair2:constraints` |
| [Level 3](../agreement-levels/Level3.md) | Trusted Access | `L2` with `credentialRequirements` (or `L1`) |
| [Level 4](../agreement-levels/Level4.md) | Community-Governed (CARE) | `L1`/`L2` with `communityGovernance` and `fair2:indigenousGovernance` |
| [Level 5](../agreement-levels/Level5.md) | Secure / Controlled Environment | `L2` with `environment: "secureHuman"` |
| [Level 6](../agreement-levels/Level6.md) | Federated Compute-to-Data | `L2` with `environment: "computeToData"` and `queryGovernance` |

The levels' constraint axes carry over into the governance blocks:
`aiTraining` and `exportRestriction` are fields of `fair2:constraints`;
`identity`, `environment` and `communityGovernance` are fields of
`fair2:access`. The `fair2:constraints`, `fair2:reuseLogging`,
`fair2:AIethicalUse` and `fair2:governanceProtocol` keys in the level pages'
examples were never defined in the FAIR² vocabulary; `fair2:constraints` is
now, with the governance model's meaning.
