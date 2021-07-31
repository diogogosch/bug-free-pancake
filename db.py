from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, MetaData, Table
from datetime import datetime
from app import engine

Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    cpf = Column(String(11), unique=True, nullable=False)
    email = Column(String(120), nullable=False)
    phone_number = Column(String(14), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return f'User {self.name}'


Base.metadata.create_all(engine)


