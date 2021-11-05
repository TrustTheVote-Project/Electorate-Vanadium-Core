from fastapi import FastAPI

# from vanadium.app.route import {router}

_routers = {
}

def application() -> FastAPI:
    app = FastAPI()
    for router, arguments in _routers.items():
        router = router.router()
        app.include_router(router, **arguments)
    return app
