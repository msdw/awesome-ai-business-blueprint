# AI Use Case Canvas

## Purpose

The AI Use Case Canvas structures the design of a specific AI-powered workflow. It forces clarity about what the AI actually does, what data it needs, what humans do, what good output looks like, and how failures are handled.

Use this canvas during Step 4 (AI Use Case Design) for every AI workflow in your product. If you have multiple AI steps in the same product, complete a separate canvas for each.

This canvas is also useful for evaluating whether AI is genuinely the right tool, or whether a simpler approach would work as well or better.

## How to Use

1. Describe one specific AI task per canvas — not the entire product.
2. Be concrete about inputs and outputs. Vague descriptions hide design problems.
3. Share with technical collaborators and potential customers to pressure-test the design.
4. Revisit after the MVP to update based on real performance.

---

## Canvas Template

| Section | Your Definition |
|---|---|
| **Workflow** | Which business process does this AI step belong to? |
| **Task** | What specific AI task is performed? (classification, generation, extraction, retrieval, summarization, etc.) |
| **Input Data** | What data goes in? Format, source, volume, freshness requirements. |
| **AI Role** | What does the AI do? (generate, rank, extract, translate, flag, suggest, etc.) |
| **Human Role** | What does a human do before, during, or after the AI step? |
| **Output** | What does the AI produce? What format? Where does it go? |
| **Quality Criteria** | What does good output look like? What is acceptable? What is unacceptable? |
| **Failure Modes** | How can the AI fail? What are the consequences of each failure mode? |
| **Risk Level** | Low / Medium / High — based on severity of consequences from errors |
| **Monitoring** | How will output quality be tracked in production? |
| **Evaluation** | How will the AI component be tested before and after deployment? |

---

## Risk Level Guide

| Level | Description |
|---|---|
| Low | Errors are annoying but easily corrected. No significant harm from failure. |
| Medium | Errors cause rework, cost, or reputation impact. Human review recommended. |
| High | Errors affect people's rights, health, finances, safety, or legal status. Human review required. |
