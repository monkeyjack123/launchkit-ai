import pytest
from pydantic import ValidationError

from app.models import LaunchProjectCreate, LaunchProjectUpdate


def test_model_validation_accepts_valid_input():
    model = LaunchProjectCreate(
        product_name="LaunchKit",
        one_liner="Generate launch assets from one clear brief.",
        target_audience="SaaS founders",
        launch_goal="Acquire first 100 waitlist users",
        tone="confident",
    )
    assert model.product_name == "LaunchKit"


def test_model_validation_rejects_short_one_liner():
    with pytest.raises(ValidationError):
        LaunchProjectCreate(
            product_name="LK",
            one_liner="too short",
            target_audience="SaaS founders",
            launch_goal="Acquire users",
            tone="confident",
        )


def test_update_model_normalizes_tone_when_provided():
    model = LaunchProjectUpdate(tone="  PlAyFuL  ")
    assert model.tone == "playful"
