from celery import Celery
import src.settings as celery_settings

celery_app = Celery('tasks')
celery_app.config_from_object(celery_settings)

if __name__ == '__main__':
    celery_app.start()
