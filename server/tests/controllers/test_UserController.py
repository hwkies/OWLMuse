import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool
from server.db.db import get_session
from server.main import app
from server import models

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session


@pytest.fixture(name="client")  
def client_fixture(session: Session):  
    def get_session_override():  
        return session

    app.dependency_overrides[get_session] = get_session_override  

    client = TestClient(app)  
    yield client  
    app.dependency_overrides.clear()  

def test_create_user(client: TestClient):
    response = client.post("/api/user/create_user", json={
        "username": "testuser",
        "email": "testuser@test.com",
        "password": "testpassword"
    })
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "testuser@test.com"
    assert "created_at" in data

def test_create_user_empty_username(client: TestClient):
    response = client.post("/api/user/create_user", json={
        "username": "",
        "email": "test@test.com",
        "password": "testpassword"
    })
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Username, email, and password cannot be empty!"

def test_create_user_empty_email(client: TestClient):
    response = client.post("/api/user/create_user", json={
            "username": "testuser",
            "email": "",
            "password": "testpassword"
    })
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Username, email, and password cannot be empty!"

def test_create_user_empty_password(client: TestClient):
    response = client.post("/api/user/create_user", json={
        "username": "testuser",
        "email": "test@test.com",
        "password": ""
    })
    data = response.json()
    assert response.status_code == 400
    assert data["detail"] == "Username, email, and password cannot be empty!"

def test_create_user_already_exists(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.post("/api/user/create_user", json={
        "username": "testuser",
        "email": "test@test.com",
        "password": "testpassword"
    })
    assert response.status_code == 500

def test_get_user(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.get(f"/api/user/get_user/{user.username}")
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "test@test.com"
    assert "created_at" in data
    assert "password" not in data

def test_get_user_not_found(client: TestClient):
    response = client.get("/api/user/get_user/nonexistentuser")
    assert response.status_code == 404

def test_login(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.post("/api/user/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "test@test.com"
    assert "created_at" in data

def test_login_incorrect_password(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.post("/api/user/login", json={
        "username": "testuser",
        "password": "wrongpassword"
    })
    assert response.status_code == 401

def test_login_incorrect_username(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.post("/api/user/login", json={
        "username": "wronguser",
        "password": "testpassword"
    })
    assert response.status_code == 401

def test_login_error(client: TestClient, mocker):
    mock_login_error =  mocker.patch("server.services.UserService.login", side_effect=Exception("Simulated server error"))
    response = client.post("/api/user/login", json={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 500
    mock_login_error.assert_called_once()

def test_update_user_email(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.patch("/api/user/update_user", json={
        "username": "testuser",
        "email": "newemail@test.com",
    })
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "newemail@test.com"
    assert "created_at" in data

def test_update_user_password(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.patch("/api/user/update_user", json={
        "username": "testuser",
        "password": "newpassword",
    })
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "test@test.com"
    assert "created_at" in data

def test_update_user_not_found(client: TestClient):
    response = client.patch("/api/user/update_user", json={
        "username": "testuser",
        "password": "newpassword",
    })
    assert response.status_code == 500

def test_update_user_error(client: TestClient, mocker):
    mock_update_error = mocker.patch("server.services.UserService.update_user", side_effect=Exception("Simulated server error"))
    response = client.patch("/api/user/update_user", json={
        "username": "testuser",
        "password": "newpassword",
    })
    assert response.status_code == 500
    mock_update_error.assert_called_once()

def test_delete_user(session: Session, client: TestClient):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    response = client.delete(f"/api/user/delete_user/{user.username}")
    data = response.json()
    assert response.status_code == 200
    assert data["username"] == "testuser"
    assert data["email"] == "test@test.com"
    assert "created_at" in data

def test_delete_user_not_found(client: TestClient):
    response = client.delete("/api/user/delete_user/nonexistentuser")
    assert response.status_code == 500