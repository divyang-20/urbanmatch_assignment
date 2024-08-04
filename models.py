from sqlalchemy import Column, Integer, String, JSON
from database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100), index=True)
    age = Column(Integer)
    gender = Column(String(10))
    email = Column(String(100), unique=True, index=True)
    city = Column(String(100), index=True)
    interests = Column(JSON)
