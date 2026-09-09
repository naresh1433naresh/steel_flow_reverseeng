from fastapi import FastAPI
from pydantic import BaseModel, Field
#pydantic model truck 
class Truck (BaseModel):
    licence_plate :str
    bundle_count: int = Field(ge=0)
#second pydantic model 

class TruckResponse(BaseModel):
    plate:str
    count:int 
    message :str

truck=Truck(licence_plate="UP16562",
            bundle_count=415)
print(truck)

app=FastAPI()
@app.get('/health')
def health():
    return{"status":"healthy"}

@app.get('/hello')
def hello():
    return {"message ":"hello steelflow "}

@app.post('/trucks',status_code=201,response_model=TruckResponse)
def create_truck(truck:Truck):
    
    return{
        "plate" : truck.licence_plate ,
        "count": truck.bundle_count,
        "message": "truck received"
    }
trucks=[

    Truck(licence_plate="up3234",bundle_count=12),
    Truck(licence_plate="up5643",bundle_count=13),
    Truck(licence_plate="up2342",bundle_count=34)

]
@app.get('/trucks')
def get_truck():
    return truck

        
        

    
@app.get("/all-trucks")
def get_all_trucks():
    return trucks

    
    
@app.get("/all-trucks")
def get_all_trucks():
    return trucks

    




