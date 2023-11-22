## Install

Install rabbitmq-server
```
apt install rabbitmq-server
```

Create a virtualenv:
```
python3 -m venv env
```

Activate the virtualenv:
```
source env/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

## Running celery 

```
celery -A src.tasks worker --loglevel=INFO --concurrency=1
```

## Running Sanic

```
sanic src.server:app
```

