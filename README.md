# launchkit-ai

AI-powered launch content generator for product teams and indie hackers.

## MVP increment (Issue 1)
This increment scaffolds a usable MVP shell with:
- FastAPI backend
- Launch project data model with required brief fields + timestamps
- Basic split-pane UI shell (`/`) for input/output workflow
- API endpoints for project create/get
- Test suite for API and model validation

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
