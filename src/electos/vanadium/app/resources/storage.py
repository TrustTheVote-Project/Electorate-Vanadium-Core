from fastapi import Depends, Request

from vanadium.app.resources.base import get_application
from vanadium.app.storage import MemoryDataStore


_storage = None


def init_resource(*args, **opts):
    """Initialize the storage.
    Called during application setup and *only* then.
    """
    _storage = MemoryDataStore(*args, **opts)
    return _storage


def get_storage(app = Depends(get_application)):
    assert hasattr(app.state, "storage"), "Application has no 'storage' defined"
    return app.state.storage
