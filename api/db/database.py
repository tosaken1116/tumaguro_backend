import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session

load_dotenv()

DATABASE = 'postgresql'
USER = os.environ["POSTGRES_USER"]
PASSWORD = os.environ["POSTGRES_PASSWORD"]
HOST = os.environ["POSTGRES_HOST"]
NAME = os.environ["POSTGRES_DB"]

SQLALCHEMY_DATABASE_URL = "{}://{}:{}@{}/{}".format(
    DATABASE, USER, PASSWORD, HOST, NAME
)

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() -> Session:
    try:
        db = sessionLocal()
        yield db
    finally:
        db.close()
