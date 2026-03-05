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
This increment adds project listing for demo workflows:
- `GET /api/projects` with pagination (`limit`) and optional tone filter (`tone`)
- Stable response contract with `items` + `total`
- API tests for list/filter behavior and deterministic test isolation

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
