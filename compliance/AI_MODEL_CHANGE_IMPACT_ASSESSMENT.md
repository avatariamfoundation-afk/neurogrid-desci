# AI_MODEL_CHANGE_IMPACT_ASSESSMENT.md

Model Modification Risk, Safety & Regulatory Impact Framework

---
 
# 1. Purpose

This document defines the AI Model Change Impact Assessment (MCIA) framework for NeuroGrid.

Its purpose is to ensure that any change to an AI model—technical, data-related, or operational—is:

Systematically assessed for safety, clinical, and regulatory impact

Evaluated before deployment

Traceable, auditable, and reversible where appropriate

Prevented from introducing silent risk into clinical workflows

No model change is considered “minor” in a clinical system.

---

# 2. Scope
This framework applies to all changes affecting:

AI models used in RPM or clinical decision support

Model parameters, architecture, or training procedures

Training, validation, or calibration datasets

Inference logic, thresholds, or confidence presentation

Deployment configuration or runtime environment

Both planned updates and emergency changes are in scope.

---

# 3. Core Principle
A change in behavior is a change in risk.
A change in risk requires justification.

Unassessed changes are prohibited.

---

# 4. Change Classification
All model changes must be classified into one of the following categories:

A. Administrative

Documentation updates

Metadata corrections

Registry annotations

B. Technical (Non-Behavioral)

Refactoring without output change

Infrastructure or performance optimizations

C. Technical (Behavioral)

Architecture modifications

Parameter updates

Retraining or fine-tuning

D. Data-Driven

New training data

Dataset expansion or filtering

Labeling methodology changes

E. Safety-Critical

Threshold adjustments

Alert logic changes

Confidence calibration updates

Classification determines assessment depth and approval requirements.

---

# 5. Mandatory Impact Dimensions
Each change must be assessed across the following dimensions:

Clinical safety

Model performance

Confidence calibration

Bias and equity impact

Data integrity

Workflow disruption

Regulatory classification

Explainability and transparency

Human oversight implications

All dimensions must be explicitly addressed.

---

# 6. Impact Severity Levels
Impact severity is rated as:

Level	Description
Low	No behavioral change
Moderate	Behavioral change without safety impact
High	Behavioral change with potential clinical impact
Critical	Direct patient safety or regulatory risk

Severity level determines escalation and approval path.

---

# 7. Assessment Artifacts
A completed MCIA must include:

Change description and rationale

Affected model identifiers and versions

Before/after performance comparison

Calibration impact analysis

Bias and subgroup impact review

Validation dataset references

Risk mitigation measures

Rollback plan

Incomplete assessments invalidate approval.

---

# 8. Review & Approval Flow
Low / Moderate Impact

Technical review

Compliance sign-off

Registry update

High Impact

Clinical expert review

Compliance approval

DAO notification or approval (if required)

Critical Impact

Safety Council review

Formal approval vote

Regulatory readiness check

No deployment occurs without required approvals.

---

# 9. Emergency Change Protocol
In declared emergencies:

Temporary changes may be deployed to mitigate immediate risk

Full MCIA must follow post hoc

Emergency changes are time-limited

Permanent adoption requires full reassessment

Emergency status does not waive accountability.

---

# 10. Registry & Traceability
All model changes must be registered with:

Unique change identifier

Impact classification and severity

Approval records

Effective dates

Superseded versions

Registry records are immutable.

---

# 11. Deployment Controls
Deployment of modified models must ensure:

Version isolation

Controlled rollout where applicable

Monitoring escalation during initial exposure

Immediate rollback capability

Silent or shadow deployment is prohibited.

---

# 12. Prohibited Practices
The following are forbidden:

Deploying changes without assessment

Downplaying impact severity

Combining multiple changes into unreviewable bundles

Bypassing clinical or compliance review

Retroactive justification of deployed changes

Violations constitute a system safety breach.

---

# 13. Audit & Inspection Readiness
MCIA records must be:

Retained indefinitely

Accessible for regulatory audit

Linked to safety and performance outcomes

Consistent with post-market surveillance findings

Gaps are treated as compliance failures.

---

# 14. Regulatory Alignment
This framework aligns with:

EU AI Act (Change management & post-market monitoring)

FDA GMLP (Model modification control)

ISO/IEC 62304 (Change control)

ISO 14971 (Risk management)

WHO AI lifecycle governance guidance

---

# 15. Ethical Position
Innovation without impact awareness is recklessness.
Control without transparency is negligence.

Every change must earn the right to exist.

# Status
Active – Mandatory Change Control Instrument
