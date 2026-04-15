---
name: tldr
description: Reads a text or file and creates a TL;DR section inserted at the top of the document. Use when asked to "create a TL;DR", "add TL;DR", "summarize this document", or "summarize this". Handles audience profiles (team, executive, client, internal ops). Do NOT use to synthesize qualitative research — use synthesize-research. Do NOT use for stakeholder updates — use storytelling.
allowed-tools: Read, Edit
---

# TL;DR Skill

Reads a text (file or pasted) and creates a concise TL;DR section, inserted at the top of the document, adapted to the target audience profile.

## When to Use

- User asks "create a TL;DR", "add TL;DR", "summarize this document", "executive summary", "summarize"
- User shares a long text and wants a structured summary
- User wants to adapt a document for a specific audience

## Workflow

1. **Identify the input**
   - If user provided a file path → read with Read tool
   - If user pasted the text → use it directly

2. **Identify the audience**
   - If the user specified → use the corresponding profile (see table below)
   - If not specified → ask before writing. Options: team / executive / client / internal ops

3. **Identify the document language** → write the TL;DR in the same language

4. **Extract key points** from the text:
   - Context (what this is and why it matters)
   - Central finding or conclusion
   - Practical implication
   - Priorities or next steps (if any)

5. **Write the TL;DR** following the audience profile (see section below)

6. **Insert in the document**
   - If from a file → use Edit to insert the section right after the main `#` title, before the first `---` or content section
   - If from pasted text → deliver the TL;DR as direct text output, no file editing

## Audience Profiles

| Profile | Focus | Tone | Length | Structure |
|---------|-------|------|--------|-----------|
| **Team** | Context + finding + priorities | Direct, technical when needed | 5–8 bullets or short paragraphs | Context → finding → implication → numbered priorities |
| **Executive** | Business impact + decision needed | No technical jargon, numbers first | Max 4 bullets | Context (1 sentence) → impact ($, %, volume) → risk/opportunity → recommended action |
| **Client** | Benefit + clarity | Positive, no internal jargon | 3–5 bullets | What changed → what improves for the client → what stays the same → next step (if any) |
| **Internal Ops** | Process + owners + actions | Pragmatic, task-oriented | Bullets + action list | What happened → who does what → deadline/dependency |

## TL;DR Format in the File

```markdown
## TL;DR

[Summary content adapted to the audience profile]

---
```

The section must be inserted immediately after the document's `#` title, before any other content.

## Anti-Patterns

- Never invent data, numbers, or quotes not present in the original text
- Never copy full sentences from the document — the TL;DR must be rewritten, not copy-pasted
- Never label the audience in the document ("for the team", "executive summary") — only the content
- Never exceed 10 lines of content in any profile
- Never use the same level of technical detail for executive or client audiences

## Example

**Input (file):** 300-line technical analysis on payment advance blocking rules
**Audience:** team

**Output inserted at the top:**

```markdown
## TL;DR

Payment advance moved $16.3M in Feb/2026 — 138% growth over 12 months. Half of active contracts use the feature at least once.

The system has 15 distinct blocking rules, mapped from source code. None of them leave a trace when triggered — every blocked attempt disappears with no record.

Of the 49.3% of contracts without an advance, there is no way to distinguish who chose not to use it from who tried and was rejected. Real demand is unknown.

Three priorities:
1. Instrument failures with a structured `reason_code` — without this, any decision about the rules is speculation
2. Fix the message for manual blocks — today it simulates "no balance" when it is actually an intentional operator block
3. Measure the impact of the geolocation rule before adjusting any threshold

---
```

## Post-Generation: Language Review

After generating the document, suggest to the user running the `spell-checker` skill for orthographic and grammar review.
