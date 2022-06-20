import os
from celery import Celery
from flask import Flask, request

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

celery = Celery('app')
celery.config_from_envvar('CELERY_CONFIG_MODULE')


@celery.task
def add(x, y):
    return x + y

app = Flask(__name__)

@app.route("/")
def addit():
    x = request.args.get('x')
    y = request.args.get('y')
    task = add.delay(x, y)
    return task.status

