"""Helpers for routes."""

import hashlib as _hashlib
import time as _time
import uuid as _uuid


class UniqueIds:

    @staticmethod
    def timestamp_id(timestamp = None):
        """Generate a unique ID based on a timestamp.

        A transaction ID is the UUID of the SHA-1 hash of the current timestamp.

        Parameters:
            timestamp: POSIX timestamp.
                Defined to allow reproduceable testing.
                By default uses the current time.

        Returns:
            (str) A generated UUID.
        """
        now = timestamp or str(_time.time()).encode("utf-8")
        hash_ = _hashlib.sha1()
        hash_.update(now)
        bytes_ = hash_.digest()[:16]
        uuid = _uuid.UUID(bytes = bytes_)
        return str(uuid)
