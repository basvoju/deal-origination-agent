from sqlalchemy import Column, Integer, String, Float, Text
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Company(Base):

    __tablename__ = "companies"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    score = Column(Float)
    report = Column(Text)