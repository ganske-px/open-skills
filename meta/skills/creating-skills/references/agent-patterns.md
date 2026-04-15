# Agent Architectural Patterns

Reference for choosing the right multi-agent pattern when designing workflows with Claude Code skills.

**Source:** Adapted from [revfactory/harness](https://github.com/revfactory/harness) agent-design-patterns.

## The 6 Patterns

### 1. Pipeline (Sequential)

Output of each agent feeds into the next. Order is strict.

```
Agent A → Agent B → Agent C → Final Output
```

**When to use:** Tasks with clear phase dependencies where each step needs the previous step's output.

**Example:** Content pipeline
```
content-regulator (decide what to produce)
  → content-writer (generate draft)
    → content-validator (validate quality)
      → content-publisher (deliver output)
```

**Anti-pattern:** Using pipeline when steps are independent — wastes time waiting.

---

### 2. Fan-out / Fan-in (Parallel → Synthesis)

Multiple agents work independently in parallel, then results are synthesized.

```
         ┌→ Agent A ─┐
Input ───┼→ Agent B ──┼→ Synthesizer → Output
         └→ Agent C ─┘
```

**When to use:** Research or analysis tasks where multiple independent sources/perspectives are needed.

**Example:** Discovery research
```
         ┌→ web-search-researcher (external benchmarks)
Topic ───┼→ data-research (internal analytics)          ──→ synthesize-research
         └→ feedback-log scan (voice of customer)
```

**Anti-pattern:** Fan-out with shared state — agents will conflict. Only use when sources are independent.

---

### 3. Expert Pool (Router → Specialist)

A router agent analyzes the input and selects the right specialist.

```
Input → Router → [Specialist A | Specialist B | Specialist C]
```

**When to use:** Tasks where the type of work varies and each type needs different expertise.

**Example:** Discovery orchestrator as router
```
User prompt → discovery-kickoff →
  ├─ "map jobs to be done" → jtbd skill
  ├─ "how might we solve [X]" → ideation skill
  ├─ "synthesize research" → synthesize-research skill
  └─ "data on [X]" → data-research skill
```

**Anti-pattern:** Router that always picks the same specialist — simplify to direct invocation.

---

### 4. Generate-Verify (Creator + Critic Loop)

One agent generates, another validates. Loop until quality gate passes.

```
Generator → Reviewer → [Pass → Output | Fail → Generator (retry)]
```

**When to use:** Creative or complex output where quality varies and objective criteria exist.

**Example:** Content creation
```
content-writer (generates draft)
  → content-validator (checks quality criteria)
    → [PASS → publish | FAIL → content-writer rewrites]
```

**Rules:**
- Maximum 2 retry iterations. **Why:** Diminishing returns after 2 — if it's still wrong, the prompt or criteria need fixing, not more attempts.
- Reviewer must use objective criteria, not subjective preference.

---

### 5. Supervisor (Central Coordinator)

One agent manages global state and dynamically distributes tasks to workers.

```
Supervisor ──→ Worker A (task from queue)
           ──→ Worker B (task from queue)
           ──→ Worker C (reatributed from A)
```

**When to use:** Large-scale operations with dynamic task allocation, where the queue changes based on results.

**Example:** Content regulator as supervisor
```
content-regulator:
  1. Reads pipeline state (what exists, what's missing)
  2. Decides what to produce next
  3. Spawns content-writer with specific brief
  4. Validates output, decides publish vs rewrite
  5. Updates pipeline state
```

**Anti-pattern:** Supervisor that does the work itself — it should coordinate, not execute.

---

### 6. Hierarchical Delegation (Recursive Decomposition)

Top-level agent decomposes objective into sub-objectives, delegates recursively.

```
Lead → Sub-lead A → Workers
     → Sub-lead B → Workers
```

**When to use:** Complex projects spanning multiple domains where each domain has its own decision-making.

**Example:** GPM workflow
```
Human → discovery-kickoff (orchestrator)
          → jtbd-facilitator (qualitative)
          → data-research (quantitative)
          → web-search-researcher (external)
        → prfaq-writer (definition)
          → initiative-checker (validation)
```

**Anti-pattern:** More than 3 levels deep — context degrades. Flatten if possible.

---

## Decision Framework: Which Pattern?

| Question | If Yes → | If No → |
|----------|----------|---------|
| Do steps depend on previous output? | Pipeline | Continue |
| Can sources work independently? | Fan-out/Fan-in | Continue |
| Does input type determine which agent to use? | Expert Pool | Continue |
| Is output quality variable and checkable? | Generate-Verify | Continue |
| Is the task queue dynamic? | Supervisor | Continue |
| Does the problem decompose into sub-problems? | Hierarchical | Simple sub-agent call |

## Execution Mode Decision

| Condition | Mode | Why |
|-----------|------|-----|
| Agents need to communicate with each other | Agent Team | SendMessage enables coordination |
| Agent just returns result to caller | Sub-agent | Simpler, no inter-agent overhead |
| Single skill can handle the task | Direct skill | No agent overhead at all |

**Default:** Sub-agent mode via the `Agent` tool. Agent Team mode requires experimental flag and is not yet broadly adopted.

## Team Size Guidelines

| Number of distinct tasks | Recommended agents |
|--------------------------|-------------------|
| 1-4 | 1-2 agents (or direct skill) |
| 5-10 | 2-3 agents |
| 10-20 | 3-5 agents |
| 20+ | 5-7 agents max |

**Optimal tasks per agent:** 4-6. More leads to context overload; fewer means the agent is underutilized.
