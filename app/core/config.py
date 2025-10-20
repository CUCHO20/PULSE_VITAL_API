from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from typing import List
from fastapi import FastAPI, Depends
from contextlib import asynccontextmanager
import os

load_dotenv()

class Settings(BaseSettings):
    mongodb_uri: str
    database_name: str = "todo_data"

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.mongodb_uri)

_initialized = False

async def init_db(document_models: List) -> None:
    global _initialized
    if not _initialized:
        db = client[settings.database_name]
        await init_beanie(database=db, document_models=document_models)
        _initialized = True

async def get_db_init():
    from app.models.sensor import SensorReading
    await init_db([SensorReading])
    yield

@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.models.sensor import SensorReading
    await init_db([SensorReading])
    yield
    client.close()