from pydantic_settings import BaseSettings
from dotenv import load_dotenv
from motor.motor_asyncio import AsyncIOMotorClient  # Cliente async para Beanie
from beanie import init_beanie
from typing import List
from fastapi import FastAPI  # Para lifespan
import os

load_dotenv()  # Carga .env

class Settings(BaseSettings):
    mongodb_uri: str
    database_name: str = "todo_data"  # ¡Nuevo! Nombre de la DB (puedes cambiarlo)

    class Config:
        env_file = ".env"

settings = Settings()

# Cliente async de Motor (NO MongoClient sync)
client = AsyncIOMotorClient(settings.mongodb_uri)

async def init_db(document_models: List) -> None:
    """Inicializa Beanie con el database async."""
    # ¡Cambio clave! Especifica la DB explícitamente en lugar de get_default_database()
    db = client[settings.database_name]  # e.g., client["pulsevital"]
    await init_beanie(database=db, document_models=document_models)

# Dependencia para lifespan (startup/shutdown)
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(app: FastAPI):
    # Startup: init DB
    from app.models.sensor import SensorReading
    await init_db([SensorReading])
    yield
    # Shutdown: cierra cliente
    client.close()