FROM python:3

RUN pip install pytest

COPY . /app
WORKDIR /app

RUN pytest -v
