from sqlalchemy import Column, Date, DateTime, ForeignKey, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from .base_class import Base


class Job(Base):
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    date = Column(Date)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', back_populates='jobs')

    time_created = Column(DateTime(timezone=True), server_default=func.now())
    time_updated = Column(DateTime(timezone=True), onupdate=func.now())
