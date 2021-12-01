from fastapi import Request

def get_application(request: Request):
    """Make application, and thus its state available as a resource.

    Allows putting all dependencies for an application on the app instance.
    """
    return request.app
