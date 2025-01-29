import pytest
from datetime import datetime
from fastapi.testclient import TestClient
from sqlmodel import create_engine, Session, SQLModel
from sqlmodel.pool import StaticPool
from server.db.db import get_session
from server.main import app
from server.services import UserService
from server import models

@pytest.fixture(name="session")
def session_fixture():
    engine = create_engine(
        "sqlite://", connect_args={"check_same_thread": False}, poolclass=StaticPool
    )
    SQLModel.metadata.create_all(engine)
    with Session(engine) as session:
        yield session

def test_create_user(session: Session):
    user = UserService.create_user(models.UserCreate(username="testuser", email="test@test.com", password="testpassword"), session)
    assert isinstance(user, models.User)
    assert user.username == "testuser"
    assert user.email == "test@test.com"

def test_create_user_already_exists(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    with pytest.raises(Exception) as excinfo:
        user = UserService.create_user(models.UserCreate(username="testuser", email="test@test.com", password="testpassword"), session)
    assert str(excinfo.value) == 'A user with this username already exists!'

def test_get_user(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    user_retrieved = UserService.get_user("testuser", session)
    assert isinstance(user_retrieved, models.User)
    assert user_retrieved.username == "testuser"
    assert user_retrieved.email == "test@test.com"

def test_get_user_does_not_exist(session: Session):
    with pytest.raises(Exception) as excinfo:
        user = UserService.get_user("testuser", session)
    assert str(excinfo.value) == "A user with that username doesn't exist!"

def test_login(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    user_logged_in = UserService.login(models.UserCredentials(username="testuser", password="testpassword"), session)
    assert isinstance(user_logged_in, models.User)
    assert user_logged_in.username == "testuser"
    assert user_logged_in.email == "test@test.com"

def test_login_incorrect_password(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    with pytest.raises(Exception) as excinfo:
        user_logged_in = UserService.login(models.UserCredentials(username="testuser", password="wrongpassword"), session)
    assert str(excinfo.value) == "Incorrect username or password!"

def test_login_incorrect_username(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()

    with pytest.raises(Exception) as excinfo:
        user_logged_in = UserService.login(models.UserCredentials(username="wronguser", password="testpassword"), session)
    assert str(excinfo.value) == "Incorrect username or password!"

def test_login_error(session: Session, mocker):
    mocker_exec = mocker.patch("sqlmodel.Session.exec", side_effect=Exception("Simulated server error"))
    with pytest.raises(Exception):
        user_logged_in = UserService.login(models.UserCredentials(username="testuser", password="testpassword"), session)
    mocker_exec.assert_called_once()

def test_update_user_email(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()
    updated_user = UserService.update_user(models.UserUpdate(username="testuser", email="update@test.com"), session)
    assert isinstance(updated_user, models.User)
    assert updated_user.username == "testuser"
    assert updated_user.email == "update@test.com"

def test_update_user_password(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()
    updated_user = UserService.update_user(models.UserUpdate(username="testuser", password="updatepassword"), session)
    assert isinstance(updated_user, models.User)
    assert updated_user.username == "testuser"
    assert updated_user.email == "test@test.com"
    assert updated_user.password == "updatepassword"

def test_update_user_does_not_exist(session: Session):
    with pytest.raises(Exception) as excinfo:
        updated_user = UserService.update_user(models.UserUpdate(username="testuser", email="test@test.com"), session)
    assert str(excinfo.value) == "A user with that username doesn't exist!"

def test_update_user_error(session: Session, mocker):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()
    mocker_exec = mocker.patch("sqlmodel.Session.exec", side_effect=Exception("Simulated server error"))
    with pytest.raises(Exception):
        updated_user = UserService.update_user(models.UserUpdate(username="testuser", email="update@test.com"), session)
    mocker_exec.assert_called_once()
    assert session.get(models.User, "testuser").email == "test@test.com"

def test_delete_user(session: Session):
    user = models.User(username="testuser", email="test@test.com", password="testpassword", created_at=datetime.now())
    session.add(user)
    session.commit()
    user_deleted = UserService.delete_user("testuser", session)
    assert isinstance(user_deleted, models.User)
    assert user_deleted.username == "testuser"
    assert user_deleted.email == "test@test.com"

def test_delete_user_does_not_exist(session: Session):
    with pytest.raises(Exception) as excinfo:
        user_deleted = UserService.delete_user("testuser", session)
    assert str(excinfo.value) == "A user with that username doesn't exist!"