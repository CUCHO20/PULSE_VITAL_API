from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.core.config import lifespan
from app.router import sensor

app = FastAPI(title="PulseVital API", lifespan=lifespan)

# CORS universal (cualquier origen)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(sensor.router)

@app.get("/")
async def root():
    return {"message": "Welcome to PulseVitalAPI"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=False)