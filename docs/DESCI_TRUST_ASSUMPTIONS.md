## DESCI_TRUST_ASSUMPTIONS.md

DeSci Trust Boundaries, Guarantees, and Non-Assumptions
Project: NeuroGrid / Aethera BioSync
Layer: DeSci (Decentralized Science)
Scope: Hackathon-Ready with Real-World Continuity

---

## 1. Purpose

This document defines the explicit trust assumptions of the DeSci layer within NeuroGrid.

It clarifies:

What the system trusts

What the system verifies

What the system does not trust

What the system refuses to assume

This is critical for judges, auditors, contributors, and future partners to correctly understand the system’s security, scientific rigor, and decentralization posture.

---

## 2. Core Trust Philosophy

NeuroGrid follows a strict principle:

Trust nothing that can be verified. Verify everything that can affect scientific outcomes.

DeSci in NeuroGrid is mechanism-driven, not reputation-driven.

---

## 3. Explicit Trust Assumptions

The system does assume the following:

# 3.1 Cryptographic Primitives Are Secure

Hash functions are collision-resistant

Digital signatures are unforgeable

Merkle constructions behave as expected

These are industry-standard assumptions.

# 3.2 Blockchain Finality Holds

BNB Chain provides probabilistic finality

Once finalized, on-chain records are immutable

Temporary reorgs are tolerated but final state is authoritative.

# 3.3 Wallet Key Ownership

Users control their private keys

Compromised keys are outside protocol responsibility

Identity is cryptographic, not biometric or institutional.

# 3.4 Deterministic Execution Can Be Fingerprinted

AI models

Runtime environments

Dependency graphs

If two executions produce different outputs under identical fingerprints, this is treated as a fault.

---

## 4. Explicit Non-Assumptions (What We Do NOT Trust)

The system does NOT assume:

# 4.1 Honest Researchers

Researchers may submit incorrect, biased, or malicious work

Provenance does not imply correctness

Verification is procedural, not moral.

# 4.2 Honest Reviewers

Peer reviewers may collude

Reviews are treated as signals, not truths

All reviews are signed, weighted, and auditable.

# 4.3 Correct Input Data

Input datasets may be flawed

Garbage-in is explicitly allowed, but documented

The system tracks what happened, not what should have happened.

# 4.4 Centralized Oversight

No foundation, DAO, or admin is trusted to curate truth

Governance cannot rewrite provenance or artifacts

Governance acts on outcomes, not on history.

---

## 5. Trust Boundaries by Layer
# 5.1 AI / MedIntel Layer

Trusted for deterministic execution only

Not trusted for semantic correctness

Outputs are treated as claims, not facts

# 5.2 Core / Blockchain Layer

Trusted for immutability

Trusted for access control enforcement

Trusted for event ordering

# 5.3 DeSci Layer

Trusted for indexing, not validation

Trusted for transparency, not correctness

Trusted for collaboration mechanics

---

## 6. Scientific Integrity Model

Scientific integrity is enforced through:

Deterministic inference

Full provenance chains

Signed attestations

Replay verification

Integrity ≠ correctness
Integrity means the system can prove what happened, not that it was right.

---

## 7. Reproducibility Trust Model

A result is considered reproducible if and only if:

Input hashes match

Model hash matches

Environment hash matches

Telemetry root matches

If any mismatch occurs:

Reproduction is invalid

Original artifact remains immutable

Discrepancy is transparent

---

## 8. Fault-Aware Trust Handling

Failures are first-class citizens.

The system assumes:

Nodes can fail

Inference can halt

Telemetry can expose faults

Faults are:

Recorded

Classified

Never hidden

Failure does not invalidate provenance.

---

## 9. Cross-Chain Trust Posture

Cross-chain interactions assume:

No shared trust between chains

Verification is hash-based only

External chains are treated as independent witnesses

No chain is trusted to validate another.

---

## 10. Incentives & Trust

Token incentives do not imply trust.

Tokens reward participation

Tokens do not validate truth

Tokens do not override provenance

Economic alignment exists alongside, not above, scientific rigor.

---

## 11. Hackathon Context Assumptions

For hackathon purposes:

Testnet deployment is sufficient

Deterministic proofs outweigh scale

Open-source transparency outweighs polish

The system is intentionally designed to scale beyond hackathon constraints without architectural change.

---

## 12. Real-World Extension Assumptions

Post-hackathon, the same trust assumptions hold for:

Clinical research pilots

Wearable device data ingestion

IoT health telemetry

E-commerce-driven hardware distribution

Funding awarded will be partially allocated toward:

Wearable medical devices

Companion applications

Secure data ingestion pipelines

These do not alter trust assumptions — only data volume.

---

## 13. Trust Model Lock

This trust model is explicitly locked.

Any future changes must:

Be versioned

Be auditable

Never retroactively alter provenance
