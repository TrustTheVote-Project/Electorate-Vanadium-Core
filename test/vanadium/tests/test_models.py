# Note: This isn't trying to test all the models.
# It's to get a feel for what their initialization looks like.

from contextlib import nullcontext as raises_none

import pytest
from pydantic import ValidationError

from vanadium.model import *


# --- Exception contexts

RAISES_MISSING = (pytest.raises, (ValidationError,), {"match": "value_error.missing"})
RAISES_NONE = (raises_none, (), {})


# --- Test data

# dict, exception context
FILE_TESTS = [
    (
        {},
        RAISES_MISSING
    ),
    (
        {
            "data": b"dGV4dA==",
        },
        RAISES_NONE
    ),
    (
        {
            "data":      b"dGV4dA==",
            "file_name": "filename.txt",
            "mime_type": "text/plain",
        },
        RAISES_NONE
    )
]


# --- Test cases

@pytest.mark.parametrize("data,raises", FILE_TESTS)
def test_file(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = File(**data)
        assert model.data == data["data"]
        assert model.file_name == data.get("file_name")
        assert model.mime_type == data.get("mime_type")

