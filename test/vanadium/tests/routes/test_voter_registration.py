from fastapi import FastAPI
from fastapi.testclient import TestClient

from vanadium.app.main import application


app = application()
client = TestClient(app)


def test_voter_registration_request():
    url = "/voter/registration/"
    transaction_id = "[TEST]"
    body = {
        "data": transaction_id
    }
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


def test_voter_registration_update():
    transaction_id = "[TEST]"
    test_data = "..."
    url = f"/voter/registration/{transaction_id}"
    body = {
        "data": test_data
    }
    response = client.put(url, json = body)
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == transaction_id
    assert data["data"] == test_data
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
