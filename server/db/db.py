import glob
import kagglehub
import pandas as pd
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session

path = kagglehub.dataset_download('kiesmanh/owlmuse')

SQLITE_URL = 'sqlite:///db/owlmuse.sqlite'
engine = create_engine(SQLITE_URL)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def load_csv_to_table(file_name: str, df: pd.DataFrame, engine):
    if file_name.startswith('hero'):
        df.to_sql('playerhero', con=engine, if_exists='append', index=False)
    elif file_name.startswith('phs'):
        df.to_sql('playermap', con=engine, if_exists='append', index=False)
    elif file_name.startswith('match'):
        df.to_sql('map', con=engine, if_exists='replace', index=False)
    elif file_name.startswith('player'):
        df.to_sql('player', con=engine, if_exists='replace', index=False)

def initialize():
    csv_files = glob.glob(path + '/*.csv')
    for file in csv_files:
        df = pd.read_csv(file)
        file_name = file.split('\\')[-1]
        load_csv_to_table(file_name, df, engine)