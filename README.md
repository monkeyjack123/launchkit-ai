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

### `GET /health`
Health check endpoint.

## Why this exists
Help teams ship launches faster with clear and measurable outputs.
