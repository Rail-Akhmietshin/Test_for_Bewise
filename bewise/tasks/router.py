from fastapi import APIRouter, Depends

from sqlalchemy.ext.asyncio import AsyncSession
from fastapi.responses import JSONResponse
from fastapi import status

from bewise.database import get_async_session
from .schemas import TaskCountValidator
from .utils import request_to_tasks, insert_task


router = APIRouter(
    prefix="/task",
    tags=["Task"]
)


@router.post("/get_tasks")
async def new_tasks(
        questions: TaskCountValidator,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    result = await request_to_tasks(questions.questions_num)

    for n, task in enumerate(result):
        response = await insert_task(task, session)
        result[n] = response

    return JSONResponse(status_code=status.HTTP_200_OK, content={"last_task": result[-1]})
