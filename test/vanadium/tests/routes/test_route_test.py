from fastapi import FastAPI
from fastapi.testclient import TestClient

from vanadium.app.main import application

app = application()
client = TestClient(app)


def test_get_test():
    response = client.get("/test/1")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == { "id": "1", "method": "GET", "option": None }


def test_get_test_with_option():
    response = client.get("/test/1?option=one")
    assert response.status_code == 200
    assert response.json() == { "id": "1", "method": "GET", "option": [ "one" ] }


def test_get_test_with_options():
    response = client.get("/test/1?option=one&option=two")
    assert response.status_code == 200
    assert response.json() == { "id": "1", "method": "GET", "option": [ "one", "two" ] }


def test_post_test():
    response = client.post("/test/2")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == { "id": "2", "method": "POST", "option": None }


def test_post_test_with_option():
    response = client.post("/test/2?option=one")
    assert response.status_code == 200
    assert response.json() == { "id": "2", "method": "POST", "option": "one" }


def test_put_test():
    response = client.put("/test/3")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == { "id": "3", "method": "PUT", "option": None }

def test_put_test_with_option():
    response = client.put("/test/3?option=one")
    assert response.status_code == 200
    assert response.json() == { "id": "3", "method": "PUT", "option": "one" }


def test_delete_test():
    response = client.delete("/test/4")
    assert response.status_code == 200
    assert response.json() == { "id": "4", "method": "DELETE", "option": None }


def test_delete_test_with_option():
    response = client.delete("/test/4?option=one")
    assert response.status_code == 200
    assert response.headers["content-type"] == "application/json"
    assert response.json() == { "id": "4", "method": "DELETE", "option": "one" }
