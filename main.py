#from typing import List
from fastapi import Depends, FastAPI, HTTPException, status,File, UploadFile
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
#import models, schemas
from .database import SessionLocal, engine
#from datetime import datetime, timedelta
#import shutil

app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}