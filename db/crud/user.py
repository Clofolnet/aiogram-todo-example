from sqlalchemy.orm import Session
from sqlalchemy.sql import exists

from db.models import User
from db.schemas import UserCreate, UserUpdate

from .base import CRUDBase


class CRUDUser(CRUDBase[User, UserCreate, UserUpdate]):
    def check_unique_by_user_id(self,
                                db: Session,
                                *,
                                user_id: int) -> bool:

        return db.query(exists().where(self.model.user_id == user_id)).scalar()

    def get_user_by_user_id(self, db: Session, *, user_id: int) -> int:
        return db.query(self.model).filter(self.model.user_id == user_id).first()


user_crud = CRUDUser(User)
