from typing import List
import databases
import sqlalchemy
from pydantic import BaseModel
from routers import ping
from fastapi import Depends, FastAPI, Header, HTTPException



# SQLAlchemy specific code, as with any other app
DATABASE_URL = "sqlite:///./bptogether.db"
# DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("text", sqlalchemy.String),
    sqlalchemy.Column("completed", sqlalchemy.Boolean),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)


class NoteIn(BaseModel):
    text: str
    completed: bool


class Note(BaseModel):
    id: int
    text: str
    completed: bool


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


# @app.get("/notes/", response_model=List[Note])
# async def read_notes():
#     query = notes.select()
#     return await database.fetch_all(query)
#
#
# @app.post("/notes/", response_model=Note)
# async def create_note(note: NoteIn):
#     query = notes.insert().values(text=note.text, completed=note.completed)
#     last_record_id = await database.execute(query)
#     return {**note.dict(), "id": last_record_id}
#


app.include_router(ping.router)

# async def get_token_header(x_token: str = Header(...)):
#     if x_token != "fake-super-secret-token":
#         raise HTTPException(status_code=400, detail="X-Token header invalid")

# app.include_router(users.router)
# app.include_router(
#     items.router,
#     prefix="/items",
#     tags=["items"],
#     dependencies=[Depends(get_token_header)],
#     responses={404: {"description": "Not found"}},
# )
