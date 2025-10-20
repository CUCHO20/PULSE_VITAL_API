# PulseVital API

## Overview
PulseVital API is a scalable, asynchronous RESTful API built with **FastAPI** for handling data from the **MAX30102 sensor** (a pulse oximeter and heart rate monitor). It processes raw sensor readings (IR and Red LED values) and calculated metrics (heart rate in bpm, SpO2 in %, temperature in °C) in batches, storing them in **MongoDB Atlas** via **Beanie ODM** and **Motor** (async MongoDB driver). The API supports ingestion of FIFO-style batches (up to 32 samples) and retrieval of readings by device ID.

### Purpose
- **Core Functionality**: Receive batched sensor data from devices (e.g., ESP32 or Arduino), validate it (e.g., ADC values 0-262143), store in MongoDB, and query recent readings for monitoring vital signs.
- **Use Cases**: IoT health monitoring apps, wearable integrations, or telemedicine prototypes. It's designed for low-latency, serverless deployment (e.g., Vercel) with auto-scaling.
- **Key Features**:
  - Async endpoints for high concurrency.
  - Pydantic validation for input/output.
  - Layered architecture for maintainability.
  - Error handling for common issues (e.g., SSL handshakes with MongoDB).
- **Tech Stack**: FastAPI 0.115, Beanie 2.0, Motor 3.7, Pydantic v2, MongoDB Atlas, Vercel for deployment.

### Development History
This API evolved from a basic FastAPI setup to a production-ready layered architecture:
- **Initial Setup**: Created virtual env, installed deps, basic `main.py` with Uvicorn.
- **DB Integration**: Added Motor/Beanie for async MongoDB, fixed SSL issues with OCSP and CA files.
- **Data Structure**: Defined Pydantic schemas for MAX30102 data (raw ADC values, metrics).
- **Layered Architecture**: Separated concerns (routers for HTTP, services for business logic, CRUD for DB ops, models/schemas for data).
- **Troubleshooting**: Resolved Pydantic v2 validators (`@field_validator`), Beanie queries (`dict filters`, `Q`), collection init (`lazy init`), and Vercel compat (versions, env vars).
- **Deployment**: Configured `vercel.json` for serverless, fixed build errors (Motor/PyMongo compat), deployed to `https://pulse-vital-api.vercel.app`.

The project emphasizes clean code, testability, and scalability for IoT workloads.

## Project Structure
Follows a **Layered (Clean) Architecture** for separation of concerns:
- **Presentation Layer** (`routers/`): HTTP endpoints and input validation.
- **Application Layer** (`services/`): Business logic (e.g., rate checks, duplicates).
- **Domain Layer** (`schemas/` & `models/`): Data models (Pydantic for validation, Beanie for persistence).
- **Infrastructure Layer** (`crud/`): DB operations.
- **Core** (`core/`): Configs, DB client, lifespan events.

```
pulse_vital_api/
├── app/
│   ├── __init__.py
│   ├── main.py              # FastAPI app entrypoint
│   ├── core/
│   │   ├── __init__.py
│   │   ├── config.py        # Env vars, Motor client, Beanie init
│   │   └── security.py      # Auth stubs (future)
│   ├── routers/
│   │   ├── __init__.py
│   │   └── sensor.py        # Endpoints: POST/GET readings
│   ├── schemas/
│   │   ├── __init__.py
│   │   └── sensor.py        # Pydantic models (SensorReading, SensorBatch)
│   ├── models/
│   │   ├── __init__.py
│   │   └── sensor.py        # Beanie Documents (SensorReading)
│   ├── services/
│   │   ├── __init__.py
│   │   └── sensor_service.py # Logic: validation, processing
│   └── crud/
│       ├── __init__.py
│       └── sensor_crud.py   # DB ops: insert, find
├── tests/
│   └── test_sensor.py       # Pytest examples
├── .env                     # Env vars (git ignore!)
├── requirements.txt         # Deps: fastapi, motor, beanie, etc.
├── vercel.json             # Vercel config (builds, routes)
└── README.md               # This file
```

## Setup and Running Locally
1. **Clone/Setup Repo**:
   ```
   git clone https://github.com/CUCHO20/PULSE_VITAL_API.git
   cd PULSE_VITAL_API
   ```

2. **Virtual Environment**:
   - Windows: `python -m venv venv` then `venv\Scripts\activate`
   - macOS/Linux: `python3 -m venv venv` then `source venv/bin/activate`

3. **Install Dependencies**:
   ```
   pip install -r requirements.txt
   ```

4. **Environment Variables** (create `.env` in root):
   ```
   MONGODB_URI=mongodb+srv://user:pass@cluster.mongodb.net/pulsevital?retryWrites=true&w=majority
   DATABASE_NAME=pulsevital
   SECRET_KEY=your-secret-key
   ```
   - Get MONGODB_URI from Atlas dashboard (add your IP to Network Access).

5. **Run the Server**:
   ```
   uvicorn app.main:app --reload --host 0.0.0.0 --port 8000
   ```
   - Open http://127.0.0.1:8000/docs for Swagger UI.

6. **Test Endpoints**:
   - **POST /sensor/readings**: Send batch (returns validated batch).
   - **GET /sensor/readings/{device_id}?limit=10**: Retrieve readings (returns list).

## Deployment to Vercel
1. Push to GitHub (main branch).
2. In Vercel dashboard: New Project > Import repo > Root: `./` > Framework: Python.
3. Add env vars (MONGODB_URI, etc.) in Settings > Environment Variables.
4. Deploy – URL: https://pulse-vital-api.vercel.app/docs.
- Notes: Serverless timeouts 10s (free tier); use Pro for longer.

## Testing
- **Manual**: Use Swagger (`/docs`) or curl/Postman.
- **Automated**: Run `pytest tests/` (add more as needed).
- **DB Verification**: Check Atlas > Collections > sensor_readings.

## Potential Improvements
- Auth: JWT in `security.py`.
- Stats Endpoint: Average HR/SpO2.
- Docker: For local/prod consistency.
- CI/CD: GitHub Actions for tests/deploy.

For issues, check Vercel logs or open an issue on GitHub. Contributions welcome!

---

### Explanation of the Diagram
- **Purpose**: Visualizes the API's internal flow, emphasizing modularity (each layer handles one concern) and async ops (e.g., `await` implied in arrows). It's a sequence diagram to show step-by-step interaction, useful for debugging or onboarding.
- **Key Elements**:
  - **Client**: External (e.g., Postman or IoT device).
  - **Layers**: Router (HTTP handling), Service (logic/validation), CRUD (DB abstraction), Model (Beanie hydration), DB (Atlas storage).
  - **Async Nature**: Arrows represent `await` calls, ensuring non-blocking for high throughput.
  - **Error Paths**: Noted for validation (e.g., 404 if no data).
  - **Relevance**: Demonstrates why the architecture scales (e.g., easy to mock CRUD for tests) and handles MAX30102 batches efficiently (query by device_id index).
- **Customization**: Extend for POST (add insert flow) or add error branches (e.g., SSL retry in config).

This covers the full development story – let me know if you need expansions!