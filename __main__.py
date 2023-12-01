from functools import partial

from sanic.worker.loader import AppLoader
from sanic import Sanic
from src.server import create_app, run_app


def main():
    loader = AppLoader(factory=partial(create_app))
    app = loader.load()
    app.prepare(port=8000, dev=True)
    Sanic.serve(primary=app, app_loader=loader)

if __name__ == "__main__":
    main()
