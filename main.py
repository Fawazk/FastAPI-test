from typing import Optional
from pydantic import BaseModel
from fastapi import FastAPI

app = FastAPI()

dummydb= []

class Data(BaseModel):
    id:int
    name:str
    price:float
    is_active:Optional[bool]=None


@app.get("/")
def read_root():
    return {"Welcome": "welcome"}

@app.get("/datas/")
def get_datas():
    return dummydb

@app.get("/data/{data_id}")
def get_data(data_id: int):
    return dummydb[data_id]

@app.post("/add-data")
def add_data(data:Data):
    dummydb.append(data.dict())
    return dummydb[-1]

@app.delete("/data-delete/{data_id}")
def delete_data(data_id:int):
    dummydb.pop(data_id)
    return {"status":"deleted success"}