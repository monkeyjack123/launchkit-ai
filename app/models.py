from __future__ import annotations

from datetime import datetime, timezone
from uuid import UUID, uuid4

from pydantic import BaseModel, Field


class LaunchProjectCreate(BaseModel):
    product_name: str = Field(min_length=2, max_length=120)
    one_liner: str = Field(min_length=10, max_length=240)
    target_audience: str = Field(min_length=5, max_length=200)
    launch_goal: str = Field(min_length=5, max_length=200)
    tone: str = Field(default="confident", min_length=3, max_length=40)


class LaunchProject(LaunchProjectCreate):
    id: UUID = Field(default_factory=uuid4)
    created_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
    updated_at: datetime = Field(default_factory=lambda: datetime.now(timezone.utc))
