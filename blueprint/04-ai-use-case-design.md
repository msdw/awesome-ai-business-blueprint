# Step 4 — AI Use Case Design

## Overview

AI use case design is the step where you define specifically what the AI does in the solution — the input, the task, the output, and the role of humans in the loop. This step prevents the common pattern of using AI because it feels powerful rather than because it meaningfully improves the workflow.

Not every problem requires AI. A rule-based system, a spreadsheet, or a well-designed form may solve the problem more reliably and at lower cost. The discipline of this step is to justify AI on merit: does it genuinely improve speed, quality, consistency, or capability compared to alternatives?

## Key Questions to Answer

- What specific AI task is being performed? (classification, generation, extraction, search, summarization, recommendation, etc.)
- What is the input data? Where does it come from? Is it available in sufficient quantity and quality?
- What is the expected output? What does "good output" look like, and how will it be evaluated?
- Why is AI better than a simpler rule-based or manual approach for this task?
- What are the most likely failure modes? How will errors be detected and handled?
- What is the role of a human in the loop? When is human review required?
- What are the privacy, security, and compliance considerations for the data involved?

## Core Activities

1. **Define the AI task type**: Choose from generation, classification, extraction, retrieval, summarization, translation, recommendation, anomaly detection, or a combination.
2. **Map the workflow**: Draw a simple diagram: input → processing → AI step → human review (if applicable) → output → action.
3. **Identify data requirements**: List the data sources, formats, volume, freshness requirements, and access constraints.
4. **Define quality criteria**: Write down what a correct, acceptable, and unacceptable output looks like.
5. **Identify failure modes**: List the ways the AI can fail and how each failure would affect the user or the business.
6. **Define human oversight requirements**: Determine which outputs need human review before use, especially in high-stakes contexts.
7. **Classify risk level**: Rate the use case as low, medium, or high risk based on the severity of consequences from errors.

## Common Mistakes

- **Using AI where a simpler solution would work better**: If the logic is fully deterministic and rule-based, a workflow tool or spreadsheet may be more reliable than an LLM.
- **Not defining what "good output" looks like**: Without an evaluation standard, quality cannot be measured or improved.
- **Ignoring hallucination and error handling**: LLMs produce incorrect outputs. Every production use case needs a strategy for detecting and managing errors.
- **Skipping the human review requirement in high-stakes domains**: Medical, legal, financial, and safety-critical outputs require human review before action.
- **Treating data availability as guaranteed**: Data that exists in theory may not be accessible, clean, or structured in practice.
- **Underestimating evaluation complexity**: Evaluating generative outputs requires effort and cannot be fully automated.

## Deliverables

- **AI use case description**: A one-paragraph summary of the workflow: input → AI task → output → human action.
- **Data requirements**: A list of data sources, formats, volume estimates, and access notes.
- **Failure mode analysis**: A table of likely failure modes, their consequences, and planned mitigations.
- **Quality criteria**: Written definition of what acceptable output looks like for this use case.
- **Risk classification**: Low / Medium / High with rationale and human oversight requirements.

## Related Templates

- `templates/mvp-specification.md`
- `templates/risk-assessment.md`
