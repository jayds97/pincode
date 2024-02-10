from typing import Union
import schemas,models
from database import get_db,engine
from fastapi import FastAPI,Depends
from sqlalchemy.orm import Session

app = FastAPI()

models.Base.metadata.create_all(bind=engine)
@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get('/first')
def test_path(db: Session = Depends(get_db)):
    all_users = db.query(models.PinDetails).all()
    return{"Message":all_users}

@app.post('/pin_det')
def pincode_det(data:schemas.pincode,db: Session = Depends(get_db)):
    print(data.pincode)
    pin_det = db.query(models.PinDetails).filter(models.PinDetails.pincode == data.pincode).all()

    print("pincode")

    
    return{"masse":pin_det}