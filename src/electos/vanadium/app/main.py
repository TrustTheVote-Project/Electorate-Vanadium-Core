from fastapi import FastAPI

from vanadium.app.route import (
    voter_registration,
)


# --- Application wide settings

# Event name => event handler
_EVENT_HANDLERS = {
}

# Error type => error handlers
_ERROR_HANDLERS = {
}

# (Middleware type, parameters dict)
_MIDDLEWARE = [
]

# Resource module names => resource initializer
_RESOURCES = {
}

# Router module names
_ROUTERS = [
    voter_registration,
]

# --- Application setup

def _setup_event_handlers(app, event_handlers):
    """Add event handlers to the application."""
    for name, handler in event_handlers.items():
        app.add_event_handler(name, handler(app))


def _setup_error_handlers(app, error_handlers):
    """Add error handlers to the application."""
    for name, handler in error_handlers.items():
        app.add_error_handler(name, handler(app))


def _setup_middleware(app, middlewares):
    """Add middleware to the application."""
    for call, parameters in middlewares:
        app.add_middleware(call, **parameters)


def _setup_routers(app, routers = None):
    """Attach routers to the application."""
    for item in routers:
        router = item.router()
        app.include_router(router)


def _setup_resources(app, resources = None):
    for name, resource in resources.items():
        setattr(app.state, name, resource.init_resource())


def _setup():
    """Application initialization, including components."""
    app = FastAPI()
    _setup_event_handlers(app, _EVENT_HANDLERS)
    _setup_error_handlers(app, _ERROR_HANDLERS)
    _setup_middleware(app, _MIDDLEWARE)
    _setup_resources(app, _RESOURCES)
    _setup_routers(app, _ROUTERS)
    return app


# --- Application entry point

def application() -> FastAPI:
    """Top-level application entry point invoked by the ASGI server."""
    app = _setup()
    print(vars(app.state))
    return app
