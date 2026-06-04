# crud.py
from sqlalchemy.orm import Session
from passlib.context import CryptContext
import models, schemas

# This handles password hashing - bcrypt is the industry standard
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(password: str) -> str:
    return pwd_context.hash(password)

def get_user_by_email(db: Session, email: str):
    # Query the database for a user with this email
    return db.query(models.User).filter(models.User.email == email).first()

def create_user(db: Session, user: schemas.UserCreate):
    # Step 1: hash the plain text password
    hashed = hash_password(user.password)
    
    # Step 2: build the DB model - notice we never store user.password
    db_user = models.User(
        name=user.name,
        email=user.email,
        hashed_password=hashed,
        is_admin=False
    )
    
    # Step 3: save to database
    db.add(db_user)      # stage it
    db.commit()          # write it to disk
    db.refresh(db_user)  # refresh to get the generated id back
    
    return db_user       # returns User DB object, NOT UserCreate


# models.py
from sqlalchemy import Column, Integer, String, Boolean
from database import Base  # import from database.py, don't redefine it

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    hashed_password = Column(String, nullable=False)
    is_admin = Column(Boolean, default=False)

#schemas 
```python
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    email: str 
    

class UserCreate(UserBase):
    password:str
   
class UserResponse(UserBase):
    id: int
   

    model_config = {
        "from_attributes": True
    }
```

also when you give me code explain well also all the crud and model scheme database and main how will these files communicate with each other ??? 
also check the code and tell me what i did wrong or what to correct !



# database.py
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# This is the database file that will be created locally
DATABASE_URL = "sqlite:///./users.db"

# The engine is the actual connection to the database
engine = create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)

# Each request gets its own session - like a temporary workspace
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base is what all your DB models will inherit from
Base = declarative_base()




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

    