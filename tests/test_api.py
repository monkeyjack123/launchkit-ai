import pytest
from fastapi.testclient import TestClient

from app.main import _DB, app


client = TestClient(app)


@pytest.fixture(autouse=True)
def clear_db():
    _DB.clear()
    yield
    _DB.clear()


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_create_and_get_project():
    payload = {
        "product_name": "LaunchKit",
        "one_liner": "Generate launch assets from one clear brief.",
        "target_audience": "Indie hackers",
        "launch_goal": "Get first 50 signups",
        "tone": "clear",
    }
    created = client.post("/api/projects", json=payload)
    assert created.status_code == 201
    body = created.json()
    project_id = body["id"]

    fetched = client.get(f"/api/projects/{project_id}")
    assert fetched.status_code == 200
    assert fetched.json()["product_name"] == payload["product_name"]


def test_create_project_contract_validation_errors():
    response = client.post(
        "/api/projects",
        json={
            "product_name": "A",
            "one_liner": "Too short",
            "target_audience": "Dev",
            "launch_goal": "Go",
            "tone": "ok",
        },
    )
    assert response.status_code == 422
    detail = response.json()["detail"]
    invalid_fields = {item["loc"][-1] for item in detail}
    assert {"product_name", "target_audience", "launch_goal", "tone"}.issubset(invalid_fields)


def test_create_project_contract_missing_required_field():
    payload = {
        "product_name": "LaunchKit",
        "target_audience": "Indie hackers",
        "launch_goal": "Get first 50 signups",
        "tone": "clear",
    }
    response = client.post("/api/projects", json=payload)
    assert response.status_code == 422
    detail = response.json()["detail"]
    assert any(item["loc"][-1] == "one_liner" for item in detail)


def test_get_missing_project_404():
    response = client.get("/api/projects/9e6b391e-bb8c-4e61-8fd8-0fa31ea8e7a0")
    assert response.status_code == 404


def test_list_projects_supports_limit_and_tone_filter():
    payloads = [
        {
            "product_name": "LaunchKit",
            "one_liner": "Generate launch assets from one clear brief.",
            "target_audience": "Indie hackers",
            "launch_goal": "Get first 50 signups",
            "tone": "clear",
        },
        {
            "product_name": "SignalBoard",
            "one_liner": "Track GTM signals from all channels in one feed.",
            "target_audience": "Growth teams",
            "launch_goal": "Acquire 20 design partners",
            "tone": "confident",
        },
        {
            "product_name": "LaunchLoop",
            "one_liner": "Convert raw notes into launch-ready copy in minutes.",
            "target_audience": "Solo founders",
            "launch_goal": "Book 15 demos",
            "tone": "clear",
        },
    ]

    for payload in payloads:
        created = client.post("/api/projects", json=payload)
        assert created.status_code == 201

    filtered = client.get("/api/projects?limit=1&tone=clear")
    assert filtered.status_code == 200
    data = filtered.json()
    assert data["total"] == 2
    assert len(data["items"]) == 1
    assert data["items"][0]["tone"] == "clear"


def test_generate_launch_kit_returns_four_channel_output():
    payload = {
        "product_name": "LaunchKit",
        "one_liner": "Generate launch assets from one clear brief.",
        "target_audience": "Indie hackers",
        "launch_goal": "Get first 50 signups",
        "tone": "clear",
    }

    response = client.post("/api/generate-launch-kit", json=payload)
    assert response.status_code == 200
    body = response.json()
    assert set(body.keys()) == {"landing_page", "product_hunt", "x_thread", "email_sequence"}
    assert len(body["email_sequence"]) == 3
    assert "headline" in body["landing_page"]
    assert "tagline" in body["product_hunt"]
    assert "tweets" in body["x_thread"]


def test_generate_launch_kit_rejects_unsupported_tone_with_actionable_error():
    payload = {
        "product_name": "LaunchKit",
        "one_liner": "Generate launch assets from one clear brief.",
        "target_audience": "Indie hackers",
        "launch_goal": "Get first 50 signups",
        "tone": "serious-enterprise",
    }

    response = client.post("/api/generate-launch-kit", json=payload)
    assert response.status_code == 400
    detail = response.json()["detail"]
    assert "Unsupported tone" in detail
    assert "clear" in detail
