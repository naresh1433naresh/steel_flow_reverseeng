from fastapi import FastAPI
from pydantic import BaseModel, Field

class Truck (BaseModel):
    licence_plate :str
    bundle_count: int = Field(ge=0)

truck=Truck(licence_plate="UP16562",
            bundle_count="415")
print(truck)

app=FastAPI()
@app.get('/health')
def health():
    return{"status":"healthy"}
@app.get('/hello')
def hello():
    return {"message ":"hello steelflow "}
@app.post('/trucks')
def create_truck(truck:Truck):
    
    return{
        "plate" : truck.licence_plate ,
        "count ": truck.bundle_count,
        "message ": "truck received"
    }
@app.get('/trucks')
def get_truck():
    return {
        "plate":truck.licence_plate,
        "count":truck.bundle_count


    }
@app.get('/trucks')
def get_truck():
    return {
        "plate":truck.licence_plate,
        "count":truck.bundle_count


    }




