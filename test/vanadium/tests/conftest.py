from contextlib import nullcontext as raises_none

from pytest import raises
from pydantic import ValidationError


# --- Exception contexts

class Raises:

    """Exception contexts used in PyTest tests.

    Abstracts out whether test cases raise exceptions or not.
    """

    # No error
    NONE = (raises_none, (), {})
    # Expected fields in model missing from value
    MISSING = (raises, (ValidationError,), {"match": "value_error.missing"})
    # Unexpected fields in value, and additional properties forbidden.
    EXTRA = (raises, (ValidationError,), {"match": "value_error.extra"})
