from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException

# importing database connection
from db.dbconfig import database, engine, metadata

# importing routes
from routers import ping

metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


app.include_router(ping.router)
