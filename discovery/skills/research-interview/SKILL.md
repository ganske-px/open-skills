---
name: research-interview
description: |
  Logs a completed qualitative interview using the CDH Timeline Interview format
  combined with JTBD Forces of Progress. Produces a structured interview file
  that connects directly to the opportunity tree and PR/FAQ customer voice sections.

  Triggers: "log an interview", "I did an interview about X",
  "transcribe interview", "log a research session", "interview notes"

  Do NOT use to plan future research — use research-plan instead.
  Do NOT use to add a single isolated feedback quote — use research-feedback instead.
---

# research-interview

Creates a new interview transcript / notes file in `{workspace}/research/interviews/`.

## When to Use

- "log an interview"
- "I did an interview with [role/company]"
- "transcribe interview about [topic]"
- "log a research session"
- "interview notes for [topic]"

## Workflow

### 1. Collect minimum information

Ask the user using `AskUserQuestion` — one question at a time, only for what was not provided:

**Open fields:**
- Participant code / label (anonymized — role, never full name)
- Company (name or anonymous ID)
- Interview date
- Related research plan (or "Exploratory")
- Related initiative

**Select field** — call `AskUserQuestion` with:
- question: "Was the interview recorded?"
- options: ["Yes — I have a recording or transcript", "No — these are memory notes"]
- type: select

### 2. Determine the file name

- Format: `INTERVIEW-[PARTICIPANT-CODE]-[YYYY-MM-DD].md`
- Example: `INTERVIEW-ops-manager-co-42-2026-04-15.md`

### 3. Create the file

Create `{workspace}/research/interviews/INTERVIEW-[code]-[date].md`.

- Fill in the header with the collected data.
- If the user provided interview content, structure it in **Timeline Interview** format (see section below).
- Explicitly capture Forces of Progress and a Job Statement candidate when identifiable.
- If no content was provided, leave the block structure ready for the user to fill in.

### 4. Connect to the opportunity tree

If there is an active OST related to the topic:
- Identify which opportunity in the tree this interview illuminates.
- Check if a new opportunity emerged that is not yet in the tree.
- Mark both in Block 5 (Insights and OST Connection) for follow-up via the OST update skill.

### 5. Identify quotes for the feedback log

At the end, ask:
- "Does this interview have any quotes that should go into the feedback log?"
- If yes: run the research-feedback skill flow for each quote.

### 6. Confirm

Inform the user of the file path created.

---

## Interview Structure — Timeline Interview (CDH + JTBD)

Interviews follow the **Timeline Interview** model from Continuous Discovery Habits (Teresa Torres),
integrated with the **JTBD** Forces of Progress framework. The goal is not to understand the
customer's routine — it is to chronologically reconstruct the "hiring or firing" event of a
solution, capturing the underlying job.

### Mandatory Blocks

**Block 1 — Participant Context**
- Role and main responsibilities
- Current tools or processes for the topic under research
- How long they have been in the role or using the current solution

**Block 2 — Event Timeline**
- "When did you first realize you needed to solve this?"
- "What happened that made this problem feel urgent?"
- "What did you try before arriving at the current solution?"
- "Walk me through the steps that led you to choose what you use today."

**Block 3 — Forces of Progress (JTBD)**
- **Push** (frustration with the current): "What bothers you most about how you solve this today?"
- **Pull** (attraction toward change): "What would make you consider switching to something different?"
- **Anxiety** (fear of change): "What concerns you about switching solutions?"
- **Habit** (inertia): "What keeps you sticking with what you have, even with the pain points?"

**Block 4 — Job Statement Candidate**

Build from the previous blocks:
`When [circumstance from Block 2] → I want to [progress identified] → so I can [outcome from Block 3]`

**Block 5 — Insights and OST Connection**
- Which opportunity in the active OST does this interview illuminate? (if OST exists)
- Did any new opportunity emerge that is not yet in the tree?
- Does this interview validate or contradict any solution hypothesis?

### End Goal

Every interview should enrich the initiative context: quotes for the PR/FAQ (resolving
`[NO CUSTOMER VOICE]` markers), job statements for the OST, and Forces of Progress to support
solution choices. An interview with no explicit connection to an OST or PR/FAQ is lost data.

---

## Rules

- Quotes are LITERAL. Never paraphrase without marking as "(paraphrase)".
- If not recorded: mark as "Memory notes — may contain inaccuracies."
- Separate facts from interpretations — keep them in distinct sections.
- One file per session. Never mix multiple interviews.
- People's names do not appear — use generic role labels.

## Output

File created at `{workspace}/research/interviews/INTERVIEW-[code]-[date].md`.
