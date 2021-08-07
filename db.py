from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Float
from sqlalchemy.orm import relationship
from datetime import datetime
from app import engine


Base = declarative_base()


class UserDB(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(80), nullable=False)
    cpf = Column(String(255), unique=True, nullable=False)
    email = Column(String(255), nullable=False)
    phone_number = Column(String(255), nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    order = relationship('OrderDB', back_populates='user')

    def __repr__(self):
        return f'User {self.name}'


class OrderDB(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    item_description = Column(String(255), nullable=False)
    item_quantity = Column(Float, nullable=False)
    item_price = Column(Float, nullable=False)
    total_value = Column(Float, nullable=False)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow)
    user = relationship('UserDB', back_populates='order')

    def __repr__(self):
        return f'Order {self.id}'


Base.metadata.create_all(engine)

