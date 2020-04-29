from typing import List

from fastapi import Depends, FastAPI, Header, HTTPException

# importing database connection
from db.dbconfig import database, engine, metadata

# importing routes
from routers import ping

from loguru import logger

# log
logger.add(
    "../logs/bpapi.log", format="{time:YYYY-MM-DD at HH:mm:ss} | {level} | {message}"
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
