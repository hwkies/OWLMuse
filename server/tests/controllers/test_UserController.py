from fastapi.testclient import TestClient
from server.controllers.UserController import router

client = TestClient(router)
def test_create_user():
    response = client.post("/api/user/create_user", json={
        "username": "testuser",
        "email": "testuser@test.com",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json().get("username") == "testuser"
    assert response.json().get("email") == "testuser@test.com"
    assert "password" not in response.json()
    assert "created_at" in response.json()