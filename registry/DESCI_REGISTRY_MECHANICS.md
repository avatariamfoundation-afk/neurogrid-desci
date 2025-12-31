# DESCI_REGISTRY_MECHANICS.md
**DeSci Artifact Registration, Validation, and Anchoring Mechanics**

---

## 1. Purpose

This document defines the **mandatory mechanics** governing how Decentralized Science (DeSci) artifacts are registered, validated, cross-linked, and anchored within the NeuroGrid ecosystem.

The DeSci registry is **not a publication platform**.  
It is a **compliance-aware scientific accountability ledger**.

---

## 2. Scope

This standard applies to all DeSci artifacts, including:

- Research protocols
- Datasets (raw, derived, synthetic)
- Analysis pipelines
- Statistical results
- Model evaluation reports
- Ethics approvals
- Funding disclosures
- Reproducibility packages

All artifacts are **off-chain by default** and **on-chain by reference only**.

---
## 3. Cost Governance & Enforcement

All registry operations defined in this document are governed by the
**Cost Ceiling Policy**.

This includes:
- Registry anchor writes
- Validation attestations
- Research trace commitments
- Batch submission mechanics

Hard gas ceilings, storage constraints, and batching requirements
are enforced as defined in:

→ `COST_CEILING_POLICY.md`

Any registry interaction that violates hard ceilings MUST revert.
Soft ceiling violations MUST trigger batching or deferral.

---

## 4. Architectural Position

DeSci Registry operates as a **downstream consumer** of NeuroGrid Core.

- ❌ No direct Core mutation
- ❌ No governance authority
- ❌ No clinical decision power
- ✅ Registry submission
- ✅ Validation dependency
- ✅ Cross-link traceability

All authority resolution occurs at **CORE level**.

---

## 5. Artifact Identity Model

Each DeSci artifact MUST be represented by:

- `artifactHash` (SHA-256 or equivalent)
- `artifactType`
- `artifactVersion`
- `owningEntity`
- `creationTimestamp`

The hash is the **sole canonical identifier**.

---

## 6. Mandatory Validation Requirements

Before registry anchoring, the following validations are required:

| Artifact Type | Required Validation |
|--------------|---------------------|
| Research Protocol | Ethics + Compliance |
| Dataset | Data Integrity + Consent |
| Analysis Code | Reproducibility |
| Results | Statistical Review |
| Model Evaluation | Performance + Bias |
| Funding Disclosure | Conflict Review |

Validations are submitted via **ValidatorModule.sol** and anchored as:


Artifacts without required validation **MUST NOT** be registered.

---

## 7. Registry Submission Flow

1. Artifact prepared off-chain
2. Required validations completed
3. Validation hash anchored to CORE
4. DeSci registry submission prepared
5. Registry record anchored to CORE
6. Cross-links created (if applicable)

No step may be skipped.

---

## 8. Core Anchoring Rules

All DeSci registry entries must be anchored using:

- `anchorRegistryRecord`
- `domain = "DESCI"`
- `recordType = "RESEARCH" | "DATA" | "ANALYSIS" | "DISCLOSURE"`

The registry record hash MUST include:
- Artifact hash
- Validation hash references
- Version identifier
- Timestamp

---

## 9. Cross-Link Requirements

Cross-links are mandatory when:

- A dataset supports a result
- A protocol precedes a study
- A funding source supports research
- A model evaluation references a dataset

Cross-links must be anchored using:

---

## 10. Versioning and Supersession

DeSci artifacts are **append-only**.

- New versions require new hashes
- Supersession must be cross-linked
- Prior versions remain immutable

Deletion is prohibited.  
Withdrawal is handled via **status annotations**, not erasure.

---

## 11. Access and Visibility

Registry metadata is:
- Publicly readable
- Pseudonymized by default
- Fully auditable

Underlying data access is governed separately by:
- Consent policies
- Access agreements
- Jurisdictional law

---

## 12. Compliance Alignment

This mechanism aligns with:

- EU Open Science principles
- GDPR / LGPD research exemptions
- NIH / Horizon reproducibility standards
- ISO 27001 data governance
- WHO AI research guidance

---

## 13. Prohibited Actions

The DeSci Registry MAY NOT:

- Register unvalidated artifacts
- Override validation outcomes
- Conceal conflicts or funding sources
- Retroactively modify records
- Anchor false provenance

Violations constitute a **governance breach**.

---

## 14. Audit and Traceability

Every registry entry must be:

- Timestamped
- Hash-addressed
- Validation-linked
- Cross-referenced
- Indefinitely auditable

There is no concept of “soft deletion”.

---

### Status
**Active – Binding DeSci Registry Standard**


