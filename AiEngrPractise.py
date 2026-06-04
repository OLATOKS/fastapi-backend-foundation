from fastapi import FastAPI, HTTPException, Depends
from sqlalchemy.orm import Session
from database import SessionLocal, engine 
from schemas import UserCreate, UserResponse 
from crud import create_user, get_user_by_email 
import models

app = FastAPI()


models.Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close() 

@app.post("/users", response_model=UserResponse)
def create_new_user(user: UserCreate, db: Session = Depends(get_db)):
    EmailCheck = get_user_by_email(db,user.email)
    if  EmailCheck:
        raise HTTPException(status_code=400, detail="Email already is used use another")
    return create_user(db,user)
                                      