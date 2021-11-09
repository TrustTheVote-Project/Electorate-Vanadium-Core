from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from vanadium.app.resource import Resources
from vanadium.model import VoterRecordsRequest
from vanadium.utils import UniqueIds


# --- Routes

_router = APIRouter(prefix = "/voter/registration")

# NOTE: These tests are not proper unit tests.
# They are *order dependent* and rely on the fact tat PyTest executes tests
# in the order they are defined.


@_router.post(
    "/",
    # response_model = # VoterRecordsResponse
    response_description = "Voter registration response",
    summary = "Initiate a new voter registration request",
)
def voter_registration_request(
    item: VoterRecordsRequest
):
    """Create a new voter registration request.

    It is an error if no record exists.
    """
    # If a transaction ID was provided use it as the unique ID.
    # Otherwise generate one from the current time.
    # (Note: not robust just good enough for testing.)
    storage = Resources.get_storage()
    unique_id = storage.insert(item.transaction_id, item)
    if unique_id:
        status = "Success"
        summary = "Voter registration request created"
    else:
        status = "Failure"
        summary = "Voter registration request already exists"
    return {
        "id":      unique_id,
        "status":  status,
        "summary": summary,
    }


@_router.get(
    "/{transaction_id}",
    summary = "Check on the status of a pending voter registration request"
)
def voter_registration_status(
    transaction_id,
):
    """Status of pending voter registration request.

    It is an error if no record is found.

    Parameters:
        `transaction_id`: The transaction ID as returned in the initial transaction.

    Limitations:

    - Only updates existing *request*. It does not update a registration
      that has been accepted or rejected, only one that is pending.
    - Lookup is only done through the transaction ID, not through other identifiers.
    """
    storage = Resources.get_storage()
    value = storage.lookup(transaction_id)
    if value:
        status = "Success"
        summary = "Transaction request is in process"
    else:
        status = "Failure"
        summary = "Voter registration request not found"
    return {
        "id":      transaction_id,
        "status":  status,
        "summary": summary,
    }


@_router.put(
    "/{transaction_id}",
    summary = "Update a pending voter registration request"
)
def voter_registration_update(
    transaction_id,
    item: VoterRecordsRequest,
):
    """Update an existing voter registration request.

    It is an error if there is no record to update.

    Parameters:
        `transaction_id`: The transaction ID as returned

    Limitations:

    - Currently only updates existing *request*. It does not update a registration
      that has been accepted or rejected, only one that is pending.
    - Lookup is only done through the transaction ID, not through other identifiers.
    """
    storage = Resources.get_storage()
    value = storage.update(transaction_id, item)
    if value:
        status = "Success"
        summary = "Pending transaction request updated(overwritten!)"
    else:
        status = "Failure"
        summary = "Voter registration request not found"
    return {
        "id":      transaction_id,
        "status":  status,
        "summary": summary,
    }


@_router.delete(
    "/{transaction_id}",
    summary = "Cancel a pending voter registration request"
)
def voter_registration_cancel(
    transaction_id,
):
    """Delete an existing request.

    It is an error if there is no record to delete.
    """
    storage = Resources.get_storage()
    value = storage.remove(transaction_id)
    if value:
        status = "Success"
        summary = "Transaction request has been cancelled"
    else:
        status = "Failure"
        summary = "Voter registration request not found"
    return {
        "id":      transaction_id,
        "status":  status,
        "summary": summary,
    }


# --- Router

_routers = [
    _router
]

def router():
    return _router
