import os
from celery import Celery
from flask import Flask, request
from celery.utils.log import get_task_logger

logger = get_task_logger(__name__)

os.environ.setdefault('CELERY_CONFIG_MODULE', 'celery_config')

celery = Celery('app')
celery.config_from_envvar('CELERY_CONFIG_MODULE')


@celery.task(autoretry_for=(Exception,), max_retries=3)
def add(x, y):
    logger.info('Adding {0} + {1}'.format(x, y))
    return x + y



app = Flask(__name__)

@app.route("/")
def addit():
    x = request.args.get('x')
    y = request.args.get('y')
    task = add.delay(x, y)
    return task.status

