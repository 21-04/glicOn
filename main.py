# main.py
from fastapi import FastAPI
#from os import stat
#from turtle import st
#from fastapi import FastAPI,status,HTTPException
#from pydantic import BaseModel
#from typing import Optional,List
#from database import SessionLocal
#import models
app = FastAPI()

@app.get("/")
def hello():
    return {"message":"Hello TutLinks.com"}