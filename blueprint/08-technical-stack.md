# Step 8 — Technical Stack

## Overview

Technical stack selection is the step where you choose the simplest architecture that allows you to ship the MVP within the target timeframe. The primary objective is not to choose the best or most scalable technology — it is to choose the technology you can deliver with confidently, at a cost you can sustain, within the time available.

Many AI projects stall because builders spend weeks evaluating competing technologies rather than building. The discipline of this step is to make a defensible decision quickly and move on.

## Key Questions to Answer

- Which LLM or AI API best fits the use case in terms of capability, cost, and reliability?
- What is the hosting and deployment strategy for the MVP?
- How will data be stored and accessed?
- What third-party integrations are required?
- What is the estimated cost of running this system at 10 users, 100 users, and 1,000 users?
- What are the privacy and security requirements for the data being processed?

## Core Activities

1. **Choose the AI model or API**: Evaluate options such as OpenAI, Anthropic, Google, Mistral, or open-source models. Consider cost per token, context window, quality, latency, and terms of service.
2. **Select the application framework**: Choose a framework or approach appropriate to the use case — web app, API, automation workflow, or CLI.
3. **Define the data architecture**: Determine how data is ingested, stored, processed, and retrieved. For RAG-based systems, evaluate vector databases.
4. **Identify required integrations**: List every external service the MVP must connect to (CRMs, email, document storage, authentication providers).
5. **Estimate infrastructure costs**: Calculate the monthly cost to run the system at expected early-stage usage volumes.
6. **Define security controls**: Identify the minimum security requirements: authentication, access control, data encryption, and audit logging.

## Common Mistakes

- **Over-engineering before validating demand**: A complex architecture is a liability at the MVP stage. Build simple, validate fast.
- **Choosing unfamiliar technologies to learn while building**: The MVP stage is not the time for learning new programming languages or frameworks. Use what you know.
- **Not estimating LLM API costs at scale**: Inference costs can be significant. A single use case that costs $0.01 per request becomes $10,000/month at 1 million requests.
- **Ignoring data privacy requirements**: Processing customer data without appropriate controls can create legal liability. Understand the applicable regulations before processing real data.
- **Treating architecture as permanent**: The MVP architecture will be replaced. Do not over-invest in components that will change.

## Deliverables

- **Tech stack decision**: A one-page summary of the chosen technologies with rationale.
- **Architecture diagram**: A simple box diagram showing the main components and data flows.
- **Cost estimate**: Monthly infrastructure cost at 10, 100, and 1,000 active users.
- **Integration list**: All external services required with notes on complexity and data access.
- **Security baseline**: Minimum security controls in place for the MVP.

## Related Templates

- `templates/mvp-specification.md`
- `templates/risk-assessment.md`
