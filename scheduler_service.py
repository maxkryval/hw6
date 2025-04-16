import time
import requests
from fastapi import FastAPI
import threading
import os

TARGET_URL = os.environ.get("MAIN_SERVICE_URL", "http://client_service:8000/run-pipeline")

app = FastAPI()


def call_main_loop():
    while True:
        try:
            print("[Scheduler] Calling main service...")
            r = requests.get(TARGET_URL)
            print("[Scheduler] Response:", r.json)
        except Exception as e:
            print("[Scheduler] Failed:", e)
        time.sleep(10)


@app.on_event("startup")
def start_scheduler():
    threading.Thread(target=call_main_loop, daemon=True).start()


@app.get("/")
def root():
    return {"status": "scheduler is alive"}
