---
name: research-feedback
description: |
  Adds a structured entry to the workspace feedback log. Captures a literal customer quote
  with metadata (source, date, signal type, persona, tags, related initiative) and
  auto-increments the entry ID.

  Triggers: "add feedback", "log customer quote", "new feedback entry",
  "add a customer comment", "log NPS comment", "feedback from [channel]"

  Do NOT use to log a full interview — use research-interview instead.
  Do NOT use to synthesize existing feedback — use synthesize-research instead.
---

# research-feedback

Adds a new structured entry to `{workspace}/research/feedback-log.md`.

## When to Use

- "add customer feedback"
- "log a customer comment"
- "quote for the feedback log"
- "log NPS / CS / support comment"
- "new feedback about [topic]"

## Workflow

### 1. Collect information

Ask using `AskUserQuestion` — one question at a time, only for what was not provided:

**Open fields:**
- The exact quote (literal — never paraphrase)
- Company or account (name or anonymous ID)
- Date (approximate if needed)
- Topic tags: free-form tags in `[UPPERCASE-TAG]` format — check existing tags in the feedback log before creating new ones

**Select fields** — call `AskUserQuestion` for each (one at a time):

**Channel:**
- question: "What channel did this feedback come from?"
- options: ["NPS survey", "Customer Success / CS call", "Support ticket", "Qualitative interview", "User research session", "Other — I'll describe it"]
- type: select

**Signal type:**
- question: "What type of signal is this?"
- options: ["Pain / frustration", "Suggestion / feature request", "Praise / positive signal", "Unmet expectation"]
- type: select

**Persona:**
- question: "What is the customer persona?"
- options: ["End user", "Buyer / decision-maker", "Admin / operator", "Partner / integrator", "Other — I'll describe it"]
- type: select

**Related initiative** (open field — or "—" if none)

### 2. Read the feedback log to determine the next ID

```
Read {workspace}/research/feedback-log.md
```
- Find the last `[FEEDBACK-NNN]` entry and increment by one.
- If the file does not exist yet, start at `[FEEDBACK-001]`.

### 3. Determine PR/FAQ visibility

Call `AskUserQuestion` with:
- question: "Can this feedback appear in a PR/FAQ or public-facing document?"
- options: ["Yes", "No", "Check later"]
- type: select

### 4. Build the entry block

```markdown
---

### [FEEDBACK-NNN]

| Field | Value |
|---|---|
| **Date** | [date or REQUIRED DATA] |
| **Channel** | [channel] |
| **Company** | [company or anonymous ID] |
| **Contact** | [generic role label — no names] |
| **Persona** | [persona] |
| **Topic** | [tags] |
| **Related initiative** | [initiative or —] |
| **PR/FAQ visible** | Yes / No / Check later |

**Quote:**
> "[literal quote]"

**Signal:** [signal type]
```

### 5. Append to the file

Insert the block:
- Before the "## Recurring Signals — Summary" section (if it exists), or
- At the end of the existing entries.

### 6. Confirm

Inform the user of the entry ID created and the file path.

## Absolute Rules

- NEVER invent or paraphrase quotes without explicitly marking as "(paraphrase)".
- If the exact context is unknown, write `[UNKNOWN CONTEXT]` — do not invent.
- People's names do not appear — use generic role labels.
- Quotes from this log always take priority over invented customer voice in PR/FAQs.

## When NOT to Use

- For quantitative data signals (analytics, SQL queries) — use the data-research skill.
- To synthesize multiple feedback entries — use synthesize-research.

## Output

New entry `[FEEDBACK-NNN]` appended to `{workspace}/research/feedback-log.md`.
