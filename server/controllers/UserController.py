from fastapi import APIRouter, HTTPException
from server.services.UserService import UserService
from server.db.db import engine, SessionDep
from server.models import UserPublic, UserCreate, UserCredentials, UserUpdate

router = APIRouter(
    prefix='/api/user'
)

user_service = UserService()

@router.get("/get_user/", response_model=UserPublic)
def get_user(username: str, session: SessionDep):
    try:
        return user_service.get_user(username, session)
    except Exception as e:
        raise HTTPException(status_code=404, detail=f'Error retrieving user: {str(e)}')

@router.post("/create_user/", response_model=UserPublic)
def create_user(user: UserCreate, session: SessionDep):
    try:
        if user.username == '' or user.email == '' or user.password == '':
            return HTTPException(status_code=400, detail='Username, email, and password cannot be empty!')
        #Room to add more exceptios if needed
        return user_service.create_user(user, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error creating new user: {str(e)}')
    
@router.post("/login/", response_model=UserPublic)
def login(credentials: UserCredentials, session: SessionDep):
    try:
        return user_service.login(credentials, session)
    except Exception as e:
        if str(e) == 'Incorrect username or password!':
            raise HTTPException(status_code=401, detail=str(e))
        raise HTTPException(status_code=500, detail=f'Error logging in: {str(e)}')
    
@router.patch("/update_user/{username}", response_model=UserPublic)
def update_user(user_update: UserUpdate, session: SessionDep):
    try:
        return user_service.update_user(user_update, session)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f'Error updating user: {str(e)}')
