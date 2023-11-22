FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client

COPY . /app

RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install

RUN apt-get update -y && apt-get upgrade -y \
    && apt-get install -y --no-install-recommends binutils libproj-dev gdal-bin libgdal-dev python3-gdal

RUN python -m pip install Pillow
