from fastapi import FastAPI
from pydantic import BaseModel,Field

#pydantic model of truck
class Truck(BaseModel):
    licence_plate:str
    bundle_count:int=Field(ge=0)
#second pydantic model of response
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
#path parameters 



@app.get("/all-trucks")
def get_all_trucks():
    return trucks

@app.get("/truck_count")
def get_truck_count():
    return {"total_trucks":len(trucks)}

#query parameters 

@app.get("/truck-search")
def search_truck(limit:int):
    return {"limit":limit}

#path parameters 

@app.get("/trucks/{truck_id}")
def get_one_truck(truck_id:int,details:bool):
    return {"truck_id":truck_id,"details":details}
#path+query parameters 
