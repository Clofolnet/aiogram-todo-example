from datetime import datetime
from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    """ Shared properties """
    user_id: int
    chat_id: str
    language_code: str
    username: Optional[str] = None
    full_name: str


class UserCreate(UserBase):
    """ Properties to receive on сomment creation """
    pass


class UserUpdate(UserBase):
    """ Properties to receive on сomment update """
    pass


class UserInDBBase(UserBase):
    """ Properties shared by models stored in DB """
    id: int
    time_created: datetime
    time_updated: Optional[datetime] = None

    class Config:
        orm_mode = True


class User(UserInDBBase):
    """ Properties to return to client """
    pass


class UserInDB(UserInDBBase):
    """ Properties properties stored in DB """
    pass
