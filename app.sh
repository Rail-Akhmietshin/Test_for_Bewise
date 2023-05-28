#!/bin/bash

while ! nc -z $POSTGRES_HOST $POSTGRES_PORT; do
  sleep 1;
done

alembic upgrade head

gunicorn bewise.main:app --workers 1 --worker-class uvicorn.workers.UvicornWorker --bind $APP_ADDRESS:$APP_PORT