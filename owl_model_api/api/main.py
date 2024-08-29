from fastapi import FastAPI
import os
import pymssql
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:4200",  # Angular development server
    "http://localhost:80",  # If you access the API directly
    # Add any other origins you might need
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_db_connection():
    server = os.getenv('MSSQL_SERVER')
    database = os.getenv('MSSQL_DB')
    username = os.getenv('MSSQL_LOGIN')
    password = os.getenv('MSSQL_PASSWORD')
    
    conn = pymssql.connect(
        server=server,  # Use the service name defined in your docker-compose.yml
        user=username,               # This should match MSSQL_USER from your environment file
        password=password,  # This should match MSSQL_SA_PASSWORD from your environment file
        database=database       # This should match MSSQL_DB from your environment file
    )
    return conn

def row_to_dict(row):
    return {
        "player": row[0],
        "maps": row[1],
        "map_wins": row[2],
        "map_win_rate" : row[3],
        "matches": row[4],
        "match_wins": row[5],
        "match_win_rate": row[6]
    }

@app.get("/api/player_win_rates")
def get_player_win_rates():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM dbo.Player_Win_Rates")
    rows = cursor.fetchall()
    data = list(map(row_to_dict, rows))
    conn.close()
    return data

@app.get("/")
def root():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT TOP 1 * FROM dbo.Users")
    row = cursor.fetchone()
    conn.close()  # Don't forget to close the connection
    return {"message": f"Database connected: {row}"}