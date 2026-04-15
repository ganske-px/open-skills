---
name: ideation
description: Generate solutions for a problem using structured brainstorming, hidden-face analysis, and decision-making. Use when the user says "brainstorm solutions", "how to solve X", "ideate solutions for X", "what alternatives do we have", "explore solutions for", "I want to think through solutions", "help me solve", or "what can we do about". Supports pre-mortem, 5 Whys, stakeholder perspectives, and second-order effects. Do NOT use when the problem is still unclear and needs discovery first. Do NOT use to decide between already-defined solutions — use product-decision instead.
---

# Ideation — Router Skill

Escalates immediately to the `ideation-agent`, which runs structured brainstorming with deep reasoning about the problem before any output.

## How to escalate

Collect minimum context if not already clear in the request, **one question at a time**.

**If the problem is not described:** call the `AskUserQuestion` tool now with:
- question: "What is the problem you want to solve?"
- type: text (open field)

**If the innovation level is not clear:** call the `AskUserQuestion` tool now with:
- question: "What level of innovation are you targeting?"
- options: ["Incremental — improvement over what already exists", "Disruptive — rethink from scratch", "Both — explore both extremes"]
- type: select

**IMPORTANT:** Call the `AskUserQuestion` tool — do not write the question as plain text. If you don't call the tool, the user cannot select options interactively.

If both the problem and innovation level are already clear in the request, escalate directly without asking.

**To escalate:** use the Agent tool with:
- subagent_type: "ideation-agent"
- description: "ideation session about [problem]"
- prompt: "[problem + innovation level + constraints + persona, as available from the request]"

Never process the ideation in this skill — always delegate to the agent.
