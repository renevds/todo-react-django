# syntax=docker/dockerfile:1
FROM python:3
ENV PYTHONUNBUFFERED=1
WORKDIR /code

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./backend/requirements.txt ./backend
WORKDIR  /backend
RUN pip install -r requirements.txt
WORKDIR ./code

# copy project
COPY . /code/