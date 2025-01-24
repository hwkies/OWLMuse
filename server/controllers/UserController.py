from fastapi import APIRouter, HTTPException
from server.utils import get_db_connection
from server.models.User import User
from server.services.UserService import UserService

router = APIRouter(
    prefix='/api/user'
)

@router.post("/create_user")
def create_user(user: User):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        user_service = UserService(cursor)
        created_user = user_service.create_user(user)
        conn.close()
        return created_user
    except Exception as e:
        return HTTPException(status_code=500, detail=f'Error creating new user: {str(e)}')
    
@router.post("/login")
def login(user: User):
    try:
        conn = get_db_connection()
        cursor = conn.cursor(as_dict=True)
        user_service = UserService(cursor)
        logged_in_user = user_service.login(user.username, user.password)
        conn.close()
        return logged_in_user
    except Exception as e:
        if str(e) == 'Invalid username or password':
            return HTTPException(status_code=401, detail=str(e))
        return HTTPException(status_code=500, detail=f'Error logging in: {str(e)}')

    