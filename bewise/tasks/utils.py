import httpx
from sqlalchemy import select, insert
from sqlalchemy.ext.asyncio import AsyncSession

from bewise.config import TASKS_API_URL
from .models import Task


async def request_to_tasks(count: int) -> dict:
    async with httpx.AsyncClient() as client:
        response = await client.get(TASKS_API_URL + f"random?count={count}")
        return response.json()


async def insert_task(task: dict, session: AsyncSession) -> dict:
    response = False

    while not response:
        query = select(Task).where(Task.task_id == task["id"])
        result = await session.execute(query)

        if result.scalars().fetchall():
            response_task = await request_to_tasks(1)
            task = response_task[0]
        else:
            response = True

    task = {
        "task_id": task["id"],
        "question": task["question"],
        "answer": task["answer"],
        "created_at": task["created_at"]
    }

    stmt = insert(Task).values(task)

    await session.execute(stmt)
    await session.commit()
    return task
