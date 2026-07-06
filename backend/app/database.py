
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker
from app.core.config import settings
try:
    engine = create_engine(settings.DATABASE_URL, echo=True)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
except Exception as e:
    raise ValueError("Failed to create database engine") from e



class Base(DeclarativeBase):
    pass
