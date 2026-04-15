---
name: launch-docs
description: "Creates and updates feature launch documents: Deploy Briefing, Complete Documentation, FAQ, and Release Notes. Use when the user says 'create deploy briefing', 'release notes', 'document a launch', 'feature documentation', 'feature FAQ', 'prepare deploy communication'. Do NOT use to create initiative PR/FAQs — use prfaq-writer. Do NOT use for recurring stakeholder updates — use storytelling."
---

# launch-docs

Router for the `launch-writer` agent. Identifies the initiative and the document(s) to create, then escalates to the agent with context.

## When to Use

- "create deploy briefing"
- "release notes for [feature]"
- "document a launch for [feature]"
- "feature FAQ"
- "prepare feature documentation"
- "launch documents"
- "prepare deploy communication"

## Workflow

### 1. Identify the initiative

Use Glob to locate automatically:
```
Glob Initiatives/Actives/**
```

If the initiative name came in the arguments, filter by the closest match. If it did not come, or if no clear match was found:

```
AskUserQuestion:
  question: "What is the initiative or feature you want to document for launch?"
  type: text
```

### 2. Identify the document(s) to create

If the document type came explicitly in the arguments, escalate directly to the agent without asking.

If it did not come:

```
AskUserQuestion:
  question: "Which launch document do you want to create or update?"
  options:
    - "Deploy Briefing — pre-deploy gate (technical team + PMs)"
    - "Complete Documentation — source of truth for the feature (internal reference)"
    - "FAQ — frequently asked questions about the feature (multiple teams)"
    - "Release Notes — launch communication (support, ops, stakeholders)"
    - "All — create the complete launch set"
  type: select
```

### 3. Escalate to the agent

With initiative and document type defined, escalate to `launch-writer`:

```
Agent:
  subagent_type: launch-writer
  description: "launch documents — [initiative name]"
  prompt: |
    Create [document type(s)] for the initiative: [initiative name]
    Initiative folder: [path found via Glob, or "not found — verify"]
    Additional context provided by the user: [original arguments, if any]
```

Do not execute document creation in this skill — delegate entirely to the agent.
