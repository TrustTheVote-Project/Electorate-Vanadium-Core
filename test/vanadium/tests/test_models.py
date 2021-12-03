# Note: This isn't trying to test all the models.
# It's to get a feel for what their initialization looks like.

from contextlib import nullcontext as raises_none

import pytest
from pydantic import ValidationError

from vanadium.models import *

from tests.conftest import Raises


# --- Test data

# dict, exception context
FILE_TESTS = [
    (
        {},
        Raises.MISSING
    ),
    (
        {
            "Data": b"dGV4dA==",
        },
        Raises.NONE
    ),
    (
        {
            "Data":     b"dGV4dA==",
            "FileName": "filename.txt",
            "MimeType": "text/plain",
        },
        Raises.NONE
    )
]


# dict, exception context
VOTER_TESTS = [
    (
        {},
        Raises.MISSING
    ),
    (
        {
            "Name":
            {
                "FullName": "First Last"
            },
        },
        Raises.NONE
    ),
    (
        {
            "Name":
            {
                "FirstName": "Jane",
                "LastName": "Doe",
                "MiddleName": [ "A" ],
            },
        },
        Raises.NONE
    ),
    (
        {
            "Name": Name(
                FirstName = "Jane",
                LastName = "Doe",
                MiddleName = [ "A" ],
            ),
        },
        Raises.NONE
    ),
    (
        {
            "ContactMethod": [
                {
                    "Type": ContactMethodType.EMAIL,
                    "Value": "jane.doe@email.com",
                },
                {
                    "Type": ContactMethodType.PHONE,
                    "Value": "999-555-1111",
                },
                {
                    "Type": ContactMethodType.OTHER,
                    "Value": "Bat signal",
                },
            ],
            "DateOfBirth": "2001-07-05",
            "Ethnicity": "White",
            "Gender": "Female",
            # "MailingAddress": None,
            "Name": {
                "FirstName": "Jane",
                "LastName": "Doe",
                "MiddleName": [ "A" ],
            },
            "Party": {
                "Name": "Independent",
            },
            # "PreviousResidenceAddress": None,
            "PreviousSignature": {
                "Source": SignatureSource.VOTER,
                "Type": SignatureType.OTHER,
                "OtherType": "photograph",
            },
            # "ResidenceAddress": None,
            "ResidenceAddressIsMailingAddress": True,
            "Signature": {
                "Date": "2020-02-29",
                "FileValue": {
                    "Data": b"W2ltYWdlIGZpbGVd",
                    "FileName": "signature.png",
                    "MimeType": "image/png",
                },
                "Source": SignatureSource.DMV,
                "Type": SignatureType.ELECTRONIC,
            },
            "VoterClassification": [
                {
                    "Assertion": AssertionValue.YES,
                    "Type": VoterClassificationType.UNITED_STATES_CITIZEN,
                },
                {
                    "Assertion": AssertionValue.UNKNOWN,
                    "Type": VoterClassificationType.RESTORED_FELON,
                },
            ],
            "VoterId": [
                {
                    "AttestNoSuchId": False,
                    "DateOfIssuance": "2017-09-22",
                    "FileValue": {
                        "Data": b"W2ltYWdlIGZpbGVd",
                        "FileName": "drivers-license.txt",
                        "MimeType": "text/plain",
                    },
                    "StringValue": "X1234567",
                    "Type": VoterIdType.DRIVERS_LICENSE,
                }
            ]
        },
        Raises.NONE
    )
]


# dict, exception context
VOTER_RECORDS_REQUEST_TESTS = [
    (
        {},
        Raises.MISSING
    ),
    (
        {
            "GeneratedDate": "2021-10-31",
            "RequestMethod": RequestMethod.MOTOR_VEHICLE_OFFICE,
            "Subject": {
                "Name": {
                    "FullName": "Milo Bloom",
                },
            },
            "Type": [
                VoterRequestType.REGISTRATION
            ],
        },
        Raises.NONE
    ),
    (
        {
            "AdditionalInfo": [
                {
                    "FileValue": {
                        "Data":      b"dGV4dA==",
                        "FileName": "filename.txt",
                        "MimeType": "text/plain",
                    },
                    "Name": "Proof of residence",
                },
            ],
            "BallotRequest": {
                "BallotReceiptPreference": [
                    BallotReceiptMethod.MAIL,
                ],
                "EndDate": "2021-11-02",
                "StartDate": "2021-11-02",
            },
            "Form": RequestForm.NVRA,
            "GeneratedDate": "2021-10-31",
            "Issuer": "Secretary of State",
            "RequestHelper": [
                {
                    "Name": {
                        "FirstName": "Alice"
                    },
                    "Phone": {
                        "Capability": [
                            PhoneCapability.VOICE,
                            PhoneCapability.SMS,
                        ],
                        "Type": ContactMethodType.PHONE,
                        "Value": "999-555-2222",
                    },
                    "Type": VoterHelperType.WITNESS,
                }
            ],
            "RequestMethod": RequestMethod.MOTOR_VEHICLE_OFFICE,
            "SelectedLanguage": "en",
            "Subject": {
                "Name": {
                    "FirstName": "Zeb",
                },
            },
            "TransactionId": 1234567,
            "Type": [
                VoterRequestType.REGISTRATION
            ],
            "VendorApplicationId": "Electorate Vanadium 0.1"
        },
        Raises.NONE
    ),
]


# --- Test cases

@pytest.mark.parametrize("data,raises", FILE_TESTS)
def test_file(data, raises):
    raises, args, opts = raises
    with raises(*args, **opts) as ex:
        model = File(**data)
        assert model.data == data["Data"]
        assert model.file_name == data.get("FileName")
        assert model.mime_type == data.get("MimeType")


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
