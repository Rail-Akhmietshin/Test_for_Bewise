FROM python:3.11

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

RUN mkdir /Bewise

WORKDIR /Bewise

COPY req.txt .

RUN pip3 install -r req.txt

COPY . /Bewise

ENV PYTHONPATH=/Bewise

RUN apt-get update && apt-get install -y netcat ffmpeg

RUN chmod a+x *.sh
