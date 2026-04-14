from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd

app = FastAPI()

class DataModel(BaseModel):
    name: str
    value: str
    email: str = None

# Load Excel file when app starts
def load_excel_data():
    try:
        df = pd.read_excel('posts_6000_raw_excel.xlsx')  # Change 'data.xlsx' to your filename
        return df.to_dict(orient='records')
    except Exception as e:
        return {"error": str(e)}

# Load data on startup
stored_data = load_excel_data()

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
