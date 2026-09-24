from fastapi import FastAPI,HTTPException
from pydantic import BaseModel,Field
import sqlite3
from sqlalchemy import create_engine


app=FastAPI()


#......................................................................................
#to have reusable functions 
def get_trucks():
    connection = sqlite3.connect("database.db")
    cursor = connection.cursor()

    cursor.execute("SELECT * FROM trucks ")
    rows = cursor.fetchall()

    connection.close()
    return rows
# adding endpoints to connect ro fastapi
@app.get("/trucks")
def read_trucks():
    return get_trucks()



#................................................................................................

    
#function to add truck attributes 
def add_truck(licence_plate,bundle_count):
    connection=sqlite3.connect("database.db")
    cursor=connection.cursor()

    cursor.execute(""" INSERT into trucks (licence_plate,bundle_count)
                        values (?,?)""",(licence_plate,bundle_count))
    connection.commit()
    connection.close()





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




@app.get("/health")
def health():
    return {"status":"healthy"}

@app.get("/hello")
def hello():
    return {"message":"hello steelflow"}
#post endpoint

@app.post("/trucks",status_code=201,response_model=TruckResponse)
def create_truck(truck:Truck):
    add_truck(truck.licence_plate,truck.bundle_count)
    return{
        "plate":truck.licence_plate,
        "count":truck.bundle_count,
        "message":"truck received"
    }
#path parameters 




@app.get("/truck_count")
def get_truck_count():
    return {"total_trucks": len(get_trucks())}

#query parameters 

@app.get("/truck-search")
def search_truck(limit:int):
    return {"limit":limit}

#path parameters 

@app.get("/trucks/{truck_id}")
def get_one_truck(truck_id:int,details:bool):
    return {"truck_id":truck_id,"details":details}
#path+query parameters
@app.get("/truck_error")
def get_truck_error():
    raise HTTPException(status_code=404,detail="truck not found ")
