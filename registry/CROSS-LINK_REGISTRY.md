# CROSS_LINK_REGISTRY.md  
**Cross-Repository Integrity & Traceability Framework**

---

## 1. Purpose

This document defines the **Cross-Link Registry** for the NeuroGrid ecosystem.  
Its function is to provide **cryptographically verifiable linkage** between artifacts, decisions, and records that span:

- NeuroGrid Core
- DeSci repository
- MedIntel repository

The Cross-Link Registry ensures that governance, research, and clinical AI artifacts remain **contextually connected without merging authority domains**.

---

## 2. Scope

The Cross-Link Registry applies to:

- Governance decisions referencing clinical artifacts
- Research outputs referencing governance approvals
- Compliance documents referencing system states
- Registry entries that require multi-repo traceability
- Audit reconstruction across repositories

It does **not**:
- Store primary content
- Replace on-chain registries
- Execute logic
- Influence clinical decisions

---

## 3. Design Principles

- Reference-only (no content storage)
- Hash-based linkage
- Explicit directionality
- Immutable historical lineage
- Regulatory containment by domain

Cross-links are **contextual bridges**, not control mechanisms.

---

## 4. Cross-Link Record Types

### A. Governance → MedIntel
- Proposal referencing model deployment
- Vote ratifying emergency clinical action
- Oversight review of AI safety artifacts

### B. MedIntel → Governance
- Safety case requiring DAO acknowledgment
- Emergency suspension notification
- Post-market surveillance escalation

### C. Research → Governance
- Funding approvals
- Ethics clearance references
- Publication disclosures

### D. System → System
- Core contract version anchoring
- Registry supersession mapping
- Emergency state propagation (metadata only)

---

## 5. Cross-Link Record Structure

Each cross-link record must contain:

- Cross-link ID
- Source repository
- Source artifact hash / registry ID
- Target repository
- Target artifact hash / registry ID
- Relationship type
- Timestamp
- Authorizing role

No record may omit directionality.

---

## 6. Creation Workflow

1. Source artifact finalized and anchored
2. Target artifact identified and validated
3. Relationship defined and reviewed
4. Cross-link hash generated
5. Cross-link recorded in DeSci registry index
6. Optional on-chain anchoring (hash only)

Cross-links may be unilateral or bidirectional, but must be explicit.

---

## 7. Update & Supersession

- Cross-links are immutable
- Supersession requires a new cross-link record
- Deprecated relationships must remain visible
- Historical graph reconstruction must be possible

---

## 8. Access & Permissions

- Read access: public
- Write access: restricted to authorized governance or compliance roles
- Emergency linking: Safety Council only
- All actions logged and auditable

---

## 9. Emergency Context

During emergencies:
- Temporary cross-links may be created
- Must be flagged as emergency-context
- Require post-event ratification
- Cannot persist without review

---

## 10. Audit & Reconstruction

The Cross-Link Registry enables:

- Full decision lineage reconstruction
- Regulatory inspection across domains
- Independent verification of claims
- Temporal consistency validation

Auditors must be able to reconstruct **why**, **when**, and **under whose authority** artifacts were connected.

---

## 11. Regulatory Alignment

This framework aligns with:

- EU AI Act traceability and governance separation
- FDA audit trail expectations
- ISO 37301 (Compliance Management)
- DeSci transparency principles

---

## 12. Prohibited Uses

The Cross-Link Registry must never:
- Imply authority transfer
- Enable DAO clinical control
- Circumvent compliance reviews
- Obscure responsibility boundaries

---

## 13. Enforcement

Improper cross-linking constitutes:
- Governance breach
- Audit finding
- Potential suspension of write privileges

---

### Status  
**Active – Binding DeSci Infrastructure Specification**

