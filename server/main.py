from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from server.utils import get_db_connection
from server.controllers import UserController

app = FastAPI()

ORIGINS = [
    "http://localhost:4200",  # Angular development server
    "http://localhost:8000",  # If you access the API directly
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserController.router)

@app.get("/api/player_win_rates")
async def get_player_win_rates():
    conn = get_db_connection()
    cursor = conn.cursor(as_dict=True)
    cursor.execute("SELECT * FROM dbo.Player_Win_Rates")
    rows = cursor.fetchall()
    conn.close()
    return rows