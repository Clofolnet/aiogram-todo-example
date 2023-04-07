from db.models import Job
from db.schemas import JobCreate, JobUpdate

from .base import CRUDBase


class CRUDJob(CRUDBase[Job, JobCreate, JobUpdate]):
    pass


job_crud = CRUDJob(Job)
