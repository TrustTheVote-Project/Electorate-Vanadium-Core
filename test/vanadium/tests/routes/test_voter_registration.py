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
    assert data["status"] == "Success"
    assert data["summary"].find("created") != -1


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_without_transaction_id(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    body.update(TransactionId = None)
    response = client.post(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["status"] == "Success"
    assert data["summary"].find("created") != -1


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_check_status(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Success"
    assert data["summary"].find("in process") != -1


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Success"
    assert data["summary"].find("updated") != -1


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_cancel(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["status"] == "Success"
    assert data["summary"].find("cancelled") != -1