from sqlalchemy import ForeignKey, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column
from uuid import UUID as UUID_TYPING, uuid4
from sqlalchemy.dialects.postgresql import UUID as UUID_COLUMN_TYPE

from bewise.database import Base
from bewise.auth.models import User


class Audio(Base):
    __tablename__ = "audio"

    metadata = MetaData()

    id: Mapped[UUID_TYPING] = mapped_column(UUID_COLUMN_TYPE(as_uuid=True), default=uuid4, primary_key=True)
    name: Mapped[str] = mapped_column(String)
    path: Mapped[str] = mapped_column(String)
    user_id: Mapped[int] = mapped_column(ForeignKey(User.id))
