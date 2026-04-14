from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

class DataModel(BaseModel):
    name: str
    value: str
    email: str = None

# Store data in memory
stored_data = []

@app.post("/api/receive")
def receive_data(data: DataModel):
    stored_data.append(data.dict())
    return {
        "status": "success",
        "received": data.dict(),
        "message": "Data received and ready for Dataverse"
    }

@app.get("/api/retrieve")
def retrieve_data():
    return {
        "status": "success",
        "data": stored_data,
        "count": len(stored_data)
    }

@app.get("/api/test")
def test():
    return {"status": "working"}
