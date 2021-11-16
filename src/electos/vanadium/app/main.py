from fastapi import FastAPI

from vanadium.app.route import (
    voter_registration,
)

_routers = [
    voter_registration,
]

def application() -> FastAPI:
    app = FastAPI()
    for item in _routers:
        router = item.router()
        app.include_router(router)
    return app
