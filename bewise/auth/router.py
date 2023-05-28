from typing import Union

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse

from .models import User
from .schemas import UsernameValidator
from bewise.database import get_async_session
from .utils import HasUser

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/create_user", response_model=UsernameValidator)
async def create_user(
        user: UsernameValidator,
        session: AsyncSession = Depends(get_async_session)
) -> Union[HTTPException, JSONResponse]:
    has_user = await HasUser(session).username(user.username)

    if has_user:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail={"Conflict": "Такой пользователь уже существует"}
        )

    new_user = User(**user.dict())
    session.add(new_user)
    await session.commit()
    await session.flush()

    return JSONResponse(
        status_code=status.HTTP_201_CREATED,
        content={
            new_user.username: {
                "id": new_user.id,
                "token": str(new_user.token)
            }
        })
