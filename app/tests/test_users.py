from fastapi.testclient import TestClient
from app import app
from pytest_bdd import scenario

client = TestClient(app)

def test_create_user():
    response = client.post("/users/", json={"username": "alice", "email": "alice@example.com"})
    assert response.status_code == 200
    data = response.json()
    assert data["username"] == "alice"

# BDD test for "Successful money transfer"
@scenario('features/transactions.feature', 'Successful money transfer')
def test_successful_money_transfer():
    pass

# BDD test for "Get an existing user"
@scenario('features/transactions.feature', 'Get an existing user')
def test_get_existing_user():
    pass
