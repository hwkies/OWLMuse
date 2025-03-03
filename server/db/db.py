import glob
import kagglehub
import pandas as pd
from typing import Annotated
from fastapi import Depends
from sqlmodel import create_engine, Session
from transformers import AutoTokenizer, AutoModelForTableQuestionAnswering

path = kagglehub.dataset_download('kiesmanh/owlmuse')

SQLITE_URL = 'sqlite:///db/owlmuse.sqlite'
engine = create_engine(SQLITE_URL)

def get_session():
    with Session(engine) as session:
        yield session

SessionDep = Annotated[Session, Depends(get_session)]

def initialize():
    tables = {'hero': pd.DataFrame(), 'phs': pd.DataFrame(), 'map': pd.DataFrame(), 'player': pd.DataFrame()}
    csv_files = glob.glob(path + '/*.csv')
    for file in csv_files:
        df = pd.read_csv(file)
        file_name = file.split('\\')[-1].split('/')[-1]
        file_start_word = file_name.split('_')[0]
        if file_start_word in tables.keys():
            tables[file_start_word] = pd.concat([tables[file_start_word], df])
    for tablename in tables.keys():
        tables[tablename].to_sql(tablename, con=engine, if_exists='replace', index=False)