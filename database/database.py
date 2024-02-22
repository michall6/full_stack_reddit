from sqlalchemy.orm import Session
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
from dotenv import load_dotenv

 
load_dotenv() 

SQLALCHEMY_USER = os.environ['SQLALCHEMY_USER'] 
SQLALCHEMY_PASSWORD = os.environ['SQLALCHEMY_PASSWORD'] 
SQLALCHEMY_SERVER = os.environ['SQLALCHEMY_SERVER'] 
SQLALCHEMY_PORT = os.environ['SQLALCHEMY_PORT'] 
SQLALCHEMY_DB = os.environ['SQLALCHEMY_DB'] 

SQLALCHEMY_DATABASE_URL = f"postgresql://{SQLALCHEMY_USER}:{SQLALCHEMY_PASSWORD}@{SQLALCHEMY_SERVER}:{SQLALCHEMY_PORT}/{SQLALCHEMY_DB}"


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# Initialize the database
Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

db:Session = next(get_db())


