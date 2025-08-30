from sqlalchemy import Column, Integer, String, Boolean, DateTime, func
from app.db.db import Base

class Todo(Base): ##ORM model - may include sensitive information in the DB layer
    __tablename__ = "todos"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(140), nullable=False, index=True)
    done = Column(Boolean, nullable=False, default=False)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
