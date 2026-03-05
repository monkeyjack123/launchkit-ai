# LaunchKit AI — MVP Backlog (First 10 GitHub Issues)

## Issue 1 — Scaffold MVP app shell and project model
**Title:** `feat: scaffold app shell and launch project data model`

**Acceptance Criteria:**
- Repository contains running web app with basic layout (input pane + output pane)
- Project entity defined with required brief fields and timestamps
- Local dev environment documented in README
- Lint/test commands run successfully

---

## Issue 2 — Build launch brief input form with validation
**Title:** `feat: implement launch brief form with required-field validation`

**Acceptance Criteria:**
- Form includes all required MVP fields
- Required-field validation prevents submission when missing
- Inline validation messages shown clearly
- Valid submission payload matches backend contract

---

## Issue 3 — Implement generation API contract and orchestration
**Title:** `feat: add generate-launch-kit API endpoint for 4-channel output`

**Acceptance Criteria:**
- API accepts project brief payload and returns structured response for all 4 assets
- Endpoint returns consistent JSON schema
- Error responses include actionable message and status code
- Unit tests cover success and failure paths

---

## Issue 4 — Add prompt templates for landing page + Product Hunt copy
**Title:** `feat: add prompt templates for landing page and Product Hunt outputs`

**Acceptance Criteria:**
- Prompt templates generate all required sections for both channels
- Output follows expected length/style constraints
- Prompts include anti-hallucination guardrails
- Snapshot tests (or fixtures) validate schema-compliant outputs

---

## Issue 5 — Add prompt templates for X thread + email sequence
**Title:** `feat: add prompt templates for X thread and 3-email launch sequence`

**Acceptance Criteria:**
- X output includes hook + 6–10 tweets + CTA
- Email output includes 3 distinct emails with subject + body
- Tone parameter influences output style
- Prompt outputs are parsable to expected schema

---

## Issue 6 — Build output UI tabs with loading and error states
**Title:** `feat: implement output tabs for 4 channels with generation status states`

**Acceptance Criteria:**
- UI renders separate tabs for Landing, Product Hunt, X, Email
- Loading indicator shown during generation
- Friendly error state shown on generation failure
- Generated content displays in readable, editable sections

---

## Issue 7 — Inline editing, copy-to-clipboard, and section regeneration
**Title:** `feat: add inline editor, copy actions, and per-section regenerate`

**Acceptance Criteria:**
- User can edit any generated section inline
- Copy button works for each section
- Regenerate action exists per section and updates only targeted section
- Section regeneration preserves untouched sections

---

## Issue 8 — Persist projects and enable recent project reload
**Title:** `feat: persist launch projects and implement recent projects list`

**Acceptance Criteria:**
- Brief inputs and generated outputs are saved in database
- User can view and reopen recent projects
- Reloaded project restores latest saved state
- Basic DB migration/setup instructions documented

---

## Issue 9 — Add product analytics events for KPI tracking
**Title:** `feat: instrument core events for activation, completion, and quality KPIs`

**Acceptance Criteria:**
- Events fire for create/start/complete/fail/regenerate/feedback flows
- Event payload includes project_id and timestamps
- Event logging can be queried to compute:
  - Launch Kit Completion Rate
  - Time-to-First-Draft
  - Activation
  - Thumbs-up rate
- Tracking plan documented in repo

---

## Issue 10 — QA pass, prompt tuning, and release checklist
**Title:** `chore: complete MVP QA, prompt tuning, and alpha release checklist`

**Acceptance Criteria:**
- End-to-end happy path tested successfully
- Top 5 observed quality issues are fixed or documented
- Release checklist completed (env vars, error logging, rollback notes)
- MVP tagged/released for internal alpha testing

---

## KPI Summary (for backlog reference)
- **Launch Kit Completion Rate:** >= 60%
- **Median Time-to-First-Draft:** <= 90s
- **Activation Rate:** >= 50%
- **Thumbs-up Quality Feedback:** >= 70% positive