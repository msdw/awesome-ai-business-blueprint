# AI Risk Canvas

## Purpose

The AI Risk Canvas structures the identification and mitigation of key risks in an AI-powered product or service. AI systems carry specific risks that traditional software does not: outputs can be incorrect in consequential ways, data handled may be sensitive, and regulatory frameworks are still evolving.

Use this canvas during Step 13 (Risk and Compliance) and revisit it when entering new customer segments, processing new data types, or deploying in new regulatory jurisdictions.

Risk assessment is not a one-time task. It should be reviewed when the product, customer base, or regulatory environment changes significantly.

## How to Use

1. Fill in every section honestly. Unknown risk is not the same as no risk.
2. Identify the highest-risk cells and build specific mitigations.
3. For high-risk use cases, involve legal counsel and domain experts.
4. Share with customers in regulated industries before deployment.

---

## Canvas Template

| Section | Your Assessment |
|---|---|
| **Data Sensitivity** | What personal, confidential, or regulated data does the system process? (PII, financial, health, legal) |
| **Output Risk** | What are the consequences of an incorrect output? (annoyance / financial loss / legal liability / safety risk) |
| **User Impact** | Who is affected by the AI output? Are they aware it is AI-generated? |
| **Regulatory Exposure** | Which regulations apply? (GDPR, CCPA, HIPAA, EU AI Act, sector-specific regulations) |
| **Security Concerns** | What are the attack surfaces? (prompt injection, data exfiltration, unauthorized access) |
| **Bias Risk** | Could the system produce systematically unfair or discriminatory outputs? For which groups? |
| **Hallucination Risk** | How often might the system produce confident but incorrect outputs? What is the consequence? |
| **Human Review** | Which outputs require human review before action? Who performs the review? What authority do they have? |
| **Audit Trail** | What is logged? Can decisions be explained and traced? Is the log tamper-resistant? |
| **Mitigation Plan** | For each high-risk cell, what specific control or process mitigates the risk? |

---

## Risk Severity Guide

| Severity | Indicator |
|---|---|
| Low | Errors are visible, easily corrected, and have no significant downstream harm |
| Medium | Errors cause rework, cost, reputational damage, or customer dissatisfaction |
| High | Errors affect individual rights, financial outcomes, health, safety, or legal status |
| Critical | Errors are irreversible or cause systemic harm to multiple people |
