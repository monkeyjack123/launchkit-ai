# LaunchKit AI — 2-Week MVP Spec

## 1) Objective
Deliver a functional web MVP that generates launch copy for 4 channels from one structured brief, with acceptable speed, usability, and output quality.

## 2) Functional Requirements

## 2.1 Project & Input
- User can create a new launch project
- Required input fields:
  - Product name
  - One-line product summary
  - Target audience
  - Problem statement
  - Solution/value proposition
  - Top 3 features/benefits
  - Offer/CTA
  - Preferred tone (e.g., bold, friendly, technical)
- Validation for required fields

## 2.2 Copy Generation
Single action to generate all 4 deliverables:

1. **Landing Page Copy**
   - Headline
   - Subheadline
   - 3 benefit bullets
   - Primary CTA

2. **Product Hunt Post**
   - Tagline (<= 60 chars target)
   - Short description
   - Full description
   - First comment draft

3. **X Thread**
   - Hook tweet
   - 6–10 tweet thread body
   - Final CTA tweet

4. **Email Sequence (3 emails)**
   - Email 1: launch announcement
   - Email 2: problem/benefit deepening
   - Email 3: CTA/final push

## 2.3 Editing & Iteration
- User can edit generated text inline
- User can regenerate per section (e.g., only X hook)
- User can copy each section to clipboard

## 2.4 Persistence
- Save project input + generated output
- Re-open recent projects

## 2.5 Basic Instrumentation
Track events:
- project_created
- generation_started
- generation_completed
- generation_failed
- section_regenerated
- project_completed_all_4_assets
- thumbs_feedback (up/down)

## 3) Non-Functional Requirements
- Median generation latency for full kit: <= 90 seconds
- System availability during MVP test window: >= 99% (best effort)
- Graceful failure messaging when generation fails
- Basic data protection: no public exposure of project data

## 4) UX Requirements
- Clean single-page workflow with 3 areas:
  1. Brief input panel
  2. Generate action/status
  3. Output tabs by channel
- Loading state with progress message during generation
- Empty-state guidance and examples

## 5) Technical Approach (MVP-level)
- Frontend: React/Next.js (or equivalent)
- Backend: Node API routes/service
- LLM provider: configurable model endpoint
- Storage: lightweight DB (Postgres/Supabase/SQLite acceptable for MVP)
- Prompting: channel-specific templates + shared product context block

## 6) Prompt Guardrails
- Avoid fabricated customer counts/revenue claims unless user provides them
- Avoid guaranteed outcome language ("will 10x")
- Keep channel-appropriate length constraints
- Preserve consistent product positioning across all outputs

## 7) Acceptance Criteria (System-Level)
1. User can submit a valid brief and receive all 4 assets in one flow
2. User can regenerate at least one section without regenerating everything
3. User can edit and copy each generated section
4. Project persists and can be reloaded with generated outputs
5. Instrumentation events fire for creation, generation, completion, and feedback

## 8) KPI Targets (First 2 weeks after release)
- Launch Kit Completion Rate >= 60%
- Time-to-First-Draft (median) <= 90s
- Activation >= 50%
- Thumbs-up feedback >= 70%

## 9) Delivery Timeline (10 working days)
### Week 1
- Day 1: Product skeleton, data model, input form
- Day 2: Generation backend contract + prompt templates v1
- Day 3: Implement landing + PH outputs
- Day 4: Implement X thread + email outputs
- Day 5: End-to-end generation + error handling

### Week 2
- Day 6: Inline editor + section regeneration
- Day 7: Persistence (save/load) + recent projects
- Day 8: Instrumentation + KPI dashboard queries (basic)
- Day 9: QA, prompt tuning, UX polish
- Day 10: Internal alpha release + fix critical bugs

## 10) Open Questions
- Auth requirement for MVP (magic link vs no-auth local projects)?
- Export format priority (clipboard only vs markdown/doc export)?
- Which model/temperature settings optimize quality vs speed?