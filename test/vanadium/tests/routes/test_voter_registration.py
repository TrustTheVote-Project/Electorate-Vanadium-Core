import re

from fastapi import FastAPI
from fastapi.testclient import TestClient

import pytest

from vanadium.app.database import MemoryDataStore
from vanadium.app.main import application
from vanadium.app.resource import storage
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


# --- Test data

VOTER_RECORDS_REQUEST_TESTS = [
    ( "nvra", "minimal" ),
    ( "nvra", "alice-zed" ),
    ( "nvra", "jane-doe" ),
]


# --- Test fixtures
#
# Notes:
#
# - The application fixture is shared. To keep each test independent of the
#   others, storage fixtures replace the application data storage on every test.
#   The one exception is that to test the storage itself at least one test needs
#   to not use the fixture storage fixtures. This modifies the original app, so
#   an application fixture with function sope is used just for that test.
#   Currently no other state on the application is changing.
#
# - The storage fixtures are FastAPI dependency overrides on the application
#   database. Unlike the application database they do *not* need to have a
#   dependency on the application since they don't, and *shouldn't*, touch
#   'app.state'.


@pytest.fixture(params = VOTER_RECORDS_REQUEST_TESTS)
def request_body(request):
    """Pre-load test data and return the body of each HTTP request."""
    package, file = request.param
    body = load_test_data(package, file)
    return body


@pytest.fixture
def empty_storage():
    """Use a data store that has no contents."""
    def get_storage():
        storage = MemoryDataStore()
        return storage
    return get_storage


@pytest.fixture
def prefilled_storage(request_body):
    """Use a data store with test data already loaded."""
    def get_storage():
        storage = MemoryDataStore()
        key = storage.insert(request_body["TransactionId"], request_body)
        assert key is not None, "Failed to prefill storage"
        return storage
    return get_storage


@pytest.fixture(scope = "module")
def app():
    app = application()
    return app


@pytest.fixture(scope = "function")
def app_ephemeral():
    app = application()
    return app


@pytest.fixture
def client_default(app_ephemeral):
    """Client that tests application data store."""
    client = TestClient(app_ephemeral)
    return client


@pytest.fixture
def client_without_data(app, empty_storage):
    """Client that overrides app storage to use a new empty data store."""
    app.dependency_overrides[storage.get_storage] = empty_storage
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}


@pytest.fixture
def client_with_data(app, prefilled_storage, request_body):
    """Client that overrides app storage to always have a record."""
    app.dependency_overrides[storage.get_storage] = prefilled_storage
    client = TestClient(app)
    yield client
    app.dependency_overrides = {}


# --- Test cases

def test_voter_registration_create_success(client_default, request_body):
    """Create a voter registration successfully.
    Uses the client provided transaction ID.
    """
    client = client_default
    body = request_body
    transaction_id = body["TransactionId"]
    url = "/voter/registration/"
    response = client.post(url, json = body)
    assert response.status_code == 201
    data = response.json()
    assert data["Action"][0] == SuccessAction.REGISTRATION_CREATED.value
    assert data["TransactionId"] == transaction_id


def test_voter_registration_create_without_transaction_id_success(client_with_data, request_body):
    """Create a voter registration without a transaction ID.
    Generates a transaction ID on the server.

    Note:
    - The storage has data in it, but this record is new.
    """
    client = client_with_data
    body = request_body
    body.update(TransactionId = None)
    url = "/voter/registration/"
    response = client.post(url, json = body)
    assert response.status_code == 201
    data = response.json()
    assert data["Action"][0] == SuccessAction.REGISTRATION_CREATED.value
    assert re.match(
        f"[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}",
        data["TransactionId"]
    ) is None


def test_voter_registration_create_failure(client_with_data, request_body):
    """Fail to create a voter registration ID, because it already exists."""
    client = client_with_data
    body = request_body
    transaction_id = body["TransactionId"]
    url = "/voter/registration/"
    response = client.post(url, json = body)
    assert response.status_code == 400
    data = response.json()
    assert "Error" in data
    assert len(data["AdditionalDetails"]) == 1
    assert data["AdditionalDetails"][0].startswith(
        "Voter registration request already exists."
    )
    assert len(data["Error"]) == 1
    assert data["Error"][0]["Name"] == RequestError.IDENTITY_LOOKUP_FAILED.value
    assert data["TransactionId"] == None


def test_voter_registration_check_status_success(client_with_data, request_body):
    """Verify that a voter registration request exists on the server."""
    client = client_with_data
    body = request_body
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.get(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id


def test_voter_registration_check_status_failure(client_without_data, request_body):
    """Verify that a voter registration request does NOT exist on the server."""
    client = client_without_data
    body = request_body
    transaction_id = body["TransactionId"]
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
    assert data["Error"][0]["Name"] == RequestError.IDENTITY_LOOKUP_FAILED.value
    assert data["TransactionId"] == transaction_id


def test_voter_registration_update_success(client_with_data, request_body):
    """Update an existing voter registration request successfully."""
    client = client_with_data
    body = request_body
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_UPDATED.value


def test_voter_registration_update_failure(client_without_data, request_body):
    """Fail to update a voter registration request because it does not exist."""
    client = client_without_data
    body = request_body
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
    assert data["Error"][0]["Name"] == RequestError.IDENTITY_LOOKUP_FAILED.value
    assert data["TransactionId"] == transaction_id


def test_voter_registration_cancel_success(client_with_data, request_body):
    """Cancel an existing voter registration request successfully."""
    client = client_with_data
    body = request_body
    transaction_id = body["TransactionId"]
    url = f"/voter/registration/{transaction_id}"
    response = client.delete(url)
    assert response.status_code == 200
    data = response.json()
    assert data["TransactionId"] == transaction_id
    assert data["Action"][0] == SuccessAction.REGISTRATION_CANCELLED.value


def test_voter_registration_cancel_failure(client_without_data, request_body):
    """Fail to cancel a voter registration request because it does not exist.
    """
    client = client_without_data
    body = request_body
    transaction_id = body["TransactionId"]
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
    assert data["Error"][0]["Name"] == RequestError.IDENTITY_LOOKUP_FAILED.value
    assert data["TransactionId"] == transaction_id
