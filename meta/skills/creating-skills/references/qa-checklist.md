# QA Checklist for Skills and Agents

Framework for verifying integration coherence between skills, agents, hooks, and the workspace. Based on the "simultaneous bilateral reading" technique from [revfactory/harness](https://github.com/revfactory/harness).

**Principle:** Components that work in isolation can break at their points of contact. This checklist verifies the seams, not the parts.

## 1. Description ↔ Body Coherence

**Check:** Does the skill description promise what the SKILL.md body actually delivers?

| Verify | How |
|--------|-----|
| Every trigger phrase in description has a corresponding workflow path in body | Read description triggers, trace each through the SKILL.md workflow |
| Every capability listed in description is implemented in body | Search body for each capability keyword |
| "Do NOT use when" exclusions don't accidentally exclude valid use cases | Test each exclusion phrase against real user scenarios |

**Common failure:** Description says "handles X, Y, and Z" but body only implements X and Y. Z was planned but never written.

## 2. Skill Triggers ↔ CLAUDE.md Triggers

**Check:** No conflict or overlap between skill triggers and hardcoded routing in CLAUDE.md.

| Verify | How |
|--------|-----|
| CLAUDE.md routing rules are consistent with skill descriptions | Compare trigger phrases side by side |
| No two skills claim the same trigger phrase | Grep all SKILL.md descriptions for shared trigger phrases |
| Priority overrides are documented in both places | Check CLAUDE.md and the skill's own SKILL.md |

**Common failure:** CLAUDE.md routes "HMW" to a discovery skill, but an ideation skill also claims "HMW" in its description. Claude randomly picks one.

## 3. Agent I/O ↔ Caller Expectations

**Check:** The agent's input/output contract matches what the caller sends/expects.

| Verify | How |
|--------|-----|
| Agent's expected input format matches the prompt template in the caller | Read agent's "## I/O Protocol" (or infer from instructions) and compare with caller's Agent tool prompt |
| Agent's output format matches what the caller reads/processes | Trace what happens to the agent's return value |
| Error cases are handled — what if agent returns nothing? | Check caller for fallback logic |

**Common failure:** Agent expects JSON input but caller sends free text. Agent produces markdown but caller tries to parse structured data.

## 4. Output Paths ↔ Directory Rules

**Check:** Every file a skill/agent creates goes to the correct directory per project conventions.

| Verify | How |
|--------|-----|
| File paths in Write calls match the project's directory structure | Grep each skill for `Write` tool calls and check the paths |
| No skill writes to a directory it shouldn't own | Compare output paths against directory ownership rules |
| Skills creating shared files don't conflict with each other | Check if two skills write to the same path |

**How to verify:** Grep each skill/agent for `Write` tool calls and file path patterns. Confirm they match the project's structure conventions.

**Common failure:** Agent writes to the root directory instead of the correct subfolder.

## 5. Hooks ↔ Skills Compatibility

**Check:** Hooks don't block legitimate output from skills/agents.

| Verify | How |
|--------|-----|
| Each blocking hook is tested against output from all skills that could trigger it | Deliberately trigger the block condition from the skill's output |
| Advisory hooks don't produce false positives on valid skill output | Test valid output against the hook's matching logic |
| New skills are validated against existing hooks | Run skill output through hook pipe-tests |

**How to verify:** For each hook, deliberately trigger the block condition from the skill's output. Confirm the hook fires AND that the skill's instructions prevent the condition.

**Common failure:** New skill is created but not tested against existing hooks. Skill produces valid output that a hook incorrectly blocks because the hook's regex is too broad.

## 6. Inter-Agent Communication

**Check:** When agents spawn other agents or invoke skills, the chain works end-to-end.

| Verify | How |
|--------|-----|
| Spawned agent receives sufficient context | Read the Agent tool prompt — does it include all needed info or just a reference? |
| Spawned agent's output is actually used by the caller | Trace the return value — is it read, processed, and integrated? |
| Timeout/failure doesn't break the parent | Check if parent has fallback for agent failure |

**Common failure:** Parent agent spawns a research agent but doesn't wait for result before writing the document. Output includes placeholders that the research agent already resolved.

## Running the Checklist

**When to run:**
- After creating a new skill or agent (checks 1, 2, 4, 5)
- After modifying a hook (check 5 against all affected skills)
- After modifying CLAUDE.md routing rules (check 2)
- Quarterly health check (all 6 checks on full inventory)

**How to run:**
1. Pick the relevant checks from above
2. For each check, read both sides of the seam simultaneously
3. Document any mismatches as issues
4. Fix mismatches before shipping the change
