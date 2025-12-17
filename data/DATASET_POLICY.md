# NeuroGrid DeSci Registry — Dataset Policy

## 1. Purpose

This document defines what constitutes a *dataset* within the NeuroGrid DeSci Registry and establishes the rules governing dataset registration, reference, usage, and attribution.

The registry does **not** store datasets. It stores cryptographic attestations and metadata that describe datasets, their provenance, and the ethical constraints under which they may be used.

---

## 2. Definition of a Dataset

Within NeuroGrid, a dataset is defined as:

> A structured or semi-structured collection of biomedical, clinical, research, or derived analytical data intended for scientific, clinical, or AI-related use.

This includes, but is not limited to:

* Post-operative monitoring outputs
* Anonymized clinical observations
* Research cohort datasets
* AI training or validation datasets
* Derived datasets produced from prior registered datasets

Raw patient-identifiable data **must never** be registered.

---

## 3. Registry Representation

Each dataset registered in the DeSci Registry must be represented by:

* A **cryptographic hash** of the dataset or dataset manifest
* A **dataset identifier** (human-readable reference)
* A **provenance declaration**
* A **usage policy reference**
* Optional linkage to parent datasets or models

The registry functions as a *ledger of claims*, not a data warehouse.

---

## 4. Provenance Requirements

All dataset registrations must declare:

* Origin of the data (clinical, research, simulated, derived)
* Method of collection or generation
* Responsible registering entity or contributor
* Whether the dataset is original or derivative

False or misleading provenance declarations constitute a registry violation.

---

## 5. Ethical Constraints

Registered datasets must comply with the following baseline principles:

* No direct personal identifiers
* No attempt to re-identify individuals
* No deceptive consent framing
* No unauthorized cross-context reuse

Ethical validation is declarative at registration time and auditable post hoc.

---

## 6. Usage Policies

Each dataset must reference a usage policy that specifies:

* Permitted use cases (research, validation, clinical support, AI training)
* Prohibited uses
* Commercial vs non-commercial allowances
* Attribution requirements

Usage policies are immutable once registered.

---

## 7. Derivative Datasets

Datasets derived from registered datasets must:

* Reference parent dataset identifiers
* Declare transformation methods
* Inherit baseline ethical constraints

Derivative datasets may impose additional restrictions but may not weaken inherited ones.

---

## 8. Revocation and Disputes

Datasets cannot be deleted from the registry.

In cases of dispute or ethical breach:

* A status flag may be applied
* Usage warnings may be attached
* Governance processes may be triggered

Historical records remain intact for auditability.

---

## 9. Separation from Core Contracts

Dataset registration and policy enforcement are **off-chain governance concerns**.

Core smart contracts reference registry entries by identifier or hash but do not validate dataset contents or ethics.

This separation preserves system integrity and jurisdictional neutrality.

---

## 10. Final Principle

> The registry records responsibility, not possession.

Ownership of data remains with its lawful custodian. NeuroGrid records only the claim that a dataset exists and the conditions under which it may be ethically referenced.

