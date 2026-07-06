import os
import sys

sys.path.insert(
    0,
    os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
)

from logging.config import fileConfig

from alembic import context
from sqlalchemy import engine_from_config, pool

from app.database import Base, db_url
from app.models import *

config = context.config

config.set_main_option(
    "sqlalchemy.url",
    db_url.replace("%", "%%")
)

if config.config_file_name is not None:
    fileConfig(config.config_file_name)

target_metadata = Base.metadata

print("Tables found:", list(Base.metadata.tables.keys()))