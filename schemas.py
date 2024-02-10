from pydantic import BaseModel,EmailStr
from typing import Optional


class pincode (BaseModel):
    pincode:int