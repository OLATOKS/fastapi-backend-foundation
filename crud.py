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