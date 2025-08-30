from pytest_bdd import given, when, then
from fastapi.testclient import TestClient
from app.src.main import app

client = TestClient(app)

@given('a user "alice" exists')
def create_alice_user():
    client.post("/users/", json={"username": "alice", "email": "alice@example.com"})

@when('I request GET /users/alice')
def get_alice_user():
    return client.get("/users/alice")

@then('the response status code should be 200')
def check_status(get_alice_user):
    response = get_alice_user
    assert response.status_code == 200
