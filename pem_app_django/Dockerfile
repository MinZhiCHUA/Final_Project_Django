FROM python:3.11-slim

WORKDIR /usr/src/app

ENV PYTHONUNBUFFERED 1

COPY requirements.txt .

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

COPY . /usr/src/app