from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str 
    

class UserCreate(UserBase):
    password:str
   
class UserResponse(UserBase):
    id: int
    is_admin: bool 
   

    model_config = {
        "from_attributes": True
    }
