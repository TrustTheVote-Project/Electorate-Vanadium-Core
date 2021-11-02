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
VOTER_TESTS = [
    (
        {},
        RAISES_MISSING
    ),
    (
        {
            "name":
            {
                "full_name": "First Last"
            },
        },
        RAISES_NONE
    ),
    (
        {
            "name":
            {
                "first_name": "Jane",
                "last_name": "Doe",
                "middle_name": [ "A" ],
            },
        },
        RAISES_NONE
    ),
    (
        {
            "name": Name(
                first_name = "Jane",
                last_name = "Doe",
                middle_name = [ "A" ],
            ),
        },
        RAISES_NONE
    ),
    (
        {
            "contact_method": [
                {
                    "type": ContactMethodType.EMAIL,
                    "value": "jane.doe@email.com",
                },
                {
                    "type": ContactMethodType.PHONE,
                    "value": "999-555-1111",
                },
                {
                    "type": ContactMethodType.OTHER,
                    "value": "Bat signal",
                },
            ],
            "date_of_birth": "2001-07-05",
            "ethnicity": "White",
            "gender": "Female",
            # "mailing_address": None,
            "name": {
                "first_name": "Jane",
                "last_name": "Doe",
                "middle_name": [ "A" ],
            },
            "party": {
                "name": "Independent",
            },
            # "previous_residence_address": None,
            "previous_signature": {
                "source": SignatureSource.VOTER,
                "type": SignatureType.OTHER,
                "other_type": "photograph",
            },
            # "residence_address": None,
            "residence_address_is_mailing_address": True,
            "signature": {
                "date": "2020-02-29",
                "file_value": {
                    "data": b"W2ltYWdlIGZpbGVd",
                    "file_name": "signature.png",
                    "mime_type": "image/png",
                },
                "source": SignatureSource.DMV,
                "type": SignatureType.ELECTRONIC,
            },
            "voter_classification": [
                {
                    "assertion": AssertionValue.YES,
                    "type": VoterClassificationType.UNITED_STATES_CITIZEN,
                },
                {
                    "assertion": AssertionValue.UNKNOWN,
                    "type": VoterClassificationType.RESTORED_FELON,
                },
            ],
            "voter_id": [
                {
                    "attest_no_such_id": False,
                    "date_of_issuance": "2017-09-22",
                    "file_value": {
                        "data": b"W2ltYWdlIGZpbGVd",
                        "file_name": "drivers-license.txt",
                        "mime_type": "text/plain",
                    },
                    "string_value": "X1234567",
                    "type": VoterIdType.DRIVERS_LICENSE,
                }
            ]
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


@pytest.mark.parametrize("data,raises", VOTER_TESTS)
def test_voter(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = Voter(**data)


@pytest.mark.parametrize("data,raises", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_records_request(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = VoterRecordsRequest(**data)
