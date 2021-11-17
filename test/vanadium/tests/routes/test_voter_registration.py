import re

from fastapi import FastAPI
# NOTE: These tests are not proper unit tests.
# They are *order dependent* and rely on the fact tat PyTest executes tests
# in the order they are defined. This will be fixed but for now they are at
# least testing the core API.

from fastapi.testclient import TestClient

import pytest

from vanadium.app.main import application
from vanadium.model import (
    RequestError,
    RequestForm,
    RequestMethod,
    SuccessAction,
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
def test_voter_registration_request_success(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    response = client.post(url, json = body)
    assert response.status_code == 201
    data = response.json()
    assert data["Action"][0] == SuccessAction.REGISTRATION_CREATED.value
    assert data["TransactionId"] == transaction_id


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_without_transaction_id_success(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    body.update(TransactionId = None)
    response = client.post(url, json = body)
    assert response.status_code == 201
    data = response.json()
    assert data["Action"][0] == SuccessAction.REGISTRATION_CREATED.value
    assert re.match(
        f"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        data["TransactionId"]
    ) is None

@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_failure(package, file):
    url = "/voter/registration/"
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    response = client.post(url, json = body)
    assert response.status_code == 400
    data = response.json()
    assert "Error" in data
    assert len(data["AdditionalDetails"]) == 1
    assert data["AdditionalDetails"][0].startswith(
        "Voter registration request already exists."
    )
    assert len(data["Error"]) == 1
    assert data["Error"][0]["Name"] == "identity-lookup-failed"
    assert data["TransactionId"] == None


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_check_status_success(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_check_status_failure(package, file):
    transaction_id = "invalid-id"
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 404
    data = response.json()
    assert "Error" in data
    assert len(data["AdditionalDetails"]) == 1
    assert data["AdditionalDetails"][0].startswith(
        "Voter registration request not found."
    )
    assert len(data["Error"]) == 1
    assert data["Error"][0]["Name"] == "identity-lookup-failed"
    assert data["TransactionId"] == "invalid-id"


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update_success(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_UPDATED.value


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update_failure(package, file):
    body = load_test_data(package, file)
    body["TransactionId"] = "invalid-id"
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.put(url, json = body)
    # Setting 'response.status_code' for 'put' isn't working.
    assert response.status_code == 404
    data = response.json()
    assert "Error" in data
    assert len(data["AdditionalDetails"]) == 1
    assert data["AdditionalDetails"][0].startswith(
        "Voter registration request not found."
    )
    assert len(data["Error"]) == 1
    assert data["Error"][0]["Name"] == "identity-lookup-failed"
    assert data["TransactionId"] == "invalid-id"


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_cancel_success(package, file):
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_CANCELLED.value


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_delete_failure(package, file):
    transaction_id = "invalid-id"
    url = f"/voter/registration/{transaction_id}"
    response = client.delete(url)
    assert response.status_code == 404
    data = response.json()
    assert "Error" in data
    assert len(data["AdditionalDetails"]) == 1
    assert data["AdditionalDetails"][0].startswith(
        "Voter registration request not found."
    )
    assert len(data["Error"]) == 1
    assert data["Error"][0]["Name"] == "identity-lookup-failed"
    assert data["TransactionId"] == "invalid-id"
