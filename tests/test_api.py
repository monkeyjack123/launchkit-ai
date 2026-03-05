from fastapi.testclient import TestClient

from app.main import app


client = TestClient(app)


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
