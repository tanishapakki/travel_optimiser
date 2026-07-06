from app.database import engine
from app.base import Base

# Import every model
from app.models import *

Base.metadata.create_all(bind=engine)

print("Tables created successfully!")