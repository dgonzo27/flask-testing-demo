# pull official base image
FROM python:3.9.0-slim-buster

# set working directory
WORKDIR /usr/src

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
    && apt-get -y install netcat gcc postgresql libpq-dev \
    && apt-get clean

# install application dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/
COPY ./requirements-dev.txt /usr/src/
RUN pip install -r requirements-dev.txt

# add app
COPY . /usr/src/

# add entrypoint.sh
COPY ./entrypoint.sh /usr/src/
RUN chmod +x /usr/src/entrypoint.sh