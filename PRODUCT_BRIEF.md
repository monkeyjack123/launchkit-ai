# LaunchKit AI — Product Brief

## 1) Product Summary
LaunchKit AI helps founders and product teams generate launch-ready marketing copy in minutes. The MVP focuses on four high-impact launch assets:
- Landing page copy
- Product Hunt post
- X (Twitter) launch thread
- Email launch sequence

The product turns a simple product input form into polished, channel-specific copy with editable tone and CTA options.

## 2) Problem
Early-stage teams struggle to produce consistent, high-quality launch messaging quickly. They often:
- Spend days drafting copy across channels
- Lose consistency in positioning and voice
- Miss launch windows due to content bottlenecks
- Lack confidence in launch narrative quality

## 3) Target Users
### Primary
- Solo founders and indie hackers preparing product launches

### Secondary
- Small startup teams (PM/marketing/founder-led)
- Agencies creating launch copy for multiple clients

## 4) Core Value Proposition
"Generate complete launch copy across your key channels in under 10 minutes — with consistent positioning and tone."

## 5) MVP Scope (2 weeks)
### In Scope
- Guided input form (product name, audience, problem, solution, key features, offer, tone)
- Generation for 4 outputs:
  1. Landing page copy (headline, subheadline, benefits, CTA)
  2. Product Hunt post (tagline, short + full description, first comment)
  3. X thread (hook + 6–10 tweets)
  4. Email sequence (3 emails: announce, value, CTA)
- Output editor with copy/refresh per section
- Project save/load (basic)

### Out of Scope (for MVP)
- Team collaboration
- Brand kit upload / deep personalization
- Multilingual generation
- Analytics dashboards beyond basic usage logging
- Direct publishing integrations (X, Product Hunt, ESP)

## 6) User Journey (MVP)
1. User creates a project
2. Fills launch brief form
3. Clicks “Generate Launch Kit”
4. Reviews generated copy by channel
5. Regenerates specific sections if needed
6. Edits and copies/exports final assets

## 7) Success Metrics (Measurable KPI)
### North Star KPI
- **Launch Kit Completion Rate**: % of created projects that generate all 4 assets in one session
  - Target (2 weeks post-release): **>= 60%**

### Supporting KPI
- **Time-to-First-Draft**: median time from form submit to first full kit generated
  - Target: **<= 90 seconds**
- **First-Session Activation**: % of signups creating at least one launch project
  - Target: **>= 50%**
- **Section Regeneration Rate**: avg regeneration actions per completed kit
  - Target: **1–4** (indicates useful iteration without severe quality gaps)
- **User Satisfaction Pulse**: in-app thumbs-up on generated kit
  - Target: **>= 70% positive**

## 8) Risks & Assumptions
### Assumptions
- Users can provide enough context in a short brief to generate usable copy
- Single-pass generation quality is high enough for editing, not blank-page replacement

### Risks
- Output quality inconsistency across niches
- Hallucinated claims in copy
- Tone mismatch to user expectations

### Mitigations
- Structured prompts with guardrails (no fabricated metrics/claims)
- Regenerate by section
- Explicit editable tone and style controls

## 9) Launch Plan (MVP)
- Private alpha with 10–20 founders
- Gather qualitative feedback on copy quality and speed
- Iterate prompt templates and UX on top 3 pain points
- Public beta launch on Product Hunt + X

## 10) Definition of MVP Success (End of initial 2-week build + 2-week validation)
- Product ships with all 4 generators
- At least 20 real users complete full launch kits
- North Star KPI reaches >= 60% in early cohort
- At least 5 users report using output in an actual launch