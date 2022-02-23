# syntax=docker/dockerfile:1
FROM python:3

# set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# set work directory
WORKDIR /code

# install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# copy project
COPY . /code/

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "devook.wsgi:application"]