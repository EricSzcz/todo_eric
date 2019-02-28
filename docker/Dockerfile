FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

COPY ../ /app

RUN pipenv install /app/Pipfile

RUN adduser -D user
USER user