from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
import pandas as pd
import kagglehub
import glob
from sqlmodel import SQLModel, create_engine
from server import models
from server.controllers import UserController

path = kagglehub.dataset_download('kiesmanh/owlmuse')

def load_csv_to_table(file_name: str, df: pd.DataFrame, engine):
    if file_name.startswith('hero'):
        df.to_sql('playerhero', con=engine, if_exists='append', index=False)
    elif file_name.startswith('phs'):
        df.to_sql('playermap', con=engine, if_exists='append', index=False)
    elif file_name.startswith('match'):
        df.to_sql('map', con=engine, if_exists='replace', index=False)
    elif file_name.startswith('player'):
        df.to_sql('player', con=engine, if_exists='replace', index=False)

def initialize(engine):
    csv_files = glob.glob(path + '/*.csv')
    for file in csv_files:
        df = pd.read_csv(file)
        file_name = file.split('\\')[-1]
        load_csv_to_table(file_name, df, engine)

@asynccontextmanager
async def lifespan(app: FastAPI):
    SQLITE_URL = 'sqlite:///db/owlmuse.sqlite'
    engine = create_engine(SQLITE_URL)
    SQLModel.metadata.create_all(engine)
    initialize(engine)
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