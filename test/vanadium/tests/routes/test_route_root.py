from fastapi import FastAPI
from fastapi.testclient import TestClient

app = FastAPI()

client = TestClient(app)


def _assert_failed_connection(response):
    headers = response.headers
    content_type = headers.get("content-type")
    assert response.status_code == 404
    assert content_type == "application/json"
    assert response.json() == { "detail": "Not Found" }


def _debug_response(response):
    r = response
    h = r.headers
    print(f"Status: {r.status_code}")
    print(f"Content-Type: {h['content-type']}")
    print(f"Headers: {h}")
    print(f"Body: {r.json() or r.text}")


def test_root_get():
    response = client.get("/")
    _assert_failed_connection(response)


def test_root_post():
    response = client.post("/")
    _assert_failed_connection(response)


def test_root_put():
    response = client.put("/")
    _assert_failed_connection(response)


def test_root_delete():
    response = client.delete("/")
    _assert_failed_connection(response)
