from fastapi import FastAPI
from app.core.config import lifespan
from app.router import sensor

app = FastAPI(title="PulseVitalAPI", lifespan=lifespan)

app.include_router(sensor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PulseVitalAPI"}