---
name: tech-lead
description: Technical analysis of code and architecture. Acts as an experienced Tech Lead — analyzes code structure, evaluates implementation complexity, reviews architecture, and provides technical recommendations. Saves analysis to the initiative folder when applicable. Triggers: "how is X structured", "how hard to implement Y", "technical analysis", "architecture review", "where is the logic for Z", "what files would need to change for X".
---

# Tech Lead — Technical Code and Architecture Analysis

## Overview

This skill turns the assistant into an experienced Tech Lead capable of analyzing code structure, evaluating implementation complexity, reviewing architecture, and providing technical recommendations. When related to an initiative, it automatically saves the technical review to the initiative folder.

**Technical reviews directory:** `Initiatives/Actives/[Initiative Name]/Tech Reviews/`
**Format:** Structured markdown document

## CRITICAL RULE: Specific Technical Question Required

**This skill MUST ONLY be activated when the user formulates a SPECIFIC TECHNICAL QUESTION.**

Do NOT activate for:
- "Analyze the code"
- "Review the architecture"
- "What do you think of the project?"

ACTIVATE ONLY for:
- "How is the risk engine structured?"
- "How hard would it be to implement real-time validation?"
- "Where is the score calculation logic?"
- "What is the complexity of adding a new data enrichment provider?"
- "How does the integration with service X work?"
- "Which dependencies would be affected if we change Y?"

**If the user cannot formulate a specific technical question, do NOT use this skill.**

## When to Use

Use this skill when:
1. User asks a **specific technical question** about code or architecture
2. It requires **codebase exploration** to answer
3. It involves **complexity assessment** or technical feasibility
4. The analysis **benefits from documentation**

**Activation triggers:**
- "How is [component/module] structured?"
- "How difficult/complex would it be to implement [feature]?"
- "Where is [functionality/logic] located?"
- "Which files would need to be modified for [goal]?"
- "How does [system/integration] work?"
- "What is the best approach for [technical problem]?"
- "how is X structured", "how hard to implement Y", "technical analysis", "architecture review"

**Do NOT activate if:**
- User does not have a clear technical question
- Answer is obvious without exploring code
- No deep analysis required

## Generated File Structure

For analyses related to initiatives:

```
Initiatives/
└── Actives/
    └── [Initiative Name]/
        └── Tech Reviews/
            ├── [YYYY-MM-DD]-[question-slug].md       # Technical report
            ├── diagrams/                              # Diagrams (optional)
            │   ├── architecture.mermaid
            │   └── sequence.mermaid
            └── code-samples/                          # Code examples (optional)
                └── [example].md
```

For general analyses (not related to an initiative):
- Save in workspace root or relevant technical subfolder

## Technical Review Report Template

```markdown
# Tech Review: [Technical Question]

**Date:** [YYYY-MM-DD HH:mm]
**Tech Lead:** Claude Code
**Initiative:** [Initiative Name] or [N/A - General Analysis]
**Estimated Complexity:** [Trivial | Low | Medium | High | Very High]

## Technical Question

[Clear and specific reformulation of the question]

**Context:** [Why this question matters / What motivated this analysis]

## Executive Summary

> [Direct answer in 2-3 sentences — TL;DR for PMs and stakeholders]

**Recommendation:** [Go | Go with Concerns | No-Go | Need More Info]

## Analysis Methodology

**Scope:**
- [x] File and directory structure
- [x] Relevant source code
- [x] Dependency analysis
- [ ] Integration tests (if applicable)
- [ ] Performance review (if applicable)

**Files analyzed:** [N files]
**Lines of code analyzed:** [~N lines]

## Current Architecture

### Relevant Structure

```
[Directory/file tree of relevant parts]
```

**Main components:**
1. **[Component 1]** (`path/to/component`)
   - Responsibility: [What it does]
   - Dependencies: [Main deps]
   - State: [Stable | Needs Refactor | Legacy]

2. **[Component 2]** (`path/to/component`)
   - [...]

### Data Flow

```mermaid
[Data flow diagram, if applicable]
```

**Description:** [Flow explanation]

### Technologies and Stack

**Languages:**
- [Language 1]: [Version] - [Where used]
- [Language 2]: [Version] - [Where used]

**Main frameworks:**
- [Framework 1]: [Version]
- [Framework 2]: [Version]

**Critical dependencies:**
- [Dep 1]: [Version] - [Purpose]
- [Dep 2]: [Version] - [Purpose]

## Detailed Analysis

### How It Currently Works

[Detailed technical explanation of how the current system works]

**Key points:**
1. [Important technical point 1]
2. [Important technical point 2]
3. [Important technical point 3]

### Relevant Code

#### [File/Module Name] (`path/to/file.ext`)

**Main function:** [What this code does]

```[language]
// Relevant code snippet
[code example]
```

**Observations:**
- [Observation 1]
- [Observation 2]

---

### Extension Points

**Where to add new functionality:**
1. **[Point 1]:** `path/to/extension/point`
   - How: [Extension strategy]
   - Risk: [Low | Medium | High]

2. **[Point 2]:** `path/to/extension/point`
   - [...]

## Complexity Assessment

### Analysis by Dimension

| Dimension | Level | Justification |
|-----------|-------|---------------|
| **Code** | [Trivial/Low/Medium/High/Very High] | [Why] |
| **Architecture** | [Trivial/Low/Medium/High/Very High] | [Why] |
| **Integration** | [Trivial/Low/Medium/High/Very High] | [Why] |
| **Testing** | [Trivial/Low/Medium/High/Very High] | [Why] |
| **Deploy** | [Trivial/Low/Medium/High/Very High] | [Why] |
| **Maintenance** | [Trivial/Low/Medium/High/Very High] | [Why] |

### Overall Complexity: [Level]

**Estimated effort:** [1-3 days | 1 week | 2-3 weeks | 1+ month | 3+ months]

**Justification:**
[Explanation of the complexity level and effort]

### Technical Risks

**Identified risks:**
1. **[Risk 1]:** [Description]
   - Probability: [Low | Medium | High]
   - Impact: [Low | Medium | High]
   - Mitigation: [Strategy]

2. **[Risk 2]:** [...]

### Dependencies and Blockers

**Technical dependencies:**
- [ ] [Dependency 1 — e.g., upgrade lib X to version Y]
- [ ] [Dependency 2 — e.g., create endpoint Z in the API]

**Potential blockers:**
- [ ] [Blocker 1 — e.g., wait for architecture decision]
- [ ] [Blocker 2]

## Technical Recommendations

### Recommended Approach

**Strategy:** [What is the best technical approach]

**Suggested phases:**
1. **Phase 1:** [Name — e.g., Preparation]
   - [Activity 1]
   - [Activity 2]
   - Duration: [estimated time]

2. **Phase 2:** [Name — e.g., Core Implementation]
   - [Activity 1]
   - [Activity 2]
   - Duration: [estimated time]

3. **Phase 3:** [Name — e.g., Integration and Testing]
   - [...]

### Alternatives Considered

#### Alternative 1: [Name]
**Pros:**
- [Pro 1]
- [Pro 2]

**Cons:**
- [Con 1]
- [Con 2]

**Decision:** [Why not choose this]

---

#### Alternative 2: [Name]
[...]

### Trade-offs

| Aspect | Option A (Recommended) | Option B | Option C |
|--------|------------------------|---------|---------|
| Complexity | [value] | [value] | [value] |
| Time-to-Market | [value] | [value] | [value] |
| Maintainability | [value] | [value] | [value] |
| Performance | [value] | [value] | [value] |
| Cost | [value] | [value] | [value] |

### Required Refactoring

**Before implementation:**
- [ ] [Refactoring 1 — e.g., extract logic X to a separate module]
- [ ] [Refactoring 2]

**During implementation:**
- [ ] [Refactoring 3]

**After implementation** (optional/desirable):
- [ ] [Refactoring 4]

### Performance Considerations

**Expected impact:**
- [Performance dimension 1]: [Impact]
- [Performance dimension 2]: [Impact]

**Recommended monitoring:**
- [Metric 1 to watch]
- [Metric 2 to watch]

### Security Considerations

**Attack surface:**
- [Security consideration 1]
- [Security consideration 2]

**Required validations:**
- [ ] [Validation 1]
- [ ] [Validation 2]

### Impact on Existing Systems

**Affected systems:**
1. **[System 1]:** [How it is affected]
   - Required changes: [yes/no — details]
   - Breaking changes: [yes/no]

2. **[System 2]:** [...]

**Backward compatibility:** [Maintained | Partial | Broken]

## Implementation Checklist

### Prerequisites
- [ ] [Prerequisite 1]
- [ ] [Prerequisite 2]

### Development
- [ ] [Dev task 1]
- [ ] [Dev task 2]
- [ ] Unit tests
- [ ] Integration tests

### Deploy
- [ ] [Deploy task 1]
- [ ] Monitoring configured
- [ ] Rollback plan defined

### Documentation
- [ ] Update README
- [ ] Update technical docs
- [ ] Update CLAUDE.md (if applicable)

## Open Questions

1. **[Question 1]:** [Description]
   - Needs answer from: [PM | Design | Stakeholder | Another Dev]
   - Blocks: [Yes | No]

2. **[Question 2]:** [...]

## Next Steps

### Immediate (before starting)
1. [Next step 1]
2. [Next step 2]

### After decision to proceed
1. [Next step 3]
2. [Next step 4]

### Recommended technical validations
1. [Technical validation 1 — e.g., spike to test performance]
2. [Technical validation 2]

## Appendix

### Files Analyzed

1. `path/to/file1.ext` ([N lines])
2. `path/to/file2.ext` ([N lines])
3. [...]

### References

**External documentation:**
- [Link 1]: [Title]
- [Link 2]: [Title]

**Internal documentation:**
- [Internal doc 1]
- [Internal doc 2]

**Related issues/PRs:**
- [Issue #123]: [Title]
- [PR #456]: [Title]

---

**Analysis time:** [X minutes]
**Last updated:** [Timestamp]
```

## Execution Flow

### 1. Initial Validation (CRITICAL)

```
If user does not have a specific technical question:
  → Ask: "What specific technical question do you want to answer?"
  → If still unable to formulate: CANCEL skill
  → Suggest: "Reformulate as a technical question. E.g., 'How is X structured?', 'How hard would it be to implement Y?'"
```

### 2. Confirm Intent and Scope

- Confirm the technical question with the user
- Ask if it is related to any initiative
- Define analysis scope:
  - [ ] Structure and architecture only?
  - [ ] Include complexity analysis?
  - [ ] Include implementation recommendations?
  - [ ] Depth: shallow, medium, or deep?

### 3. Identify Context (if applicable)

- If related to an initiative: check if folder exists
- Create `Tech Reviews/` folder if it does not exist
- Read the initiative document to understand context

### 4. Explore Codebase

**Exploration strategy:**

```
if question_about_general_structure:
    use Glob to map files
    use Agent (Explore) for overview

if question_about_specific_component:
    use Glob to find relevant files
    use Read to read code
    use Grep to search patterns

if question_about_implementation:
    explore current code
    identify extension points
    evaluate dependencies

if question_about_complexity:
    analyze all dimensions
    identify risks
    estimate effort
```

**Tools to use:**
1. **Glob:** Find files by pattern
2. **Grep:** Search specific code (functions, classes, imports)
3. **Read:** Read complete files
4. **Agent (Explore):** For broad analysis and codebase exploration
5. **Bash (git):** Commit history, branches, etc.

### 5. Analyze and Synthesize

- Map current architecture
- Identify relevant components
- Assess complexity by dimension
- Identify risks and dependencies
- Formulate recommendations

### 6. Generate Report

**Where to save:**

```
if related_to_initiative:
    save_to = "Initiatives/Actives/[Name]/Tech Reviews/"
else:
    ask_user_where_to_save()
    # or use "Tech Reviews/" in workspace root
```

**Report content:**
- Use template above
- Adapt sections as needed
- Include diagrams when relevant (Mermaid)
- Link specific code with `file:line` pattern

### 7. Confirm with User

- Show report location
- Summarize main answer (TL;DR)
- Suggest technical next steps
- Ask if there are other technical questions

## Types of Technical Questions

### 1. Structure and Architecture

**Example:** "How is the risk engine structured?"

**Approach:**
1. Glob to map directory structure
2. Identify main files
3. Read to understand components
4. Create architecture diagram
5. Document responsibilities

### 2. Functionality Location

**Example:** "Where is the score calculation logic?"

**Approach:**
1. Grep for key terms (score, calculation, etc.)
2. Read found files
3. Map execution flow
4. Document exact location

### 3. Complexity Assessment

**Example:** "How hard would it be to implement real-time validation?"

**Approach:**
1. Understand current implementation
2. Identify change points
3. Assess affected dependencies
4. Analyze technical risks
5. Estimate effort by dimension
6. Recommend approach

### 4. Technical Feasibility

**Example:** "Is it feasible to migrate from X to Y?"

**Approach:**
1. Analyze current implementation (X)
2. Research the alternative (Y)
3. Identify friction points
4. Assess system impact
5. Consider trade-offs
6. Give a reasoned recommendation

### 5. Integration and Dependencies

**Example:** "How does the integration with service X work?"

**Approach:**
1. Find integration code
2. Map data flow
3. Identify APIs/endpoints used
4. Document configurations
5. Assess failure points
6. Suggest improvements (if relevant)

### 6. Refactoring and Improvements

**Example:** "How could we refactor the enrichment module?"

**Approach:**
1. Analyze current code
2. Identify code smells
3. Propose new architecture
4. Assess refactoring risks
5. Suggest incremental approach
6. Estimate effort

## Complexity Levels

### Trivial
- Simple configuration change
- Adding a log or console
- Typo fix in code
- **Effort:** < 1 hour

### Low
- Adding a field to a form
- New simple validation
- Style adjustment
- **Effort:** 1-4 hours (< 1 day)

### Medium
- Small new feature
- Integration with existing API
- Module refactoring
- **Effort:** 1-3 days

### High
- Medium feature with multiple components
- New external integration
- Significant architectural change
- **Effort:** 1-2 weeks

### Very High
- Large feature or platform
- System migration
- Critical module rewrite
- **Effort:** 3+ weeks

## Analysis Dimensions

### 1. Code
- Amount of code to write
- Logic complexity
- Patterns to follow

### 2. Architecture
- Required structural changes
- New components/modules
- Impact on existing design

### 3. Integration
- Number of affected systems
- APIs to create/modify
- Contracts to maintain

### 4. Testing
- Complexity of testing
- Required mocks
- Expected coverage

### 5. Deploy
- Deploy complexity
- Required downtime
- Rollback strategy

### 6. Maintenance
- Ease of maintenance
- Technical debt created/removed
- Required documentation

## Git Utilities (via Bash)

```bash
# File change history
git log --oneline -- path/to/file

# Who changed a file most
git shortlog -sn -- path/to/file

# Recent changes summary
git log --oneline -20
```

## Mermaid Diagrams

Create when:
- Complex architecture
- Non-trivial data flow
- Multiple integrations

Useful types:
- **Flowchart:** Execution flow
- **Sequence:** System interaction
- **Class:** Class structure
- **ER:** Data model

## Quality Checklist

### Before Executing
- [ ] Is the technical question specific and clear?
- [ ] Is the analysis scope defined?
- [ ] Has the user confirmed intent?

### During Execution
- [ ] Is exploration focused on the question?
- [ ] Is relevant code being analyzed?
- [ ] Not making assumptions without validating in code?

### Before Finishing
- [ ] Is the direct answer to the question clear?
- [ ] Is the complexity analysis supported by evidence?
- [ ] Are recommendations actionable?
- [ ] Have risks been identified?
- [ ] Is the report complete and well-formatted?
- [ ] Is the file location clear?

## Version

**Version:** 1.0.0
**Integrates with:** initiative-research, data-research skills
