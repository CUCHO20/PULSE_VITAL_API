from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient
from beanie import init_beanie
from typing import List
from fastapi import FastAPI
import os

load_dotenv()

class Settings(BaseSettings):
    mongodb_uri: str
    database_name: str = "todo_data"

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.mongodb_uri)

async def init_db(document_models: List) -> None:
    db = client[settings.database_name]
    await init_beanie(database=db, document_models=document_models)

from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    from app.models.sensor import SensorReading
    await init_db([SensorReading])
    yield
    client.close()