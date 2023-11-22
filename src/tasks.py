from time import sleep
from src.celery import celery_app

@celery_app.task(name="add")
def add(x, y):
    sleep(20)
    return x + y

@celery_app.task(name="initialise")
def initialise():
    sleep(20)
    return None
