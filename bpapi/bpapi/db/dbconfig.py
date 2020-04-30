from databases import Database
from sqlalchemy import (ARRAY, Column, DateTime, Integer, MetaData, String,
                        Table, create_engine, func)

# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./bptogether.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

# SQLAlchemy
# engine = create_engine(DATABASE_URL)
engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
metadata = MetaData()
notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)

# databases query builder
database = Database(DATABASE_URL)
