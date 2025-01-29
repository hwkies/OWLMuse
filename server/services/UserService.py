from datetime import datetime
from server.models import UserPublic, User, UserCreate, UserCredentials, UserUpdate
from sqlmodel import select
from server.db.db import SessionDep

def get_user(username: str, session: SessionDep) -> UserPublic:
    """
    Get a user by their username.

    Args:
        username (str): The username of the user to get.
    
    Returns:
        UserPublic: The user object without the password.
    """
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise Exception("A user with that username doesn't exist!")
    return user


def create_user(user: UserCreate, session: SessionDep) -> UserPublic:
    """
    Create a new user with the given username, email, and password.

    Args:
        username (str): The username of the new user.
        email (str): The email of the new user.
        password (str): The password of the new user.
    
    Returns:
        UserPublic: The created user object without the password.
    """
    user = User(username=user.username, email=user.email, password=user.password, created_at=datetime.now())
    oldUser = session.exec(select(User).where(User.username == user.username)).first()
    if oldUser:
        raise Exception('A user with this username already exists!')
    session.add(user)
    session.commit()
    return user

    

def login(credentials: UserCredentials, session: SessionDep) -> UserPublic:
    """
    Log in a user with the given username and password.

    Args:
        username (str): The username of the user to log in.
        password (str): The password of the user to log in.
    
    Returns:
        UserPublic: The logged in user object without the password.
    """
    user = session.exec(select(User).where(User.username == credentials.username).where(User.password == credentials.password)).first()
    if not user:
        raise Exception("Incorrect username or password!")
    return user
    

def update_user(user_update: UserUpdate, session: SessionDep) -> UserPublic:
    """
    Update a users email or password.

    Args:
        username: The username of the account to update.
        email: The new email for the account.
        password: The new password for the account.

    Returns:
        UserPublic: The updated user object without the password.
    """
    user = session.exec(select(User).where(User.username == user_update.username)).first()
    if not user:
        raise Exception("A user with that username doesn't exist!")
    user_data = user_update.model_dump(exclude_unset=True)
    user.sqlmodel_update(user_data)
    session.add(user)
    session.commit()
    session.refresh(user)
    return user

def delete_user(username: str, session: SessionDep) -> UserPublic:
    """
    Delete a user by their username.

    Args:
        username (str): The username of the user to delete.
    
    Returns:
        UserPublic: The deleted user object.
    """
    user = session.exec(select(User).where(User.username == username)).first()
    if not user:
        raise Exception("A user with that username doesn't exist!")
    session.delete(user)
    session.commit()
    return user
