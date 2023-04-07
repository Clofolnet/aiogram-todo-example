from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base_class import Base


class User(Base):
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    chat_id = Column(String)
    language_code = Column(String)
    username = Column(String)
    full_name = Column(String)
    jobs = relationship('Job', back_populates='user')

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
