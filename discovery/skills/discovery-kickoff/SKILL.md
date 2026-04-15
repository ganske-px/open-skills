---
name: discovery-kickoff
description: |
  Orchestrates the full discovery cycle for a product idea or hypothesis. Reads the
  current workspace state, identifies evidence gaps, and presents a curated menu of
  discovery paths for the user to choose from. After the choice, invokes the
  corresponding skill with consolidated context.

  Triggers: "discovery kickoff", "explore the idea of X", "how might we X",
  "HMW X", "start discovery for X", "I want to discover X", "where do I start for X"

  Do NOT use when the user already knows the problem and wants to ideate solutions
  directly — use ideation instead.
  Do NOT use to synthesize already-completed research — use synthesize-research instead.
---

# discovery-kickoff

> **Priority:** This skill is the process orchestrator for PM discovery work. For HMW and
> discovery triggers, it takes priority over standalone brainstorming skills. Do not invoke
> brainstorming separately — this skill orchestrates brainstorming, ideation, and JTBD
> internally.

Reads the current workspace state, identifies evidence gaps, and presents a curated menu
of questions for the user to choose from. After the choice, invokes the corresponding skill
with the context already consolidated.

## Input

**If the topic was not provided in the trigger:** call `AskUserQuestion` with:
- question: "What idea or HMW do you want to explore?"
- type: text

**Classify the input type:**
- Starts with "how might we", "HMW", or similar problem framing → `type = HMW`
- Otherwise → `type = free_idea`

## Workspace Read

Execute silently before building the menu.

### Step 1 — Existence check (Glob)

```
Glob {workspace}/initiatives/actives/**          → does a similarly named initiative exist?
Glob {workspace}/research/feedback-log.md        → does a feedback log exist?
Glob {workspace}/research/interviews/INTERVIEW-* → do interview files exist?
Glob {workspace}/research/jtbd/**                → have jobs already been extracted?
Glob {workspace}/analysis/**                     → do internal analyses exist?
Glob {workspace}/research/plans/PLAN-*           → does a research plan exist?
```

### Step 2 — Selective read (only if something was found)

| If found | Action |
|---|---|
| Initiative | Read first 30 lines → extract status and hypothesis |
| Feedback log | Grep for the topic → count related entries |
| Analyses | Grep for the topic in analysis folder → list relevant files (never ask the user for file names) |
| JTBD | Read file headers → list already-mapped jobs |

### Step 3 — Gap map (internal, not shown to user)

```
customer_voice:      true if feedback log has related entries OR interviews exist
quantitative_data:   true if Grep found related analyses
jobs_mapped:         true if JTBD files found related to the topic
formal_hypothesis:   true if an initiative folder with a similar name exists
research_plan:       true if PLAN-* found related to the topic
active_initiative:   true if initiative folder with similar name found
```

## Question Menu

Build the menu by applying the rules below. Show at most 4 visible options. If more options
are eligible, group the remainder under "Other possible paths".

### Display rules

| Question | Condition to show | Destination skill |
|---|---|---|
| "What is the customer trying to do in this context?" | `jobs_mapped = false` AND `type = free_idea` | `jtbd` |
| "What solutions could we explore for this problem?" | always (first position if `type = HMW`) | `ideation` |
| "What do the data already tell us about this problem?" | always | `data-research` |
| "What does the market or industry already know about this?" | always (group under "Other paths" if menu is full) | `web-search` |
| "What have customers already said about this?" | `customer_voice = true` | `synthesize-research` |
| "How can we collect more customer voice on this?" | `customer_voice = false` | `research-plan` |
| "What would the product hypothesis look like?" | `formal_hypothesis = false` | `Initiatives:create` |
| "Do we have enough evidence to bet on this initiative?" | `active_initiative = true` AND at least 2 other fields = `true` | `product-decision` |

### Menu format

Call `AskUserQuestion` with:
- question: "Where do you want to start the discovery of [topic]?"
- options: [list of questions filtered by the rules above]
- type: select

**Behavior for HMW:** move "What solutions could we explore?" to first position. Do not show
"What is the customer trying to do?" — the HMW already frames the problem.

## Execution after selection

### 1. Build context briefing

```
topic: [idea or HMW provided]
input_type: free_idea | HMW
existing_initiative: [name + status] or null
related_feedback: [N entries] or null
existing_analyses: [list of relevant files] or null
existing_jobs: [list] or null
```

### 2. Invoke the skill with context

| Selection | Invocation |
|---|---|
| "What is the customer trying to do?" | `Skill(jtbd, args: "Map jobs for [topic]. [briefing]")` |
| "What solutions could we explore?" | `Skill(ideation, args: "Ideate solutions for [topic]. [briefing]")` |
| "What do the data already tell us?" | `Skill(data-research, args: "[topic]. [briefing]")` |
| "What does the market or industry know?" | `Skill(web-search, args: "[topic + briefing as context. Research: benchmarks, market solutions, trends, how the industry solves this]")` |
| "What have customers already said?" | `Skill(synthesize-research, args: "Synthesize feedback on [topic]. [briefing]")` |
| "How can we collect more customer voice?" | `Skill(research-plan, args: "Research plan for [topic]. [briefing]")` |
| "What would the product hypothesis look like?" | `Skill(Initiatives:create, args: "[topic]. [briefing]")` |
| "Do we have enough evidence?" | `Skill(product-decision, args: "Initiative gate for [topic]. [briefing]")` |

### 3. Return loop

After the skill returns, call `AskUserQuestion` with:
- question: "Do you want to explore another discovery path for [topic]?"
- options: ["Yes — show me the menu again", "No — done"]
- type: select

If "Yes": re-read the workspace (gaps may have changed) and present the updated menu.
If "No": close.

## Anti-patterns

- Never ask for a file name or path — use Glob + Grep to find them
- Never invent data or feedback — if `customer_voice = false`, show the collection option, not the synthesis option
- Do not show all options indiscriminately — the gap filter is the core value of this skill
- Do not execute directly without presenting the menu first
