from pydantic import BaseModel, Field   
from typing import Optional

class TodoCreate(BaseModel): # Request for POST
    title: str = Field(min_length=1, max_length=140)
    done: bool = False

class TodoRead(BaseModel): # Request for GET
    id: int
    title: str
    done: bool 
    class Config:
        from_attributes = True
        
class TodoUpdate(BaseModel): # Request for Patch
    title: Optional[str] = None
    done: Optional[bool] = None


