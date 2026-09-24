from sqlalchemy import create_engine
from sqlalchemy import Column,Integer,String
from sqlalchemy.orm import declarative_base



engine = create_engine("sqlite:///database.db")
Base = declarative_base()

class TruckDB(Base):
    _tablename_= "trucks"
    
    id = Column(Integer,primary_key=True)
    licence_plate= Column(String)
    bundle_count = Column(Integer)
    
    

