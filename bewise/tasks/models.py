
from datetime import datetime
from sqlalchemy import Integer, String, MetaData, Text
from sqlalchemy.orm import mapped_column, Mapped

from bewise.database import Base


class Task(Base):
    __tablename__ = "task"

    metadata = MetaData()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    task_id: Mapped[int] = mapped_column(Integer, unique=True)
    question: Mapped[str] = mapped_column(Text)
    answer: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(String(255), nullable=True)
