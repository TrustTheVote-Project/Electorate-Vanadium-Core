# Shared resources
# There are numerous ways to do this better but simple is good enough for now.

from vanadium.app.database import MemoryDataStore


class Resources:

    # Shared storage used by routes.

    _storage = None

    @classmethod
    def get_storage(class_):
        if class_._storage is None:
            class_._storage = MemoryDataStore()
        return class_._storage
