from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID

from fastapi import FastAPI, HTTPException, Query

from .generator import generate_launch_kit
from fastapi.responses import FileResponse

from .models import LaunchKitOutput, LaunchProject, LaunchProjectCreate, LaunchProjectList

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


@app.get("/api/projects/{project_id}", response_model=LaunchProject)
def get_project(project_id: UUID) -> LaunchProject:
    project = _DB.get(project_id)
    if not project:
        raise HTTPException(status_code=404, detail="project not found")
    project.updated_at = datetime.now(timezone.utc)
    return project


@app.get("/")
def app_shell() -> FileResponse:
    static_file = Path(__file__).parent / "static" / "index.html"
    return FileResponse(static_file)
