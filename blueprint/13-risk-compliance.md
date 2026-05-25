# Step 13 — Risk and Compliance

## Overview

Risk and compliance is the step where you identify, assess, and plan mitigations for the key risks facing your AI business. These risks span technical, market, legal, privacy, security, and operational dimensions.

AI businesses carry a specific set of risks that traditional software businesses do not: outputs can be incorrect in consequential ways, data handled in training or inference may be sensitive, regulatory frameworks are evolving rapidly, and dependence on third-party model providers creates concentration risk.

Addressing risk is not about preventing all failure — it is about identifying the risks that could be fatal or damaging and putting proportional controls in place.

## Key Questions to Answer

- What are the top 3 technical risks? (model failure, data quality, API dependency, hallucination)
- What are the top 3 market risks? (competitor response, churn, pricing pressure, buyer procurement delays)
- Are there compliance or regulatory requirements applicable to this use case or industry?
- What is the plan if the primary LLM API provider changes pricing, terms, or availability?
- What personal or sensitive data is processed? Under which legal framework?
- What happens when the AI produces incorrect output in a high-stakes context?

## Core Activities

1. **Build a risk register**: List the top 10 risks across technical, market, legal, privacy, and operational dimensions. For each risk, assess the probability, the potential impact, and the mitigation plan.
2. **Classify compliance requirements**: Determine which regulations apply based on your geography, the customer's geography, the industry, and the data types processed. Common frameworks include GDPR, CCPA, HIPAA, and AI-specific regulations.
3. **Define human oversight requirements**: For any output used in decisions affecting people, specify who reviews the output and what authority they have to override or reject it.
4. **Plan for model provider risk**: Document your plan if your primary LLM provider becomes unavailable, changes pricing significantly, or modifies their terms of service.
5. **Establish data handling policies**: Specify what data is collected, how it is stored, how long it is retained, and who has access.
6. **Define an incident response plan**: Identify what you will do if the system produces harmful output, if there is a data breach, or if a key component fails.

## Common Mistakes

- **Deploying in regulated domains without appropriate review**: Healthcare, finance, legal, and employment domains have specific requirements that must be addressed before production use.
- **No contingency plan for API price increases**: Several AI providers have raised prices significantly. A business with no alternative provider is exposed to margin destruction.
- **Not monitoring AI output quality in production**: Output quality can degrade as context changes. Monitoring is a business requirement, not an optional feature.
- **Treating compliance as a one-time task**: Regulations evolve. Compliance is an ongoing responsibility.
- **Ignoring bias risk**: AI systems can produce systematically biased outputs. In hiring, lending, healthcare, or public services, this creates legal and ethical exposure.

## Deliverables

- **Risk register**: A table of the top 10 risks with probability, impact, and mitigation for each.
- **Compliance checklist**: A list of applicable regulations and your current compliance status for each.
- **Human oversight plan**: A description of which outputs require human review and the authority structure for overrides.
- **Data handling plan**: Documentation of what data is collected, how it is stored, and who can access it.
- **Incident response basics**: A short plan for what to do if the system fails, produces harmful output, or is involved in a data breach.

## Related Templates

- `templates/risk-assessment.md`
- `templates/delivery-checklist.md`
