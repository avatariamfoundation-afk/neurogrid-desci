# DATA_RETENTION_AND_ARCHIVAL_POLICY.md

## 1. PURPOSE
This policy defines mandatory requirements for the retention, archival, and secure disposal of all data assets within the DeSci repository, ensuring regulatory compliance, scientific integrity, auditability, and long-term research reproducibility.

## 2. SCOPE
This policy applies to:
- Clinical data
- Research datasets
- AI training and validation data
- Model outputs and inference logs
- Governance, DAO, and decision records
- Audit logs and compliance artifacts

## 3. DATA CLASSIFICATION
All data must be classified prior to retention determination:

- **Critical Regulated Data**: Clinical, patient-related, or regulated biomedical data
- **Scientific Research Data**: Experimental, observational, and derived datasets
- **AI Lifecycle Data**: Training, testing, calibration, and performance data
- **Governance Records**: DAO decisions, policy changes, approvals
- **Operational Metadata**: Logs, telemetry, and system records

## 4. RETENTION REQUIREMENTS

### 4.1 Minimum Retention Periods
- Critical Regulated Data: **Minimum 10 years**
- Scientific Research Data: **Minimum 7 years**
- AI Lifecycle Data: **Minimum 7 years**
- Governance Records: **Permanent**
- Operational Metadata: **Minimum 3 years**

Retention periods may be extended where required by jurisdictional regulation, ongoing litigation, or scientific reproducibility needs.

### 4.2 Retention Clock Initiation
Retention periods begin from the latest of:
- Data creation date
- Last active use in a validated study or model
- Regulatory submission or approval date

## 5. ARCHIVAL REQUIREMENTS

### 5.1 Archival Eligibility
Data eligible for archival must:
- Be inactive for operational use
- Retain scientific, regulatory, or historical value
- Be verified for integrity prior to archival

### 5.2 Archival Standards
Archived data must:
- Be immutable (write-once)
- Maintain cryptographic integrity hashes
- Retain full provenance and lineage metadata
- Be encrypted at rest and in transit
- Support controlled retrieval for audits and replication

### 5.3 Storage Separation
Archived data must be stored separately from active systems to reduce exposure and operational risk.

## 6. ACCESS CONTROL
- Archived data access is restricted to authorized governance, compliance, or audit roles
- All access events must be logged and retained permanently
- Retrieval actions require documented justification

## 7. DATA DISPOSAL
Upon expiration of retention obligations:
- Data must be securely erased using verifiable destruction methods
- Disposal actions must be logged and auditable
- Disposal must not violate any active regulatory, legal, or scientific holds

## 8. HOLDS AND EXCEPTIONS
Retention suspension applies when data is subject to:
- Regulatory investigation
- Legal proceedings
- Active scientific replication or dispute

Holds must be documented and reviewed periodically.

## 9. GOVERNANCE AND OVERSIGHT
- This policy is governed by the DAO governance framework
- Amendments require formal approval and version control
- Compliance is reviewed annually or upon regulatory change

## 10. ENFORCEMENT
Failure to comply with this policy may result in:
- Access revocation
- Governance sanctions
- Regulatory escalation where applicable

## 11. VERSION CONTROL
All versions of this policy must be retained permanently with full change history.

---
**Status:** Enforced  
**Applies To:** All DeSci Data Assets  

