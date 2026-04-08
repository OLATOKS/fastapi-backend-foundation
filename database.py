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

