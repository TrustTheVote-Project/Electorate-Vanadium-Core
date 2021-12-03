from typing import List, Optional

from fastapi import APIRouter, Query


# --- Routes

_router = APIRouter(prefix = "/test")


@_router.get(
    "/{id}",
    summary = "Status of a pending request"
)
def get_test(
    id,
    version: int = 1,
    option: Optional[List[str]] = Query(None)
):
    """Return information about a pending request."""
    return { "id": id, "method": "GET", "option": option }


@_router.post(
    "/{id}",
    summary = "Post data"
)
def post_test(
    id,
    version: int = 2,
    option: Optional[str] = None
):
    """Return information about a pending request."""
    return { "id": id, "method": "POST", "option": option }


@_router.put(
    "/{id}",
    summary = "Replace a request"
)
def put_test(
    id,
    version: int = 3,
    option: Optional[str] = None
):
    """Create or replace an existing request."""
    return { "id": id, "method": "PUT", "option": option }


@_router.delete(
    "/{id}",
    summary = "Delete a request"
)
def delete_test(
    id,
    version: int = 4,
    option: Optional[str] = None
):
    """Delete an existing request."""
    return { "id": id, "method": "DELETE", "option": option }


# --- Router

_routers = [
    _router
]

def router():
    return _router
