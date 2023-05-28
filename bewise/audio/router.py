import os

from fastapi import APIRouter, UploadFile, File, Depends, Form, status, BackgroundTasks, HTTPException
from fastapi.responses import FileResponse, JSONResponse
from uuid import UUID
from typing import Annotated, Union

from sqlalchemy.ext.asyncio import AsyncSession

from bewise.auth.utils import HasUser
from bewise.config import APP_ADDRESS, APP_PORT
from .utils import add_audiofile_to_db, get_audiofile_from_db, convert_wav_to_mp3

from bewise.database import get_async_session

router = APIRouter(
    prefix="/audio",
    tags=["Audio"]
)


@router.post("/upload")
async def upload_audiofile(
        user_id: Annotated[int, Form()],
        token: Annotated[UUID, Form()],
        file: Annotated[UploadFile, File()],
        background_tasks: BackgroundTasks,
        session: AsyncSession = Depends(get_async_session)
) -> JSONResponse:
    user = await HasUser(session).id_and_token(user_id, token)

    wav_file_path = os.path.join(os.getcwd(), "bewise", "audio", "audiofiles", file.filename)
    mp3_file_path = wav_file_path.replace('.wav', '.mp3')

    if user:
        if wav_file_path == mp3_file_path:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail={"Error": "Incorrect audio file format"}
            )
        created = True
        if not os.path.exists(mp3_file_path):
            background_tasks.add_task(convert_wav_to_mp3, wav_file_path, mp3_file_path, file.file)
            created = False

        audiofile = await add_audiofile_to_db(file.filename, mp3_file_path, user_id, session)


        return JSONResponse(
            status_code=status.HTTP_200_OK if created else status.HTTP_201_CREATED,
            content={
                "Download URL":
                    f"http://{APP_ADDRESS}:{APP_PORT}/audio/record?audiofile_id={audiofile.id}&user={audiofile.user_id}"
            })
    else:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail={
                "User": "No such user was found. Access denied"
            })


@router.get("/record")
async def get_audiofile(
        audiofile_id: UUID,
        user: int,
        session: AsyncSession = Depends(get_async_session)
) -> FileResponse:
    audiofile = await get_audiofile_from_db(audiofile_id, session)

    if audiofile.user_id == user:
        return FileResponse(
            path=audiofile.path,
            filename=audiofile.name.replace('.wav', '.mp3'),
            media_type='multipart/form-data'
        )
    raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail={"Access": "Denied"})
