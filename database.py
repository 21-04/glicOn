from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine=create_engine("postgresql://postgres:postgres@localhost/glic_on",
engine=create_engine("postgres://kksaxgkfdbsznv:fa92b66c4a5fc5aea5dc505b79ee52919c90d0bfc8a87d1eb0f2282225381d69@ec2-54-167-152-185.compute-1.amazonaws.com:5432/ddnj2ujdmlg5u0",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
