from uuid import UUID

from pydantic import BaseModel


class AudioUserCreate(BaseModel):
    id: int
    unique_token: UUID
