---
name: spell-checker
description: Corrects spelling, grammar, and style in texts. Use when asked to "spell check", "proofread this", "check grammar", "review text quality", "correct the text", "fix spelling errors", or "check spelling". Applies an optional workspace glossary if present. Do NOT use to rewrite content (use content-writer) or validate author voice.
---

# Spell Checker

Multi-language text correction with awareness of workspace-level language rules and an optional glossary.

## When to Use

- User asks to correct or proofread text
- A new document or section needs orthographic/grammar review
- Incremental review after manual edits by the user

## Workflow

### 1. Load workspace glossary (optional)

Before any correction, check whether a `glossary.md` file exists in the workspace root:
- If found → read it and extract:
  - Forbidden terms and their required replacements
  - Canonical product/brand names (correct capitalization and spelling)
  - Domain-specific terms and their preferred forms
- If not found → skip this step and proceed with standard language rules only

### 2. Read the indicated file

- Works with any file type (`.md`, `.txt`, converted `.docx`, code with comments, etc.)
- If the file is large, process in sections

### 3. Identify and correct

Apply corrections in the following categories, in this order of priority:

#### A. Glossary rules (highest priority — only when glossary is present)
- Forbidden terms → apply the required replacements from `glossary.md`
- Product/brand names → apply canonical capitalization from `glossary.md`
- Domain-specific terms → apply preferred forms from `glossary.md`
- Note: glossary rules apply regardless of the document language

#### B. Spelling and typing errors
- Misspelled words
- Swapped, duplicated, or missing letters
- Run-together words (e.g., "ofthe" → "of the")

#### C. Accents and diacritics
- Missing or incorrect accent marks
- Apply rules for the document's detected language

#### D. Agreement and concordance
- Subject-verb agreement
- Noun-adjective agreement (gender and number, for applicable languages)

#### E. Punctuation and formatting
- Commas, periods, dashes
- Redundancies (e.g., "and etc." → "etc.")
- Consistent capitalization (sentence start, proper nouns, acronyms)
- Spacing

#### F. Internal consistency
- If the document uses a pattern (e.g., "Trust Cycle" in the title), ensure the same pattern repeats in the body
- If technical terms appear in a foreign language, keep their original spelling

### 4. Apply corrections

- Use Edit/Write to apply directly to the file
- For large files, apply in blocks

### 5. Present summary

After applying, list a grouped summary by category:

```
Corrections applied:
- **Glossary rules:** X replacements (list the main ones)
- **Spelling:** X corrections (list the main ones)
- **Accents/diacritics:** X corrections
- **Agreement:** X corrections (list)
- **Punctuation:** X adjustments
- **Consistency:** X adjustments (list)
```

## Operation Modes

### Complete mode (default)
Reviews the entire file at once. Use when the user asks to correct a file for the first time.

### Incremental mode
Reviews only new or changed sections. Use when:
- The user says "I added another section, review it"
- The user made manual changes and asks for a new review
- The file was already reviewed earlier in the same conversation

In incremental mode, apply all the same rules already discussed in the conversation (naming, glossary, etc.) without requiring the user to repeat them.

## Guidelines

- **Never alter content or context** — only correct form
- **Do not rewrite sentences** — correct the minimum necessary to make it right
- **Preserve the author's tone** — do not formalize informal text or vice versa
- **Preserve passages in other languages** — English taglines, technical terms, etc. stay as-is (correct only if they have an error in their own language)
- **Flag ambiguous corrections** — if a correction might change the meaning, use AskUserQuestion to confirm before applying
- **Consistency over preference** — if the document already uses a pattern, follow the document's pattern even if another form is also acceptable

## Anti-Patterns

- Do not add emojis, comments, or extra formatting
- Do not reorganize sections or paragraphs
- Do not suggest content improvements (scope is language only)
- Do not translate passages intentionally written in another language
- Do not add docstrings, headers, or metadata that did not exist
- Do not "improve" style — only correct what is wrong

## Supported Languages

- **English** — primary language, standard grammar rules
- **Portuguese (BR)** — full orthographic and grammar correction
- **Spanish** — standard grammar correction
- For other languages, apply basic spelling corrections only

Glossary rules (if a `glossary.md` is present) apply **regardless of the document language**.

## Clarifications with the User

Use **AskUserQuestion** whenever:
- A correction might change the meaning of a sentence
- There is ambiguity about a term (e.g., a word that could be a product name or a common noun)
- It is unclear whether a passage in another language is intentional or an error
- The document mixes patterns and it is not obvious which to follow
- A term flagged in the glossary appears in a technical context where the original form may be acceptable

**Never assume** — asking is better than correcting incorrectly.

## Limitations

- Does not replace human review for legal or regulatory texts
- Does not correct argumentative style or narrative structure
