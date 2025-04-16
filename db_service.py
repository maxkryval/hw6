from fastapi import FastAPI

app = FastAPI()
db_storage = []


@app.get("/")
def root():
    return {"description": "In-memory Database Service"}


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/save")
def save_data(payload: dict):
    db_storage.append(payload)
    return {"status": "saved", "data": payload}


@app.get("/get")
def get_data():
    return {"data": db_storage}