from fastapi.testclient import TestClient
from sqlalchemy.orm import Session

def test_register(client: TestClient, db: Session):
    response = client.post("/api/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert response.json()["email"] == "test@example.com"

def test_login(client: TestClient, db: Session):
    client.post("/api/auth/register", json={
        "email": "test@example.com",
        "username": "testuser",
        "first_name": "Test",
        "last_name": "User",
        "password": "testpassword"
    })
    response = client.post("/api/auth/login", data={
        "username": "testuser",
        "password": "testpassword"
    })
    assert response.status_code == 200
    assert "access_token" in response.json()