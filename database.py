from sqlalchemy.orm import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

#engine=create_engine("postgresql://postgres:postgres@localhost/glic_on",
engine=create_engine("postgres://ckqgsphkotwums:23579a1afa2016c0b6fde9a01e0d0d1567183513ef402b8894d08bf7753e0f9d@ec2-3-209-226-234.compute-1.amazonaws.com:5432/d4tqr0kj7tedd9",
    echo=True
)

Base=declarative_base()

SessionLocal=sessionmaker(bind=engine)
