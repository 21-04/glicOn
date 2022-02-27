#from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
import os
from sqlalchemy.dialects.postgresql import *
#engine=create_engine("postgresql://postgres:postgres@localhost/glic_on",
url="postgres://vpfamjobcgsdey:42d7379e819411a64c12846e52b2ff2d6f672d4c1d67e737ac9b3febb286be46@ec2-3-227-195-74.compute-1.amazonaws.com:5432/d9b0m9c48qafim"
engine=create_engine(url,
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
