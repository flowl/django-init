FROM python:3.8-slim

RUN apt-get update && apt-get install -y gcc gettext libgettextpo-dev default-libmysqlclient-dev netcat

ENV PYTHONUNBUFFERED 1

RUN mkdir /app/
WORKDIR /app/

COPY requirements.txt /app/

RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
