from time import sleep

from sanic import Sanic
from sanic.response import json

from asgiref.sync import sync_to_async

from src.tasks import add, initialise

app = Sanic("MyHelloWorldApp")

running_tasks=[]

@app.listener("after_server_start")
async def init(app):
    result = await sync_to_async(initialise.delay)()

@app.get('/generate')
async def generate(request):
    result = await sync_to_async(add.delay)(5, 2)
    running_tasks.append(result)
    return json({'running': result.id})

@app.get("/status")
async def status(request):
    return json({
        'response': [{
            'id': t.id,
            'status': t.status,
            'result': t.result
        } for t in running_tasks]
    })


