from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy import Column, Integer, Text

Base = declarative_base()

class hello(Base):
    __tablename__ = "content"
    id = Column(Integer, primary_key=True)
    value = Column(Text, nullable=False)