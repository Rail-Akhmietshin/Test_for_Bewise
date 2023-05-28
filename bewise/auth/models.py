from uuid import uuid4, UUID as UUID_TYPING

from sqlalchemy import String, Integer, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.dialects.postgresql import UUID as UUID_COLUMN_TYPE

from bewise.database import Base


class User(Base):
    __tablename__ = "bewise_user"

    metadata = MetaData()

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    username: Mapped[str] = mapped_column(String(100), unique=True, nullable=False)
    token: Mapped[UUID_TYPING] = mapped_column(UUID_COLUMN_TYPE(as_uuid=True), default=uuid4, unique=True)


