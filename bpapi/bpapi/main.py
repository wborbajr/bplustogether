from typing import List

# importing database connection
from bpapi.db.dbconfig import database, engine, metadata
from fastapi import Depends, FastAPI, Header, HTTPException
from loguru import logger
# importing routes
from bpapi.routers import notes, ping

# log
logger.add(
    "../logs/bpapi.log",
    format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}",
)

metadata.create_all(engine)


app = FastAPI()


@app.on_event("startup")
async def startup():
    logger.info("Database Startup")
    await database.connect()


@app.on_event("shutdown")
async def shutdown():
    logger.info("Database Shutdown")
    await database.disconnect()


app.include_router(ping.router)
app.include_router(notes.router, prefix="/notes", tags=["notes"])
