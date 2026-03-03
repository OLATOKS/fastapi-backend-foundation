from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{"message":"AI backend is running"}

@app.get("/about")
def about():
    return {"message": "This is the AI backend foundation project"}

@app.get("/user/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}

#@app.post("/tk")
#def yeahhhhhhhh(data: dict):
    #return {"you_sent": data}
