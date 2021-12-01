from fastapi import Depends, Request

from vanadium.app.database import MemoryDataStore
from vanadium.app.resource.base import get_application


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
