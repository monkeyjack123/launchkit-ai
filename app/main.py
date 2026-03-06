from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID

from fastapi import FastAPI, HTTPException, Query

from .generator import SUPPORTED_TONES, TONE_GUIDELINES, generate_launch_kit
from fastapi.responses import FileResponse

from .models import (
    LaunchKitOutput,
    LaunchProject,
    LaunchProjectCreate,
    LaunchProjectList,
    LaunchProjectStats,
    LaunchProjectUpdate,
    OutputSchemaResponse,
    SupportedTonesResponse,
    ToneGuidelinesResponse,
)

app = FastAPI(title="LaunchKit AI MVP", version="0.1.0")

_DB: dict[UUID, LaunchProject] = {}


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok"}


@app.post("/api/projects", response_model=LaunchProject, status_code=201)
def create_project(payload: LaunchProjectCreate) -> LaunchProject:
    project = LaunchProject(**payload.model_dump())
    _DB[project.id] = project
    return project


@app.get("/api/projects", response_model=LaunchProjectList)
def list_projects(
    limit: int = Query(default=20, ge=1, le=100),
    tone: str | None = Query(default=None, min_length=3, max_length=40),
) -> LaunchProjectList:
    projects = sorted(_DB.values(), key=lambda project: project.updated_at, reverse=True)
    if tone:
        normalized_tone = tone.strip().lower()
        projects = [project for project in projects if project.tone == normalized_tone]
    return LaunchProjectList(items=projects[:limit], total=len(projects))


@app.post("/api/generate-launch-kit", response_model=LaunchKitOutput)
def generate_launch_kit_output(payload: LaunchProjectCreate) -> LaunchKitOutput:
    try:
        return generate_launch_kit(payload)
    except ValueError as exc:
        raise HTTPException(status_code=400, detail=str(exc)) from exc


@app.get("/api/meta/tones", response_model=SupportedTonesResponse)
def supported_tones() -> SupportedTonesResponse:
    return SupportedTonesResponse(tones=sorted(SUPPORTED_TONES), default_tone="confident")


@app.get("/api/meta/tone-guidelines", response_model=ToneGuidelinesResponse)
def tone_guidelines() -> ToneGuidelinesResponse:
    return ToneGuidelinesResponse(default_tone="confident", guidelines=TONE_GUIDELINES)


@app.get("/api/meta/output-schema", response_model=OutputSchemaResponse)
def output_schema() -> OutputSchemaResponse:
    return OutputSchemaResponse(
        channels=["landing_page", "product_hunt", "x_thread", "email_sequence"],
        required_fields={
            "landing_page": ["headline", "subheadline", "primary_cta", "proof_points", "key_bullets"],
            "product_hunt": ["tagline", "first_comment", "launch_checklist", "cta"],
            "x_thread": ["hook", "tweets", "cta"],
            "email_sequence": ["subject", "body"],
        },
        constraints={
            "product_hunt.tagline": "Max 60 characters",
            "landing_page.proof_points": "Exactly 3 proof points",
            "x_thread.tweets": "Exactly 4 tweets",
            "email_sequence": "Exactly 3 emails",
        },
    )


@app.get("/api/projects/stats", response_model=LaunchProjectStats)
def project_stats() -> LaunchProjectStats:
    projects = sorted(_DB.values(), key=lambda project: project.updated_at, reverse=True)
    tone_breakdown: dict[str, int] = {}
    for project in projects:
        tone_breakdown[project.tone] = tone_breakdown.get(project.tone, 0) + 1

    latest_project_id = projects[0].id if projects else None
    return LaunchProjectStats(
        total_projects=len(projects),
        tone_breakdown=tone_breakdown,
        latest_project_id=latest_project_id,
    )


@app.get("/api/projects/{project_id}", response_model=LaunchProject)
def get_project(project_id: UUID) -> LaunchProject:
    project = _DB.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="project not found")
    project.updated_at = datetime.now(timezone.utc)
    return project


@app.patch("/api/projects/{project_id}", response_model=LaunchProject)
def update_project(project_id: UUID, payload: LaunchProjectUpdate) -> LaunchProject:
    project = _DB.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="project not found")

    changes = payload.model_dump(exclude_unset=True)
    for key, value in changes.items():
        setattr(project, key, value)

    project.updated_at = datetime.now(timezone.utc)
    _DB[project.id] = project
    return project


@app.get("/")
def app_shell() -> FileResponse:
    static_file = Path(__file__).parent / "static" / "index.html"
    return FileResponse(static_file)
