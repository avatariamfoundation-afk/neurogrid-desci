## DESCI_SCOPE.md

DeSci Enhancement & Structural Hardening Scope
Project: NeuroGrid / Aethera BioSync
Network: BNB Chain (Hackathon) → Multi-Chain (Post-Hackathon)

--- 

## 1. Purpose and Scope

This document defines the explicit scope, boundaries, and execution intent of the DeSci (Decentralized Science) layer within the NeuroGrid ecosystem.

The DeSci layer is responsible for transforming deterministic AI outputs and on-chain artifacts into verifiable, collaborative, incentive-aligned scientific workflows.

This scope is designed to satisfy:

Hackathon evaluation requirements (clarity, feasibility, decentralization)

Real-world scientific integrity requirements (reproducibility, attribution, fault handling)

Long-term ecosystem growth (research networks, incentives, governance)

---

## 2. DeSci Layer Responsibilities (Authoritative)

The DeSci layer does not perform inference and does not control core protocol logic.

Its responsibilities are strictly defined as:

Scientific collaboration coordination

Artifact sharing and discovery

Peer review and attestation workflows

Reputation and contribution signaling

Incentive routing for validated scientific work

Long-term reproducibility guarantees

---

## 3. In-Scope Capabilities
### 3.1 Research Artifact Lifecycle

The DeSci layer manages the post-emission lifecycle of artifacts produced by MedIntel and registered via NeuroGrid-Core.

In scope:

Artifact indexing

Metadata enrichment

Version lineage tracking

Immutable reference linking (hash + chain reference)

Status mirroring (accepted / rejected / disputed)

Out of scope:

Artifact mutation

Core registry authority override

### 3.2 Peer Review & Attestation

The DeSci layer enables human and agent-based scientific review without compromising determinism.

In scope:

Reviewer registration (wallet-based identity)

Review submission (signed attestations)

Deterministic scoring aggregation

Conflict flagging

Transparent review history

Out of scope:

Subjective ranking

Hidden moderation

Centralized approval

### 3.3 Reproducibility Framework

Scientific credibility is enforced through replayability and verification.

In scope:

Deterministic replay references

Input dataset hashes

Model version identifiers

Environment fingerprints

Execution receipts

Out of scope:

Hosting compute

Storing raw sensitive biomedical data

### 3.4 Incentives & Funding Signals

The DeSci layer provides signals, not monetary authority.

In scope:

Contribution scoring

Reputation weighting

Funding eligibility markers

Reward routing instructions to Core

Out of scope:

Token minting

Treasury control

Monetary policy

---

## 4. Structural Hardening Principles

The DeSci layer follows non-negotiable hardening constraints:

No Single Point of Trust

All Actions Are Signed

All Decisions Are Replayable

All Failures Are Deterministic

All Incentives Are Transparent

---

## 5. Determinism & Fault Awareness

The DeSci layer must remain fault-aware but not fault-authoritative.

In scope:

Fault code propagation

Review rejection on deterministic fault presence

Dispute markers for downstream governance

Out of scope:

Slashing execution

Validator punishment

---

## 6. Interfaces & Integration Boundaries
### 6.1 Upstream Dependencies

MedIntel (Inference outputs)

NeuroGrid-Core (Artifact registry, telemetry, roles)

Deterministic Telemetry Stream

### 6.2 Downstream Consumers

Governance modules

Funding DAOs

External research networks

Analytics dashboards

===

## 7. Hackathon Alignment

For hackathon evaluation, the DeSci layer demonstrates:

Open scientific collaboration

Verifiable research workflows

On-chain transparency

Clear separation of concerns

Immediate real-world relevance

The system is intentionally minimal yet complete, avoiding speculative features while proving end-to-end scientific decentralization.

---

## 8. Post-Hackathon Expansion (Non-Blocking)

Explicitly out of current scope but planned:

Federated research clusters

Cross-institution data escrow

Privacy-preserving compute (ZK-ML)

Journal and publication integrations

Academic credential bridging

These are intentionally excluded to preserve hackathon focus and execution reliability.

---

## 9. Funding Utilization Context (Judge Insight)

A portion of awarded hackathon funds will be allocated toward:

Building a public-facing research interface

Launching an IoT-linked e-commerce footprint

Integrating wearable medical devices

Developing companion applications for biosignal ingestion

This ensures that DeSci outputs move from theory to market-validated impact.

---

## 10. Scope Lock

This document locks the DeSci scope for the current execution phase.

Any feature not explicitly listed as in scope is considered out of scope by default.

Status: Scope Locked
Phase: DeSci Enhancement & Structural Hardening
Authority: Execution Lead (Protocol)
Last Updated: Hackathon Submission Phase
