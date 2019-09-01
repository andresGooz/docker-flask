from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Date
Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    firstname= Column(String)
    lastname = Column(String)
    email = Column(String)
    password = Column(Integer)
    cellphone = Column(Integer)
