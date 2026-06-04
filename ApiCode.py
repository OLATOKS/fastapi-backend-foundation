from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


users = []

class User(BaseModel):
    name: str
    age: int
    is_admin : bool = False

@app.get("/")
def home():
    return{"message":"AI backend is running"}


@app.post("/create-user")
def create_user(user:User):
    users.append(user)
    return{
        "message": "user created successfully",
        "user":user
    }

@app.get("/users")
def get_all_users():
    return {"users": users}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    try:
        return {"user": users[user_id]}
    except IndexError:
        return {"error": "User not found"}