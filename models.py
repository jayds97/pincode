from sqlalchemy import Column,Integer,String
from database import Base
from sqlalchemy.sql.sqltypes import TIMESTAMP
from sqlalchemy.sql.expression import text


class PinDetails(Base):
    __tablename__ ="all_india_PO_list_without_APS_offices_ver2_lat_long"
    
    
    officename =Column(String(50),nullable=True)
    pincode =Column(Integer,nullable=False)
    officeType = Column(String(50),nullable=True)
    Deliverystatus = Column(String(50),nullable=True)
    divisionname = Column(String(50),nullable=True)
    regionname = Column(String(50),nullable=True)
    circlename = Column(String(50),nullable=True)
    Taluk = Column(String(50),nullable=True)
    Districtname = Column(String(50),nullable=True)
    statename = Column(String(50),nullable=True)
    Telephone = Column(String(50),nullable=True)
    Related_Suboffice = Column(String(50),nullable=True)
    Related_Headoffice = Column(String(50),nullable=True)
    longitude = Column(String(50),nullable=True)
    latitude = Column(String(50),nullable=True)
    id = Column(Integer,primary_key=True,autoincrement=True)