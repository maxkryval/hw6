from fastapi import FastAPI, Header, HTTPException
import requests
import os
from dotenv import load_dotenv
from fastapi.responses import JSONResponse

load_dotenv()
app = FastAPI()

APP_TOKEN = os.getenv("OPENROUTER_API_KEY")
DB_SERVICE_URL = "http://localhost:8001"
BUSINESS_SERVICE_URL = "http://localhost:8002"


@app.get("/")
def root():
    return JSONResponse(content={"description": "Client Service - orchestrates DB and Business Logic"})


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/run-pipeline")
def run_pipeline(authorization: str = Header(...)):
    print("Expected:", f"Bearer {APP_TOKEN}")
    print("Received:", authorization)
    if authorization != f"Bearer {APP_TOKEN}":
        raise HTTPException(status_code=401, detail="Unauthorized")

    db_data = requests.get(f"{DB_SERVICE_URL}/get").json()
    if not db_data["data"]:
        raise HTTPException(status_code=404, detail="No data in DB")

    last_item = db_data["data"][-1]
    processed = requests.post(f"{BUSINESS_SERVICE_URL}/process", json=last_item).json()
    save_response = requests.post(f"{DB_SERVICE_URL}/save", json=processed).json()
    return {"result": save_response}