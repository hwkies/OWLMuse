from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from sqlmodel import SQLModel
from server.db.db import engine, initialize
from server import models
from server.controllers import UserController

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLModel.metadata.create_all(engine)
    initialize()
    yield
    SQLModel.metadata.drop_all(engine)
    
app = FastAPI(lifespan=lifespan)

ORIGINS = [
    "http://localhost:4200",
    "http://localhost:8000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=ORIGINS,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(UserController.router)