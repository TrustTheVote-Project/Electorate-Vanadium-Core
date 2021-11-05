from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest

from vanadium.app.main import application
from vanadium.model import (
    RequestForm,
    RequestMethod,
    Voter,
    VoterRequestType,
    VoterRecordsRequest,
)

app = application()
client = TestClient(app)


# --- Test data

REQUEST_TEMPLATES = {
    "minimal": {
        "Form": RequestForm.NVRA.value,
        "GeneratedDate": "2020-07-05",
        "RequestMethod": RequestMethod.VOTER_VIA_INTERNET.value,
        "Type": [
            VoterRequestType.REGISTRATION.value
        ]
    }
}

VOTERS = {
    "minimal": {
        "Name": {
            "FirstName": "First",
            "LastName": "Last",
        }
    }
}


VOTER_RECORDS_REQUEST_TESTS = [
    ( REQUEST_TEMPLATES["minimal"], VOTERS["minimal"] )
]


# ---

@pytest.mark.parametrize("template,voter", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request(template, voter):
    url = "/voter/registration/"
    transaction_id = "[TEST]"
    body = template.copy()
    body.update(Subject = voter)
    response = client.post(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "<generated new ID>"
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Created")


@pytest.mark.parametrize("template,voter", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_with_transaction_id(template, voter):
    url = "/voter/registration/"
    transaction_id = "[TEST]"
    body = template.copy()
    body.update(Subject = voter, TransactionId = transaction_id)
    response = client.post(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Created")


def test_voter_registration_check_status():
    transaction_id = "[TEST]"
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Checked")


@pytest.mark.parametrize("template,voter", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update(template, voter):
    transaction_id = "[TEST]"
    test_data = "..."
    url = f"/voter/registration/{transaction_id}"
    body = template.copy()
    body.update(Subject = voter)
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Updated")


def test_voter_registration_cancel():
    transaction_id = "[TEST]"
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Checked")
