from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field, field_validator
from typing import Any


class LaunchProjectCreate(BaseModel):
    product_name: str = Field(min_length=2, max_length=120)
    one_liner: str = Field(min_length=10, max_length=240)
    target_audience: str = Field(min_length=5, max_length=200)
    launch_goal: str = Field(min_length=5, max_length=200)
    tone: str = Field(default="confident", min_length=3, max_length=40)

    @field_validator("tone")
    @classmethod
    def normalize_tone(cls, value: str) -> str:
        return value.strip().lower()


class LaunchProject(LaunchProjectCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))


class LaunchProjectList(BaseModel):
    items: list[LaunchProject]
    total: int


class LaunchProjectStats(BaseModel):
    total_projects: int
    tone_breakdown: dict[str, int]
    latest_project_id: UUID | None = None


class SupportedTonesResponse(BaseModel):
    tones: list[str]
    default_tone: str


class ToneGuidelinesResponse(BaseModel):
    default_tone: str
    guidelines: dict[str, dict[str, str]]


class OutputSchemaResponse(BaseModel):
    channels: list[str]
    required_fields: dict[str, list[str]]
    constraints: dict[str, str]


class LaunchKitOutput(BaseModel):
    landing_page: dict[str, Any]
    product_hunt: dict[str, Any]
    x_thread: dict[str, Any]
    email_sequence: list[dict[str, str]]
