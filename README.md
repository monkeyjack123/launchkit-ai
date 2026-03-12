# launchkit-ai

AI-powered launch content generator for product teams and indie hackers.

## MVP increment (Issue 1)
This increment scaffolds a usable MVP shell with:
- FastAPI backend
- Launch project data model with required brief fields + timestamps
- Basic split-pane UI shell (`/`) for input/output workflow
- API endpoints for project create/get
- Test suite for API and model validation

## MVP increment (Issue 2)
This increment adds a usable brief submission flow:
- Interactive launch brief form wired to `POST /api/projects`
- Client-side field validation with inline error messages
- API contract validation tests for malformed payloads and missing required fields
- Success state that renders created project JSON as demo output

## MVP increment (Issue 3)
This increment adds generation orchestration for demo workflows:
- `POST /api/generate-launch-kit` returns 4-channel structured output
- Channel bundles: landing page, Product Hunt copy, X thread, and 3-email sequence
- Actionable 400 error for unsupported tone values
- API tests for success and failure paths

## MVP increment (Issue 4)
This increment improves tone handling consistency across create/list/generate flows:
- Normalizes `tone` inputs (trim + lowercase) at API contract level
- Makes tone filtering case-insensitive and whitespace-tolerant in `GET /api/projects`
- Adds regression tests for normalized create + filter behavior

## MVP increment (Issue 5)
This increment adds lightweight portfolio visibility for launch ops:
- New `GET /api/projects/stats` endpoint with aggregate project counts
- Tone distribution breakdown for quick campaign mix checks
- Latest project pointer for basic recency tracking in dashboards
- API coverage for empty + populated stats scenarios

## MVP increment (Issue 6)
This increment hardens launch content template quality for landing + Product Hunt output:
- Added explicit landing-page proof points (anti-hallucination + clarity guardrails)
- Added Product Hunt launch checklist field for pre-post verification cues
- Enforced tagline trimming to 60 chars for marketplace-style brevity
- Added API tests validating template shape and guardrail content

## MVP increment (Issue 7)
This increment exposes output-contract metadata for client builders:
- Added `GET /api/meta/output-schema` for channel-level required fields
- Added explicit generation constraints (tagline length, tweet/email counts, proof-point count)
- Added API tests to lock schema ordering and constraint values

## MVP increment (Issue 8)
This increment adds partial-update support for saved launch projects:
- Added `PATCH /api/projects/{project_id}` to update selected brief fields
- Preserves existing fields when omitted to support iterative brief refinement
- Normalizes `tone` during updates (trim + lowercase) for consistent filtering/analytics
- Added model + API tests for update success and 404 handling

## MVP increment (Issue 9)
This increment adds baseline analytics instrumentation for KPI tracking:
- Auto-records lifecycle events (`project_created`, `generation_started`, `generation_completed`, `generation_failed`, `project_updated`)
- Added manual event ingestion endpoint for UX signal capture (`feedback_submitted`)
- Added `GET /api/analytics/summary` for quick event-volume and event-type rollups
- Added API tests covering lifecycle auto-logging and manual feedback event capture

## MVP increment (Issue 9 follow-up)
This increment closes the regenerate analytics gap:
- Added `POST /api/projects/{project_id}/regenerate` for per-section regeneration (`landing_page`, `product_hunt`, `x_thread`, `email_sequence`)
- Regeneration now records `section_regenerated` analytics events
- Added API test coverage for regenerate output contract + analytics tracking

## Quickstart

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
pytest
uvicorn app.main:app --reload
```

Open: `http://127.0.0.1:8000/`

## API

### `GET /api/projects?limit=20&tone=clear`
List launch projects ordered by latest update.

Query params:
- `limit` (1-100, default 20)
- `tone` (optional exact tone match)

Response:
```json
{
  "items": [],
  "total": 0
}
```

### `POST /api/generate-launch-kit`
Generate structured launch assets from a brief.

Example payload:
```json
{
  "product_name": "LaunchKit",
  "one_liner": "Generate launch assets from one clear brief.",
  "target_audience": "Indie hackers",
  "launch_goal": "Get first 50 signups",
  "tone": "clear"
}
```

Response keys:
- `landing_page`
- `product_hunt`
- `x_thread`
- `email_sequence`

### `GET /api/meta/tones`
Return supported launch tones and default tone for client-side form controls.

Response:
```json
{
  "tones": ["clear", "confident", "playful", "technical"],
  "default_tone": "confident"
}
```

### `GET /api/projects/stats`
Return aggregate project stats for quick dashboard summaries.

Response:
```json
{
  "total_projects": 3,
  "tone_breakdown": {
    "clear": 2,
    "confident": 1
  },
  "latest_project_id": "f7e0f915-4d5f-4f6d-a99d-737f95ad6a1a"
}
```

### `GET /api/meta/tone-guidelines`
Return per-tone writing guidance for client-side prompt helpers and UX hints.

Response:
```json
{
  "default_tone": "confident",
  "guidelines": {
    "clear": {
      "voice": "Straightforward and concrete.",
      "focus": "Clarity, outcomes, and low-jargon messaging."
    },
    "confident": {
      "voice": "Bold and decisive without hype.",
      "focus": "Momentum, differentiation, and clear CTA intent."
    }
  }
}
```

### `GET /api/meta/output-schema`
Return generation output contract metadata for frontend validators/editors.

Response:
```json
{
  "channels": ["landing_page", "product_hunt", "x_thread", "email_sequence"],
  "required_fields": {
    "landing_page": ["headline", "subheadline", "primary_cta", "proof_points", "key_bullets"],
    "product_hunt": ["tagline", "first_comment", "launch_checklist", "cta"],
    "x_thread": ["hook", "tweets", "cta"],
    "email_sequence": ["subject", "body"]
  },
  "constraints": {
    "product_hunt.tagline": "Max 60 characters",
    "landing_page.proof_points": "Exactly 3 proof points",
    "x_thread.tweets": "Exactly 4 tweets",
    "email_sequence": "Exactly 3 emails"
  }
}
```

### `POST /api/projects/{project_id}/regenerate`
Regenerate one output section for a saved project and track the action in analytics.

Example payload:
```json
{
  "section": "x_thread"
}
```

### `POST /api/analytics/events`
Record a product analytics event.

Example payload:
```json
{
  "event_type": "feedback_submitted",
  "project_id": "f7e0f915-4d5f-4f6d-a99d-737f95ad6a1a"
}
```

Supported `event_type` values:
- `project_created`
- `generation_started`
- `generation_completed`
- `generation_failed`
- `project_updated`
- `feedback_submitted`
- `section_regenerated`

### `GET /api/analytics/summary`
Return aggregate event counters for quick KPI rollups.

Response:
```json
{
  "total_events": 12,
  "by_type": {
    "project_created": 4,
    "generation_started": 3,
    "generation_completed": 3,
    "feedback_submitted": 2
  },
  "latest_event_at": "2026-03-11T05:45:00Z"
}
```

### `POST /api/projects`
Create a launch project.

Example payload:
```json
{
  "product_name": "LaunchKit",
  "one_liner": "Generate launch assets from one clear brief.",
  "target_audience": "Indie hackers",
  "launch_goal": "Get first 50 signups",
  "tone": "clear"
}
```

### `GET /api/projects/{project_id}`
Load a previously created project.

### `PATCH /api/projects/{project_id}`
Partially update a launch project.

Example payload:
```json
{
  "launch_goal": "Get first 100 signups",
  "tone": "confident"
}
```

### `GET /health`
Health check endpoint.

## Why this exists
Help teams ship launches faster with clear and measurable outputs.
