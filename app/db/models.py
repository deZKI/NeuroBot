from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs
from sqlalchemy.orm import declarative_base, relationship
from datetime import datetime

Base = declarative_base()


# Модель пользователя
class User(AsyncAttrs, Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    telegram_id = Column(Integer, unique=True)
    first_name = Column(String)
    last_name = Column(String)

    history = relationship("History", back_populates="user")


# Модель истории запросов
class History(AsyncAttrs, Base):
    __tablename__ = "history"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    query = Column(String)
    response = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)

    user = relationship("User", back_populates="history")


# Модель знаний
class Knowledge(AsyncAttrs, Base):
    __tablename__ = "knowledge"

    id = Column(Integer, primary_key=True, index=True)
    question = Column(String, unique=True)
    answer = Column(String)
