---
name: creating-skills
description: Create new Claude Code skills following best practices. Use when asked to "create a new skill", "build a skill for [task]", "design a skill", "make a repeatable workflow", or "encode knowledge about [topic]". Handles skill structure, frontmatter, documentation, integration, trigger validation, and QA checklist. Do NOT use when editing an existing skill's behavior (just edit the SKILL.md directly). Do NOT use when creating hooks — use creating-hooks instead.
allowed-tools: Read, Write, Glob, Grep, WebFetch
---

# Creating Skills

> **Execution Note**: When using this skill, follow the Creation Workflow explicitly, ask clarifying questions during Discovery, and do not skip phases.

A skill is a self-contained folder of instructions, scripts, and resources that Claude loads dynamically to improve performance on specialized tasks.

## When to Create a Skill

| Scenario | Create Skill? | Rationale |
|----------|---------------|-----------|
| Task repeats 3+ times | Yes | Encode the pattern once |
| Task requires specific workflow | Yes | Capture the exact steps |
| Task uses external tools/scripts | Yes | Document the integration |
| Task needs domain knowledge | Yes | Embed expertise |
| One-off simple task | No | Direct execution is faster |
| Task varies too much | No | Skills need consistency |

## Creation Workflow

Follow this sequence exactly:

### Phase 1: Requirements Gathering
1. **Ask the user** to describe the skill's purpose
2. **Work through Discovery questions** (see next section) - present them and capture answers
3. **Confirm understanding** - summarize what you'll build before proceeding

### Phase 2: Design
4. **Draft the skill name** (lowercase, hyphens, descriptive)
5. **Write the description field** following the formula below
6. **Outline the structure** - which sections are needed?
7. **Identify resources** - scripts, templates, reference files?

### Phase 3: Implementation
8. **Create the skill directory** at `.claude/skills/<skill-name>/`
9. **Write SKILL.md** using the template
10. **Create supporting files** (scripts, examples, resources) if needed
11. **Verify against checklist**

### Phase 4: Integration
12. **Test execution** - manually verify the skill works
13. **Update documentation** - CLAUDE.md, team docs, related skills
14. **Document creation** - add to skills registry if one exists

## Discovery Questions

Work through these with the user before writing:

### 1. Purpose
- What problem does this skill solve?
- What task becomes easier/faster/more consistent?

### 2. Trigger Conditions
- When should Claude activate this skill?
- What keywords/phrases signal its use? (List at least 3)
- What context makes it relevant?

### 3. Workflow
- What are the exact steps to complete the task? (Number them)
- What's the input? What's the output?
- Are there decision points or branches?

### 4. Resources
- What tools are needed? (Bash, Read, Write, external APIs)
- Are there scripts to execute?
- Are there reference files or templates?

### 5. Constraints
- What should NOT be done?
- What are common mistakes to avoid?
- What are the limitations?

### 6. Examples
- What's a concrete example of correct use?
- What does success look like?

## Skill Structure

```
.claude/skills/<skill-name>/
├── SKILL.md           # Required: Main instructions
├── scripts/           # Optional: Executable scripts
│   └── tool.py
├── examples/          # Optional: Templates/samples
│   └── template.md
└── resources/         # Optional: Reference materials
    └── guidelines.md
```

### Complexity Guide

| Task Characteristics | Skill Type | Structure Needed |
|---------------------|------------|------------------|
| Single tool, linear steps | Simple | SKILL.md only |
| Multiple tools, conditional logic | Moderate | SKILL.md + examples/ |
| External scripts, data processing | Complex | Full structure with scripts/ |
| Domain knowledge repository | Reference | SKILL.md + resources/ |
| Large skill with multiple patterns | Granular | SKILL.md + references/ subfolders |

### Additional References

| Need | Read This File |
|------|----------------|
| Choosing multi-agent architecture | `references/agent-patterns.md` |
| Verifying skill/agent integration quality | `references/qa-checklist.md` |

## Token-Efficient Reference Organization

**Critical Principle**: Loading unnecessary tokens wastes context and money. Large skills should split content into granular files, loading only what's needed.

### When to Use Granular References

| Skill Size | Approach |
|------------|----------|
| < 200 lines | Keep everything in SKILL.md |
| 200-500 lines | Consider splitting largest sections |
| > 500 lines | **Must** use granular references |

### Granular Structure Pattern

```
.claude/skills/<skill-name>/
├── SKILL.md                    # Router: WHEN + WHERE to find content
└── references/
    ├── <category-1>/           # One folder per major category
    │   ├── item-a.md           # One file per item
    │   └── item-b.md
    ├── <category-2>/
    │   ├── item-c.md
    │   └── item-d.md
    └── common.md               # Shared content (if any)
```

### SKILL.md as Router

For large skills, SKILL.md should:
1. **Identify** what the user needs (decision tree)
2. **Route** to the specific reference file
3. **NOT contain** the full content of patterns/templates

**Router Pattern Example:**
```markdown
## Quick Decision Tree

| Need | Read This File |
|------|----------------|
| Pattern A | `references/patterns/a.md` |
| Pattern B | `references/patterns/b.md` |
| Example X | `references/examples/x.md` |

## Inline Summary (optional)

Brief summary of Pattern A for quick reference.
**Full template**: Read `references/patterns/a.md`
```

### File Design Rules

Each reference file must be:
1. **Self-contained** - All info needed to use that pattern
2. **Single-purpose** - One pattern/template/example per file
3. **Consistent** - Same structure across similar files

### Example: Prompt Engineering Skill

```
prompt-engineering/
├── SKILL.md                           # ~150 lines (router only)
└── references/
    ├── techniques/                    # 8 techniques, load ONE
    │   ├── zero-shot.md
    │   ├── few-shot.md
    │   ├── cot.md
    │   └── ...
    ├── frameworks/                    # 3 frameworks, load ONE
    │   ├── costar.md
    │   ├── crispe.md
    │   └── 5c.md
    ├── examples/                      # Examples, load ONE
    │   ├── agent-definition.md
    │   └── subagent-spawn.md
    └── anti-patterns.md               # Debugging reference
```

**Token savings**: Instead of loading ~3000 tokens for all techniques, load ~300 tokens for the one needed.

### Anti-Pattern: Monolithic Skills

**Bad**: One 800-line SKILL.md with everything
- Wastes tokens on unused content
- Harder to maintain
- Slower to parse

**Good**: 150-line router + granular reference files
- Only loads what's needed
- Easy to update individual patterns
- Each file has single responsibility

## SKILL.md Template

```markdown
---
name: skill-name
description: [Use description formula below]
allowed-tools: Tool1, Tool2  # Optional: Restrict available tools
---

# Skill Name

[One paragraph explaining the skill's purpose]

## When to Use

[Bullet list of trigger scenarios]

## Workflow

[Step-by-step numbered instructions]

## Commands/Scripts

[If applicable, document any scripts with examples]

## Guidelines

[Best practices and rules to follow]

## Anti-Patterns

[What to avoid - be specific]

## Error Handling

[How to handle failures and edge cases]

## Examples

[Concrete examples of correct usage]

## Limitations

[Known constraints or edge cases]
```

## Frontmatter Fields

| Field | Required | Purpose | Example |
|-------|----------|---------|---------|
| `name` | Yes | Unique identifier (lowercase, hyphens) | `database-migrations` |
| `description` | Yes | Routing + context (see formula) | "Manage database schema..." |
| `allowed-tools` | No | Restrict tools for security/focus | `Bash, Read, Write` |

### Description Formula

**Why:** The description is the ONLY mechanism Claude uses to decide whether to invoke a skill. Claude reads the `available_skills` list and matches user intent against descriptions. Claude is conservative by default — a vague description means the skill never fires. The description must compensate by being explicit and "pushy".

Use this structure:
```
[Action verb] [what it does]. Use when [trigger phrase 1], [trigger phrase 2], or [trigger phrase 3]. Handles [capability 1], [capability 2], and [capability 3]. Do NOT use when [near-miss exclusion 1] or [near-miss exclusion 2].
```

**Rules:**
1. List 3-5 concrete trigger phrases (verbs/sentences the user would say)
2. Include "Do NOT use when" for near-miss scenarios that should go to a different skill
3. Be specific enough that Claude can decide without ambiguity
4. Err on the side of being too explicit — undertriggering is worse than overtriggering

**Good Examples:**
- "Generate AI images using the vision model. Use when asked to 'create images', 'generate illustrations', or 'make visual assets'. Handles basic generation, reference-based consistency, and background images. Do NOT use when generating charts or data visualizations (use storytelling instead)."
- "Perform standardized code reviews. Use when asked to 'review code', 'check this PR', or 'give feedback on changes'. Handles diff analysis, checklist verification, and structured feedback. Do NOT use when user wants to write or fix code (that's implementation, not review)."

**Bad Examples:**
- "Image generation tool" (no triggers, no capabilities, no exclusions)
- "Helps with databases" (vague, no specifics)

## Writing Principles

### 1. Why-First Principle
- Every rule in a skill MUST have a reason. **Why:** Rules without reasons become cargo cult — followed blindly, applied in wrong contexts, and impossible to judge in edge cases.
- Format: state the rule, then add `**Why:**` on the same or next line.
- Example: "Never auto-approve without human review. **Why:** False positives in code review erode trust in the entire process."
- If you can't articulate why, the rule probably shouldn't exist.

### 2. Lean Principle
- Every sentence must justify its cost in the context window. **Why:** Skills are loaded into a limited context; unnecessary text crowds out useful instructions and degrades Claude's performance.
- Cut text that Claude already knows (general programming knowledge, obvious best practices).
- Generalize instead of listing every case — one principle beats ten specific rules.
- If a section could be derived from the skill's examples, remove the section.

### 3. Clarity Over Completeness
- Write for execution, not understanding
- Claude will follow these instructions literally
- Remove ambiguity; be explicit

### 4. Action-Oriented Language
- Use imperative verbs: "Create", "Run", "Check", "Validate"
- Avoid passive voice
- Each instruction should be executable

### 5. Decision Trees
- Make branching logic explicit
- Use tables for quick reference
- Include "if X then Y" patterns

### 6. Concrete Examples
- Show don't tell
- Include both correct and incorrect examples
- Use realistic scenarios

### 7. Negative Space
- Define what NOT to do
- Anti-patterns prevent common mistakes
- Limitations set expectations

### 8. Explicit Boundaries
- Specify exact number of steps (not "several steps")
- Define length limits when relevant ("in 3-5 bullet points")
- Set iteration limits ("retry up to 3 times")

## Error Handling Patterns

Every skill should include:

### Prerequisites Check
```markdown
Before starting:
- [ ] Required files exist at: [paths]
- [ ] Required tools are available: [tools]
- [ ] User has provided: [inputs]

If any prerequisite fails:
1. List what's missing
2. Suggest how to resolve it
3. Ask user to confirm before proceeding
```

### Fallback Strategy
```markdown
If [primary approach] fails:
1. Try [alternative approach]
2. If that fails, ask user for manual input
3. Document the issue for skill improvement
```

## Cross-Platform Python

If your skill uses Python scripts:
- **Never** use `python3` or `python` directly in commands
- **Never** hardcode venv paths like `venv/bin/python`
- **Always** use a cross-platform launcher script that handles virtual environment detection automatically

Example pattern for SKILL.md:
```bash
# Run script via cross-platform launcher
.claude/bin/python-run .claude/skills/my-skill/scripts/tool.py --arg value

# With virtual environment
.claude/bin/python-run --venv .claude/skills/my-skill/venv scripts/tool.py

# Install dependencies
.claude/bin/python-run --pip package-name
```

Create a launcher at `.claude/bin/python-run` that detects the active Python environment and delegates to the correct interpreter.

## Trigger Validation Protocol

**Why:** A skill that never fires is worse than no skill — it wastes maintenance effort and gives false confidence. Testing triggers after creation catches mismatches between description and actual user behavior.

After creating any skill, generate and document a trigger validation block at the bottom of the SKILL.md:

```markdown
## Trigger Validation

### Should Trigger (8-10 prompts)
1. "[exact phrase a user would say]" → expected behavior
2. "[variation with different wording]" → expected behavior
...

### Should NOT Trigger (8-10 near-miss prompts)
1. "[phrase that sounds similar but belongs to another skill]" → goes to [other skill]
2. "[phrase in the same domain but different intent]" → direct execution
...
```

**Rules:**
- Should-trigger prompts must be natural language (how a real user talks, not how a developer writes)
- Should-NOT-trigger prompts must be near-misses — close enough to be confusing. Easy exclusions don't test anything.
- Vary: tone (formal/casual), explicitness (direct vs contextual), language
- If you can't write 8 distinct should-trigger prompts, the skill may be too narrow
- If you can't write 8 distinct should-NOT-trigger prompts, the skill may overlap with others

## Verification Checklist

Before finalizing a skill:

- [ ] Frontmatter has `name` and `description`
- [ ] Description follows the formula (action + triggers + capabilities + exclusions)
- [ ] Description includes "Do NOT use when" for near-miss scenarios
- [ ] Every rule has a **Why:** line explaining the reason
- [ ] Workflow is step-by-step numbered instructions
- [ ] All scripts/tools are documented with examples
- [ ] Examples are concrete and testable
- [ ] Anti-patterns are included
- [ ] Error handling is specified
- [ ] Limitations are stated
- [ ] File paths are relative to project root
- [ ] **Token efficiency**: If > 500 lines, use granular references
- [ ] **Trigger validation**: 8-10 should-trigger + 8-10 should-NOT-trigger prompts documented

## Integration

After creating a skill:

1. **Test**: Execute the skill manually to verify it works
2. **Document**: Update parent docs (CLAUDE.md, team docs)
3. **Connect**: Update related skills/agents that need to know about it
4. **Announce**: If part of a team workflow, notify relevant agents

## Skill Categories

| Category | Examples | Characteristics |
|----------|----------|-----------------|
| **Tool Integration** | image-gen, front-matter | Wraps external scripts/APIs |
| **Workflow** | deploy, spawn | Multi-step processes |
| **Knowledge** | brand-guidelines | Domain expertise/standards |
| **Design** | frontend-design | Creative direction + principles |

## Common Mistakes

1. **Vague descriptions** - Claude can't route to the skill
2. **Missing examples** - Claude guesses instead of following patterns
3. **No anti-patterns** - Same mistakes repeat
4. **Hardcoded paths** - Breaks in different environments
5. **Over-engineering** - Simple tasks don't need complex skills
6. **Skipping Discovery** - Skill doesn't match actual needs
7. **No error handling** - Fails silently on edge cases
8. **Hardcoded `python3` or venv paths** — use a cross-platform launcher script for Python execution

## Complete Example

**Full walkthrough**: Read `references/example-code-review.md` for a step-by-step example of creating a code review skill using all 4 phases.
