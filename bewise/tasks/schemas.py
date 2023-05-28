from datetime import datetime
from pydantic import BaseModel


class TasksCreate(BaseModel):
    id: int
    task_id: int
    question: str
    answer: str
    created_at: datetime


class TaskCountValidator(BaseModel):
    questions_num: int = 1