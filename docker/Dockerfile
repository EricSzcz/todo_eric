FROM python:3.6

ENV PYTHONBUFFERED 1

RUN mkdir /app
WORKDIR /app

ADD ./todo_eric /app/

RUN pip3 install -r /app/docker/requirements.txt

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]