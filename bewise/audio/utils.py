import asyncio
import os
import shutil

from uuid import UUID

from pydub import AudioSegment
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from .models import Audio


async def add_audiofile_to_db(name: str, path: str, user_id: int, session: AsyncSession) -> Audio:
    new_record = Audio(name=name, path=path, user_id=user_id)
    session.add(new_record)
    await session.commit()
    await session.flush()
    return new_record


async def get_audiofile_from_db(audiofile: str | UUID, session: AsyncSession) -> Audio | None:
    params = Audio.id if isinstance(audiofile, UUID) else Audio.path
    query = select(Audio).where(params == audiofile)
    response = await session.execute(query)
    return response.scalars().first()


async def convert_wav_to_mp3(wav_file_path: str, mp3_file_path: str, file) -> None:
    with open(wav_file_path, "wb") as buffer:
        shutil.copyfileobj(file, buffer)

    ffmpeg_directory = os.path.join("/", "usr", "bin", "ffmpeg")
    AudioSegment.converter = ffmpeg_directory
    AudioSegment.ffprobe = ffmpeg_directory

    audio = AudioSegment.from_wav(wav_file_path)
    await asyncio.to_thread(audio.export, mp3_file_path, format='mp3')
    await asyncio.to_thread(os.remove, wav_file_path)
