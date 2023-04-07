from datetime import date, datetime
from typing import Optional

from pydantic import BaseModel


class JobBase(BaseModel):
    """ Shared properties """
    user_id: int
    title: str
    date: date


class JobCreate(JobBase):
    """ Properties to receive on сomment creation """
    pass


class JobUpdate(JobBase):
    """ Properties to receive on сomment update """
    pass


class JobInDBBase(JobBase):
    """ Properties shared by models stored in DB """
    id: int
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class Job(JobInDBBase):
    """ Properties to return to client """
    pass


class JobInDB(JobInDBBase):
    """ Properties properties stored in DB """
    pass
