# RPM_ALERT_SEVERITY_SCORING.md

## 1. Purpose
This document defines the standardized framework for scoring, classifying, and responding to Remote Patient Monitoring (RPM) alerts within the DeSci-governed RPM subsystem. The objective is to ensure consistent clinical prioritization, patient safety, regulatory defensibility, and decentralized auditability across all RPM-generated alerts.

This framework is binding across all RPM-integrated AI models, clinical workflows, DAO-governed processes, and escalation protocols.

---

## 2. Scope
This policy applies to:
- All RPM devices integrated into the DeSci RPM layer
- All AI-generated, hybrid, or rule-based RPM alerts
- All clinical responders and DAO-authorized oversight roles
- All jurisdictions in which RPM services are deployed

---

## 3. Governing Principles
- **Patient Safety Supremacy:** Severity scoring prioritizes clinical risk above operational convenience.
- **Clinical Interpretability:** All severity bands map to clinically meaningful actions.
- **Deterministic Logic with Governed Override:** Scoring is deterministic; overrides are logged and governed.
- **DAO Auditability:** All scores and transitions are immutably traceable.
- **Automation Constraints:** Severity scoring alone must not trigger irreversible automated clinical actions.

---

## 4. Severity Scoring Model

### 4.1 Severity Score Range
All RPM alerts are assigned a continuous **Severity Score (SS)**:

**SS ∈ [0.0 – 100.0]**

---

### 4.2 Severity Classification Bands
| Band | Score Range | Classification | Clinical Interpretation |
|-----|------------|----------------|-------------------------|
| S0 | 0.0 – 9.9 | Informational | No clinical risk |
| S1 | 10.0 – 29.9 | Low | Mild deviation from baseline |
| S2 | 30.0 – 49.9 | Moderate | Requires clinician review |
| S3 | 50.0 – 69.9 | High | Time-sensitive risk |
| S4 | 70.0 – 84.9 | Critical | Immediate clinical action |
| S5 | 85.0 – 100.0 | Life-Threatening | Emergency escalation |

---

## 5. Scoring Dimensions
The Severity Score is calculated as a weighted composite of the following dimensions:

| Dimension | Description |
|---------|-------------|
| Physiological Deviation | Distance from patient-specific baseline |
| Rate of Change | Speed and direction of deterioration |
| Signal Confidence | Sensor fidelity and data completeness |
| Patient Risk Profile | Age, comorbidities, historical risk |
| Contextual Modifiers | Recent events, time sensitivity |
| Model Confidence | AI certainty and validated performance |

---

## 6. Weight Governance
- Default weights are approved via DAO-governed Clinical Oversight
- Weight modifications require:
  - Formal DAO proposal
  - Simulation and validation evidence
  - Change Control approval
- Jurisdiction-specific weight adjustments must be disclosed and logged

---

## 7. Escalation Mapping
| Severity Band | Mandatory Action |
|--------------|------------------|
| S0 | Log only |
| S1 | Passive dashboard notification |
| S2 | Clinician review within SLA |
| S3 | Active clinician alert |
| S4 | Immediate clinician + supervisory alert |
| S5 | Emergency protocol activation |

---

## 8. Human-in-the-Loop Requirements
- Alerts ≥ S2 require documented human acknowledgment
- S4 and S5 alerts require dual acknowledgment
- All overrides must include rationale, identity, and timestamp

---

## 9. Abuse, Drift, and Manipulation Detection
- Recurrent downgrading of high-severity alerts triggers DAO review
- Severity score distributions are continuously monitored
- Anomalous scoring behavior is escalated under Governance Failure Escalation

---

## 10. Logging and Traceability
Each RPM alert record must include:
- Raw input data
- Dimension-level component scores
- Final Severity Score and band
- Actions taken
- Overrides applied
- Cryptographic timestamp and node identity

All records are immutable and retained per decentralized retention policy.

---

## 11. Regulatory and DeSci Alignment
This framework aligns with:
- Clinical risk management standards
- Post-market surveillance requirements
- AI transparency and explainability obligations
- DeSci accountability and public audit principles

---

## 12. Review and Update Cycle
- Reviewed quarterly or upon:
  - Sentinel clinical events
  - Model updates
  - Regulatory or DAO mandate changes
- Emergency amendments permitted under Governance Emergency Safety Trigger

---

## 13. Ownership and Authority
**Owner:** DeSci RPM Clinical Governance Council  
**Approval Authority:** Independent Oversight Charter  
**Effective Date:** System Go-Live  
**Version Control:** Governed under AI Model Change Control

---

