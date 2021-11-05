from typing import Optional

from fastapi import APIRouter
from pydantic import BaseModel

from vanadium.model import VoterRecordsRequest


# --- Routes

_router = APIRouter(prefix = "/voter/registration")


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
    transaction_id = (
        item.transaction_id if item.transaction_id else "<generated new ID>"
    )
    return {
        "id":      transaction_id,
        "status":  "Nominal success",
        "summary": "Created voter registration request",
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
    return {
        "id":      transaction_id,
        "status":  "Nominal success",
        "summary": "Checked status of voter registration request",
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
    return {
        "id":      transaction_id,
        "status":  "Nominal success",
        "summary": "Updated voter registration request",
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
    return {
        "id":      transaction_id,
        "status":  "Nominal success",
        "summary": "Deleted voter registration request",
    }


# --- Router

_routers = [
    _router
]

def router():
    return _router
