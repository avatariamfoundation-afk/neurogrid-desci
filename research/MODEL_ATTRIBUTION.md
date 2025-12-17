# MODEL_ATTRIBUTION.md  
**NeuroGrid DeSci Registry – Model Attribution & Lineage Policy**

---

## 1. Purpose

This document defines how **AI and computational models** are attributed, registered, and referenced within the NeuroGrid decentralized science (DeSci) ecosystem.

The objectives are to ensure:

- Transparent scientific lineage  
- Verifiable provenance of models  
- Clear contributor attribution  
- Ethical and legal accountability  
- Alignment with DeSci, medical research, and future regulatory frameworks  

NeuroGrid does **not** store or execute models.  
It records **cryptographic attestations, metadata, and lineage references** only.

---

## 2. Definition of a “Model”

Within NeuroGrid, a *model* refers to any computational artifact used for inference, prediction, or analysis, including:

- Machine learning models (classical or deep learning)
- Statistical or probabilistic models
- Hybrid AI systems (rule-based + learned components)
- Federated or distributed learning models
- Ensemble or composite systems

Models may exist off-chain; however, their **identity, lineage, and attribution must be registrable**.

---

## 3. Model Registration Principles

### 3.1 Registry, Not Custody
- NeuroGrid never hosts, trains, or executes models
- Only hashes, metadata, and references are recorded
- Model artifacts remain under contributor or institutional control

### 3.2 Attribution Before Authority
A model must be registered and attributed **before** it may:
- Be referenced in funded research
- Receive DAO recognition
- Be cited in downstream work
- Be eligible for incentives or acknowledgements

---

## 4. Required Model Metadata

Each registered model must include the following metadata.

### Mandatory Fields
- **Model Identifier** (unique registry ID)
- **Model Hash** (cryptographic fingerprint of the model artifact)
- **Model Type** (e.g., CNN, Transformer, Statistical, Hybrid)
- **Training Paradigm** (centralized, federated, self-supervised, etc.)
- **Primary Dataset Hash(es)**  
  (must reference registered datasets)
- **Contributor Identifier(s)**
- **Declared Use Case** (research, clinical support, simulation, etc.)
- **Date of Registration**

### Optional Fields
- Model version
- Performance benchmarks (with references)
- Known limitations or bias disclosures
- Regulatory classification (if applicable)

---

## 5. Dataset–Model Lineage

Every model must declare its **dataset lineage**.

### 5.1 Lineage Rules
- Models may not reference unregistered datasets
- Derived datasets must be explicitly linked
- Synthetic or augmented datasets must declare source lineage

### 5.2 Lineage Integrity
- Lineage records are append-only
- Historical entries cannot be altered or removed
- Corrections require new attribution records, not deletion

---

## 6. Contributor Attribution

### 6.1 Who Is a Contributor
Contributors may include:
- Individual researchers
- Research groups
- Institutions
- DAOs or collectives
- Federated learning participants (where applicable)

### 6.2 Attribution Scope
Attribution may apply to:
- Model architecture
- Training methodology
- Dataset curation
- Optimization or fine-tuning
- Validation or benchmarking

### 6.3 Contributor Responsibility
By registering a model, contributors attest that:
- They have the right to reference the model
- Dataset usage complies with declared policies
- No prohibited or undisclosed data sources were used

False attribution constitutes a **governance violation**.

---

## 7. Derivative and Fine-Tuned Models

### 7.1 Derivative Definition
A derivative model includes:
- Fine-tuned versions
- Transfer-learned models
- Distilled models
- Ensemble models incorporating registered components

### 7.2 Attribution Requirements
Derivative models must:
- Reference all parent models
- Declare the transformation method
- Preserve original contributor attribution
- Add new contributors where applicable

---

## 8. Governance & Dispute Resolution

### 8.1 Governance Authority
Model attribution disputes fall under:
- NeuroGrid DAO governance
- Ethics and compliance review processes
- Designated arbitration mechanisms (if defined)

### 8.2 Dispute Scenarios
Disputes may arise from:
- Misattributed contributors
- Undeclared dataset usage
- False performance claims
- Unauthorized derivative claims

Possible resolutions include:
- Public registry annotations
- Revocation of recognition or incentives
- DAO-level sanctions

---

## 9. Regulatory & Ethical Alignment

This policy is designed to align with:
- LGPD (Brazil)
- GDPR (European Union)
- Research ethics frameworks
- Medical AI governance standards
- Anticipated AI regulatory regimes

No personally identifiable or protected data is stored on-chain.

---

## 10. Guiding Principle

> **NeuroGrid attributes knowledge, not ownership.**  
>  
> Attribution enables accountability, transparency, and trust — without centralized custody.

---

### Status
**Registry Policy – Active Draft**  
Subject to DAO ratification and future amendments.
