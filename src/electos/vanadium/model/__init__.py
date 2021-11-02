"""Model classes."""

from enum import Enum
from pydantic import BaseModel

from .classes import *
from .enumerations import *


# Drop all declarations that aren't schema models.
# Note that this will preserve 'Enum' or 'BaseModel'.
def _drop_non_models(names):
    bases = (Enum, BaseModel)
    for name in names:
        entry = globals()[name]
        if not name.startswith("_") and (
            not isinstance(entry, type) or
            not issubclass(entry, bases)
        ):
            del globals()[name]

_drop_non_models(dir())
del _drop_non_models
