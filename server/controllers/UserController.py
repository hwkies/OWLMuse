from fastapi import APIRouter, HTTPException
from server.services import UserService
from server.db.db import SessionDep
from server.models import UserPublic, UserCreate, UserCredentials, UserUpdate

router = APIRouter(
    prefix='/api/users'
)

@router.get("/get_user/{username}", response_model=UserPublic)
def get_user(username: str, session: SessionDep):
    try:
        return UserService.get_user(username, session)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f'Error retrieving user: {str(e)}')

@router.post("/create_user/", response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
    if user.username == "" or user.email == "" or user.password == "":
        raise HTTPException(status_code=400, detail='Username, email, and password cannot be empty!')
    try:
        #Room to add more exceptios if needed
        return UserService.create_user(user, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating new user: {str(e)}')
    
@router.post("/login/", response_model=UserPublic)
def login(credentials: UserCredentials, session: SessionDep):
    try:
        return UserService.login(credentials, session)
    except Exception as e:
        if str(e) == 'Incorrect username or password!':
            raise HTTPException(status_code=401, detail=str(e))
        raise HTTPException(status_code=500, detail=f'Error logging in: {str(e)}')
    
@router.patch("/update_user/", response_model=UserPublic)
def update_user(user_update: UserUpdate, session: SessionDep):
    try:
        return UserService.update_user(user_update, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating user: {str(e)}')
    
@router.delete("/delete_user/{username}", response_model=UserPublic)
def delete_user(username: str, session: SessionDep):
    try:
        return UserService.delete_user(username, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error deleting user: {str(e)}')
