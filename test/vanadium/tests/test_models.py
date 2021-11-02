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


# dict, exception context
VOTER_RECORDS_REQUEST_TESTS = [
    (
        {},
        RAISES_MISSING
    ),
    (
        {
            "generated_date": "2021-10-31",
            "request_method": RequestMethod.MOTOR_VEHICLE_OFFICE,
            "subject": {
                "name": {
                    "full_name": "Milo Bloom",
                },
            },
            "type": [
                VoterRequestType.REGISTRATION
            ],
        },
        RAISES_NONE
    ),
    (
        {
            "additional_info": [
                {
                    "file_value": {
                        "data":      b"dGV4dA==",
                        "file_name": "filename.txt",
                        "mime_type": "text/plain",
                    },
                    "name": "Proof of residence",
                },
            ],
            # "ballot_request": {
            #     "ballot_receipt_reference": BallotReceiptMethod.MAIL,
            #     "start_date": "2021-11-02",
            #     "end_date": "2021-11-02",
            # },
            "form": RequestForm.NVRA,
            "generated_date": "2021-10-31",
            "issuer": "Secretary of State",
            "request_helper": [
                {
                    "name": {
                        "first_name": "Alice"
                    },
                    "phone": {
                        "capability": [
                            PhoneCapability.VOICE,
                            PhoneCapability.SMS,
                        ],
                        "type": ContactMethodType.PHONE,
                        "value": "999-555-2222",
                    },
                    "type": VoterHelperType.WITNESS,
                }
            ],
            "request_method": RequestMethod.MOTOR_VEHICLE_OFFICE,
            "selected_language": "en",
            "subject": {
                "name": {
                    "first_name": "Zeb",
                },
            },
            "transaction_id": 1234567,
            "type": [
                VoterRequestType.REGISTRATION
            ],
            "vendor_application_id": "Electorate Vanadium 0.1"
        },
        RAISES_NONE
    ),
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


@pytest.mark.parametrize("data,raises", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_records_request(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = VoterRecordsRequest(**data)
