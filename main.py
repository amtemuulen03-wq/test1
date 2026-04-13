from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class DataModel(BaseModel):
    name: str
    value: str
    email: str = None

@app.post("/api/receive")
def receive_data(data: DataModel):
    # Your data is here
    print(f"Received: {data.name}, {data.value}")
    return {
        "status": "success",
        "received": data.dict(),
        "message": "Data received and ready for Dataverse"
    }

@app.get("/api/test")
def test():
    return {"status": "working"}
