---
name: synthesize-research
description: |
  Synthesizes qualitative research — interviews, feedback log entries, and research notes —
  into structured insights organized by theme. Maps themes to the opportunity tree (OST)
  and surfaces customer-language evidence ready for PR/FAQ or initiative documents.

  Triggers: "synthesize research", "what do the interviews tell us about X",
  "research synthesis for X", "what are customers saying about X",
  "consolidate feedback", "extract themes from interviews",
  "fill in the customer voice section", "insights for the OST"

  Do NOT use for external web or market research — use web-search instead.
  Do NOT use to log a new interview — use research-interview instead.
---

# synthesize-research

Synthesizes local qualitative research into structured insights, connecting directly
to the opportunity tree and initiative documents.

## Sources

| Source | Path | Content |
|---|---|---|
| Feedback log | `{workspace}/research/feedback-log.md` | Structured quotes with tags and channel |
| Interviews | `{workspace}/research/interviews/INTERVIEW-*.md` | Timeline Interview transcripts (Blocks 1–5) |
| Extracted JTBD | `{workspace}/research/jtbd/` | Processed job statements |
| Research plans | `{workspace}/research/plans/PLAN-*.md` | Research context and hypotheses |

## When to Use

- "synthesize research on [topic]"
- "what are customers saying about [topic]"
- "consolidate feedback from [period / initiative]"
- "extract themes from the interviews"
- "which pain points come up most in the feedback"
- "insights for the OST of [outcome]"
- "fill in [NO CUSTOMER VOICE] in the PR/FAQ"

## Workflow

### 1. Collect material

Read sources relevant to the topic:
- Feedback log — filter by tag or related initiative
- Interview files — focus on Block 3 (Forces of Progress) and Block 4 (Job Statement)
- If there is an active OST: read it to understand which opportunities are already mapped
- If JTBD has been extracted: use as a starting point for job statements

### 2. Identify themes

Group quotes and observations by emerging theme. **Do not start from pre-defined
categories** — let the themes emerge from the data.

For each theme identified:
- **Name in customer language** (not product language — not "improve registration" but "I can't tell if a provider is still active")
- Frequency: how many independent sources mention it
- Intensity: level of frustration or urgency expressed (High / Medium / Low)
- Representative quotes (literal, with feedback ID or interview code)
- Associated Forces of Progress: Push / Pull / Anxiety / Habit

### 3. Map to the opportunity tree (OST)

For each theme identified:
- **Already exists as an opportunity in the OST?** → add evidence to the existing opportunity
- **Not in the OST?** → flag as a new candidate opportunity
- **Contradicts an OST opportunity?** → mark as a tension — investigate before discarding

### 4. Produce the synthesis document

```markdown
## Synthesis: [General Topic]

Date: [date]
Sources analyzed: [N feedback entries, M interviews]
Related OST: [path or "does not exist yet"]

---

### Theme 1 — [Name in customer language]

**Frequency:** [N independent sources]
**Intensity:** High / Medium / Low
**Primary Force of Progress:** Push / Pull / Anxiety / Habit

**Representative quotes:**
> "[literal quote]" — [role], [channel / FEEDBACK-ID]
> "[literal quote]" — [role], [channel / FEEDBACK-ID]

**Job Statement candidate:**
When [circumstance] → I want to [progress] → so I can [outcome]

**OST connection:** [existing opportunity / new candidate / tension with opportunity X]
**Ready for PR/FAQ:** Yes / Partially / No — [specify gap]

---

### Theme 2 — ...
```

### 5. Save and connect

- Save to `{workspace}/research/synthesis/SYNTHESIS-[topic]-[YYYY-MM-DD].md`
- If there is an active OST: suggest updating it with new evidence via the OST update skill
- If there is a draft PR/FAQ: indicate which quotes resolve `[NO CUSTOMER VOICE]` markers
- If neither exists: suggest creating an OST with the themes identified via the OST creation skill

## Rules

- Quotes are literal. Never paraphrase without marking as "(paraphrase)".
- Frequency matters, but one quote of high intensity (strong Push) outweighs five low-intensity ones.
- Themes from fewer than 2 independent sources are signals — not conclusions.
- Do not synthesize beyond the available sources. If data is insufficient: declare the limitation explicitly.
- People's names do not appear — always use generic role labels.

## Output

File at `{workspace}/research/synthesis/SYNTHESIS-[topic]-[date].md` containing:
- Themes in customer language (frequency + intensity + quotes + job statement candidate)
- OST mapping (existing evidence / new candidate / tension)
- Clear indication of which insights are ready for a PR/FAQ
