# RPM_CLINICAL_OVERRIDE_LOGIC.md
**Human-in-the-Loop Clinical Override Control Framework**

---

## 1. Purpose

This document defines the **mandatory clinical override logic** governing all Remote Patient Monitoring (RPM) systems within the NeuroGrid ecosystem.

Its objective is to:
- Preserve clinician authority over AI outputs
- Prevent unsafe automation
- Ensure patient safety during uncertainty
- Protect clinicians from retaliation when overriding AI

Clinical judgment is **superseding authority**, not an exception path.

---

## 2. Scope

This framework applies to:
- All RPM alerting systems
- All AI-assisted risk stratification models
- All automated monitoring workflows
- All NeuroGrid RPM deployments

It is binding across **MedIntel execution**, **DeSci governance**, and **Core audit layers**.

---

## 3. Core Override Principles

Clinical override logic is governed by the following principles:

1. **Human Supremacy** – Clinicians always outrank AI outputs  
2. **Non-Penalization** – Overrides carry no negative consequences  
3. **Immediate Effect** – Overrides take effect instantly  
4. **Auditability** – All overrides are logged and reviewable  
5. **Reversibility** – Overrides may be revised by clinicians only  

---

## 4. Override Authority

Override authority is granted to:
- Licensed clinicians assigned to the patient
- On-call clinical supervisors
- Emergency clinical response teams

The following are explicitly prohibited from overriding:
- DAO members
- Token holders
- AI system operators without clinical credentials
- Automated agents

---

## 5. Override Trigger Conditions

Clinicians may override RPM outputs when:
- AI alerts conflict with clinical assessment
- Contextual patient information is missing
- Device data integrity is questionable
- Patient-reported symptoms contradict model outputs
- Ethical or safety concerns arise

No justification threshold is required for emergency overrides.

---

## 6. Override Actions

Permitted override actions include:
- Risk tier reassignment
- Alert suppression
- Alert escalation
- Monitoring frequency adjustment
- Temporary model bypass
- Manual intervention initiation

Overrides may be time-bound or indefinite, as defined by the clinician.

---

## 7. Override Execution Logic

Upon override:
1. AI outputs are suspended or superseded
2. Human-defined parameters take precedence
3. Alert routing updates immediately
4. Monitoring continues under override conditions
5. System prevents automatic rollback

No automated system may reverse an override without human authorization.

---

## 8. Mandatory Override Logging

Each override event must record:
- Clinician identifier (pseudonymous allowed)
- Patient pseudonymous ID
- Timestamp
- Affected system components
- Override type
- Duration (if time-bound)
- Optional clinical rationale

Lack of rationale does not invalidate an override.

---

## 9. Override Safeguards

The system must enforce:
- Override persistence across model updates
- Protection from alert re-triggering loops
- Lockout prevention during emergencies
- Conflict detection between overrides and automation

Override logic must fail **open to safety**, not automation.

---

## 10. Abuse Prevention Controls

To prevent misuse without restricting safety:
- Pattern-based review (not real-time blocking)
- Post-hoc audit sampling
- Peer clinical review only
- No automated penalties

Override frequency alone is not evidence of abuse.

---

## 11. Audit & Review

Override activity is subject to:
- Periodic clinical safety review
- Ethics committee oversight
- Regulatory audit access

Audits focus on **system improvement**, not clinician discipline.

---

## 12. Regulatory Alignment

This framework aligns with:
- FDA human-in-the-loop guidance
- EU AI Act human oversight requirements
- ISO 62304 clinical software safety
- ISO 14971 risk management
- WHO AI ethics in healthcare

---

## 13. Ethical Position

> **When machines hesitate, humans decide.  
> When machines err, humans intervene.**

Clinical authority is non-negotiable.

---

## 14. Binding Status

This document is:
- Mandatory across all RPM implementations
- Enforced via system architecture
- Protected by governance policy
- Amendable only through compliant governance processes

---

### Status
**Active – RPM Clinical Override Logic Framework**

