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

## 3. Architectural Position

DeSci Registry operates as a **downstream consumer** of NeuroGrid Core.

- ❌ No direct Core mutation
- ❌ No governance authority
- ❌ No clinical decision power
- ✅ Registry submission
- ✅ Validation dependency
- ✅ Cross-link traceability

All authority resolution occurs at **CORE level**.

---

## 4. Artifact Identity Model

Each DeSci artifact MUST be represented by:

- `artifactHash` (SHA-256 or equivalent)
- `artifactType`
- `artifactVersion`
- `owningEntity`
- `creationTimestamp`

The hash is the **sole canonical identifier**.

---

## 5. Mandatory Validation Requirements

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

