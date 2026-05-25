# Risk Assessment Template

## Purpose

This template helps you identify, assess, and plan mitigations for the key risks in your AI product or service. Complete this assessment before deploying to production and review it when significant changes occur.

Risk assessment is not about eliminating all risk. It is about identifying risks that could be fatal, harmful, or damaging, and putting proportional controls in place.

For high-stakes or regulated use cases, this template should be reviewed with legal counsel and domain experts.

---

## Risk Assessment

### Part 1 — Data Sensitivity

**What personal or sensitive data does the system process?**

| Data Type | Sensitivity Level | Applicable Regulation | Storage Location | Access Controls |
|---|---|---|---|---|
| | Low / Medium / High | GDPR / CCPA / HIPAA / Other | | |
| | | | | |

**Data handling summary:**

- Data is collected from: ___
- Data is stored at: ___
- Data is retained for: ___
- Data is deleted when: ___
- Who has access: ___

---

### Part 2 — Output Criticality

**What decisions or actions depend on the AI output?**

| Output | Used For | Stakes if Wrong | Human Review Required |
|---|---|---|---|
| | | Low / Medium / High / Critical | Yes / No |
| | | | |

---

### Part 3 — Legal and Regulatory Domain

**Which regulatory domains apply to this use case?**

- [ ] General data protection (GDPR, CCPA)
- [ ] Healthcare (HIPAA, MDR)
- [ ] Finance (MiFID, PSD2, SEC rules)
- [ ] Employment (EEOC, local labor law)
- [ ] Legal (unauthorized practice of law concerns)
- [ ] Education
- [ ] Public services
- [ ] AI-specific regulation (EU AI Act)
- [ ] None identified

**Compliance notes:**

[Write here: specific requirements and current compliance status]

---

### Part 4 — Security Controls

| Control | Status | Notes |
|---|---|---|
| Authentication | [ ] In place [ ] Planned [ ] Not applicable | |
| Access control (role-based) | [ ] In place [ ] Planned [ ] Not applicable | |
| Data encryption in transit | [ ] In place [ ] Planned [ ] Not applicable | |
| Data encryption at rest | [ ] In place [ ] Planned [ ] Not applicable | |
| Audit logging | [ ] In place [ ] Planned [ ] Not applicable | |
| Prompt injection protection | [ ] In place [ ] Planned [ ] Not applicable | |
| Rate limiting | [ ] In place [ ] Planned [ ] Not applicable | |

---

### Part 5 — Risk Register

| # | Risk | Category | Probability | Impact | Mitigation | Owner |
|---|---|---|---|---|---|---|
| 1 | | Technical | Low / Med / High | Low / Med / High | | |
| 2 | | Market | | | | |
| 3 | | Legal | | | | |
| 4 | | Privacy | | | | |
| 5 | | Operational | | | | |
| 6 | | | | | | |
| 7 | | | | | | |

---

### Part 6 — Human Oversight Plan

**Outputs requiring human review before action:**

| Output | Review Frequency | Reviewer Role | Override Authority |
|---|---|---|---|
| | Every output / Sampled / Flagged | | Yes / No |
| | | | |

---

### Part 7 — Evaluation Plan

**How AI output quality will be measured:**

| Method | Frequency | Threshold for Alert |
|---|---|---|
| Manual spot check | | |
| Automated quality metric | | |
| Customer feedback review | | |

---

### Part 8 — Incident Response

**What happens if the system produces harmful or incorrect output?**

1. Detection: Who identifies the issue and how?
2. Containment: How is the system paused or the output corrected?
3. Notification: Who is notified, and when?
4. Root cause: How is the root cause identified?
5. Resolution: How is the issue fixed and verified?
6. Documentation: Where is the incident recorded?

**Incident response contact:** ___

**Escalation path:** ___
