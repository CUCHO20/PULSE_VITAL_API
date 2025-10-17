from beanie import init_beanie
from dotenv import load_dotenv
from pydantic_settings import BaseSettings
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

class Settings(BaseSettings):
    mongodb_uri: str

    class Config:
        env_file = ".env"

settings = Settings()

client = AsyncIOMotorClient(settings.mongodb_uri)

async def init_db():
    await init_beanie(
        database=client.get_default_database(),
        document_models=[],
    )

async def get_db():
    try:
        yield client
    finally:
        pass