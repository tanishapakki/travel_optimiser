import os

from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from dotenv import load_dotenv

load_dotenv()
db_url = os.getenv("DATABASE_URL")
if not db_url:
    raise ValueError("DATABASE_URL is not set in the environment")
try:
    engine = create_engine(db_url, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    raise ValueError("Failed to create database engine") from e



class Base(DeclarativeBase):
    pass
