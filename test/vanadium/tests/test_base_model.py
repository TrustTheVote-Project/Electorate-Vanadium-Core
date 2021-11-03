from enum import Enum
from typing import Literal, Optional

import pytest

from vanadium.model.base import SchemaModel

from tests.conftest import Raises


# --- Test classes

class Status(Enum):

    ALPHA = "alpha"
    BETA = "beta"
    FINAL = "final-release"


class Package(SchemaModel):

    """Subclass of SchemaModel."""

    _model_type: Literal["Test.Package"] = "Test.Package"

    name: str
    description: Optional[str] = None
    status: Status


# --- Test cases

# data, exception context
INIT_TESTS = [
    (
        {},
        Raises.MISSING
    ),
    (
        {
            "name": "test-package",
        },
        Raises.MISSING
    ),
    (
        {
            "name": "test-package",
            "status": Status.ALPHA,
        },
        Raises.NONE
    ),
    (
        {
            "name": "test-package",
            "description": "Dummy placeholder for testing",
            "status": Status.ALPHA,
        },
        Raises.NONE
    ),
    (
        {
            "name": "test-package",
            "status": Status.ALPHA,
            "debug": True,
        },
        Raises.EXTRA
    )
]


# data, assigned valued, exception context
ASSIGNMENT_TESTS = [
    # Assigning additional properties is disallowed
    (
        {
            "name": "test-package",
            "status": Status.ALPHA,
        },
        ( "debug", True ),
        (pytest.raises, (ValueError,), {})
    )
]


# data, dict, json
_DICT_JSON_TESTS = [
    (
        {
            "name": "test-package",
            "status": Status.ALPHA,
        },
        {
            "name": "test-package",
            "description": None,
            "status": Status.ALPHA,
        },
        "{\n"
        '    "name": "test-package",\n'
        '    "description": null,\n'
        '    "status": "alpha"\n'
        "}",
    ),
]


DICT_TESTS = [(_[0], _[1]) for _ in _DICT_JSON_TESTS]


JSON_TESTS = [(_[0], _[2]) for _ in _DICT_JSON_TESTS]


@pytest.mark.parametrize("data,raises", INIT_TESTS)
def test_base_model_init(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = Package(**data)


@pytest.mark.parametrize("data,assign,raises", ASSIGNMENT_TESTS)
def test_base_model_assign(data, assign, raises):
    """Trying to set additional properies should fail."""
    raises, args, opts = raises
    model = Package(**data)
    with raises(*args, **opts) as ex:
        name, value = assign
        setattr(model, name, value)


@pytest.mark.parametrize("data,expected", DICT_TESTS)
def test_base_model_dict(data, expected):
    model = Package(**data)
    assert model.dict() == expected


@pytest.mark.parametrize("data,expected", JSON_TESTS)
def test_base_model_json(data, expected):
    model = Package(**data)
    assert model.json(indent = 4) == expected
