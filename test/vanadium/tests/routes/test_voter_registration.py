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


# --- Test fixtures

# Share one application across all tests
@pytest.fixture(scope = "module")
def app():
    app = application()
    return app


@pytest.fixture
def client(app):
    client = TestClient(app)
    return client


# --- Test data

VOTER_RECORDS_REQUEST_TESTS = [
    ( "nvra", "minimal" ),
    ( "nvra", "alice-zed" ),
    ( "nvra", "jane-doe" ),
]


# --- Test cases

@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_success(package, file, client):
    """Create a voter registration successfully.
    Uses the client provided transaction ID.
    """
    url = "/voter/registration/"
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    response = client.post(url, json = body)
    assert response.status_code == 201
    data = response.json()
    assert data["Action"][0] == SuccessAction.REGISTRATION_CREATED.value
    assert data["TransactionId"] == transaction_id


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_request_without_transaction_id_success(package, file, client):
    """Create a voter registration without a transaction ID.
    Generates a transaction ID on the server.
    """
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
def test_voter_registration_request_failure(package, file, client):
    """Fail to create a voter registration ID, because it already exists."""
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
def test_voter_registration_check_status_success(package, file, client):
    """Verify that a voter registration request exists on the server."""
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_check_status_failure(package, file, client):
    """Verify that a voter registration request does NOT exist on the server."""
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
def test_voter_registration_update_success(package, file, client):
    """Update an existing voter registration request successfully."""
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_UPDATED.value


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_update_failure(package, file, client):
    """Fail to update a voter registration request because it does not exist."""
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
def test_voter_registration_cancel_success(package, file, client):
    """Cancel an existing voter registration request successfully."""
    body = load_test_data(package, file)
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_CANCELLED.value


@pytest.mark.parametrize("package,file", VOTER_RECORDS_REQUEST_TESTS)
def test_voter_registration_cancel_failure(package, file, client):
    """Fail to cancel a voter registration request because it does not exist."""
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
