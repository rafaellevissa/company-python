from .base import Base
from utils.bcrypt import hash_password
from sqlalchemy import Column, String, Integer, DateTime, func

class UserModel(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(200), unique=True)
    email = Column(String(200))
    password = Column(String(200))
    create_at = Column(DateTime, default=func.now())

    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = hash_password(password)


