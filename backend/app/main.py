from fastapi import FastAPI
from pydantic import BaseModel,Field

class Truck(BaseModel):
    licence_plate:str
    bundle_count:int=Field(ge=0)

class TruckResponse(BaseModel):
    plate:str
    count:int
    message:str

truck=Truck(
    licence_plate="UP16562",
    bundle_count=415
)

print(truck)

trucks=[
    Truck(licence_plate="up3234",bundle_count=12),
    Truck(licence_plate="up5643",bundle_count=13),
    Truck(licence_plate="up2342",bundle_count=34)
]

app=FastAPI()

@app.get("/health")
def health():
    return {"status":"healthy"}

@app.get("/hello")
def hello():
    return {"message":"hello steelflow"}

@app.post("/trucks",status_code=201,response_model=TruckResponse)
def create_truck(truck:Truck):
    trucks.append(truck)
    return{
        "plate":truck.licence_plate,
        "count":truck.bundle_count,
        "message":"truck received"
    }

@app.get("/trucks")
def get_one_truck():
    return truck

@app.get("/all-trucks")
def get_all_trucks():
    return trucks

@app.get("/truck_count")
def get_truck_count():
    return {"total_trucks":len(trucks)}