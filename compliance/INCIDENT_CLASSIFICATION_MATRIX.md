# INCIDENT_CLASSIFICATION_MATRIX
NeuroGrid Compliance & Safety Layer

## 1. Purpose
This document defines the **formal incident classification system** for the NeuroGrid ecosystem.  
It standardizes how incidents are identified, categorized, escalated, and resolved across clinical, technical, governance, and regulatory domains.

Incident classification is a **compliance and safety control**, not an operational convenience.

---

## 2. Scope
This matrix applies to:
- Remote Patient Monitoring (RPM) systems
- Clinical AI and decision-support models
- Data pipelines and storage layers
- Governance and DAO operations
- DeSci research infrastructure
- Human operators and authorized contributors

It governs incidents affecting:
- Patient safety
- Data integrity
- Regulatory compliance
- System availability
- Governance legitimacy

---

## 3. Classification Principles
All incident classification adheres to the following principles:

1. **Patient Safety First** – Safety impact overrides all other considerations  
2. **Worst-Case Bias** – Classify upward when uncertainty exists  
3. **Traceability** – Every incident must be auditable  
4. **Non-Retaliation** – Reporting an incident cannot be penalized  
5. **Regulatory Readiness** – Classifications must withstand external review  

---

## 4. Incident Severity Levels

### Level 0 – Informational
Definition:
- No harm
- No system malfunction
- No compliance exposure

Examples:
- Non-impacting log anomaly
- Benign alert misfire
- Documentation mismatch

Response:
- Logged only
- No escalation
- Periodic review

---

### Level 1 – Minor
Definition:
- Localized issue
- No patient harm
- No regulatory breach

Examples:
- Temporary data latency
- Non-critical sensor dropout
- UI display error

Response:
- Logged and reviewed
- Corrective action scheduled
- No external notification

---

### Level 2 – Moderate
Definition:
- System degradation
- Potential patient impact if unresolved
- Internal policy deviation

Examples:
- Repeated RPM signal loss
- AI model confidence degradation
- Delayed clinician notification

Response:
- Incident ticket opened
- Responsible team notified
- Resolution SLA enforced
- Compliance review required

---

### Level 3 – Major
Definition:
- High risk of patient harm
- Confirmed safety control failure
- Reportable compliance concern

Examples:
- Incorrect risk stratification
- Alert suppression without authorization
- Data integrity compromise

Response:
- Immediate escalation
- Mandatory human review
- Temporary system safeguards applied
- Compliance and oversight notified

---

### Level 4 – Critical
Definition:
- Actual or imminent patient harm
- Regulatory breach
- Systemic governance failure

Examples:
- Missed life-threatening alert
- Unauthorized clinical decision automation
- Data breach involving patient records

Response:
- Emergency protocols activated
- Human control enforced
- Regulator notification initiated (if required)
- Full incident investigation launched

---

## 5. Incident Domains

Each incident must be tagged with one or more domains:

- **Clinical Safety**
- **Data Protection & Privacy**
- **AI Model Behavior**
- **System Availability**
- **Governance & Ethics**
- **Security & Access Control**

Domain tagging does not reduce severity classification.

---

## 6. Classification Matrix

| Severity | Patient Impact | Compliance Risk | System Impact | Escalation |
|--------|----------------|-----------------|---------------|------------|
| Level 0 | None | None | None | None |
| Level 1 | None | Minimal | Local | Internal |
| Level 2 | Potential | Moderate | Partial | Management |
| Level 3 | High Risk | Significant | Broad | Oversight |
| Level 4 | Actual / Imminent | Severe | Systemic | Emergency |

---

## 7. Default Escalation Rules
If classification is unclear:
- Default to **Level 2**
- Enable alerts
- Notify responsible authority
- Reclassify after review

Downgrading severity requires documented justification.

---

## 8. Incident Ownership
Each incident must have:
- Assigned owner
- Backup authority
- Defined resolution timeline
- Closure criteria

Unowned incidents are a compliance violation.

---

## 9. Documentation & Audit
Every incident record must include:
- Unique incident ID
- Severity level
- Domain tags
- Timestamp
- Detection source
- Actions taken
- Resolution outcome

All records are immutable and audit-ready.

---

## 10. Regulatory Alignment
This matrix aligns with:
- ISO 14971 (Risk Management)
- IEC 62304 (Medical Software)
- FDA post-market surveillance expectations
- EU MDR vigilance requirements
- OECD AI incident governance guidance

---

## 11. Governance Interaction
Certain incidents automatically trigger:
- Independent Oversight review
- DAO notification
- Temporary privilege restriction
- Policy reassessment

Governance actions must not delay safety response.

---

## 12. Binding Status
This classification matrix is:
- Mandatory across all NeuroGrid systems
- Enforced via compliance controls
- Subject to periodic review
- Amendable only through approved governance process

Failure to classify or report incidents correctly constitutes a compliance breach.

---

### Status
**Active – Incident Classification Matrix**

