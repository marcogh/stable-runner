from sanic import Blueprint
from sanic.response import json

bp = Blueprint('stable', url_prefix="api/v1/stable")

running_tasks=[]

# @bp.get('/generate/<prompt:str>')
# async def generate(request, prompt):
#     result = await sync_to_async(generate_from_prompt.delay)(prompt)
#     running_tasks.append(result)
#     return json({'id': result.id})

@bp.get("/status")
async def status(request):
    return json({
        'results': [{
            'initialized': app.ctx.pipe is not None,
            'id': t.id,
            'status': t.status,
            'result': t.result
        } for t in running_tasks]
    })
