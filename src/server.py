import logging
from time import sleep

from sanic import Sanic
from sanic.response import json

from asgiref.sync import sync_to_async

from src.managers import managers
from src.stable import initialise
from src.tasks import generate_from_prompt

logging.basicConfig(level=logging.DEBUG)

running_tasks=[]

def attach_endpoints(app):

    @app.get('/generate/<prompt:str>')
    async def generate(request, prompt):
        result = await sync_to_async(generate_from_prompt.delay)(prompt)
        running_tasks.append(result)
        return json({'id': result.id})

    @app.get("/status")
    async def status(request):
        return json({
            'results': [{
                'initialized': app.ctx.pipe is not None,
                'id': t.id,
                'status': t.status,
                'result': t.result
            } for t in running_tasks]
        })

def create_app():
    app = Sanic("StableRunner")

    @app.listener("after_server_start")
    async def initialize(*args, **kwargs):
        await managers.initialize()

    @app.listener('after_server_stop')
    async def teardown(*args, **kwargs):
        await managers.teardown()

    attach_endpoints(app)
    return app

def run_app(sanic_app):
    sanic_app.run(auto_reload=True)


# @app.listener('after_server_start')
# async def init(app):
#     logging.debug(f'app: {initialise}')
#     pipe, scheduler = await sync_to_async(initialise)()
#     app.ctx.pipe = pipe
#     app.ctx.scheduler = scheduler
# 
