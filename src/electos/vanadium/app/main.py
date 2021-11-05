from fastapi import FastAPI

from vanadium.app.route import _test

_routers = [
    _test
]

def application() -> FastAPI:
    app = FastAPI()
    for item in _routers:
        router = item.router()
        print(item, router)
        app.include_router(router)
    return app
