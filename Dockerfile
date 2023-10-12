FROM python:3.11-slim-buster

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN apt-get update && apt-get install -y postgresql-client

COPY . /app


RUN pip install --no-cache-dir poetry \
    && poetry config virtualenvs.create false \
    && poetry install

CMD ["poetry", "run", "python", "src/manage.py", "runserver", "0.0.0.0:8000"]