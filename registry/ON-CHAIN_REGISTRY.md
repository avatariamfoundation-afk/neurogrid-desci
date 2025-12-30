# ON_CHAIN_REGISTRY.md  
**Decentralized Registry Anchoring & Integrity Framework**

---

## 1. Purpose

This document defines the **On-Chain Registry architecture** for the NeuroGrid DeSci repository.  
The registry serves as an immutable anchoring layer for governance, research, compliance, and system metadata **without storing clinical data**.

Its primary function is to provide:
- Verifiable integrity
- Tamper resistance
- Transparent auditability
- Cross-repository traceability

---

## 2. Scope

The On-Chain Registry applies to:

- Governance artifacts
- Research registry entries
- Ethics and compliance approvals
- Funding allocations
- DAO resolutions
- System state hashes
- Cross-repository references (Core ↔ DeSci ↔ MedIntel)

It explicitly **excludes**:
- Patient-identifiable data
- Raw RPM streams
- Model weights
- Clinical outputs

---

## 3. Registry Design Principles

- **Hash-only anchoring**
- **Append-only records**
- **Human-readable off-chain, machine-verifiable on-chain**
- **Separation of governance and clinical domains**
- **Jurisdiction-neutral design**

The blockchain is a **source of truth for integrity**, not for execution of care.

---

## 4. Registry Record Types

### A. Governance Records
- Proposal hashes
- Vote outcomes
- Committee resolutions
- Emergency actions

### B. Research Records
- Study registration
- Protocol versioning
- Reproducibility attestations
- Publication disclosures

### C. Compliance Records
- Ethics approvals
- Regulatory checkpoints
- Audit attestations
- Policy version anchors

### D. System Records
- System logic versions
- Emergency state flags
- Backup activation markers
- Kill-switch activations (metadata only)

---

## 5. Record Structure (Abstract)

Each registry entry must include:

- Record ID
- Record type
- Content hash (SHA-256 or equivalent)
- Originating repository
- Timestamp
- Signer role (DAO / Committee / System)
- Optional cross-link references

---

## 6. Submission Flow

1. Off-chain document finalized
2. Compliance or governance validation
3. Hash generated
4. Hash submitted to Core registry contract
5. Transaction confirmed
6. Reference ID recorded in DeSci index

No record may be edited after anchoring.

---

## 7. Update & Supersession Rules

- Records are never overwritten
- Updates require:
  - New record
  - Explicit supersession reference
- Historical lineage must remain intact

---

## 8. Access & Transparency

- Registry is publicly readable
- Submission is permissioned
- Write access limited to authorized roles
- Observers may independently verify integrity

---

## 9. Cross-Repository Linking

The On-Chain Registry provides cryptographic linkage between:

- `NeuroGrid-core`
- `desci`
- `medintel`

This enables:
- End-to-end traceability
- Audit reconstruction
- Regulatory inspection without data exposure

---

## 10. Emergency Registry Mode

During declared emergencies:
- Emergency markers may be written
- Post-event ratification required
- All emergency entries are flagged and reviewable

---

## 11. Compliance Alignment

The registry design aligns with:

- EU AI Act (governance traceability)
- FDA audit trail expectations
- LGPD / GDPR data minimization
- ISO 27001 / 37301
- DeSci transparency principles

---

## 12. Prohibited Uses

The registry must never be used to:
- Store personal data
- Influence clinical decisions
- Encode medical advice
- Bypass compliance workflows

---

## 13. Audit & Verification

All registry entries:
- Are independently verifiable
- Support Merkle or hash proof validation
- Can be reconstructed off-chain
- Are retained indefinitely

---

### Status  
**Active – Binding Infrastructure Specification**

