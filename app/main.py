from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path
from uuid import UUID

from fastapi import FastAPI, HTTPException
from fastapi.responses import FileResponse

from .models import LaunchProject, LaunchProjectCreate

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
