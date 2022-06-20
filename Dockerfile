FROM python:3.9

WORKDIR /usr/src/app

RUN pip install celery[redis]==4.4.7 flask

COPY app.py .
COPY celery_config.py .
