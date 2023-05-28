from uuid import UUID

from sqlalchemy import select

from .models import User


class HasUser:
    def __init__(self, session):
        self.session = session

    async def get_result(self, query) -> User | None:
        response = await self.session.execute(query)
        return response.scalars().first()

    async def username(self, username) -> User | None:
        query = select(User).where(User.username == username)
        return await self.get_result(query)

    async def id_and_token(self, unique_id: int, unique_token: UUID) -> User | None:
        query = select(User).where(User.id == unique_id and User.token == unique_token)
        return await self.get_result(query)
