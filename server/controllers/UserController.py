from fastapi import APIRouter, HTTPException
from server.utils import get_db_connection
from server.models import User
from server.services.UserService import UserService

router = APIRouter(
    prefix='/api/user'
)

@router.post("/create_user")
def create_user(user: User):
    try:
        pass
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Error creating new user: {str(e)}')
    
@router.post("/login")
def login(user: User):
    try:
        pass
    except Exception as e:
        if str(e) == 'Invalid username or password':
            return HTTPException(status_code=401, detail=str(e))
        return HTTPException(status_code=500, detail=f'Error logging in: {str(e)}')

    