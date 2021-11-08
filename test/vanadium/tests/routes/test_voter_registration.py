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

from tests.conftest import load_test_data


app = application()
client = TestClient(app)


# --- Test data

VOTER_RECORDS_REQUEST_TESTS = [
    ( "nvra", "minimal" ),
    ( "nvra", "alice-zed" ),
    ( "nvra", "jane-doe" ),
]


# ---

@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    response = client.post(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == body["TransactionId"]
    assert data["status"] == "Nominal success"
    assert data["summary"].startswith("Created")


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_without_transaction_id(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    body.update(TransactionId = None)
    response = client.post(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == "<generated new ID>"
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


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update(package, file):
    transaction_id = "[TEST]"
    test_data = "..."
    url = f"/voter/registration/{transaction_id}"
    body = load_test_data(package, file)
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
