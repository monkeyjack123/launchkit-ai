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


def test_get_missing_project_404():
    response = client.get("/api/projects/9e6b391e-bb8c-4e61-8fd8-0fa31ea8e7a0")
    assert response.status_code == 404
